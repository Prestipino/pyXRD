#!/usr/bin/env python
##############################################################################
#  by Lello
##############################################################################

"""class L
"""

from .pt_tables import pt_p
from . import transformations as tr
# :Author transformations:
#  `Christoph Gohlke <http://www.lfd.uci.edu/~gohlke/>`_
import math
from numpy import pi, dot, allclose, array, mean, vstack, tile, sum, sqrt
#from imolecule import draw, generate
#from imolecule.format_converter import json_to_pybel

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
        if isinstance(other, Atom):
            return self['location'] + other['location']
        return self['location'].__add__(other)

    def __radd__(self, other):
        return self['location'] + other

    def __sub__(self, other):
        if isinstance(other, Atom):
            return self['location'] - other['location']
        return self['location'].__sub__(other)

    def __rsub__(self, other):
        return self['location'] - other

    def __neg__(self):
        return self['location'].__neg__()


class Bond(dict):
    def __init__(self, atoms=None, order=1, **kwds):
        dict.__init__(self, **kwds)
        self.update({'atoms': atoms, 'order': order})


class CMolec(list):
    def __init__(self, label=None, *args, **kwds):
        list.__init__(self, *args, **kwds)
        self.label = label
        self.basis = array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
        self.bonds = []

    def __getslice__(self, index1, index2):
        out = super(CMolec, self).__getslice__(index1, index2)
        return CMolec(self.label, out)

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
        vol *= math.sqrt(1 - cosa**2 - cosb**2 - cosg **
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

    def __genGen__(self, func, subset=None, elements=None, rem_old=False):
        """General generator
        """
        subset = self.atom_list(subset)

        def ele_list(li, ele): return ele if ele else [
            i['element'] for i in li]
        atom_list = list(zip(ele_list(subset, elements), subset))

        def roundix(x): return round(x, 5)
        for elex, atom in atom_list:
            new_pos = list(map(roundix, func(atom['location'])))
            if rem_old:
                self.remove(atom)
            if self.__check_pos__(new_pos):
                self.append(Atom(elex, new_pos, atom.label))

    @property
    def geom_center(self, subset=None):
        _zero = array([0.0, 0.0, 0.0])
        for i in range(len(_zero)):
            _zero[i] = mean([j + 0 for j in self])
        return _zero

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

    def import_from(self, data, format='auto', refresh=False):
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

        if format == 'pybel':
            self.pybel_m = data
        if refresh:
            for i, item in enumerate(j_son['atoms']):
                self[i].update(Atom().update(j_son['atoms']))
        else:
            self.__init__(label=j_son.get('name', None))
            for i, item in enumerate(j_son['atoms']):
                self.append(Atom(**item))
            if 'bonds' in j_son:
                self.bonds = j_son['bonds']

    def genR(self, angle, axis,
             subset=None, elements=None, rem_old=False):
        '''generate atoms by one rotation 
           angle = degree
           axis = axis along the rotation
           subset list of labels of atom subjected to the operation
        '''
        angle = angle / 180.0 * pi
        Rmat = tr.rotation_matrix(angle, axis)[:3, :3].T

        def Rotate(pos): return dot(pos, Rmat)
        self.__genGen__(Rotate, subset, elements, rem_old)

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

        def Mirror(pos): return dot(pos, Rmat)
        self.__genGen__(Mirror, subset, elements, rem_old)

    def genC(self, order, axis,
             subset=None, elements=None):
        '''generate atoms by M simmetry
           order = Corder  ex C1 C2 C 3
           axis = axis along the rotation
           subset list of labels of atom subjected
        '''
        angle = 360.0 / order
        subset = self.atom_list(subset)
        for iterC in range(1, order):
            self.genR(angle * iterC, axis, subset, elements, False)

    def genT(self, vector, lenght=None,
             subset=None, elements=None, rem_old=False):
        '''generate atoms by translation along a vector
           vector = Corder  ex C1 C2 C 3
           lenght = how much is translate
           subset list of labels of atom subjected
        '''
        if isinstance(vector, Atom):
            vector = vector['location']
        if lenght:
            vector = array(vector) / tr.vector_norm(vector) * lenght

        def Translate(pos): return array(pos) + array(vector)
        self.__genGen__(Translate, subset, elements, rem_old)

    def genI(self, point=[0, 0, 0],
             subset=None, elements=None, rem_old=False):
        '''generate atoms by inversion respect a point
           point : invesion point
           subset list of labels of atom subjected
        '''
        if isinstance(point, Atom):
            point = point['location']

        def Inv(pos): return ((array(pos) - array(point)) * -1) + array(point)
        self.__genGen__(Inv, subset, elements, rem_old=False)

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

#    def draw(self, bond=True):
#        self.to__pybel(bond=bond)
#        draw(self.pybel_m, format='pybel')

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

    def del_elem(self, subset):
        # if type_del=='element':
        if not(isinstance(subset, list)):
            subset = [subset]
        delete_list = [j for j in self if j['element'] in subset]
        for i in delete_list:
            self.remove(i)
        return

    def sel_elem(self, subset):
        # if type_del=='element':
        if not(isinstance(subset, list)):
            subset = [subset]
        delete_list = [j for j in self if j['element'] in subset]
        return delete_list

#    def to__pybel(self, bond=True):
#        '''convert to pybel addinf a pybel properties
#        '''
#        if self.bonds:
#            self.pybel_m = json_to_pybel(
#                {'atoms': self, 'bonds': self.bonds}, infer_bonds=bond)
#        else:
#            self.pybel_m = json_to_pybel({'atoms': self}, infer_bonds=bond)
def distance(vector):
    return tr.vector_norm(vector)


def search_bond(molecule, min_d=0.65, max_d=3.20, cov=True):
    location = molecule.export('matrix')
    bonds = list()
    for i, atom in enumerate(location):
        vdist = (location - tile(atom, (len(molecule), 1)))**2
        vdist = sqrt(sum(vdist, axis=1))
        for j, dist in enumerate(vdist[i:]):
            if (dist < min_d) or (dist > max_d):
                continue
            el_i, el_j = molecule[i]['element'], molecule[i + j]['element']
            if cov:
                if dist > pt_p(el_i, 'cov_r') + pt_p(el_j, 'cov_r'):
                    continue
            at_type = frozenset((el_i, el_j))
            bonds.append(
                {'bond_l': dist, 'elems': at_type, 'atoms': [i, i + j]})
    return bonds


