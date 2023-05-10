# -*- coding: utf-8 -*-
"""
*GSASIIElem: functions for element types*
-----------------------------------------

"""
# Copyright: 2008, Robert B. Von Dreele & Brian H. Toby (Argonne National Laboratory) +Prestino
########### SVN repository information ###################
# $Date$
# $Author$
# $Revision$
# $URL$
# $Id$
########### SVN repository information ###################
from . import atmdata
import numpy as np




def GetXFFCoeff(El):
    """Read X-ray form factor coefficients from `atomdata.py` file

    :param str El: element 1-2 character symbol, case irrevelant
    :return: `FormFactors`: list of form factor dictionaries
    
    Each X-ray form factor dictionary is:
    
    * `Symbol`: 4 character element symbol with valence (e.g. 'NI+2')
    * `Z`: atomic number
    * `fa`: 4 A coefficients
    * `fb`: 4 B coefficients
    * `fc`: C coefficient
    
    """
    return atmdata.XrayFF[El]


def XScatFac(El, SQ):
    """compute value of form factor

    :param El: list of elements
    :param SQ: (sin-theta/lambda)**2
    :return: real part of form factor

    t think about your_array.squeeze()
    """
    fa = np.array(atmdata.XrayFF[el]['fa'] for el in El)
    fb = np.array(atmdata.XrayFF[el]['fa'] for el in El)
    fc = np.array(atmdata.XrayFF[el]['fc'] for el in El)
    t = -fb[:, :, np.newaxis] * SQ
    return np.sum(fa[:, :, np.newaxis] * np.exp(t), axis=0) + fc[:, np.newaxis]


def EScatFac(El, SQ):
    """compute value of form factor

    :param El: list of elements
    :param SQ: (sin-theta/lambda)**2
    :return: real part of form factor

    t think about your_array.squeeze()
    """
    fa = np.array(atmdata.ElecFFFF[el]['fa'] for el in El)
    fb = np.array(atmdata.ElecFFFF[el]['fa'] for el in El)
    t = -fb[:, :, np.newaxis] * SQ
    return np.sum(fa[:, :, np.newaxis] * np.exp(t), axis=0)


def NScatL(El):
    """compute value of form factor

    :param El: list of elements
    :param SQ: (sin-theta/lambda)**2
    :return: real part of form factor

    t think about your_array.squeeze()
    """
    return np.array([atmdata.AtmBlens[el]['SL'] for el in El])[:, np.newaxis]


        # radiation == 'florentine':
            #     datasc = np.genfromtxt('f0_peng.dat', skip_header=0,
            #                            names=True, encoding='ascii',
            #                            delimiter=',')

            #     all_elements = list(datasc['Element'])
            #     try:
            #         index = [all_elements.index(el) for el in elems]
            #     except ValueError as ve:
            #         raise Exception('Element not available: %s' % ve)
            #     datasc = datasc[index]

            #     fqe = np.zeros([len(hkl_qm), len(elems)])
            #     # Loop over elements
            #     for n, atom in datasc:
            #         # Array multiplication over Qmags
            #         f = atom['a1'] * np.exp(-atom['b1'] * s2) + \
            #             atom['a2'] * np.exp(-atom['b2'] * s2) + \
            #             atom['a3'] * np.exp(-atom['b3'] * s2) + \
            #             atom['a4'] * np.exp(-atom['b4'] * s2) + \
            #             atom['a5'] * np.exp(-atom['b5'] * s2)
            #         fqe[:, n] = f