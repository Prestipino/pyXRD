#!/usr/bin/env python
##############################################################################
#  by Lello
##############################################################################

"""class L
"""

from .pt_tables import pt_p
from . import transformations as tr
import copy
# :Author transformations:
#  `Christoph Gohlke <http://www.lfd.uci.edu/~gohlke/>`_
import math
from numpy import pi, dot, allclose, array, mean, vstack, tile
import numpy as np
import Dans_Diffraction as dans


si_imolecule = True
try:
    import imolecule
except ImportError:
    si_imolecule = False

#from imolecule import draw, generate
#from imolecule.format_converter import json_to_pybel

_EXACT_COSD = {
    0.0: +1.0, 60.0: +0.5, 90.0: 0.0, 120.0: -0.5,
    180.0: -1.0, 240.0: -0.5, 270.0: 0.0, 300.0: +0.5
}

_gen_pre = 5
_tol_r = 1e-6
_tol_abs = 1e-8


def filtCh(string):
    return ''.join(filter(str.isalpha, string))


def cosd(x):
    """Return the cosine of x (measured in degrees).
    Avoid round-off errors for exact cosine values.
    """
    rv = _EXACT_COSD.get(x % 360.0)
    if rv is None:
        rv = math.cos(math.radians(x))
    return rv


def sind(x):
    """Return the sine of x (measured in degrees).
    Avoid round-off errors for exact sine values.
    """
    return cosd(90.0 - x)


class Atom(dict):
    def __init__(self, element=None, location=None, label=None, **kwds):
        dict.__init__(self, **kwds)
        if element is None:
            raise ValueError('element must be differet from None')
        location = array(location)
        self.label = label
        self.update({'element': element, 'location': location})

    def __add__(self, other):
        out = copy.deepcopy(self)
        if isinstance(other, Atom):
            out['location'].__iadd__(other['location'])
        out['location'].__iadd__(other)
        return out

    def __iadd__(self, other):
        self['location'].__iadd__(other)

    def __radd__(self, other):
        return self['location'] + other

    def __sub__(self, other):
        out = copy.deepcopy(self)
        if isinstance(other, Atom):
            out['location'].__isub__(other['location'])
        out['location'].__isub__(other)
        return out

    def __isub__(self, other):
        self['location'].__isub__(other)

    def __rsub__(self, other):
        return -self['location'] + other

    def __neg__(self):
        out = copy.deepcopy(self)
        out['location'] *= -1
        return out

    def __mul__(self, other):
        out = copy.deepcopy(self)
        if isinstance(other, Atom):
            out['location'].__imul__(other['location'])
        out['location'].__imul__(other)
        return out

    def __imul__(self, other):
        self['location'].__imul__(other)

    def __matmul__(self, other):
        out = copy.deepcopy(self)
        out['location'] = out['location'] @ other
        return out

    def __round__(self, digit):
        out = copy.deepcopy(self)
        out['location'] = np.round(out['location'], digit)
        return out



class Bond(dict):
    def __init__(self, atoms=None, order=1, **kwds):
        dict.__init__(self, **kwds)
        self.update({'atoms': atoms, 'order': order})


