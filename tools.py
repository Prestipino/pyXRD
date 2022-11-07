import numpy as np

X_WL = {'Cr': {'Ka': 2.29100, 'Ka1': 2.28970, 'Ka2': 2.29361, 'Kb': 2.08487},
        'Fe': {'Ka': 1.93736, 'Ka1': 1.93604, 'Ka2': 1.93998, 'Kb': 1.75661},
        'Co': {'Ka': 1.79026, 'Ka1': 1.78897, 'Ka2': 1.79285, 'Kb': 1.62079},
        'Cu': {'Ka': 1.54184, 'Ka1': 1.54056, 'Ka2': 1.54439, 'Kb': 1.39222},
        'Mo': {'Ka': 0.71073, 'Ka1': 0.70930, 'Ka2': 0.71359, 'Kb': 0.63229}}

dspacing = {"Si 111": 3.13467, "Si 311" :1.63702, "Si 511" :1.04514 } 


def E2T(Ener, dspacing):
    """Calculate The angle for an Energy in eV or KeV given a dspacing
       accept, "integer", "float", monodimensional array
       return corrisponding angle in degree
    """

    if (isinstance(Ener, float) or isinstance(Ener, int) or isinstance(
                    Ener, np.float64) or isinstance(Ener, np.float32)):
        if Ener > 1000:
            the = np.rad2deg(
                np.arcsin((1.23984E-6 / (Ener)) * 1E10 / (2 * dspacing)))
        if Ener < 1000:
            the = np.rad2deg(np.arcsin((
                1.23984E-6 / (Ener * 1000)) * 1E10 / (2 * dspacing)))
    else:
        if Ener[0] > 1000:
            the = np.rad2deg(
                np.arcsin((1.23984E-6 / (Ener)) * 1E10 / (2 * dspacing)))
        if Ener[0] < 1000:
            the = np.rad2deg(
                np.arcsin((1.23984E-6 / (Ener * 1000)) * 1E10 / (2 * dspacing)))
    return the


def E2W(Ener):
    """Convert from Energy to waelenght (angstrom)
    E=hv hplank =6.626e-34 Js or 4.13566733 eV/s
    v=frequency = c/W c=299792458 m/s
    E=hc/W
    """
    if Ener > 1000:
        WL = (1.23984E-6 / Ener) * 1E10
    if Ener < 1000:
        WL = (1.23984E-6 / ((Ener))) * 1E7
    return WL


def W2E(WL):
    if WL > 1e-3:
        WL *= 1e-10
    Ener = (1.23984E-6 / WL)
    return Ener


def Bragg_2T(dspacing, WL=1.5405981E-10, Energy=False):
    """Bragg relation return 2Theta
    """
    if Energy:
        WL = E2W(Energy)
    if dspacing > 1e-3:
        dspacing *= 1e-10
    if WL > 1e-3:
        WL *= 1e-10
    return 2 * np.degrees(np.arcsin(WL / dspacing * 0.5))


def Bragg_WL(T2, dspacing):
    """Bragg relation return wavelengh
    """
    #if dspacing > 1e-3:  dspacing*=1e-10
    return np.sin(radians(T2 / 2)) * 2 * dspacing


def Bragg_E(T2, dspacing):
    """from 2 Theta angle and dspacing return the energy in eV
       in diffraction condition
       E=hc/(sin(theta)*2d)))
    """
    return Bragg_WL(T2, dspacing)


def Bragg_d(T2, WL=1.5406, Energy=False):
    """from Theta angle and Energyg return the d_spacing
       if Energy is a value WL is not used
       ex:
       Bragg_d(25, 1.54)  == Bragg_d(25, Energy=9000)
    """
    if Energy:
        return E2W(Energy) / np.sin(radians(T2 / 2)) * 0.5
    if WL > 1e-3:
        WL *= 1e-10
    return WL / np.sin(np.radians(T2 / 2)) * 0.5


def T2new_lambda(T2, WLi=1.5405981E-10, WLf=1.5405981E-10):
    if WLi > 1e-3:
        WLi *= 1e-10
    if WLf > 1e-3:
        WLf *= 1e-10
    return 2 * np.degrees(np.arcsin(np.sin(np.radians(T2) / 2.0) * WLf / WLi))
