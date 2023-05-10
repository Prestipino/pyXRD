try:
    from Dans_Diffraction.classes_crystal import Crystal, Cell
except ImportError:
    print('Dans_Diffraction not installed, no periodic structure functionality')
from .pt_tables import pt_p, N_av
from struct import pack
import numpy as np
from .bvparm2016 import valence_param as vbs
from .bvparm2016 import s_softBV
# library installed spglib Atsushi Togo and Isao Tanaka
import spglib
from . import MBV
#import pyximport; pyximport.install()

import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second


_EXACT_COSD = {
    0.0: +1.0, 60.0: +0.5, 90.0: 0.0, 120.0: -0.5,
    180.0: -1.0, 240.0: -0.5, 270.0: 0.0, 300.0: +0.5
}

_tol_r = 1e-6
_tol_abs = 1e-8


def cosd(x):
    """Return the cosine of x (measured in degrees).
    Avoid round-off errors for exact cosine values.
    """
    rv = _EXACT_COSD.get(x % 360.0)
    if rv is None:
        rv = np.cos(np.radians(x))
    return rv


def sind(x):
    """Return the sine of x (measured in degrees).
    Avoid round-off errors for exact sine values.
    """
    return cosd(90.0 - x)


def __type2D__(x):
    xx = x.replace('+', ' +').replace('-', ' -').split(' ')
    if len(xx) == 2:
        return [xx[0], float(xx[1])]
    if len(xx) == 1:
        return [xx[0], 0.0]
    else:
        return


def __type2A__(x):
    return x.replace('+', ' +').replace('-', ' -').split(' ')[0]


