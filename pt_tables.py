#!usr/bin/python
# -*- coding: utf-8 -*-
# pt_table.py

"""set of funcion for atomic weight calculation

the modules contain some data
N_av            constant   avogadro number
Faraday         constant   Faraday constant        (C/mol) n coulomb equal to a mole of e- 
elements        list       Names of atoms
atomic_weigh    dict       Atomic weight of atoms  uma
bond_distances  dict       bond distance           Angstrom
"""

from Dans_Diffraction import functions_crystallography as crys_tool



def pt_p(atom, property):
    """available property
       'At_w'    : atomic weight  
       'Z'       : atomic number   
       'cov_r'   : covalent radii
       'sym'     : atomic symbol        
       'e_conf'  : electronic conf.
       'ox_st'   : oxydation state
       'bon_dis' : typical bond distances
       'edges'   : x-ray edges
       -------------------------
       ex.
       pt_p(34, 'sym')
       pt_p('Cu', 'At_w')
       
    """
    ava_prop=['At_w', 'Z', 'cov_r', 'sym', 'e_conf', 'ox_st', 'edges', 'bon_dis']
    if atom:    
        if isinstance(atom, int):
           if property=='sym':return elements[atom]
           else: atom = elements[atom]   
    assert atom in elements, 'element unknown'
    assert property in ava_prop, 'property unknown'
    if property=='e_conf' : return e_conf(pt_prop[atom]['Z'])
    if property=='ox_st'  : return set(Common_OxStates[pt_prop[atom]['Z']]) 
    if property=='edges' : return Edge_energy[atom]
    if property=='bon_dis'  :
       a = [i for i in bond_distances.keys() if atom in i.split('-')]
       return {x: bond_distances[x] for x in a}
    return pt_prop[atom][property] 


#: avoGadRo number
N_av=6.02214129e23      #avocado number

#: Faraday constant
Faraday= 96485.3329     # faraday n electron in 1 coulomb


# Regle approximative de Klechkowski pour le remplissage des électrons dans les atomes
Klechkowski=['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']


from scipy import interpolate


elements = ["", "H" , "He", "Li", "Be", "B" , "C" , "N" , "O" , "F" , "Ne", "Na",
            "Mg", "Al", "Si", "P" , "S" , "Cl", "Ar", "K" , "Ca", "Sc", "Ti", "V" , "Cr", "Mn",
            "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y" ,
            "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I" ,
            "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho",
            "Er", "Tm", "Yb", "Lu", "Hf", "Ta", "W" , "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl",
            "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cu"] 
            