class CMolec(list):
    def __init__(self, label=None, atoms=None):
        if atoms:
            super().__init__(item for item in atoms)
        else:
            super().__init__()
        self.label = label
        self.basis = array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
        self.bonds = []

    def __getitem__(self, subscript):
        if subscript is None:
            return self[:]
        if isinstance(subscript, int):
            return super().__getitem__(subscript)
        if isinstance(subscript, list):
            subscript = np.array(subscript)
        if isinstance(subscript, tuple):
            subscript = np.array(subscript)
        if isinstance(subscript, np.ndarray):
            if subscript.dtype == bool:
                mout = CMolec(self.label,
                              [i for i, j in zip(self, subscript) if j])
            elif subscript.dtype.kind == 'i':
                mout = CMolec(self.label, [self[int(i)]for i in subscript])
            elif subscript.dtype.kind == '<U2':
                mout = CMolec(self.label,
                              [a for a in self if a.label in list(subscript)])
        elif isinstance(subscript, slice):
            mout = CMolec(self.label, super().__getitem__(subscript))
        else:
            raise KeyError('not valid key')
        return mout

    def __repr__(self):
        out = str()
        for i, j in enumerate(self):
            out = "%s %s-%s %s\n" % (out, str(i), j.label, j.__repr__())
        return out

    def __check_pos__(self, pos):
        return not(any([allclose(pos, i['location']) for i in self[:]]))

    def __findCell__(self):
        a = tr.vector_norm(self.basis[:, 0])
        b = tr.vector_norm(self.basis[:, 1])
        c = tr.vector_norm(self.basis[:, 2])
        alpha = tr.angle_between_vectors(self.basis[:, 1], self.basis[:, 2])
        alpha = round(math.degrees(abs(alpha)), 3)
        beta = tr.angle_between_vectors(self.basis[:, 0], self.basis[:, 2])
        beta = round(math.degrees(abs(beta)), 3)
        gamma = tr.angle_between_vectors(self.basis[:, 0], self.basis[:, 1])
        gamma = round(math.degrees(abs(gamma)), 3)
        return array([a, b, c, alpha, beta, gamma])

    def __frac2cart__(self, cell):
        cosa = cosd(cell[3])
        cosb = cosd(cell[4])
        cosg, sing = cosd(cell[5]), sind(cell[5])
        vol = cell[0] * cell[1] * cell[2]
        vol *= np.sqrt(1 - cosa**2 - cosb**2 - cosg **
                         2 + 2 * cosa * cosb * cosg)
        matrix = array([0.0] * 9)
        matrix.resize(3, 3)
        matrix[0, 0] = cell[0]
        matrix[0, 1] = cell[1] * cosg
        matrix[0, 2] = cell[2] * cosb
        matrix[1, 1] = cell[1] * sing
        matrix[1, 2] = cell[2] * (cosa - cosb * cosg) / sing
        matrix[2, 2] = vol / (cell[0] * cell[2] * sing)
        return matrix

    def search_bonds(self, min_d=0.65, max_d=3.2, cov_r=True):
        bonds = search_bond(self, min_d=min_d, max_d=max_d, cov=cov_r)
        self.bonds = [Bond(**i) for i in bonds]

    def export(self, filename=None, format='moldraw'):
        ''' convert to 
        moldraw
        matrix
        m45 : for jana rigid body

        '''
        cell = self.__findCell__().round(2)
        output = list()
        if format == 'moldraw':
            stringa = '{0:2d}   {1: 3.5f} {2: 3.5f} {3: 3.5f}'
            output.append('TITLE')
            output.append(self.label if self.label else ' ')
            output.append('CELL')
            output.append(' '.join(map(str, cell)))
            output.append('COORD')
            for i_atom in self:
                an = pt_p(i_atom['element'], 'Z')
                output.append(stringa.format(an, *i_atom['location']))
            output.append('0 0.0 0.0 0.0')
            if self.bonds:
                def flatten(l): return [str(item)
                                        for sublist in l for item in sublist['atoms']]
                output.append('CONNB')
                output.append(str(len(self.bonds)))
                lines = len(self.bonds) // 16
                for i in range(lines):
                    output.append(
                        ' '.join(flatten(self.bonds[i * 16:i * 16 + 16])))
                if len(self.bonds) % 16:
                    output.append(' '.join(flatten(self.bonds[lines * 16:])))
        if format == 'mld':
            stringa = '{0:2d}   {1: 3.5f} {2: 3.5f} {3: 3.5f}'
            output.append(self.label if self.label else 'TITLE')
            output.append('pyXRD')
            Counts_line = '{0:d} {1:d} 0 0 0 0 0 V2000'.format(len(self),  len(self.bonds)  )
            output.append(Counts_line)
            #for i_atom in self:            

        if format == 'm45':
            stringa = '{0:9s}{jo:2d}{jo:3d}     {jo:1.6f}'
            stringa += '{1: 1.6f}{2: 1.6f}{3: 1.6f}  {jj:1d}'
            output.append('cell ' + ' '.join(map(str, cell)))
            output.append('pgroup C1 \nscdist C-C 1.52 ')
            for j, i_at in enumerate(self):
                an = '{0:s}{1:d}'.format(i_at['element'], j + 1)
                output.append(stringa.format(
                    an, *i_at['location'], jo=1, jj=0))
        if format == 'matrix':
            output = vstack([i['location'] for i in self])

        if filename:
            with open(filename, 'w') as filefile:
                filefile.write('\n'.join(output))
            return
        else:
            return output

    def geom_center(self, subset=None):
        return np.mean(self[subset].xyz, axis=0)

    @property
    def xyz(self):
        return np.array([ele['location'] for ele in self])

    @xyz.setter
    def xyz(self, xyz):
        for ele, pos in zip(self, xyz):
            ele['location'] = pos

    def atom_list(self, subset=None):
        """ element is a list of element to transform newly generated atoms
            (must have the same dimension of subset)
        """
        def check_type(x, y): return all(isinstance(z, y) for z in x)

        if subset is None:
            subset = self[:]
        elif not(isinstance(subset, (list, tuple))):
            subset = list(subset)
        if check_type(subset, (str, str)):
            subset = [a for a in self if a.label in subset]
        elif check_type(subset, Atom):
            pass
        elif check_type(subset, int):
            subset = [self[i] for i in subset]
        elif isinstance(subset, Atom):
            subset = [subset]
        else:
            raise ValueError('subset should be a list of atom \
                                \/label/integer or an atom')
        return subset

    @classmethod
    def import_from(cls, data, format='auto'):
        if format == 'm45':
            try:
                indata = open(data)
                data_st = indata.readlines()
                indata.close()
            except IOError:
                data_st = data.split('\n')
            atomlist = []
            for il, line in enumerate(data_st):
                if len(line.split()) == 0:
                    continue
                    print('x')
                elif line.split()[0] == 'cell':
                    jolly, a, b, c, al, be, ga = line.split()
                    cell = list(map(float, [a, b, c, al, be, ga]))
                    fmatrix = self.__frac2cart__(cell)
                elif line.split()[0] == 'scdist':
                    jolly, scdist, sclabel = line.split()
                elif il > 3:
                    line.replace('-', ' -')
                    label, jolly, jo, occ, x, y, z, sym = line.split()
                    xyz = array(list(map(float, [x, y, z])))
                    atomlist.append({'element': label[0],
                                     'location': dot(fmatrix, xyz)})
            j_son = {'atoms': atomlist}

        elif format == 'auto' and data[-3:] == 'mol' or format == 'moldraw':
            try:
                indata = open(data)
                data_st = indata.readlines()
                indata.close()
            except IOError:
                data_st = data.split('\n')
            ######## search atoms #########
            cell = list(map(float, data_st[3].split()))
            if cell == [1.0] * 3 + [90.0] * 3:
                fmatrix = array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
            else:
                fmatrix = self.__frac2cart__(cell)
            atomlist = []
            for line in data_st[5:]:
                Zxyz = array(list(map(float, line.split())))
                if Zxyz[0] < 1:
                    break
                atomlist.append({'element': pt_p(int(Zxyz[0]), 'sym'),
                                 'location': dot(fmatrix, Zxyz[1:])})
            j_son = {'atoms': atomlist}
            ######## search bonds #########
            bond_l = ['CONNB' in line for line in data_st]
            bond_l = bond_l.index(True) + 1 if True in bond_l else False
            bond_n = int(data_st[bond_l]) if bond_l else 0
            if bond_n != 0:
                bonds = []
                for line in data_st[bond_l + 1:]:
                    bonds.extend(line.split())
                    if len(bonds) == 2 * bond_n:
                        bonds = list(map(int, bonds))
                        bonds = [bonds[i * 2:i * 2 + 2] for i in range(bond_n)]
                        break
                j_son['bonds'] = [Bond(i) for i in bonds]

        elif format == 'auto' and data[-3:] == 'xyz' or format == 'xyz':
            try:
                indata = open(data)
                data_st = indata.readlines()
                indata.close()
            except IOError:
                data_st = data.split('\n')
            j_son = {'name': data_st[1]}
            data = np.genfromtxt(data_st[2:2 + int(data_st[0])],
                                 dtype=['S2', 'f', 'f', 'f'],
                                 names=['e', 'x', 'y', 'z'])
            j_son['atoms'] = [{'element': a['e'].decode("utf-8").strip(),
                               'location': np.array([a['x'], a['y'], a['z']])}
                              for a in data]

        elif format == 'auto' or format == 'json' or isinstance(data, dict):
            j_son = data

        output = cls(label=j_son.get('name', None))
        for i, item in enumerate(j_son['atoms']):
            output.append(Atom(**item))
        if 'bonds' in j_son:
            output.bonds = j_son['bonds']
        else:
            output.search_bonds()
        return output

    def genR(self, angle, axis,
             subset=None, rem_old=False):
        '''generate atoms by one rotation 
           angle = degree
           axis = axis along the rotation
           subset list of labels of atom subjected to the operation
        '''
        angle = angle / 180.0 * pi
        Rmat = tr.rotation_matrix(angle, axis)[:3, :3].T
        for atom in self[subset]:
            new = round(atom @ Rmat, _gen_pre)
            if rem_old:
                atom['location'] = new['location']
            else:
                if self.__check_pos__(new['location']):
                    self.append(new)

    def genM(self, point, normal,
             subset=None, elements=None, rem_old=False):
        '''generate atoms by a mirror
           point = passing from the plane
           norml = axis normal the mirror
           subset list of labels of atom subjected
        '''
        if isinstance(point, Atom):
            point = point['location']
        Rmat = tr.reflection_matrix(point, normal)[:3, :3].T

        for atom in self[subset]:
            new = round(atom @ Rmat, _gen_pre)
            if rem_old:
                atom['location'] = new['location']
            else:
                if self.__check_pos__(new['location']):
                    self.append(new)

    def genC(self, order, axis,
             subset=None):
        '''generate atoms by M simmetry
           order = Corder  ex C1 C2 C 3
           axis = axis along the rotation
           subset list of labels of atom subjected
        '''
        angle = 360.0 / order
        subset = self[subset]
        for iC in range(1, order):
            Rmat = tr.rotation_matrix(angle * iC, axis)[:3, :3].T
            for atom in subset:
                new = round(atom @ Rmat, _gen_pre)
                if self.__check_pos__(new['location']):
                    self.append(new)

    def genT(self, vector, lenght=None,
             subset=None, rem_old=False):
        '''generate atoms by translation along a vector
           vector = array light
           lenght = how much is translate
           subset list of labels of atom subjected
        '''
        if isinstance(vector, Atom):
            vector = vector['location']
        if lenght:
            vector = array(vector) / tr.vector_norm(vector) * lenght
        for atom in self[subset]:
            new = round(atom + vector, _gen_pre)
            if rem_old:
                atom['location'] = new['location']
            else:
                if self.__check_pos__(new['location']):
                    self.append(new)

    def genI(self, point=[0, 0, 0],
             subset=None, elements=None, rem_old=False):
        '''generate atoms by inversion respect a point
           point : invesion point
           subset list of labels of atom subjected
        '''
        if isinstance(point, Atom):
            point = point['location']

        for atom in self[subset]:
            new = round(-atom + (2 * point), _gen_pre)
            if rem_old:
                atom['location'] = new['location']
            else:
                if self.__check_pos__(new['location']):
                    self.append(new)

    def allig(self, vector1, vector2,
              subset=None, elements=None, rem_old=True):
        """allign two vectors
        the two vector could be also two atoms
        """
        if isinstance(vector1, Bond):
            vector1 = self[vector1['atoms'][0]] - self[vector1['atoms'][1]]
        if isinstance(vector1, Atom):
            vector1 = vector1['location']
        if isinstance(vector2, Atom):
            vector2 = vector1['location']
        axis = tr.vector_product(vector1, vector2)
        angle = tr.angle_between_vectors(vector1, vector2) / pi * 180
        self.genR(angle, axis, subset, elements, rem_old)

    def center(self):
        self.genT(-self.geom_center(), rem_old=True)

    if si_imolecule:
        def draw(self, bonds=True, cell=False,
                 camera_type='orthographic', **options):
            """
            options = {
              drawingType: Can be "ball and stick", wireframe, "space filling"
              camera_type:  Can be "perspective" or orthographic"
              shader: can be "toon", "basic", "phong", or "lambert"
            to underline an atom define a key color in the atom
            };

            """
            j_son = {"atoms": list(self)}
            for atom in j_son['atoms']:
                atom['element'] = filtCh(atom['element'])
            if bonds:
                j_son['bonds'] = [{i: di[i] for i in ['atoms', 'order']}
                                  for di in self.bonds]
            if cell:
                j_son['unitcell'] = self.basis
            imolecule.draw(j_son, format='json',
                           camera_type=camera_type, **options)

    def change_basis(self, transf_mat):
        """ perform a base change X'=XA 
            X  are the coordinate in the old bases
            X' are the coordinate in the new bases
            A is the tranformation matrix composed by 
            X' rappresentation of X basis vectors
        """
        transf_mat = array(transf_mat)
        for j, item in enumerate(self):
            self[j]['location'] = dot(item['location'], transf_mat)
        for im, jm in zip(*transf_mat.nonzero()):
            transf_mat[im, jm] = transf_mat[im, jm]**-1
        self.basis = dot(self.basis, transf_mat.T)
        return

    def sel_elem(self, subset):
        # if type_del=='element':
        if not(isinstance(subset, list)):
            subset = [subset]
        return [j for j, at in enumerate(self) if at['element'] in subset]

    def calculate_scattering(self, hkl, radiation=None):
        """
        """
        elems = np.array([ele['element'] for ele in self], dtype=str)
        x, y, z = np.array([ele['location'] for ele in self], dtype=np.float).T

        hkl = np.asarray(hkl, dtype=np.float).reshape([-1, 3])
        self.basis_R = np.linalg.inv(self.basis).T
        hkl_q = np.dot(hkl, self.basis_R)
        hkl_qm = np.sqrt(np.sum(hkl_q**2, axis=1))
        s2 = (hkl_qm / 2) ** 2

        # ### Scattering function f0
        if radiation == 'electron':
            fqe = dans.fc.electron_scattering_factor(elems, 2 * hkl_qm * pi)
        elif radiation == 'X-ray':
            fqe = dans.fc.xray_scattering_factor_WaasKirf(elems, 2 * hkl_qm * pi)
        elif radiation == 'neutron':
            fqe = dans.fc.neutron_scattering_length(elems)
        elif radiation == 'florentine':
            datasc = np.genfromtxt('f0_peng.dat', skip_header=0, names=True,
                                   encoding='ascii', delimiter=',')

            all_elements = list(datasc['Element'])
            try:
                index = [all_elements.index(el) for el in elems]
            except ValueError as ve:
                raise Exception('Element not available: %s' % ve)
            datasc = datasc[index]

            fqe = np.zeros([len(hkl_qm), len(elems)])
            # Loop over elements
            for n, atom in datasc:
                # Array multiplication over Qmags
                f = atom['a1'] * np.exp(-atom['b1'] * s2) + \
                    atom['a2'] * np.exp(-atom['b2'] * s2) + \
                    atom['a3'] * np.exp(-atom['b3'] * s2) + \
                    atom['a4'] * np.exp(-atom['b4'] * s2) + \
                    atom['a5'] * np.exp(-atom['b5'] * s2)
                fqe[:, n] = f

        # debye-waller
        try:
            B = np.array([ele['B'] for ele in self])
        except KeyError:
            B = 1
        DW = np.exp(-s2[:, None] * B)

        # occ
        try:
            occ = np.array([ele['occ'] for ele in self], dtype=np.float)
        except KeyError:
            occ = 1

        # phase term
        phase_sf = np.exp(-2j * np.pi * (hkl[:, 0:1] * x
                                         + hkl[:, 1:2] * y
                                         + hkl[:, 2:3] * z))

        # f0 * phase
        return hkl_q, np.sum(DW * phase_sf * fqe * occ, axis=1)


def distance(vector):
    return tr.vector_norm(vector)


def search_bond(molecule, min_d=0.65, max_d=3.20, cov=True):
    location = molecule.export(format='matrix')
    bonds = list()
    for i, atom in enumerate(location):
        vdist = (location - tile(atom, (len(molecule), 1)))**2
        vdist = np.sqrt(np.sum(vdist, axis=1))
        for j, dist in enumerate(vdist[i:]):
            if (dist < min_d) or (dist > max_d):
                continue
            el_i = filtCh(molecule[i]['element'])
            el_j = filtCh(molecule[i + j]['element'])
            if cov:
                if dist > pt_p(el_i, 'cov_r') + pt_p(el_j, 'cov_r'):
                    continue
            at_type = frozenset((el_i, el_j))
            bonds.append(
                {'bond_l': dist, 'elems': at_type, 'atoms': [i, i + j]})
    return bonds