class Crystal(Crystal):

    @classmethod
    def import_from(cls, data, format='auto'):
        """
        import from other format
        available format are:
            moldraw
            cfl
            spglib __babel
        """
        # ## utility functions###########################
        def strip_float(x):
            return float(x.split('(')[0])
        # ###############################################
        try:
            indata = open(data)
            data_st = indata.readlines()
            indata.close()
        except IOError as x:
            data_st = data.split('\n')
            if len(data_st) < 2:
                raise x
        except TypeError:
            pass
        # ###############################################
        if format == 'auto' and data[-3:] == 'mol' or format == 'moldraw':
            print('moldraw')

            # ####### search atoms #########
            cell = list(map(float, data_st[3].split()))
            if cell == [1.0] * 3 + [90.0] * 3:
                fmatrix = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
            else:
                print('ERROR')
                fmatrix = self.__frac2cart__(cell)
            atomlist = []
            for line in data_st[5:]:
                Zxyz = array(list(map(float, line.split())))
                if Zxyz[0] < 1:
                    break
                atomlist.append({'element': pt_p(int(Zxyz[0]), 'sym'),
                                 'location': Zxyz[1:]},
                                )
            j_son = {'atoms': atomlist}
        ######## search bonds #########
        elif (format == 'auto' and data[-3:].lower() == 'cfl') or format == 'crysfml':
            print('crysfml')
            Asym_atoms = dict()
            Atom_strings = ('type', 'x', 'y', 'z', 'Biso', 'cr_occ')
            for lin in data_st:
                if lin.split()[0].upper() == 'CELL':
                    Cell = np.array(list(map(strip_float, lin.split()[1:])))
                if lin.split()[0].upper() == 'SPGR':
                    Spgr = lin.upper().replace('SPGR', '').strip()
                if lin.split()[0].upper() == 'ATOM':
                    xx = lin.split()[1:8]
                    xx = xx[:2] + [strip_float(i) for i in xx[2:]]
                    if len(xx) == 7:
                        pass
                    elif len(xx) == 6:
                        xx.insert(5, 0.042)
                    assert not xx[0] in Asym_atoms, '{} label already present'.format(
                        xx[0])
                    Asym_atoms.update(
                        {xx[0]: dict(list(zip(Atom_strings, xx[1:])))})
            print(Spgr)
            SpaceGroup = GIIt.StandardizeSpcName(Spgr)
            er, Spgr = GIIt.SpcGroup(SpaceGroup)
            # check if occupatio are chemical or crystallographyc:  if one
            # occ>1
            occ_type_chem = False
            for lab, at in list(Asym_atoms.items()):
                at['sit_sym'], at['mult'], Ndup, dupDir = GIIt.SytSym(
                    [at[i] for i in 'xyz'], Spgr)
                at['occ'] = round(
                    at['cr_occ'] * Spgr['SGGmult'] * 1.0 / at['mult'], 4)
                if at['occ'] > 1.0:
                    occ_type_chem = True
            if occ_type_chem:    # se ci siamo sbagliati
                for lab, at in list(Asym_atoms.items()):
                    at['occ'], at['cr_occ'] = at['cr_occ'], round(
                        at['cr_occ'] * 1.0 * at['mult'] / Spgr['SGGmult'], 4)

            out = cls()
            out.Cell.update_cif({zip(['_cell_length_a'  ,'_cell_length_b',
                                       '_cell_length_c', '_cell_angle_alpha',
                                       '_cell_angle_beta','_cell_angle_gamma'], 
                                     Cell)})
            

            return out(
                Cell=Cell,
                Asym_atoms=Asym_atoms,
                SpaceGroup=SpaceGroup,
                Spgr=Spgr)
        ######## other cases #########
        elif (format == 'auto' and isinstance(data, tuple) or format == 'spglib'):

            AsymAtom = {}
            Atoms_cell = {}
            convert_l = {}
            x = data
            Sym = spglib.get_symmetry(x)
            for i, j in enumerate(np.unique(Sym['equivalent_atoms'])):
                label = pt_p(x[2][j], 'sym') + str(i + 1)
                AsymAtom[label] = {
                    'occ': 1,
                    'x': x[1][j][0],
                    'y': x[1][j][1],
                    'z': x[1][j][2],
                    'type': pt_p(
                        x[2][j],
                        'sym')}
                convert_l[j] = label

            Atoms_cell['label'] = [convert_l[j]
                                   for j in Sym['equivalent_atoms']]
            Atoms_cell['xyz'] = x[1]
            SG = GIIt.spgbyNum[int(spglib.get_spacegroup(
                x).split('(')[1].replace(')', ''))]
            return cls(
                basis=x[0].T,
                Asym_atoms=AsymAtom,
                SpaceGroup=SG,
                Atoms_cell=Atoms_cell)
        ######## other cases #########
        else:
            print('not recognized format')

    def __setinfo(self):
        er, self.Spgr = GIIt.SpcGroup(self.SpaceGroup)
        for lab, at in list(self.Asym_atoms.items()):
            at['sit_sym'], at['mult'], Ndup, dupDir = GIIt.SytSym(
                [at[i] for i in 'xyz'], self.Spgr)
        self.basis, B = GIIt.cell2AB(self.Cell)
        self.G, self.g = GIIt.cell2Gmat(self.Cell)
        self.info = {}
        self.info['deOrt'] = B
        self.info['Vol'] = round(np.sqrt(np.linalg.det(self.g)), 3)
        def AtomTy(x): return x.replace(
            '+', ' +').replace('-', ' -').split(' ')[0]
        self.info['LabelComp'] = {}
        self.info['Comp'] = {}
        for lab, at in list(self.Asym_atoms.items()):
            comp = round(at['occ'] * at['mult'], 3)
            self.info['LabelComp'].update({lab: comp})

            print(AtomTy(at['type']), self.info['Comp'])
            if AtomTy(at['type']) in self.info['Comp']:
                self.info['Comp'][AtomTy(at['type'])] += comp
            else:
                self.info['Comp'][AtomTy(at['type'])] = comp
        self.info['Cr_den'] = sum(
            [pt_p(i, 'At_w') * j for i, j in list(self.info['Comp'].items())]) / self.info['Vol']
        self.info['Cr_den'] = round(self.info['Cr_den'] * 1e24 / N_av, 3)
        self.info['Neutrality'] = sum(
            [
                at['occ'] *
                at['mult'] *
                __type2D__(
                    at['type'])[1] for at in list(
                    self.Asym_atoms.values())])
        if abs(self.info['Neutrality']) > 0.2:
            print('attention charge unbalanced {:4.2f}'.format(
                self.info['Neutrality']))

    def export(self, filename=None, format='vesta'):
        '''convert to moldraw
        '''
        output = list()
        if format == 'vesta':
            ext = '.vesta'
            output.append('#VESTA_FORMAT_VERSION 3.1.9\n\n')
            output.append('CRYSTAL\nTITLE')
            output.append('TITLE\n  -FILE CREATED FROM pyXRD\n\n')
            output.append('IMPORT_STRUCTURE')
            output.append('{:s}{}'.format(filename, '.cif'))
            if hasattr(self, 'grid'):
                output.append('\nIMPORT_DENSITY 1')
                output.append(
                    '+1.000000E+000 {:s}{:s}'.format(filename, '.pgrid'))
            pass
            self.export(filename=filename, format='cif')

            if hasattr(self, 'grid'):
                with open(filename + '.pgrid', 'wb') as outf:
                    outf.write(pack('4i', 3, 0, 0, 0))  # file format version
                    # Title 80 characters
                    outf.write(
                        pack('80s', self.Title.ljust(80).encode('utf-8')))
                    # gType 0 for *.ggrid, 1 for *.pgrid
                    outf.write(pack('i', 1))
                    outf.write(pack('i', 0))  # fType 0
                    outf.write(pack('i', 1))  # nVal dummy
                    outf.write(pack('i', 3))  # dimension
                    # numbers of voxels
                    outf.write(pack('3i', *self.grid.shape))
                    # Total number of voxels
                    outf.write(pack('i', self.grid.size))
                    outf.write(pack('6f', *self.Cell))  # lattice parameters
                    # for k in range(mapdata.shape[2]):
                    #    for j in range(mapdata.shape[1]):
                    #        for i in range(mapdata.shape[0]):
                    #            outf.write(pack('f', mapdata[i, j, k]))
                    grid = self.grid.T.flatten().astype(np.float32)
                    outf.write(grid.tobytes())

        if format == 'cif':
            ext = '.cif'
            stringa = '#' + '=' * 71 + '\n'
            output.append(stringa)
            output.append('# CRYSTAL DATA\n')
            stringa = '#' + '-' * 71 + '\n'
            output.append(stringa)
            output.append('data_phase_1\n\n')
            stringa = '_chemical_name_common'.ljust(
                40) + '\'xxFL-FILE IMPORTED FROM CIF-FILE:CDPOO\''
            output.append(stringa)
            stringa = '_cell_length_a'.ljust(40) + str(self.Cell[0])
            output.append(stringa)
            stringa = '_cell_length_b'.ljust(40) + str(self.Cell[1])
            output.append(stringa)
            stringa = '_cell_length_c'.ljust(40) + str(self.Cell[2])
            output.append(stringa)
            stringa = '_cell_angle_alpha'.ljust(40) + str(self.Cell[3])
            output.append(stringa)
            stringa = '_cell_angle_beta'.ljust(40) + str(self.Cell[4])
            output.append(stringa)
            stringa = '_cell_angle_gamma'.ljust(40) + str(self.Cell[5])
            output.append(stringa)
            stringa = '_space_group_name_H-M_alt'.ljust(
                40) + '\'{}\''.format(self.SpaceGroup)
            output.append(stringa)
            stringa = '_space_group_IT_number'.ljust(
                40) + '{:d}'.format(GIIt.spgbyNum.index(self.SpaceGroup))
            output.append(stringa)
            output.append('\n\nloop_')
            output.extend(['   _atom_site_label',
                           '   _atom_site_occupancy',
                           '   _atom_site_fract_x',
                           '   _atom_site_fract_y',
                           '   _atom_site_fract_z',
                           '   _atom_site_adp_type',
                           '   _atom_site_U_iso_or_equiv',
                           '   _atom_site_type_symbol'])
            for lab, atom in list(self.Asym_atoms.items()):
                stringa = '   {:<11s}{:<8.4f}'.format(lab, atom['occ'])
                stringa = '{:s}{:<14.4f}{:<14.4f}{:<14.4f}'.format(
                    stringa, atom['x'], atom['y'], atom['z'])
                stringa = '{:s}Uiso  0.004200 {:<s}'.format(
                    stringa, atom['type'])
                output.append(stringa)

        if filename:
            fullfilename = filename + ext
            with open(fullfilename, 'w') as filefile:
                filefile.write('\n'.join(output))
            return
        else:
            return output

    def __fill_cell(self):
        self.Atoms_cell = {'label': [], 'xyz': []}
        for lab, atom in list(self.Asym_atoms.items()):
            xx = GIIt.GenAtom([atom[i] for i in 'xyz'], self.Spgr)
            self.Atoms_cell['xyz'].extend([i[0] for i in xx])
            self.Atoms_cell['label'].extend([lab] * len(xx))
        self.Atoms_cell['xyz'] = np.array(self.Atoms_cell['xyz'])

    def make_box(self, m=None, center=True, s=None):
        """m lenght of the box list [x,y,z]
           s shift of the box       [x,y,z ]
        """
        self.__fill_cell()
        if m is None:
            return
        m = np.abs(np.array(m))
        for axe, mult in enumerate(m):
            a_shift = np.zeros(3)
            a_shift[axe] = 1
            for i in range(int(mult)):
                if i == 0:
                    continue
                a_s = a_shift * i
                self.Atoms_cell['xyz'] = np.vstack(
                    (self.Atoms_cell['xyz'], self.Atoms_cell['xyz'] - a_s))
                self.Atoms_cell['label'].extend(self.Atoms_cell['label'])
        pass
        if center:
            s = np.where((m - 1) / 2 > 0, (m - 1) / 2 > 0, 0) * -1
        if s is not None:
            self.Atoms_cell['xyz'] = self.Atoms_cell['xyz'] - s

    def search_distance(
            self,
            min_d=0.65,
            max_d=3.60,
            bond=False,
            stampa=True,
            **kargs):
        m_c = np.ceil(max_d / self.Cell[:3]) * 2 + 1
        # print m_c
        self.make_box(m=m_c, center=True)
        # location=molecule.export('matrix')
        for lab, asatom in list(self.Asym_atoms.items()):
            dist = self.Atoms_cell['xyz'] - \
                np.array([asatom[i] for i in 'xyz'])
            dist = np.dot(self.basis, dist.T).T
            dist *= dist
            dist = np.sqrt(np.sum(dist, axis=1))
            dis_i = np.argsort(dist)
            asatom['distances'] = []
            for j in dis_i:
                if dist[j] > min_d:
                    if dist[j] > max_d:
                        del dist
                        break
                    else:
                        asatom['distances'].append({'label': self.Atoms_cell['label'][j],
                                                    'xyz': self.Atoms_cell['xyz'][j],
                                                    'dist': round(dist[j], 3),
                                                    'type': self.Asym_atoms[self.Atoms_cell['label'][j]]['type']})
            pass
        if stampa:
            print('\n')
            for lab, asatom in list(self.Asym_atoms.items()):
                print(
                    '-' * 44,
                    '\n',
                    'Atom {} distance between {:} and {:} Ang'.format(
                        lab,
                        min_d,
                        max_d))
                print('distance    label     x       y       z')
                for dis in asatom['distances']:
                    print(
                        '{: 5.3f}        {:<5} {: 5.3f}  {: 5.3f}  {: 5.3f} '.format(
                            dis['dist'], dis['label'], *dis['xyz']))
                print('-' * 44, '\n' * 2)

    def sBVS(self, min_d=0.65, max_d=3.60, stampa=True, BvsPar=None):
        """parameters
           {Label1:{ Label2: ncode, Label2 :[Ro, b] }, species1:{species2 :n code} }
        """
        # ----------------------------------------------------------
        def symb_ok(x): return True if '+' in x or '-' in x else False

        def cou_split(x):
            sym1, val1 = x[0].replace('+', ' +').replace('-', ' -').split(' ')
            sym2, val2 = x[1].replace('+', ' +').replace('-', ' -').split(' ')
            return [sym1, int(val1), sym2, int(val2)]
        # ----------------------------------------------------------

        print('\n')
        self.search_distance(min_d=min_d, max_d=max_d, stampa=0)
        tvb = set()
        for lab, asatom in list(self.Asym_atoms.items()):
            for dis in asatom['distances']:
                tvb.add(frozenset([asatom['type'], dis['type']]))
        # tvb became a dictionary
        tvb = dict(list(zip(list(tvb), [None] * len(tvb))))

        if tvb == {}:
            print('no distance available')
            return
        if BvsPar is None:
            for couple in tvb:
                cou = list(couple)
                assert symb_ok(cou[0]), 'symbol error {:s}'.format(cou[0])

                if len(cou) == 1:
                    if cou[0][:-1] + '9' in vbs.anion:
                        inp = dict(
                            list(zip(['Cat', 'Anion'], [cou[0][:-2]] * 2)))
                    else:
                        inp = None

                if len(cou) == 2:
                    assert symb_ok(cou[1]), 'symbol error {:s}'.format(cou[1])
                    if cou[1] in vbs.anion and not(cou[0] in vbs.anion):
                        inp = dict(
                            list(zip(['Cat', 'VCat', 'Anion', 'VAnion'], cou_split(cou))))
                    elif cou[0] in vbs.anion and not(cou[1] in vbs.anion):
                        inp = dict(
                            list(zip(['Anion', 'VAnion', 'Cat', 'VCat'], cou_split(cou))))
                    else:
                        inp = None
                if inp:
                    if len(vbs.search_bvp(**inp)
                           ) > 0 or vbs.search_bvp(inp['Cat'], 9, inp['Anion']):
                        print('\n' * 3, "##" * 24)
                        try:
                            print("parameters available for {}{:+d} and {}{:+d}".format(
                                inp['Cat'], inp['VCat'], inp['Anion'], inp['VAnion']))
                            print("##" * 24, '\n')
                            print("defined ox. states ")
                            print(vbs.search_bvp(**inp))
                            print("not specific")
                            print(vbs.search_bvp(inp['Cat'], 9, inp['Anion']))
                        except BaseException:
                            print("parameters available for  ", cou)
                            print(vbs.search_bvp(inp['Cat'], 9, inp['Anion']))

                    else:
                        print(vbs.search_bvp(**inp), ' for ', cou)
                    print('write R0 and b or the index of an entry')
                    param = input().split()
                    print("##" * 24, '\n' * 3)
                    if len(param) == 2:
                        R0, b = list(map(float, param))
                        tvb[couple] = {"Ro": R0, "B": b}
                    if len(param) == 1:
                        index = int(param[0])
                        tvb[couple] = {
                            "Ro": vbs[index]["Ro"], "B": vbs[index]["B"]}
                    else:
                        pass

                else:
                    print(
                        'write R0 and b for ',
                        cou if len(cou) == 2 else cou * 2)
                    param = input().split()
                    if len(param) == 2:
                        R0, b = list(map(float, param))
                        tvb[couple] = {"Ro": R0, "B": b}
        pass

        tvb = dict((i, j) for i, j in list(tvb.items()) if j)
        print(tvb)
        for lab, asatom in list(self.Asym_atoms.items()):
            for dis in asatom['distances']:
                xx = frozenset([asatom['type'], dis['type']])
                if xx in tvb:
                    if asatom['type'] in vbs.anion and not dis['type'] in vbs.anion:
                        pr = -1
                    else:
                        pr = 1
                    dis['vi'] = pr * \
                        np.exp((tvb[xx]["Ro"] - dis['dist']) / tvb[xx]["B"])
                    dis['vi'] *= self.Asym_atoms[dis['label']]['occ']

        if stampa:
            print('\n')
            for lab, asatom in list(self.Asym_atoms.items()):
                summa = 0.0
                print(
                    '-' * 44,
                    '\n',
                    'Atom {} BVS between {:} and {:} Ang'.format(
                        lab,
                        min_d,
                        max_d))
                print('distance    label    bond-valence')
                for dis in asatom['distances']:
                    if 'vi' in dis:
                        print(
                            '{: 5.3f}        {:<5}    {: 3.2f}  '.format(
                                dis['dist'], dis['label'], dis['vi']))
                        summa += dis['vi']
                print('-' * 44)
                print('bond valence sum for {:s} ={: 3.2f}'.format(lab, summa))
                print('-' * 44, '\n' * 2)

    @staticmethod
    def crys2spglib(x):
        x.__fill_cell()
        numbers = [__type2A__(x.Asym_atoms[i]['type'])
                   for i in x.Atoms_cell['label']]
        numbers = [pt_p(i, 'Z') for i in numbers]
        return (x.basis.T, x.Atoms_cell['xyz'], numbers)

    def find_primitive(self):
        self.__fill_cell()
        cell = crystal.crys2spglib(self)
        self.primitive = crystal.import_from(
            spglib.find_primitive(cell), format='spglib')

    def makeP1(self):
        if hasattr(self, 'Atoms_cell'):
            pass
        else:
            self.__fill_cell()
        Asym = {}
        i = 0
        for lab, xyz in zip(self.Atoms_cell['label'], self.Atoms_cell['xyz']):
            i += 1
            sym = __type2A__(self.Asym_atoms[lab]['type'])
            label = sym + str(i)
            Asym[label] = {
                'occ': self.Asym_atoms[lab]['occ'],
                'x': xyz[0],
                'y': xyz[1],
                'z': xyz[2],
                'type': self.Asym_atoms[lab]['type']}
        return crystal(Cell=self.Cell, Asym_atoms=Asym, SpaceGroup='P1')

    def BVSmap(self, cation, sampling, min_d=0.65, max_d=3.60, BVpars=None):
        """ cor.BVSmap('Cd', [20,20,20])
            BVpars {'S-2':[index], 'Te-2':[R0, b]} or 'soft'

        """
        ## utility functions#############################
        def giv_typ(x): return self.Asym_atoms[i]['type']
        ################################################
        m_c = np.ceil(max_d / self.Cell[:3]) * 2 + 1
        # print m_c
        self.make_box(m=m_c, center=True)
        # reduction on other atom to the minimum
        # atoms far
        le = max_d / self.Cell[:3]
        co = self.Atoms_cell['xyz']
        xx = np.where((co[:,
                          0] < le[0] + 1) * (co[:,
                                                0] > -le[0]) * (co[:,
                                                                   1] < le[1] + 1) * (co[:,
                                                                                         1] > -le[1]) * (co[:,
                                                                                                            2] < le[2] + 1) * (co[:,
                                                                                                                                  2] > -le[2]))
        self.Atoms_cell['xyz'] = self.Atoms_cell['xyz'][xx]
        self.Atoms_cell['label'] = np.array(self.Atoms_cell['label'])[xx]
        # atoms cation removal
        co = self.Atoms_cell['label']
        xx = [i for i in range(len(co)) if not __type2A__(
            cation) in self.Atoms_cell['label'][i]]
        self.Atoms_cell['label'] = self.Atoms_cell['label'][xx]
        self.Atoms_cell['xyz'] = self.Atoms_cell['xyz'][xx]
        #####################################################

        # Ask BV param
        labels = [
            i for i in list(
                self.Asym_atoms.keys()) if not(
                __type2A__(cation) in i)]
        BV_p = []
        if BVpars:
            if isinstance(BVpars, dict):
                for i in labels:
                    if giv_typ(i) in list(BVpars.keys()):
                        param = BVpars[giv_typ(i)]
                        if len(param) == 2:
                            BV_p.append(param)
                        elif len(param) == 1:
                            index = int(param[0])
                            BV_p.append([vbs[index]["Ro"], vbs[index]["B"]])
                        else:
                            raise ValueError('pippo')
                    else:
                        BV_p.append([0, 0])

            elif BVpars == 'soft':
                for i in labels:
                    param = s_softBV(cation, giv_typ(i))
                    BV_p.append([param[0], param[1]])
            else:
                raise ValueError('not clear param')

        else:
            for i in labels:
                print(
                    "parameters available for {} and {}".format(
                        cation, __type2A__(i)))
                print("##" * 24, '\n')
                print("defined ox. states ")
                print(
                    vbs.search_bvp(
                        cation, Anion=__type2A__(
                            self.Asym_atoms[i]['type'])))
                print('write R0 and b or the index of an entry')
                param = input().split()
                print("##" * 24, '\n' * 3)
                if len(param) == 2:
                    R0, b = list(map(float, param))
                    BV_p.append([R0, b])
                if len(param) == 1:
                    index = int(param[0])
                    BV_p.append([vbs[index]["Ro"], vbs[index]["B"]])
                else:
                    BV_p.append([0, 0])

        ##
        BV_p = np.array(BV_p, dtype=np.double)
        labels_n = np.array([labels.index(i)
                             for i in self.Atoms_cell['label']], dtype=np.int)
        self.grid = MBV.BVM(
            self.basis,
            np.array(
                sampling,
                dtype=np.int),
            labels_n,
            self.Atoms_cell['xyz'],
            BV_p,
            min_d,
            max_d)
        winsound.Beep(frequency, duration)

        # math.exp((R0-Ri)/B)

        # bonds=list()
        # for i,atom in enumerate(location):
        #    vdist=(location- tile(atom,(len(molecule),1)))**2
        #    vdist= sqrt(sum(vdist, axis=1))
        #    for j, dist in enumerate(vdist[i:]):
        #        if (dist < min_d) or (dist > max_d):
        #            continue
        #        el_i, el_j = molecule[i]['element'],molecule[i+j]['element']
        #        if cov:
        #            if dist > pt_p(el_i,'cov_r')+pt_p(el_j,'cov_r'):
        #               continue
        #        at_type=frozenset((el_i, el_j))
        #        bonds.append({'bond_l':dist, 'elems':at_type, 'atoms':[i,i+j]})
        # return bonds