pt_prop ={'H'  : {'Z': 1, 'At_w': 1.0079, 'cov_r': 0.31, 'PauliX': 2.2},
          'He' : {'Z': 2, 'At_w': 4.0026, 'cov_r': 0.28, 'PauliX': 0.0},
          'Li' : {'Z': 3, 'At_w': 6.941, 'cov_r': 1.28, 'PauliX': 0.98},
          'Be' : {'Z': 4, 'At_w': 9.0122, 'cov_r': 0.96, 'PauliX': 1.57},
          'B' : {'Z': 5, 'At_w': 10.811, 'cov_r': 0.85, 'PauliX': 2.04},
          'C' : {'Z': 6, 'At_w': 12.0107, 'cov_r': 0.76, 'PauliX': 2.55},
          'N' : {'Z': 7, 'At_w': 14.0067, 'cov_r': 0.71, 'PauliX': 3.04},
          'O' : {'Z': 8, 'At_w': 15.9994, 'cov_r': 0.66, 'PauliX': 3.44},
          'F' : {'Z': 9, 'At_w': 18.9984, 'cov_r': 0.57, 'PauliX': 3.98},
          'Ne' : {'Z': 10, 'At_w': 20.1797, 'cov_r': 0.58, 'PauliX': 0.0},
          'Na' : {'Z': 11, 'At_w': 22.9897, 'cov_r': 1.66, 'PauliX': 0.93},
          'Mg' : {'Z': 12, 'At_w': 24.305, 'cov_r': 1.41, 'PauliX': 1.31},
          'Al' : {'Z': 13, 'At_w': 26.9815, 'cov_r': 1.21, 'PauliX': 1.61},
          'Si' : {'Z': 14, 'At_w': 28.0855, 'cov_r': 1.11, 'PauliX': 1.9},
          'P' : {'Z': 15, 'At_w': 30.9738, 'cov_r': 1.07, 'PauliX': 2.19},
          'S' : {'Z': 16, 'At_w': 32.065, 'cov_r': 1.05, 'PauliX': 2.58},
          'Cl' : {'Z': 17, 'At_w': 35.453, 'cov_r': 1.02, 'PauliX': 3.16},
          'Ar' : {'Z': 18, 'At_w': 39.948, 'cov_r': 1.06, 'PauliX': 0.0},
          'K' : {'Z': 19, 'At_w': 39.0983, 'cov_r': 2.03, 'PauliX': 0.82},
          'Ca' : {'Z': 20, 'At_w': 40.078, 'cov_r': 1.76, 'PauliX': 1.0},
          'Sc' : {'Z': 21, 'At_w': 44.9559, 'cov_r': 1.7, 'PauliX': 1.36},
          'Ti' : {'Z': 22, 'At_w': 47.867, 'cov_r': 1.6, 'PauliX': 1.54},
          'V' : {'Z': 23, 'At_w': 50.9415, 'cov_r': 1.53, 'PauliX': 1.63},
          'Cr' : {'Z': 24, 'At_w': 51.9961, 'cov_r': 1.39, 'PauliX': 1.66},
          'Mn' : {'Z': 25, 'At_w': 54.938, 'cov_r': 1.39, 'PauliX': 1.55},
          'Fe' : {'Z': 26, 'At_w': 55.845, 'cov_r': 1.32, 'PauliX': 1.83},
          'Co' : {'Z': 27, 'At_w': 58.9332, 'cov_r': 1.26, 'PauliX': 1.88},
          'Ni' : {'Z': 28, 'At_w': 58.6934, 'cov_r': 1.24, 'PauliX': 1.91},
          'Cu' : {'Z': 29, 'At_w': 63.546, 'cov_r': 1.69, 'PauliX': 1.9},
          'Zn' : {'Z': 30, 'At_w': 65.39, 'cov_r': 1.22, 'PauliX': 1.65},
          'Ga' : {'Z': 31, 'At_w': 69.723, 'cov_r': 1.22, 'PauliX': 1.81},
          'Ge' : {'Z': 32, 'At_w': 72.64, 'cov_r': 1.2, 'PauliX': 2.01},
          'As' : {'Z': 33, 'At_w': 74.9216, 'cov_r': 1.19, 'PauliX': 2.18},
          'Se' : {'Z': 34, 'At_w': 78.96, 'cov_r': 1.2, 'PauliX': 2.55},
          'Br' : {'Z': 35, 'At_w': 79.904, 'cov_r': 1.2, 'PauliX': 2.96},
          'Kr' : {'Z': 36, 'At_w': 83.8, 'cov_r': 1.16, 'PauliX': 3.0},
          'Rb' : {'Z': 37, 'At_w': 85.4678, 'cov_r': 2.2, 'PauliX': 0.82},
          'Sr' : {'Z': 38, 'At_w': 87.62, 'cov_r': 1.95, 'PauliX': 0.95},
          'Y' : {'Z': 39, 'At_w': 88.9059, 'cov_r': 1.9, 'PauliX': 1.22},
          'Zr' : {'Z': 40, 'At_w': 91.224, 'cov_r': 1.75, 'PauliX': 1.33},
          'Nb' : {'Z': 41, 'At_w': 92.9064, 'cov_r': 1.64, 'PauliX': 1.6},
          'Mo' : {'Z': 42, 'At_w': 95.94, 'cov_r': 1.54, 'PauliX': 2.16},
          'Tc' : {'Z': 43, 'At_w': 98, 'cov_r': 1.47, 'PauliX': 1.9},
          'Ru' : {'Z': 44, 'At_w': 101.07, 'cov_r': 1.46, 'PauliX': 2.2},
          'Rh' : {'Z': 45, 'At_w': 102.906, 'cov_r': 1.42, 'PauliX': 2.28},
          'Pd' : {'Z': 46, 'At_w': 106.42, 'cov_r': 1.39, 'PauliX': 2.2},
          'Ag' : {'Z': 47, 'At_w': 107.868, 'cov_r': 1.45, 'PauliX': 1.93},
          'Cd' : {'Z': 48, 'At_w': 112.411, 'cov_r': 1.44, 'PauliX': 1.69},
          'In' : {'Z': 49, 'At_w': 114.818, 'cov_r': 1.42, 'PauliX': 1.78},
          'Sn' : {'Z': 50, 'At_w': 118.71, 'cov_r': 1.39, 'PauliX': 1.96},
          'Sb' : {'Z': 51, 'At_w': 121.76, 'cov_r': 1.39, 'PauliX': 2.05},
          'Te' : {'Z': 52, 'At_w': 127.6, 'cov_r': 1.38, 'PauliX': 2.1},
          'I' : {'Z': 53, 'At_w': 126.904, 'cov_r': 1.39, 'PauliX': 2.66},
          'Xe' : {'Z': 54, 'At_w': 131.293, 'cov_r': 1.4, 'PauliX': 2.6},
          'Cs' : {'Z': 55, 'At_w': 132.905, 'cov_r': 2.44, 'PauliX': 0.79},
          'Ba' : {'Z': 56, 'At_w': 137.327, 'cov_r': 2.15, 'PauliX': 0.89},
          'La' : {'Z': 57, 'At_w': 138.905, 'cov_r': 2.07, 'PauliX': 1.1},
          'Ce' : {'Z': 58, 'At_w': 140.116, 'cov_r': 2.04, 'PauliX': 1.12},
          'Pr' : {'Z': 59, 'At_w': 140.908, 'cov_r': 2.03, 'PauliX': 1.13},
          'Nd' : {'Z': 60, 'At_w': 144.24, 'cov_r': 2.01, 'PauliX': 1.14},
          'Pm' : {'Z': 61, 'At_w': 145, 'cov_r': 1.99, 'PauliX': 1.13},
          'Sm' : {'Z': 62, 'At_w': 150.36, 'cov_r': 1.98, 'PauliX': 1.17},
          'Eu' : {'Z': 63, 'At_w': 151.964, 'cov_r': 1.98, 'PauliX': 1.2},
          'Gd' : {'Z': 64, 'At_w': 157.25, 'cov_r': 1.96, 'PauliX': 1.2},
          'Tb' : {'Z': 65, 'At_w': 158.925, 'cov_r': 1.94, 'PauliX': 1.1},
          'Dy' : {'Z': 66, 'At_w': 162.5, 'cov_r': 1.92, 'PauliX': 1.22},
          'Ho' : {'Z': 67, 'At_w': 164.93, 'cov_r': 1.92, 'PauliX': 1.23},
          'Er' : {'Z': 68, 'At_w': 167.259, 'cov_r': 1.89, 'PauliX': 1.24},
          'Tm' : {'Z': 69, 'At_w': 168.934, 'cov_r': 1.9, 'PauliX': 1.25},
          'Yb' : {'Z': 70, 'At_w': 173.04, 'cov_r': 1.87, 'PauliX': 1.1},
          'Lu' : {'Z': 71, 'At_w': 174.967, 'cov_r': 1.87, 'PauliX': 1.27},
          'Hf' : {'Z': 72, 'At_w': 178.49, 'cov_r': 1.75, 'PauliX': 1.3},
          'Ta' : {'Z': 73, 'At_w': 180.948, 'cov_r': 1.7, 'PauliX': 1.5},
          'W' : {'Z': 74, 'At_w': 183.84, 'cov_r': 1.62, 'PauliX': 2.36},
          'Re' : {'Z': 75, 'At_w': 186.207, 'cov_r': 1.51, 'PauliX': 1.9},
          'Os' : {'Z': 76, 'At_w': 190.23, 'cov_r': 1.44, 'PauliX': 2.2},
          'Ir' : {'Z': 77, 'At_w': 192.217, 'cov_r': 1.41, 'PauliX': 2.2},
          'Pt' : {'Z': 78, 'At_w': 195.078, 'cov_r': 1.36, 'PauliX': 2.28},
          'Au' : {'Z': 79, 'At_w': 196.966, 'cov_r': 1.36, 'PauliX': 2.54},
          'Hg' : {'Z': 80, 'At_w': 200.59, 'cov_r': 1.32, 'PauliX': 2.0},
          'Tl' : {'Z': 81, 'At_w': 204.383, 'cov_r': 1.45, 'PauliX': 1.62},
          'Pb' : {'Z': 82, 'At_w': 207.2, 'cov_r': 1.46, 'PauliX': 1.87},
          'Bi' : {'Z': 83, 'At_w': 208.98, 'cov_r': 1.48, 'PauliX': 2.02},
          'Po' : {'Z': 84, 'At_w': 209, 'cov_r': 1.4, 'PauliX': 2.0},
          'At' : {'Z': 85, 'At_w': 210, 'cov_r': 1.5, 'PauliX': 2.2},
          'Rn' : {'Z': 86, 'At_w': 222, 'cov_r': 1.5, 'PauliX': 2.2},
          'Fr' : {'Z': 87, 'At_w': 223, 'cov_r': 2.6, 'PauliX': 0.7},
          'Ra' : {'Z': 88, 'At_w': 226, 'cov_r': 2.21, 'PauliX': 0.9},
          'Ac' : {'Z': 89, 'At_w': 227, 'cov_r': 2.15, 'PauliX': 1.1},
          'Th' : {'Z': 90, 'At_w': 232.038, 'cov_r': 2.06, 'PauliX': 1.3},
          'Pa' : {'Z': 91, 'At_w': 231.036, 'cov_r': 2.0, 'PauliX': 1.5},
          'U' : {'Z': 92, 'At_w': 238.029, 'cov_r': 1.96, 'PauliX': 1.38},
          'Np' : {'Z': 93, 'At_w': 237, 'cov_r': 1.9, 'PauliX': 1.36},
          'Pu' : {'Z': 94, 'At_w': 244, 'cov_r': 1.87, 'PauliX': 1.28},
          'Am' : {'Z': 95, 'At_w': 243, 'cov_r': 1.8, 'PauliX': 1.13},}

