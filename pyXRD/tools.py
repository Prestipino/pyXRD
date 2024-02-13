import numpy as np
import xraydb as xdb
from .PStrut import Crystal


def npsind(x): return np.sin(x * np.pi / 180.)
def npcosd(x): return np.cos(x * np.pi / 180.)


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
    if np.all(Ener > 1000):
        WL = (1.23984E-6 / Ener) * 1E10
    if np.all(Ener < 1000):
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
        return E2W(Energy) / np.sin(np.radians(T2 / 2)) * 0.5
    if WL > 1e-3:
        WL *= 1e-10
    return WL / np.sin(np.radians(T2 / 2)) * 0.5


def CTHM(dspacing, WL=1.5406):
    """Fullprof polarization correction constant for mono
    """
    return npcosd(Bragg_2T(dspacing, WL))**2


def corPol(T2, cthm=1, K=0.5):
    """
    T2 = 2theta degreee
    output:
    return array with polarization correction function

    ex:
    -----------------------------
    y_kalphaave = y_kalpha/corPol(T2, cthm=0.7899) * corPol(T2, cthm=1)

    """
    return (1 - K) + K * cthm * np.cos(np.radians(T2)) ** 2


def Absorb(Geometry, MuR, Tth, Phi=0, Psi=0):
    '''Calculate sample absorption correction from Gsas2
    :param str Geometry: one of 'Cylinder','Bragg-Brentano','Tilting Flat Plate in transmission','Fixed flat plate'
    :param float MuR: absorption coeff * sample thickness/2 or radius
    :param Tth: 2-theta scattering angle - can be numpy array
    :param float Phi: flat plate tilt angle - future
    :param float Psi: flat plate tilt axis - future
    '''

    def muRunder3(MuR, Sth2):
        T0 = 16.0 / (3. * np.pi)
        T1 = (25.99978 - 0.01911 * Sth2**0.25) * np.exp(-0.024551 * Sth2) + \
            0.109561 * np.sqrt(Sth2) - 26.04556
        T2 = -0.02489 - 0.39499 * Sth2 + 1.219077 * Sth2**1.5 - \
            1.31268 * Sth2**2 + 0.871081 * Sth2**2.5 - 0.2327 * Sth2**3
        T3 = 0.003045 + 0.018167 * Sth2 - 0.03305 * Sth2**2
        Trns = -T0 * MuR - T1 * MuR**2 - T2 * MuR**3 - T3 * MuR**4
        return np.exp(Trns)

    def muRover3(MuR, Sth2):
        T1 = 1.433902 + 11.07504 * Sth2 - 8.77629 * Sth2 * Sth2 + \
            10.02088 * Sth2**3 - 3.36778 * Sth2**4
        T2 = (0.013869 - 0.01249 * Sth2) * np.exp(3.27094 * Sth2) + \
            (0.337894 + 13.77317 * Sth2) / (1.0 + 11.53544 * Sth2)**1.555039
        T3 = 1.933433 / (1.0 + 23.12967 * Sth2)**1.686715 - \
            0.13576 * np.sqrt(Sth2) + 1.163198
        T4 = 0.044365 - 0.04259 / (1.0 + 0.41051 * Sth2)**148.4202
        Trns = (T1 - T4) / (1.0 + T2 * (MuR - 3.0))**T3 + T4
        return Trns / 100.

    Sth2 = npsind(Tth / 2.0)**2
    # Lobanov & Alte da Veiga for 2-theta = 0; beam fully illuminates sample
    if 'Cylinder' in Geometry:
        if isinstance(MuR, np.ndarray):
            MuRSTh2 = np.vstack((MuR, Sth2))
            AbsCr = np.where(MuRSTh2[0] <= 3.0,
                             muRunder3(MuRSTh2[0], MuRSTh2[1]),
                             muRover3(MuRSTh2[0], MuRSTh2[1]))
            return AbsCr
        else:
            if MuR <= 3.0:
                return muRunder3(MuR, Sth2)
            else:
                return muRover3(MuR, Sth2)
    elif 'Bragg' in Geometry:
        return 1.0
    # assumes sample plane is perpendicular to incident beam
    elif 'Fixed' in Geometry:
        # and only defined for 2theta < 90
        MuT = 2. * MuR
        T1 = np.exp(-MuT)
        T2 = np.exp(-MuT / npcosd(Tth))
        Tb = MuT - MuT / npcosd(Tth)
        return (T2 - T1) / Tb
    # assumes symmetric tilt so sample plane is parallel to diffraction vector
    elif 'Tilting' in Geometry:
        MuT = 2. * MuR
        cth = npcosd(Tth / 2.0)
        return np.exp(-MuT / cth) / cth


def vds2fds(T2, Inte):
    """
    convert variable divergence slits to fixed divergence slits
    args:
    -------------------
    T2 : 2theta array
    Inte serie of arrays, for instance data end error
    """
    return Int / npsind(T2 / 2.0)


def T2new_lambda(T2, WLi=1.5405981E-10, WLf=1.5405981E-10):
    if WLi > 1e-3:
        WLi *= 1e-10
    if WLf > 1e-3:
        WLf *= 1e-10
    return 2 * np.degrees(np.arcsin(np.sin(np.radians(T2) / 2.0) * WLf / WLi))


def MuR(R, Mat, EneWL=0.71, pack=0.6, density=False, compo=False):
    """Calculate MuR
    args:
    -------------------------
    R radious of cappillary (mm)
    Mat: composition (str) or Crystal object
         if crystal object density is not necessary
    EneWL: energy of waveleght 
           values < 5 are considered wavelegh in angstrom
           5 < values  < 100 are considered energy in keV
           value > 100 are considered energy in eV
    compo: boolean output components
    """

    if isinstance(Mat, Crystal):
        density = Mat.Properties.density() * pack
        Comp = Mat.Properties.molname()
    elif isinstance(Mat, str):
        Comp = Mat
    else:
        raise ValueError('Work Only with string and Crystal object')

    if isinstance(EneWL, np.ndarray):
        EneWL0 = EneWL[0]
    elif isinstance(EneWL, list):
        EneWL0 = EneWL[0]
        EneWL = np.ndarray(EneWL)
    else:
        EneWL0 = EneWL

    if EneWL0 < 5:
        energy = W2E(EneWL)
    elif EneWL0 < 100:
        energy = EneWL * 1000
    elif EneWL0 > 100:
        energy = EneWL
    else:
        raise ValueError('only positives values')
    R = R / 10  # conversion to cm-1
    if compo:
        out = xdb.material_mu_components(Comp, energy, density)
        return {i: out['density'] * np.prod(out[i]) / out['mass'] for i in out['elements']}
    return xdb.material_mu(Comp, energy, density) * R
