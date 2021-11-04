# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 13:11:52 2019

@author: guest


#example
    Mod_str=database.mod_obj(database.retrive_str('Model/*.cfl'))
    Mod_str.retrive(wik='6d', chem_s='Ge+4')
    Mod_str.reduce(wik='6d', chem_s='Ge+4')
"""

import glob
import numpy as np

from itertools import combinations, combinations_with_replacement


wik2 = {'1': 'a',
        '2': 'd',
        '3': 'c',
        '4': 'f',
        '5': 'e'}

wiks = {'a': {'m': 2, 'coor': '0.00000  0.00000  0.00000  '},
        'd': {'m': 6, 'coor': '0.25000  0.00000  0.50000  '},
        'c': {'m': 6, 'coor': '0.25000  0.50000  0.00000  '},
        'f': {'m': 12, 'coor': '0.25745  0.00000  0.00000 '},
        'e': {'m': 8, 'coor': '0.25150  0.25150  0.25150  '},
        'general': {'m': 24}}


def g_wiks(w=wiks, val=None, gen=False):
    v = lambda j: j[val] if val else j
    g = lambda i: True if gen else i != 'general'
    return {i: v(j) for i, j in w.items() if g(i)}


other_sites = {'S1': {'elem': 'S',
                      'coor': '0.12270  0.12270  0.12270',
                      'Biso': 1,
                      'c_occ': 0.33333},
               'S2': {'elem': 'S',
                      'coor': '0.37640  0.36950  0.12140',
                      'Biso': 1,
                      'c_occ': 1.0}}


def short_notation(comb):
    """for mod_list class
    """
    out = []
    for iter_c in comb:
        stringa = []
        iter_cset = set(iter_c)
        for site in iter_cset:
            site_c = iter_c.count(site)
            stringa.append('%s%d' % (site, site_c))
        stringa.sort()
        out.append(stringa)
    return out


class mod_list(list):
    """list type notation for configuration
       possible to combine more condition by multiplication
       [('aFe', 'aFe', 'fFe', 'fFe', 'fFe', 'fFe', 'fFe', 'fFe'),
        ('aFe', 'aFe', 'fFe', 'fFe', 'fFe', 'fFe', 'fFe', 'eFe'),
        ('aFe', 'aFe', 'fFe', 'fFe', 'fFe', 'fFe', 'fFe', 'dFe'),
        .......
    """

    def __init__(self, seq, wiks, other_sites=None):
        super().__init__(seq)
        self.wiks = wiks
        self.other_sites = other_sites

    @classmethod
    def generate_model(cls, cation, N_cations, debug=0,
                       wiks=wiks, other_sites=None):
        """typical use 
           generate_model('Ge', 4)
        """
        sm = g_wiks(wiks, val='m')
        list_site = [i + cation for i in sm.keys()]
        z = list(combinations_with_replacement(list_site, N_cations))

        if debug:
            print(len(z))
        to_delete = []
        for i, jz in enumerate(z):
            for site in list_site:
                if sm[site[0]] < N_cations:
                    if jz.count(site) > sm[site[0]]:
                        to_delete.append(i)
                        break
        for i in reversed(to_delete):
            del z[i]

        if debug:
            print(len(z))
        return cls(z, wiks, other_sites)

    def convert_database(self, add='Cu'):
        """convert to mod_obj
        """
        wiks = self.wiks
        sm = g_wiks(wiks, 'm')

        def modi2obji(modi):
            """convert an item from obj_mod to mod_list
                Args:
                    removes list(str): list of the specise
                                        that should be not included
                ('aFe', 'aFe', 'fFe', 'fFe', 'fFe', 'fFe', 'fFe', 'fFe')
            """

            obji = {i: {} for i in sm.keys()}
            for sit_spc in set(modi):
                obji[sit_spc[0]].update({sit_spc[1:]: modi.count(sit_spc)})
            for sit_l, sit in obji.items():
                occu = sum(list(sit.values()))
                if occu < sm[sit_l]:
                    sit.update({add: sm[sit_l] - occu})
            return obji

        return mod_obj([modi2obji(modi) for modi in self],
                       self.wiks, self.other_sites)

    def __mul__(self, other):
        tot_comb = []
        sm = g_wiks(self.wiks, val='m')
        # print(len(self)*len(other))
        for Fe in self:
            for Ge in other:
                conto = [i[0] for i in Fe] + [i[0] for i in Ge]
                for site in sm.keys():
                    if conto.count(site) > sm[site]:
                        break
                else:
                    tot_comb.append(Fe + Ge)

        # print(len(tot_comb))
        return mod_list(tot_comb)

    def __getitem__(self, subscript):
        if isinstance(subscript, slice):
            return mod_obj(super().__getitem__(subscript),
                           self.wiks, self.other_sites)
        else:
            return super().__getitem__(subscript)


class mod_obj(tuple):
    """ other kind of notation for configuration
        easier to filter
    ({'12f': {'Fe': 6, 'Cu': 6},
      '2a': {'Fe': 2},
      '6d': {'Cu': 6},
      '6c': {'Cu': 6},
      '8e': {'Cu': 8}},
     {'12f': {'Fe': 5, 'Cu': 7},
      '2a': {'Fe': 2},
      '8e': {'Fe': 1, 'Cu': 7},
      '6d': {'Cu': 6},
      '6c': {'Cu': 6}}
    """

    def __new__(cls, seq, wiks, other_sites=None):
        return super().__new__(cls, tuple(seq))

    def __init__(self, seq, wiks, other_sites=None):
        self.wiks = wiks
        self.other_sites = other_sites

    @classmethod
    def from_cfl(cls, files_condition='*.cfl', conv=wik2, wiks=wiks):
        """used to create a mod_obj
           Mod_str=database.mod_obj(database.retrive_str('Model/*.cfl'))
           conv to0 convert label to site
           wiks = wiks dictionary
        """


        cfl_list = glob.glob(files_condition)
        assert len(cfl_list) > 0, "empty database"
        model = list()

        for index, f_name in enumerate(cfl_list):
            with open(f_name) as lfile:
                cfl = lfile.readlines()
            atom = {}
            for line in cfl:
                if line[:4] == 'ATOM':
                    stringhe = line.split()
                    chem = stringhe[2]
                    occu = stringhe[7]
                    site = stringhe[1][-1]
                    if chem[0] != 'S':
                        natom = float(occu) * sm['general']
                        if conv:
                            atom[conv[site]].update({chem: round(natom, 2)})
                        else:
                            atom[site].update({chem: round(natom, 2)})
            model.append(atom)

        print('done')
        out
        return cls(model)

    def filter(self, wik, chem_s, cond, N=False):
        """ check a chemical condition 
        used to create a condition
            Args:
                wik (str)   : wikoff site
                chem_s (str): atomic specie
                cond (str)  : string to evaluate
                N     (bool): if true return the index f
                              or wich the condition is True
            Returns:
                array of bolean if N=False
                array of int (indexes) if N = True
            Example:
                Sn4.filter('a', 'Sn', '>1', N=True)
        """
        qq = self.retrive(wik, chem_s)
        evalu = eval('qq' + cond)
        if N:
            return np.arange(len(self))[evalu] + 1
        else:
            return evalu

    def reduce(self, rcond, N=False):
        """ reduce following a condition 
        used  a condition create by filter or retrive
            Args:
                rcond (bool array)  : array from filtering evaluate
                N     (bool): if true return the index f
                              or wich the condition is True
            Returns:
                array of bolean if N=False
                array of int (indexes) if N = True
            Example:
                Sn4.filter('a', 'Sn', '>1', N=True)
        """
        N_reduced = [i for i in range(len(self)) if rcond[i]]
        if N:
            return np.asarray(N_reduced) + 1
        else:
            return mod_obj([self[i] for i in N_reduced])

    def retrive(self, wik, chem_s):
        """return the occupation in a wik site if chem is present else 0 
           for all the models
           eXAMPLE:
              Sn4.retricve('a', 'Ge+4')
        """
        qq = [i[wik][chem_s] if chem_s in i[wik].keys() else 0 for i in self]
        return np.array(qq)

    def reorder(self, other):
        """reorder the tuple using an array in wich the other order is defined
        example:
           pippo.reorder([0,3,2,6,8])
        """
        try:
            out = []
            for i in other:
                out.append(self.index(i))
            return out
        except ValueError:
            print(i)

    def sorted(self, atom, wik_order={'8e': 'a', '6c': 'b', '6d': 'c', '12f': 'd'}):
        """change order of models
           using increasing the order in respect the wik order
        """
        def sortt(elem, atom, order):
            out = []
            for site in elem:
                if atom in elem[site].keys():
                    if site in wik_order.keys():
                        out.append(order[site] * int(elem[site][atom]))
            return ''.join(sorted(out))
        out = list(self)
        out.sort(key=lambda elem: sortt(elem, atom, wik_order))
        return mod_obj(out)

    def convert_mod_list(self, item=None, remove=['Cu']):
        """convert an item from obj_mod to mod_list
            Args:
                removes list(str): list of the specise
                                    that should be not included
            {'f': {'Fe': 6, 'Cu': 6},'a': {'Fe': 2},'d': {'Cu': 6},
             'c': {'Cu': 6},'e': {'Cu': 8}}
        """
        def obji2modi(obji):
            comb = []
            for site_l, site in obji.items():
                for spc, sto in site.items():
                    if not(spc in remove):
                        for i in range(sto):
                            comb.append('%sspc' % site_l)
            return comb

        return mod_list([obji2modi(item)] for item in self)

    def save_cfl(self, title='TITLE xx',
                 cell='10.604 10.604 10.604 90 90 90',
                 spg='SPGR  P -4 3 n',
                 Biso=0.5, other_format=False, other_sites=other_sites):
        """
        if len(self)> 1 save else return a list of strings
        """

        other_sites = self.other_sites or other_sites

        for i, obji in enumerate(self):
            stringa = [i + '\n' for i in [title, cell, spg]]
            if other_sites:
                for osite_l, osite in other_sites.itertools():
                    stringa.append('ATOM {:s} {:s}   {:s} {:2.4f}{:1.7f}\n'.format(
                        osite_l, osite['elem'], osite['coor'], osite["Biso"], osite["c_occ"]))

            for site_l, site in g_wiks(wiks).items():
                for spc, n in obji[site_l].items():
                    stringa.append('ATOM {:s} {:s}   {:s} {:2.4f}{:1.7f}\n'.format(
                                   spc + site['m'], spc, site['coor'],
                                   Biso, n / wiks['general']['m']))

            name = 'model_{:03d}'.format(i + 1)
            if other_format:
                if other_format == 'cif':
                    stringa.append('create_cif file=%s.cif\n' % name)
                if other_format == 'pcr':
                    stringa.append('create_pcr file=%s.pcr\n' % name)

            with open(name + '.cfl', 'w') as cldfile:
                cldfile.writelines(stringa)

    def _obji2pcrxyz(self, item, Spg='SPGR  P -4 3 n', patterns=0, Npr=7,
                     Biso=0.5, sincry=False, commands=False, title='title'):
        """
        Create the lines in pcf file between Data for PHASE to Profile
            Args:
                Spg (str): space group
                Pattern (int): if 0 old format
                               else new format
                command (list): command to put in command line
        """
        obji = self[item]
        wiks = self.wiks
        other_sites = self.other_sites

        pcr_lines = []
        pcr_lines.append('!  Data for PHASE number:   1\n')
        pcr_lines.append('!' + '-' * 72 + '\n')
        pcr_lines.append(f'{title:s} \n!\n')
        if commands:
            pcr_lines.append(commands)

        Nat = sum([len(i) for i in obji.values()])
        if patterns:
            pcr_lines.append('!Nat Dis Ang Jbt Isy Str Furth        ATZ     Nvk More\n')
            pcr_lines.append(f'{Nat:d}   0   0   0   0   0   0       0   0   0\n')
            pcr_lines.append(f'!Contributions (0/1) of this phase to the  {patterns:d} patterns\n')
            pcr_lines.append(' 1' * patterns + '\n')
            for i in range(patterns):
                pcr_lines.append(f'!Irf Npr Jtyp  Nsp_Ref Ph_Shift for Pattern#  {i+1:d}\n')
                pcr_lines.append(f'{4 if sincry else 0:d}   {Npr:d}    0      0      0\n')
                pcr_lines.append(f'! Pr1    Pr2    Pr3   Brind.   Rmua   Rmub   Rmuc     for Pattern#  {i+1:d}\n')
                pcr_lines.append('0.000  0.000  0.000  0.000  0.000  0.000  0.000\n')

        else:
            pcr_lines.append('!Nat Dis Ang Pr1 Pr2 Pr3 Jbt Irf Isy Str Furth       ATZ    Nvk Npr More\n')
            pcr_lines.append(f'{Nat:d}   0   0 0.0 0.0 1.0   {4 if sincry else 0:d}   0   0   0   0      0      0   {Npr:d}   0\n')

        pcr_lines.append('!\n!\n')
        pcr_lines.append(f'{Spg:s}                 <--Space group symbol\n')
        pcr_lines.append('!Atom   Typ       X        Y        Z     Biso       Occ     In Fin N_t Spc /Codes\n')

        post = '  0   0   0    0\n                  0.00     0.00     0.00     0.00      0.00\n'

        if other_sites:
            for o_sl, o_si in other_sites.items():
                val = (o_sl, o_si['elem'], o_si['coor'], o_si["Biso"], o_si["c_occ"], post)
                pcr_lines.append('{:3s}    {:5s}   {:s} {:2.4f}   {:1.5f}{:s}'.format(*val))

        for sl, si in g_wiks(wiks).items():
            for spc, n in obji[sl].items():
                val = (sl + spc, spc, si['coor'], Biso, n / wiks['general']['m'], post)
                pcr_lines.append('{:3s}    {:5s}   {:s} {:2.4f}   {:1.5f}{:s}'.format(*val))

        return pcr_lines

    def __getitem__(self, subscript):
        if isinstance(subscript, slice):
            return mod_obj(super().__getitem__(subscript),
                           self.wiks, self.other_sites)
        else:
            return super().__getitem__(subscript)



# example
# Mod_str.retrive(wik='6d', chem_s='Ge+4')