Common_OxStates =   [(None),
                     ( -1 ,  1 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  1 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  1 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  1 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     ( -4 , -3 , -2 , -1 ,  1 ,  2 ,  3 ,  4 ),   
                     ( -3 ,  3 ,  5 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     ( -2 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     ( -1 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  1 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     ( -4 ,  4 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     ( -3 ,  3 ,  5 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     ( -2 ,  2 ,  4 ,  6 ,  0 ,  0 ,  0 ,  0 ),
                     ( -1 ,  1 ,  3 ,  5 ,  7 ,  0 ,  0 ,  0 ),
                     (  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  1 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  4 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  5 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  6 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  4 ,  7 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  3 ,  6 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     ( -4 ,  2 ,  4 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     ( -3 ,  3 ,  5 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     ( -2 ,  2 ,  4 ,  6 ,  0 ,  0 ,  0 ,  0 ),
                     ( -1 ,  1 ,  3 ,  5 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  1 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  4 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  5 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  4 ,  6 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  4 ,  7 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  4 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  4 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  1 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     ( -4 ,  2 ,  4 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     ( -3 ,  3 ,  5 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     ( -2 ,  2 ,  4 ,  6 ,  0 ,  0 ,  0 ,  0 ),
                     ( -1 ,  1 ,  3 ,  5 ,  7 ,  0 ,  0 ,  0 ),
                     (  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  1 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  4 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  4 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  5 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  4 ,  6 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  4 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  4 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  4 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  4 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  1 ,  2 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  1 ,  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  4 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     ( -2 ,  2 ,  4 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     ( -1 ,  1 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  1 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  4 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  5 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  6 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  5 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  4 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  2 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  3 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  4 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  5 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  6 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  7 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ),
                     (  8 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 ,  0 )]           

def e_conf(ne):
    """print electronic configuration for an atom
    """
    assert ne>0, 'atomic number should > 0'
    ep={'s':2, 'p':6, 'd':10, 'f':14}
    NG=[2,10,18,36,54,86]
    NL=[i for i in NG if ne-i>0]
    if NL==[]: 
           return '1s{:d}'.format(ne)
    else: NL=NL[-1]       
    NG_i='{:d}s'.format(NG.index(NL)+2)
    start=Klechkowski.index(NG_i)
    old ='[{:s}] '.format(pt_p(NL, 'sym'))
    ne-=NL
    for i in Klechkowski[start:]:
        ne-= ep[i[-1]]
        if ne > 0:
           old = '{:s}{:s}{:d} '.format(old,i,ep[i[-1]])
        else:
           return   '{:s}{:s}{:d} '.format(old,i,ep[i[-1]]+ne)
             
QN_Transition = ["K","L1","L2","L3"]
Transition =	[ {"K": "1s"},	{"L1": "2s"},	{"L2": "2p1/2"},	{"L3": "2p3/2"},	{"M1": "3s"},	{"M2": "3p1/2"},	{"M3": "3p3/2 "},	{"M4": "3d3/2"},	{"M5": "3d5/2"},	{"N1": "4s"},	{"N2": "4p1/2"},	{"N3": "4p3/2"},	{"N4": "4d3/2"},	{"N5": "4d5/2"},	{"N6": "4f5/2"},	{"N7": "4f7/2"},	{"O1": "5s"},	{"O2": "5p1/2 "},	{"O3": "5p3/2"},	{"O4": "5d3/2"},	{"O5": "5d5/2"},	{"P1": "6s"},	{"P2": "6p1/2"},	{"P3": "6p3/2"} ],
Edge_energy ={                                                                            
   "H"  :    [13.6  ],
   "He" :    [24.6  ],
   "Li" :    [54.7  ],
   "Be" :    [111.5 ],                                                                                                                                                                                                                                                                                                        
   "B"  :    [188   ],
   "C"  :    [284.2 ],      
   "N"  :    [409.9   , 37.3 ],                             
   "O"  :    [543.1   , 41.6 ],   
   "F"  :    [696.7],         
   "Ne" :    [870.2   , 48.5    , 21.7    , 21.6    ],
   "Na" :    [1070.8  , 63.5    , 30.65   , 30.81   ],                                                         
   "Mg" :    [1303.0  , 88.7    , 49.78   , 49.50   ],
   "Al" :    [1559.6  , 117.8   , 72.95   , 72.55   ],                                                                                                                                                                                                                                                                                                                                                                                                           
   "Si" :    [1839    , 149.7   , 99.82   , 99.42   ],
   "P"  :    [2145.5  , 189     , 136     , 135     ],
   "S"  :    [2472    , 230.9   , 163.6   , 162.5   ],
   "Cl" :    [2822.4  , 270     , 202     , 200     ],
   "Ar" :    [3205.9  , 326.3   , 250.6   , 248.4   , 29.3    , 15.9    , 15.7   ],
   "K"  :    [3608.4  , 378.6   , 297.3   , 294.6   , 34.8    , 18.3    , 18.3   ],
   "Ca" :    [4038.5  , 438.4   , 349.7   , 346.2   , 44.3    , 25.4    , 25.4   ],
   "Sc" :    [4492    , 498.0   , 403.6   , 398.7   , 51.1    , 28.3    , 28.3   ],
   "Ti" :    [4966    , 560.9   , 460.2   , 453.8   , 58.7    , 32.6    , 32.6   ],
   "V"  :    [5465    , 626.7   , 519.8   , 512.1   , 66.3    , 37.2    , 37.2   ],
   "Cr" :    [5989    , 696.0   , 583.8   , 574.1   , 74.1    , 42.2    , 42.2   ],
   "Mn" :    [6539    , 769.1   , 649.9   , 638.7   , 82.3    , 47.2    , 47.2   ],
   "Fe" :    [7112    , 844.6   , 719.9   , 706.8   , 91.3    , 52.7    , 52.7   ],
   "Co" :    [7709    , 925.1   , 793.2   , 778.1   , 101.0   , 58.9    , 59.9   ],
   "Ni" :    [8333    , 1008.6  , 870.0   , 852.7   , 110.8   , 68.0    , 66.2   ],
   "Cu" :    [8979    , 1096.7  , 952.3   , 932.7   , 122.5   , 77.3    , 75.1   ],
   "Zn" :    [9659    , 1196.2  , 1044.9  , 1021.8  , 139.8   , 91.4    , 88.6  ,  10.2   ,  10.1 ],
   "Ga" :    [10367   , 1299.0  , "-"     , 1143.2  , 1116.4  , 159.5   , 103.5 ,  100.0  ,  18.7    , 18.7    ],
   "Ge" :    [11103   , 1414.6  , "-"     , 1248.1  , "-"     , 1217.0  , "-"   ,  180.1  ,  124.9   , 120.8   ,  29.8    , 29.2   ],
   "As" :    [11867   , 1527.0  , "-"     , 1359.1  , "-"     , 1323.6  , "-"   ,  204.7  ,  146.2   , 141.2   ,  41.7    , 41.7   ],
   "Se" :    [12658   , 1652.0  , "-"     , 1474.3  , "-"     , 1433.9  , "-"   ,  229.6  ,  166.5   , 160.7   ,  55.5    , 54.6   ],
   "Br" :    [13474   , 1782    , 1596    , 1550    , 257     , 189     , 182   ,  70     ,  69   ],  
   "Kr" :    [14326   , 1921    , 1730.9  , 1678.4  , 292.8   , 222.2   , 214.4 ,  95.0   ,  93.8    , 27.5    ,  14.1    , 14.1   ],
   "Rb" :    [15200   , 2065    , 1864    , 1804    , 326.7   , 248.7   , 239.1 ,  113.0  ,  112     , 30.5    ,  16.3    , 15.3   ],
   "Sr" :    [16105   , 2216    , 2007    , 1940    , 358.7   , 280.3   , 270.0 ,  136.0  ,  134.2   , 38.9    ,  21.3    , 20.1   ],
   "Y"  :    [17038   , 2373    , 2156    , 2080    , 392.0   , 310.6   , 298.8 ,  157.7  ,  155.8   , 43.8    ,  24.4    , 23.1   ],
   "Zr" :    [17998   , 2532    , 2307    , 2223    , 430.3   , 343.5   , 329.8 ,  181.1  ,  178.8   , 50.6    ,  28.5    , 27.1   ],
   "Nb" :    [18986   , 2698    , 2465    , 2371    , 466.6   , 376.1   , 360.6 ,  205.0  ,  202.3   , 56.4    ,  32.6    , 30.8   ],
   "Mo" :    [20000   , 2866    , 2625    , 2520    , 506.3   , 411.6   , 394.0 ,  231.1  ,  227.9   , 63.2    ,  37.6    , 35.5   ],
   "Tc" :    [21044   , 3043    , 2793    , 2677    , 544     , 447.6   , 417.7 ,  257.6  ,  253.9   , 69.5    ,  42.3    , 39.9   ],
   "Ru" :    [22117   , 3224    , 2967    , 2838    , 586.1   , 483.5   , 461.4 ,  284.2  ,  280.0   , 75.0    ,  46.3    , 43.2   ],
   "Rh" :    [23220   , 3412    , 3146    , 3004    , 628.1   , 521.3   , 496.5 ,  311.9  ,  307.2   , 81.4    ,  50.5    , 47.3   ],
   "Pd" :    [24350   , 3604    , 3330    , 3173    , 671.6   , 559.9   , 532.3 ,  340.5  ,  335.2   , 87.1    ,  55.7    , 50.9   ],      
   "Ag" :    [25514   , 3806    , 3524    , 3351    , 719.0   , 603.8   , 573.0 ,  374.0  ,  368.3   , 97.0    ,  63.7    , 58.3   ], 
   "Cd" :    [26711   , 4018    , 3727    , 3538    , 772.0   , 652.6   , 618.4 ,  411.9  ,  405.2   , 109.8   ,  63.9    , 63.9    , 11.7    , 10.7    ],                                                      
   "In" :    [27940   , 4238    , 3938    , 3730    , 827.2   , 703.2   , 665.3 ,  451.4  ,  443.9   , 122.9   ,  73.5    , 73.5    , 17.7    , 16.9    ],
   "Sn" :    [29200   , 4465    , 4156    , 3929    , 884.7   , 756.5   , 714.6 ,  493.2  ,  484.9   , 137.1   ,  83.6    , 83.6    , 24.9    , 23.9    ],                                                                            
   "Sb" :    [30491   , 4698    , 4380    , 4132    , 946     , 812.7   , 766.4 ,  537.5  ,  528.2   , 153.2   ,  95.6    , 95.6    , 33.3    , 32.1    ],
   "Te" :    [31814   , 4939    , 4612    , 4341    , 1006    , 870.8   , 820.0 ,  583.4  ,  573.0   , 169.4   ,  103.3   , 103.3   , 41.9    , 40.4    ],
   "I"  :    [33169   , 5188    , 4852    , 4557    , 1072    , 931     , 875   ,  630.8  ,  619.3   , 186     ,  123     , 123     , 50.6    , 48.9    ],
   "Xe" :    [34561   , 5453    , 5107    , 4786    , 1148.7  , 1002.1  , 940.6 ,  689.0  ,  676.4   , 213.2   ,  146.7   , 145.5   , 69.5    , 67.5    , "-"    , "-"     , 23.3    , 13.4    , 12.1    ],
   "Cs" :    [35985   , 5714    , 5359    , 5012    , 1211    , 1071    , 1003  ,  740.5  ,  726.6   , 232.3   ,  172.4   , 161.3   , 79.8    , 77.5    , "-"    , "-"     , 22.7    , 14.2    , 12.1    ],
   "Ba" :    [37441   , 5989    , 5624    , 5247    , 1293    , 1137    , 1063  ,  795.7  ,  780.5   , 253.5   ,  192     , 178.6   , 92.6    , 89.9    , "-"    , "-"     , 30.3    , 17.0    , 14.8    ],
   "La" :    [38925   , 6266    , 5891    , 5483    , 1362    , 1209    , 1128  ,  853    ,  836     , 274.7   ,  205.8   , 196.0   , 105.3   , 102.5   , "-"    , "-"     , 34.3    , 19.3    , 16.8    ],
   "Ce" :    [40443   , 6549    , 6164    , 5723    , 1436    , 1274    , 1187  ,  902.4  ,  883.8   , 291.0   ,  223.2   , 206.5   , 109     , "-"     , 0.1    , 0.1     , 37.8    , 19.8    , 17.0    ],
   "Pr" :    [41991   , 6835    , 6440    , 5964    , 1511    , 1337    , 1242  ,  948.3  ,  928.8   , 304.5   ,  236.3   , 217.6   , 115.1   , 115.1   , 2.0    , 2.0     , 37.4    , 22.3    , 22.3    ],
   "Nd" :    [43569   , 7126    , 6722    , 6208    , 1575    , 1403    , 1297  ,  1003.3 ,  980.4   , 319.2   ,  243.3   , 224.6   , 120.5   , 120.5   , 1.5    , 1.5     , 37.5    , 21.1    , 21.1    ],     
   "Pm" :    [45184   , 7428    , 7013    , 6459    , "-"     , 1471    , 1357  ,  1052   ,  1027    , "-"     ,  242     , 242     , 120     , 120     ],  
   "Sm" :    [46834   , 7737    , 7312    , 6716    , 1723    , 1541    , 1420  ,  1110.9 ,  1083.4  , 347.2   ,  265.6   , 247.4   , 129     , 129     , 5.2    , 5.2     , 37.4    , 21.3    , 21.3    ],
   "Eu" :    [48519   , 8052    , 7617    , 6977    , 1800    , 1614    , 1481  ,  1158.6 ,  1127.5  , 360     ,  284     , 257     , 133     , 127.7   , 0      , 0       , 32      , 22      , 22      ],  
   "Gd" :    [50239   , 8376    , 7930    , 7243    , 1881    , 1688    , 1544  ,  1221.9 ,  1189.6  , 378.6   ,  286     , 271     , "-"     , 142.6   , 8.6    , 8.6     , 36      , 28      , 21      ],
   "Tb" :    [51996   , 8708    , 8252    , 7514    , 1968    , 1768    , 1611  ,  1276.9 ,  1241.1  , 396.0   ,  322.4   , 284.1   , 150.5   , 150.5   , 7.7    , 2.4     , 45.6    , 28.7    , 22.6    ],
   "Dy" :    [53789   , 9046    , 8581    , 7790    , 2047    , 1842    , 1676  ,  1333   ,  1292.6  , 414.2   ,  333.5   , 293.2   , 153.6   , 153.6   , 8.0    , 4.3     , 49.9    , 26.3    , 26.3    ],
   "Ho" :    [55618   , 9394    , 8918    , 8071    , 2128    , 1923    , 1741  ,  1392   ,  1351    , 432.4   ,  343.5   , 308.2   , 160     , 160     , 8.6    , 5.2     , 49.3    , 30.8    , 24.1    ],
   "Er" :    [57486   , 9751    , 9264    , 8358    , 2207    , 2006    , 1812  ,  1453   ,  1409    , 449.8   ,  366.2   , 320.2   , 167.6   , 167.6   , "-"    , 4.7     , 50.6    , 31.4    , 24.7    ],
   "Tm" :    [59390   , 10116   , 9617    , 8648    , 2307    , 2090    , 1885  ,  1515   ,  1468    , 470.9   ,  385.9   , 332.6   , 175.5   , 175.5   , "-"    , 4.6     , 54.7    , 31.8    , 25.0    ],
   "Yb" :    [61332   , 10486   , 9978    , 8944    , 2398    , 2173    , 1950  ,  1576   ,  1528    , 480.5   ,  388.7   , 339.7   , 191.2   , 182.4   , 2.5    , 1.3     , 52.0    , 30.3    , 24.1    ],
   "Lu" :    [63314   , 10870   , 10349   , 9244    , 2491    , 2264    , 2024  ,  1639   ,  1589    , 506.8   ,  412.4   , 359.2   , 206.1   , 196.3   , 8.9    , 7.5     , 57.3    , 33.6    , 26.7    ],
   "Hf" :    [65351   , 11271   , 10739   , 9561    , 2601    , 2365    , 2108  ,  1716   ,  1662    , 538     ,  438.2   , 380.7   , 220.0   , 211.5   , 15.9   , 14.2    , 64.2    , 38      , 29.9    ],
   "Ta" :    [67416   , 11682   , 11136   , 9881    , 2708    , 2469    , 2194  ,  1793   ,  1735    , 563.4   ,  463.4   , 400.9   , 237.9   , 226.4   , 23.5   , 21.6    , 69.7    , 42.2    , 32.7    ],
   "W"  :    [69525   , 12100   , 11544   , 10207   , 2820    , 2575    , 2281  ,  1872   ,  1809    , 594.1   ,  490.4   , 423.6   , 255.9   , 243.5   , 33.6   , 31.4    , 75.6    , 45.3    , 36.8    ],
   "Re" :    [71676   , 12527   , 11959   , 10535   , 2932    , 2682    , 2367  ,  1949   ,  1883    , 625.4   ,  518.7   , 446.8   , 273.9   , 260.5   , 42.9   , 40.5    , 83      , 45.6    , 34.6    ],
   "Os" :    [73871   , 12968   , 12385   , 10871   , 3049    , 2792    , 2457  ,  2031   ,  1960    , 658.2   ,  549.1   , 470.7   , 293.1   , 278.5   , 53.4   , 50.7    , 84      , 58      , 44.5    ],
   "Ir" :    [76111   , 13419   , 12824   , 11215   , 3174    , 2909    , 2551  ,  2116   ,  2040    , 691.1   ,  577.8   , 495.8   , 311.9   , 296.3   , 63.8   , 60.8    , 95.2    , 63.0    , 48.0    ],
   "Pt" :    [78395   , 13880   , 13273   , 11564   , 3296    , 3027    , 2645  ,  2202   ,  2122    , 725.4   ,  609.1   , 519.4   , 331.6   , 314.6   , 74.5   , 71.2    , 101.7   , 65.3    , 51.7    ],
   "Au" :    [80725   , 14353   , 13734   , 11919   , 3425    , 3148    , 2743  ,  2291   ,  2206    , 762.1   ,  642.7   , 546.3   , 353.2   , 335.1   , 87.6   , 84.0    , 107.2   , 74.2    , 57.2    ],
   "Hg" :    [83102   , 14839   , 14209   , 12284   , 3562    , 3279    , 2847  ,  2385   ,  2295    , 802.2   ,  680.2   , 576.6   , 378.2   , 358.8   , 104.0  , 99.9    , 127     , 83.1    , 64.5    , 9.6     , 7.8     ],
   "Tl" :    [85530   , 15347   , 14698   , 12658   , 3704    , 3416    , 2957  ,  2485   ,  2389    , 846.2   ,  720.5   , 609.5   , 405.7   , 385.0   , 122.2  , 117.8   , 136.0   , 94.6    , 73.5    , 14.7    , 12.5    ],
   "Pb" :    [88005   , 15861   , 15200   , 13035   , 3851    , 3554    , 3066  ,  2586   ,  2484    , 891.8   ,  761.9   , 643.5   , 434.3   , 412.2   , 141.7  , 136.9   , 147     , 106.4   , 83.3    , 20.7    , 18.1    ],
   "Bi" :    [90524   , 16388   , 15711   , 13419   , 3999    , 3696    , 3177  ,  2688   ,  2580    , 939     ,  805.2   , 678.8   , 464.0   , 440.1   , 162.3  , 157.0   , 159.3   , 119.0   , 92.6    , 26.9    , 23.8    ],
   "Po" :    [93105   , 16939   , 16244   , 13814   , 4149    , 3854    , 3302  ,  2798   ,  2683    , 995     ,  851     , 705     , 500     , 473     , 184    , 184     , 177     , 132     , 104     , 31      , 31      ],
   "At" :    [95730   , 17493   , 16785   , 14214   , 4317    , 4008    , 3426  ,  2909   ,  2787    , 1042    ,  886     , 740     , 533     , 507     , 210    , 210     , 195     , 148     , 115     , 40      , 40      ],
   "Rn" :    [98404   , 18049   , 17337   , 14619   , 4482    , 4159    , 3538  ,  3022   ,  2892    , 1097    ,  929     , 768     , 567     , 541     , 238    , 238     , 214     , 164     , 127     , 48      , 48      , 26 ],
   "Fr" :    [101137  , 18639   , 17907   , 15031   , 4652    , 4327    , 3663  ,  3136   ,  3000    , 1153    ,  980     , 810     , 603     , 577     , 268    , 268     , 234     , 182     , 140     , 58      , 58      , 34      , 15      ,15      ],
   "Ra" :    [103922  , 19237   , 18484   , 15444   , 4822    , 4490    , 3792  ,  3248   ,  3105    , 1208    ,  1058    , 879     , 636     , 603     , 299    , 299     , 254     , 200     , 153     , 68      , 68      , 44      , 19      ,19      ],
   "Ac" :    [106755  , 19840   , 19083   , 15871   , 5002    , 4656    , 3909  ,  3370   ,  3219    , 1269    ,  1080    , 890     , 675     , 639     , 319    , 319     , 272     , 215     , 167     , 80      , 80      ],       
   "Th" :    [109651  , 20472   , 19693   , 16300   , 5182    , 4830    , 4046  ,  3491   ,  3332    , 1330    ,  1168    , 966.4   , 712.1   , 675.2   , 342.4  , 333.1   , 290     , 229     , 182     , 92.5    , 85.4    , 41.4    , 24.5    ,16.6    ],
   "Pa" :    [112601  , 21105   , 20314   , 16733   , 5367    , 5001    , 4174  ,  3611   ,  3442    , 1387    ,  1224    , 1007    , 743     , 708     , 371    , 360     , 310     , 232     , 232     , 94      , 94      ],       
   "U"  :    [115606  , 21757   , 20948   , 17166   , 5548    , 5182    , 4303  ,  3728   ,  3552    , 1439    ,  1271    , 1043    , 778.3   , 736.2   , 388.2  , 377.4   , 321     , 257     , 192     , 102.8   , 94.2    , 43.9    , 26.8    ,16.8    ]}
   



# Tabulation of curve core hole width versus Z from K. Rahkonen and K. Krause, Atomic Data and Nuclear DataTables, Vol 14, Number 2, 1974.   
gamach ={                                                                                                                       
  'K': [ [ 0.99,  10.0, 20.0, 40.0, 50.0, 60.0, 80.0,  95.1], [0.02,   0.28,  0.75,  4.8, 10.5, 21.0, 60.0, 105.0] ],
  'L1': [ [ 0.99, 18.0, 22.0, 35.0, 50.0, 52.0, 75.0,  95.1], [0.07,   3.9,   3.8,   7.0,  6.0,  3.7,  8.0,  19.0] ],
  'L2': [ [ 0.99, 17.0, 28.0, 31.0, 45.0, 60.0, 80.0,  95.1], [0.001,  0.12,  1.4,   0.8,  2.6,  4.1,  6.3,  10.5] ],
  'L3': [ [ 0.99, 17.0, 28.0, 31.0, 45.0, 60.0, 80.0,  95.1], [0.001,  0.12,  0.55,  0.7,  2.1,  3.5,  5.4,   9.0] ],
  'M1': [ [ 0.99, 20.0, 28.0, 30.0, 36.0, 53.0, 80.0,  95.1], [0.001,  1.0,   2.9,   2.2,  5.5, 10.0, 22.0,  22.0] ],
  'M2': [ [ 0.99, 20.0, 22.0, 30.0, 40.0, 68.0, 80.0,  95.1], [0.001,  0.001, 0.5,   2.0,  2.6, 11.0, 15.0,  16.0] ],
  'M3': [ [ 0.99, 20.0, 22.0, 30.0, 40.0, 68.0, 80.0,  95.1], [0.001,  0.001, 0.5,   2.0,  2.6, 11.0, 10.0,  10.0] ],
  'M4': [ [ 0.99, 36.0, 40.0, 48.0, 58.0, 76.0, 79.0,  95.1], [0.0006, 0.09,  0.07,  0.48, 1.0,  4.0,  2.7,   4.7] ],
  'M5': [ [ 0.99, 36.0, 40.0, 48.0, 58.0, 76.0, 79.0,  95.1], [0.0006, 0.09,  0.07,  0.48, 0.87, 2.2,  2.5,   4.3] ],
  'N1': [ [ 0.99, 30.0, 40.0, 47.0, 50.0, 63.0, 80.0,  95.1], [0.001,  0.001, 6.2,   7.0,  3.2, 12.0, 16.0,  13.0] ],
  'N2': [ [ 0.99, 40.0, 42.0, 49.0, 54.0, 70.0, 87.0,  95.1], [0.001,  0.001, 1.9,  16.0,  2.7, 13.0, 13.0,   8.0]],
  'N3': [ [ 0.99, 40.0, 42.0, 49.0, 54.0, 70.0, 87.0,  95.1], [0.001,  0.001, 1.9,  16.0,  2.7, 13.0, 13.0,   8.0] ],
  'N4': [ [ 0.99, 40.0, 50.0, 55.0, 60.0, 70.0, 81.0,  95.1], [0.001,  0.001, 0.15,  0.1,  0.8, 8.0,  8.0,  5.0] ],
  'N5': [ [ 0.99, 40.0, 50.0, 55.0, 60.0, 70.0, 81.0,  95.1], [0.001,  0.001, 0.15,  0.1,  0.8, 8.0,  8.0,  5.0] ],
  'N6': [ [ 0.99, 71.0, 73.0, 79.0, 86.0, 90.0, 95.0, 100.0], [0.001,  0.001, 0.05,  0.22, 0.1, 0.16, 0.5,  0.9] ],    
  'N7': [ [ 0.99, 71.0, 73.0, 79.0, 86.0, 90.0, 95.0, 100.0], [0.001,  0.001, 0.05,  0.22, 0.1, 0.16, 0.5,  0.9] ]}    


def getGamach(Z,EdgeKind):
    """getGamma function to obtain the width of core hole level
    
    input:
    Z: atomic number (integer)
    EdgeKind: kind of edge (string)
    
    output:
    width: core hole in eV
    
    example:
    getGamach(40,"L1")
    >> 8.790...."""
    
    gamach_spline = interpolate.splrep(gamach[EdgeKind][0], gamach[EdgeKind][1], s=0)
    return  interpolate.splev(Z,gamach_spline)




bond_distances={'H-H' :.74,'H-B' :1.19,'H-C' :1.09,'H-Si':1.48,'H-Ge':1.53,'H-Sn':1.70,'H-N' :1.01,'H-P' :1.44,'H-As':1.52,
                'H-O' :0.96,'H-S' :1.34,'H-Se':1.46,'H-Te':1.70,'H-F' :0.92,'H-Cl':1.27,'H-Br':1.41,'H-I' :1.61,
                'B-Cl' :1.75,                
                'C-Cl':1.54,'C--C':1.34,'C---C':1.20,'C-Si':1.85,'C-Ge':1.95,'C-Sn':2.16,'C-Pb':2.30,'C--N':1.47,'C--N':1.29,'C---N':1.16,
                'C-P':1.84,'C-O':1.43,'C--O':1.20,'C---O':1.13,'C-S':1.82,'C--S':1.60,'C-F':1.35,'C-Cl':1.77,'C-Br':1.94,'C-Si':2.14,
                'Si-Si':2.33,'Si-O':1.63,'Si-S':2.00,'Si-F':1.60,'Si-Cl':2.02,'Si-Br':2.15,'Si-I':2.43,
                'Ge-Ge':2.41,'Ge-F':1.68,'Ge-Cl':2.10,'Ge-Br':2.30,
                'Sn-Cl':2.33,'Sn-Br':2.50,'Sn-I':2.70,
                'Pb-Cl':2.42,'Pb-I':2.79,
                'N-N':1.45,'N--N':1.25,'N---N':1.10,'N-O':1.40,'N--O':1.21,'N-F':1.36,'N-Cl':1.75,
                'P-P':2.21,'P-O':1.63,'P--O':1.50,'P--S':1.86,'P-F':1.54,'P-Cl':2.03,
                'As-As':2.43,'As-O':1.78,'As-F':1.71,'As-Cl':2.16,'As-Br':2.33,'As-I':2.54,
                'Sb-Cl':2.32,                                       
                'O-O':1.48,'O-O':1.21,'O-F':1.42,
                'S--O':1.43,'S-S':2.05,'S--S':1.49,'S-F':1.56,'S-Cl':2.07,
                'Se--Se':2.15,                                         
                'F-F':1.42,	
                'Cl-Cl':1.99,	
                'Br-Br':2.28,	
                'I--I':2.67,'I-F':1.91,'I-Cl':2.32}	


dspacing = {"Si 111": 3.13467, "Si 311" :1.63702, "Si 511" :1.04514 }               
elem_wave = {'Cr': {'Ka':2.29100, 'Ka1':2.28970, 'Ka2':2.29361, 'Kb':2.08487},
               'Fe': {'Ka':1.93736, 'Ka1':1.93604, 'Ka2':1.93998, 'Kb':1.75661},
               'Co': {'Ka':1.79026, 'Ka1':1.78897, 'Ka2':1.79285, 'Kb':1.62079},
               'Cu': {'Ka':1.54184, 'Ka1':1.54056, 'Ka2':1.54439, 'Kb':1.39222},
               'Mo': {'Ka':0.71073, 'Ka1':0.70930, 'Ka2':0.71359, 'Kb':0.63229}}

XRD_constant = {'elem_wave':elem_wave, 'bond_distances':bond_distances, 
                'dspacing':dspacing, 'Avogadro':6.02214129e23, 'Faraday':96485.3329}
