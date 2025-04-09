# -*- coding: utf-8 -*-
# molcomp.py

"""set of funcion for atomic weight calculation

the modules contain some data
N_av            constant   avogadro number
Faraday         constant   Faraday constant        (C/mol) n coulomb equal to a mole of e- 
elements        list       Names of atoms
atomic_weigh    dict       Atomic weight of atoms  uma
bond_distances  dict       bond distance           Angstrom
"""

#: avoGadRo number
N_av = 6.02214129e23  # avocado number


Faraday = 96485.3329     # faraday n electron in 1 coulomb


atomic_weigh = {"H": 1.0079, "He": 4.0026, "Li": 6.941, "Be": 9.0122,
                "B": 10.811, "C": 12.0107, "N": 14.0067, "O": 15.9994,
                "F": 18.9984, "Ne": 20.1797, "Na": 22.9897, "Mg": 24.305,
                "Al": 26.9815, "Si": 28.0855, "P": 30.9738, "S": 32.065,
                "Cl": 35.453, "Ar": 39.948, "K": 39.0983, "Ca": 40.078,
                "Sc": 44.9559, "Ti": 47.867, "V": 50.9415, "Cr": 51.9961,
                "Mn": 54.938, "Fe": 55.845, "Co": 58.9332, "Ni": 58.6934,
                "Cu": 63.546, "Zn": 65.39, "Ga": 69.723, "Ge": 72.64,
                "As": 74.9216, "Se": 78.96, "Br": 79.904, "Kr": 83.8,
                "Rb": 85.4678, "Sr": 87.62, "Y": 88.9059, "Zr": 91.224,
                "Nb": 92.9064, "Mo": 95.94, "Tc": 98, "Ru": 101.07,
                "Rh": 102.906, "Pd": 106.42, "Ag": 107.868, "Cd": 112.411,
                "In": 114.818, "Sn": 118.71, "Sb": 121.76, "Te": 127.6,
                "I": 126.904, "Xe": 131.293, "Cs": 132.905, "Ba": 137.327,
                "La": 138.905, "Ce": 140.116, "Pr": 140.908, "Nd": 144.24,
                "Pm": 145, "Sm": 150.36, "Eu": 151.964, "Gd": 157.25,
                "Tb": 158.925, "Dy": 162.5, "Ho": 164.93, "Er": 167.259,
                "Tm": 168.934, "Yb": 173.04, "Lu": 174.967, "Hf": 178.49,
                "Ta": 180.948, "W": 183.84, "Re": 186.207, "Os": 190.23,
                "Ir": 192.217, "Pt": 195.078, "Au": 196.966, "Hg": 200.59,
                "Tl": 204.383, "Pb": 207.2, "Bi": 208.98, "Po": 209, "At": 210,
                "Rn": 222, "Fr": 223, "Ra": 226, "Ac": 227, "Th": 232.038,
                "Pa": 231.036, "U": 238.029, "Np": 237, "Pu": 244, "Am": 243,
                "Cm": 247, "Bk": 247, "Cf": 251, "Es": 252, "Fm": 257,
                "Md": 258, "No": 259, "Lr": 262, "Rf": 261, "Db": 262,
                "Sg": 266, "Bh": 264, "Hs": 277, "Mt": 268}

import re
at_w = atomic_weigh


atom_p = re.compile('([A-Z][a-z]?)(\d*\.?\d*)')
braket_p = re.compile('(\([\w.]*\))(\d*\.?\d*)')


def mul(x, y):
    return str(float(x) * float(y)) if (x and y) else x or y


def longjoin(x, y):
    return "".join(["".join((item[0], mul(item[1], y))) for item in x])


def longjoin_space(x, y):
    return " ".join(["".join((item[0], mul(item[1], y))) for item in x])


def weight(formula):
    """Calculate the atomic weight for one formula
    """
    sample = c_formula(formula)
    return sample.MW


class c_formula():
    """Class defining formula
       a way to renormalize a text chemistry formuala
       ----------------
       ex.
       ----------------
       H2O= c_formula('H2O')
    """

    def __init__(self, Formula):
        if isinstance(Formula, dict):
            self.formula = Formula
            self.brute = ' '.join([x[0] + str(x[1])
                                   for x in list(Formula.items())])
        else:
            self.start_formula = Formula
            self.__bruteformula__()
        self.__WP_c__()

    def __bruteformula__(self):
        stringa = self.start_formula

        def inbraket(grb):
            s1 = re.findall(atom_p, grb.group(0))
            return longjoin(s1, grb.group(2))
        while True:
            if stringa.find(")") > -1:
                stringa = re.sub(braket_p, inbraket, stringa)
            else:
                form = re.findall(atom_p, stringa)
                self.formula = {}
                for ele, sto in form:
                    sto = sto if sto else 1.0
                    if ele in self.formula.keys():
                        self.formula[ele] += sto
                    else:
                        self.formula[ele] = sto
                self.brute = longjoin_space(form, "")
                return

    def __MW_c__(self):
        """molecular weight calculation
        """
        self.MW = 0
        for i, j in re.findall(atom_p, self.brute):
            self.MW += at_w[i] * float(j) if j else at_w[i]

    def __WP_c__(self):
        """weight % calculation
        """
        if not(hasattr(self, "MW")):
            self.__MW_c__()
            self.WP = {}
        for i, j in re.findall(atom_p, self.brute):
            self.WP[i] = at_w[i] * \
                float(j) / self.MW if j else at_w[i] / self.MW

    def Omol_c(self, grammi):
        self.Omol = (grammi / self.MW) * self.formula["O"]
        # print self.Omol


def exchange(mol1, x1, mol2, x2):
    return (mol1 * x1 + mol2 * x2) / (mol1 + mol2)


if __name__ == "__main__":
    while True:
        formula = input(
            "\n######################################\n\
            Write formula or type quit to exit\n\n")
        if formula == "quit":
            break
        sample = c_formula(formula)
        formula2 = input("""
                Which information M =molecular weigh
                W= weigh percent
                B= bruteformula
                O= Number of mole of O
                E= number of O18 Exchange iteration

                It is possible more letter example (BWM)
                """)
        if formula2 == "":
            formula2 = "BMW"
        for i in formula2:
            if i == "M":
                print("\nMolecular weight:\n ", sample.MW, " uma")
            elif i == "B":
                print("\nBrute formula:\n ", sample.brute)
            elif i == "W":
                print("\nWeight percent")
                for j in sample.WP:
                    print(j, " = ", round(sample.WP[j], 6) * 100, " %")
            elif i == "O":
                gram = input("indicate the grams of materials  ")
                sample.Omol_c(float(gram))
                print(sample.Omol, "Mole of O in ",
                      gram, " grams of ", formula)
            elif i == "E":
                v_mole = input(
                    "\nindicate the number of mole in the vessel   ")
                percent18 = 0
                gram = input("indicate the grams of materials             ")
                sample.Omol_c(float(gram))
                jiter = 0
                while percent18 < .99:
                    percent18 = exchange(
                        sample.Omol, percent18, float(v_mole), 1)
                    jiter += 1
                    print("Exchange ", jiter, "O18 present in the sample ",
                          round(percent18 * 100, 2), "%")
            pass
            print("\n\n\n\n")
