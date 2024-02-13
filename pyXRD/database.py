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
from pickle import dump, load
from itertools import combinations_with_replacement as _comb_re
import matplotlib.pyplot as plt

# wik2 = {'1': 'a',
#        '2': 'd',
#        '3': 'c',
#        '4': 'f',
#        '5': 'e'}

wiks = {'a': {'m': 2, 'coor': '0.00000  0.00000  0.00000  '},
        'd': {'m': 6, 'coor': '0.25000  0.00000  0.50000  '},
        'c': {'m': 6, 'coor': '0.25000  0.50000  0.00000  '},
        'f': {'m': 12, 'coor': '0.25745  0.00000  0.00000 '},
        'e': {'m': 8, 'coor': '0.25150  0.25150  0.25150  '},
        'general': {'m': 24}}


def _wiks(w=wiks, val=None, gen=False):
    """produces data from wiks
    """
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


def _short_notation(comb):
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


class propieta:
    def __init__(self, name, owner_instance, seq):
        self.owni = owner_instance
        self.name = name
        assert len(owner_instance) == len(seq), 'different lenght'
        for mod_i, val in zip(owner_instance, seq):
            setattr(mod_i, self.name, val)

    def __get__(self, instance, owner_type):
        return np.array([getattr(i, self.name) for i in self.owni])


class mod_dic(dict):
    """
    """

    def obji2modi(self, remove):
        comb = []
        for site_l, site in self.items():
            for spc, sto in site.items():
                if not(spc in remove):
                    for i in range(sto):
                        comb.append(f'{site_l:s}{spc:s}')
        return comb

    def v_str(self, remove=[]):
        """create lisible string with configuration
        """
        if remove is False:
            remove = []
        finstr = ''
        for site in self.keys():
            finstr += f']{site:s}['
            for spc, val in self[site].items():
                if spc in remove:
                    continue
                finstr += f'{spc:s}{val:d}'
        return finstr[1:] + ']'


class _mod_list(list):
    """list type notation for configuration
       possible to combine more condition by multiplication
       [('aFe', 'aFe', 'fFe', 'fFe', 'fFe', 'fFe', 'fFe', 'fFe'),
        ('aFe', 'aFe', 'fFe', 'fFe', 'fFe', 'fFe', 'fFe', 'eFe'),
        ('aFe', 'aFe', 'fFe', 'fFe', 'fFe', 'fFe', 'fFe', 'dFe'),
        .......
    """

    def __init__(self, seq, **kargs):
        super().__init__(seq)
        for k, v in kargs.items():
            setattr(self, k, v)
        self._kargs = kargs

    @classmethod
    def generate_model(cls, cation, N_cations, debug=0, **kargs):
        """typical use
           generate_model('Ge', 4)
        """
        sm = _wiks(wiks, val='m')
        list_site = [i + cation for i in sm.keys()]
        z = list(_comb_re(list_site, N_cations))

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
        return cls(z, **kargs)

    def convert_database(self, add='Cu'):
        """convert to mod_obj
        """
        self._kargs.update({'buffer': add})

        wiks = self.wiks
        sm = _wiks(wiks, 'm')

        def modi2obji(modi):
            """convert an item from obj_mod to mod_list
                Args:
                    removes list(str): list of the specise
                                        that should be not included
                ('aFe', 'aFe', 'fFe', 'fFe', 'fFe', 'fFe', 'fFe', 'fFe')
            """

            obji = mod_dic({i: {} for i in sm.keys()})
            for sit_spc in set(modi):
                obji[sit_spc[0]].update({sit_spc[1:]: modi.count(sit_spc)})
            for sit_l, sit in obji.items():
                occu = sum(list(sit.values()))
                if occu < sm[sit_l]:
                    sit.update({add: sm[sit_l] - occu})
            return obji

        return mod_obj([modi2obji(modi) for modi in self],
                       **self._kargs)

    def __mul__(self, other):
        assert self.wiks == other.wiks, 'different wiks'
        tot_comb = []
        sm = _wiks(self.wiks, val='m')
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
        return _mod_list(tot_comb, **self._kargs)

    def __add__(self, other):
        assert self.wiks == other.wiks, 'different wiks'
        tot_comb = []
        # print(len(self)*len(other))
        # print(self)
        for Ge in other:
            if Ge not in self:
                self.append(Ge)
        # return #_mod_list(tot_comb, **self._kargs)
        return self


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

    def __new__(cls, seq, wiks, other_sites=None, buffer=None,
                Spg=None, Biso=None):
        return super().__new__(cls, tuple(seq))

    def __init__(self, seq, wiks, other_sites=None, buffer=None,
                 Spg=None, Biso=None):
        self._kargs = {'wiks': wiks,
                       'other_sites': other_sites,
                       'buffer': buffer,
                       'Spg': Spg,
                       'Biso': Biso}

        self.__value__set__ = []

    def _get_kargs(self, key):
        return self._kargs[key]

    def _set_kargs(self, value, key):
        self._kargs[key] = value


    wiks = property(lambda self: self._get_kargs('wiks'),
                    lambda self, val: self._set_kargs(val, 'wiks'))
    other_sites = property(lambda self: self._get_kargs('other_sites'),
                           lambda self, val: self._set_kargs(val,
                                                             'other_sites'))
    buffer = property(lambda self: self._get_kargs('buffer'),
                      lambda self, val: self._set_kargs(val, 'buffer'))
    Spg = property(lambda self: self._get_kargs('Spg'),
                   lambda self, val: self._set_kargs(val, 'Spg'))
    Biso = property(lambda self: self._get_kargs('Biso'),
                    lambda self, val: self._set_kargs(val, 'Biso'))

    def __getattribute__(self, attr):
        # If the attribute does not exist, super().__getattribute__()
        # will raise an AttributeError
        got_attr = super().__getattribute__(attr)
        try:
            # Try "manually" invoking the descriptor protocol __get__()
            return got_attr.__get__(self, type(self))
        except AttributeError:
            # Attribute is not a descriptor, just return it:
            return got_attr

    def __delattr__(self, attr):
        if attr in self.__value__set__:
            for imod in self:
                delattr(imod, attr)
            self.__value__set__.remove(attr)

        del self.__dict__[attr]

    def __str__(self):
        return '\n'.join([i.v_str() for i in self])

    @classmethod
    def generate_model(cls, cations, N_cations, buffer, wiks,
                       other_sites=None):
        '''
        '''
        if isinstance(cations, str):
            cations = [cations]
        if isinstance(N_cations, int):
            N_cations = [N_cations]
        assert len(N_cations) == len(cations), 'len cation and N_cations'

        z0 = _mod_list.generate_model(cations[0], N_cations[0],
                                      wiks=wiks,
                                      other_sites=other_sites)
        for cat, ncat in zip(cations[1:], N_cations[1:]):
            zi = _mod_list.generate_model(cat, ncat,
                                          wiks=wiks,
                                          other_sites=other_sites)
            z0 = z0 * zi
        return z0.convert_database(add=buffer)

    @classmethod
    def from_cfl(cls, files_condition='*.cfl', wiks=wiks, conv=None):
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
                        natom = float(occu) * wiks['general']['m']
                        if conv:
                            atom[conv[site]].update({chem: round(natom, 2)})
                        else:
                            atom[site].update({chem: round(natom, 2)})
            model.append(atom)

        print('done')
        return cls(model)

    @classmethod
    def load(cls, filename):
        with open(filename, 'rb') as infile:
            a = load(infile)
        return a

    def save(self, filename):
        with open(filename, 'wb') as outfile:
            dump(self, outfile)
        return

    def filter(self, wik, chem_s, cond, N=False):
        """ check a chemical condition
        used to create a condition
            Args:
                wik (str)   : wikoff site
                chem_s (str): atomic specie
                cond (str)  : string to evaluate
                N     (bool): if true return the index f
                              or which the condition is True
            Returns:
                array of bolean if N=False
                array of int (indexes) if N = True
            Example:
                Sn4.filter('a', 'Sn', '>1', N=True)
        """
        qq = self.retrive(wik, chem_s)
        evalu = eval('qq' + cond)
        N_array = np.array(range(len(self)))[evalu]
        if N:
            return N_array
        else:
            return self[evalu]

    def retrive(self, wik, chem_s):
        """return the occupation in a wik site if chem is present else 0
           for all the models
           eXAMPLE:
              Sn4.retricve('a', 'Ge+4')
        """
        qq = [i[wik][chem_s] if chem_s in i[wik].keys() else 0 for i in self]
        return np.array(qq)

    def sorted(self, atom, wik_order={'e': 'a', 'c': 'b',
                                      'd': 'c', 'f': 'd'}):
        """change order of models
           using increasing the order in respect the wik order

           Args:
                wik_order (dict): {site name: priority (string)}
                          (list)  [site order]
        """
        if isinstance(wik_order, list):
            wik_order = {i: str(j) for i, j in zip(wik_order,
                                                   range(len(wik_order)))}

        def sortt(elem, atom, order):
            out = []
            for site in elem:
                if atom in elem[site].keys():
                    if site in wik_order.keys():
                        out.append(order[site] * int(elem[site][atom]))
            return ''.join(sorted(out))
        out = list(self)
        out.sort(key=lambda elem: sortt(elem, atom, wik_order))
        mout = mod_obj(out, **self._kargs)
        for vals in self.__value__set__:
            mout.values_set([getattr(i, vals) for i in mout], vals)
        return mout

    def _convert_mod_list(self, remove=['Cu']):
        """convert an item from obj_mod to mod_list
            Args:
                removes list(str): list of the specise
                                    that should be not included
            {'f': {'Fe': 6, 'Cu': 6},'a': {'Fe': 2},'d': {'Cu': 6},
             'c': {'Cu': 6},'e': {'Cu': 8}}
        """

        return _mod_list([item.obji2modi(remove) for item in self],
                         **self._kargs)

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
                for osite_l, osite in other_sites.items():
                    stringa.append('ATOM {:s} {:s}   {:s} {:2.4f}{:1.7f}\n'.format(
                        osite_l, osite['elem'], osite['coor'], osite["Biso"], osite["c_occ"]))

            for site_l, site in _wiks(wiks).items():
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

    def Atoms(self, item):
        """
        Create the lines in pcf file between Data for PHASE to Profile
            Args:
                Spg (str): space group
                Pattern (int): if 0 old format
                               else new format
                command (list): command to put in command line
        """

        if (self.Biso is None):
            raise ValueError('self.Biso or self.Spg are None')

        Atoms_i = {}
        Atoms_i['u'] = []
        Atoms_i['v'] = []
        Atoms_i['w'] = []
        Atoms_i['label'] = []
        Atoms_i['type'] = []
        Atoms_i['uiso'] = []
        Atoms_i['occupancy'] = None

        if other_sites:
            for o_sl, o_si in other_sites.items():
                ui, vi, wi = o_si['coor'].split()
                Atoms_i['u'].append(float(ui))
                Atoms_i['v'].append(float(vi))
                Atoms_i['w'].append(float(wi))
                Atoms_i['biso'].append(o_si["Biso"] / (8 * np.pi**2))
                Atoms_i['type'].append(o_si['elem'])
                Atoms_i['label'].append(o_sl)
                Atoms_i['occupancy'].append(o_si["ch_occ"])

        for sl, si in _wiks(wiks).items():
            for spc, n in self[item].items():
                ui, vi, wi = si['coor'].split()
                Atoms_i['u'].append(float(ui))
                Atoms_i['v'].append(float(vi))
                Atoms_i['w'].append(float(wi))
                Atoms_i['biso'].append(self.Biso / (8 * np.pi**2))
                Atoms_i['type'].append(spc)
                Atoms_i['label'].append(sl + spc)
                Atoms_i['occupancy'].append(n / wiks['general'])

        return Atoms_i


    def _objipcrxyz(self, item, patterns=0, Npr=7, Nsp_Ref=0,
                    sincry=False,
                    commands=False, title='title', Rmub=2,
                    postSi=f'{"0   "*4}\n{" "*18}{"0.00     "*5}',
                    postAt=f'{"0   "*4}\n{" "*18}{"0.00     "*5}'):
        """
        Create the lines in pcf file between Data for PHASE to Profile
            Args:
                Spg (str): space group
                Pattern (int): if 0 old format
                               else new format
                command (list): command to put in command line
        """

        if (self.Biso is None) or (self.Spg is None):
            raise ValueError('self.Biso or self.Spg are None')

        obji = self[item]
        wiks = self.wiks
        other_sites = self.other_sites

        pcr_lines = []
        pcr_lines.append('!  Data for PHASE number:   1\n')
        pcr_lines.append('!' + '-' * 72 + '\n')
        pcr_lines.append(f'{title:s} \n!\n')
        if commands:
            pcr_lines.append(commands)
            pcr_lines.append('\n')

        Nat = sum([len(i) for i in obji.values()]) + len(other_sites)
        if patterns:
            if not(hasattr(Npr, '__iter__')):
                Npr = [Npr] * patterns
            if not(hasattr(Nsp_Ref, '__iter__')):
                Nsp_Ref = [Nsp_Ref] * patterns
            pcr_lines.append('!Nat Dis Ang Jbt Isy Str Furth        ATZ     Nvk More\n')
            pcr_lines.append(f'{Nat:d}   0   0   0   0   0   0       0   0   0\n')
            pcr_lines.append(f'!Contributions (0/1) of this phase to the  {patterns:d} patterns\n')
            pcr_lines.append(' 1' * patterns + '\n')
            for i in range(patterns):
                pcr_lines.append(f'!Irf Npr Jtyp  Nsp_Ref Ph_Shift for Pattern#  {i+1:d}\n')
                pcr_lines.append(f'{4 if sincry else 0:d}   {Npr[i]:d}    0      {Nsp_Ref[i]:d}      0\n')
                pcr_lines.append(f'! Pr1    Pr2    Pr3   Brind.   Rmua   Rmub   Rmuc     for Pattern#  {i+1:d}\n')
                pcr_lines.append(f'0.000  0.000  0.000  0.000  0.000  {Rmub:3.2f}  0.000\n')

        else:
            pcr_lines.append('!Nat Dis Ang Pr1 Pr2 Pr3 Jbt Irf Isy Str Furth       ATZ    Nvk Npr More\n')
            pcr_lines.append(f'{Nat:d}   0   0 0.0 0.0 1.0   {4 if sincry else 0:d}   0   0   0   0      0      0   {Npr:d}   0\n')

        pcr_lines.append('!\n!\n')
        pcr_lines.append(f'{self.Spg:s}                 <--Space group symbol\n')
        pcr_lines.append('!Atom   Typ       X        Y        Z     Biso       Occ     In Fin N_t Spc /Codes\n')

        if other_sites:
            for o_sl, o_si in other_sites.items():
                val = (o_sl, o_si['elem'], o_si['coor'], o_si["Biso"], o_si["c_occ"], f'  {postSi}\n')
                pcr_lines.append('{:3s}    {:5s}   {:s} {:2.4f}   {:1.5f}{:s}'.format(*val))

        for sl, si in _wiks(wiks).items():
            for spc, n in obji[sl].items():
                val = (sl + spc, spc, si['coor'], self.Biso, n / wiks['general']['m'], f'  {postAt}\n')
                pcr_lines.append('{:3s}    {:5s}   {:s} {:2.4f}   {:1.5f}{:s}'.format(*val))

        return pcr_lines

    def values_set(self, seq, nam):
        try:
            delattr(self, nam)
        except KeyError:
            pass
        except AttributeError:
            pass
        setattr(self, nam, propieta(nam, self, seq))
        self.__value__set__.append(nam)

    def scatter_sites(self, atom, site, ReSC, label=''):
        """ hl =high limit for test
        """
        plt.xlabel('model nb.')
        plt.title('%s %s' % (label, site))
        if isinstance(ReSC, str):
            plt.ylabel(ReSC)
            ReSC = getattr(self, ReSC)
        ReSC = np.array(ReSC)
        for i in range(self.wiks[site]['m'] + 1):
            cond = '== %d' % i  # Define condition
            Mod_i = self.filter(site, atom, cond, N=1)
            i_legend = '%s %s:%d' % (atom, site, i)  # Define label
            if len(Mod_i) > 0:
                plt.scatter(Mod_i, ReSC[Mod_i], marker='s', label=i_legend)
        plt.legend()

    def scatter_site(self, index, ReSC, label='', marker='+',
                     color='r', size=900):
        """ plot a cross on the index
            hl =high limit for test
        """
        legend = self[index].v_str(remove=[self.buffer])
        if isinstance(ReSC, str):
            ReSC = getattr(self, ReSC)
        plt.scatter([index], [ReSC[index]], marker=marker,
                    c=color, s=size, label=legend)
        plt.legend()

    def __getitem__(self, subscript):
        self._kargs = {'wiks': self.wiks,
                       'other_sites': self.other_sites,
                       'buffer': self.buffer,
                       'Spg': self.Spg,
                       'Biso': self.Biso}
        if isinstance(subscript, int):
            return super().__getitem__(subscript)
        if isinstance(subscript, list):
            subscript = np.array(subscript)
        if isinstance(subscript, tuple):
            subscript = np.array(subscript)
        if isinstance(subscript, np.ndarray):
            if subscript.dtype == bool:
                mout = mod_obj([i for i, j in zip(self, subscript) if j],
                               **self._kargs)
            if subscript.dtype.kind == 'i':
                mout = mod_obj([self[int(i)]for i in subscript],
                               **self._kargs)
        elif isinstance(subscript, slice):
            mout = mod_obj(super().__getitem__(subscript),
                           **self._kargs)
        else:
            raise KeyError('not valid key')
        for vals in self.__value__set__:
            seq = [getattr(i, vals) for i in mout]
            mout.values_set(seq, vals)
        return mout

    def __mul__(self, other):
        assert self.wiks == other.wiks, 'different wiks'
        assert self.buffer == other.buffer, 'different buffer'

        first = self._convert_mod_list([self.buffer])
        second = other._convert_mod_list([other.buffer])

        m_l = first * second

        return m_l.convert_database(add=self.buffer)

    def __add__(self, other):
        assert self.wiks == other.wiks, 'different wiks'
        assert self.buffer == other.buffer, 'different buffer'

        first = self._convert_mod_list([self.buffer])
        second = other._convert_mod_list([other.buffer])

        m_l = first + second

        return m_l.convert_database(add=self.buffer)

    def __getnewargs_ex__(self):
        return ([i for i in self],), self._kargs
