from numpy import pi
import numpy as np
import matplotlib.pyplot as plt

try:
    from matplotlib.widgets import TextBox
except Exception as e:
    pass


# from indexed import IndexedOrderedDict as ODict

from lmfit.model import Model, ModelResult

c_ln2 = np.log(2.0)
c_ln2pi = c_ln2 / pi
c_s2pi = np.sqrt(2 * pi)
c_f2 = np.sqrt(c_ln2 * pi)
# define a range around a peak
Gpeak_range = 0.5


# ###########     Plot function     ##################
def newfigure(pattern, *args, **kargs):
    plt.figure()
    plt.plot(pattern[0], pattern[1])
    plt.xlabel('2$\Theta$($\degree$)')
    plt.ylabel('Intensity (Counts)')

# ##########       Util functions      #################


def index_of(arr, val):
    """return index of array nearest to a value
       same of n.searchsorted
    """
    if val < min(arr):
        return 0
    return np.abs(arr - val).argmin()


def ran_peak(x, center, range=None):
    """returns the index before and after center
       use a fixed range defined as global in the module
    """
    if not range:
        range = Gpeak_range
    return index_of(x, center - range), index_of(x, center + range) + 1


def data_lim(data, drs):
    """limit the data using an array with two values
    """
    return data[:, index_of(data[0], drs[0]): index_of(data[0], drs[1]) + 1]


def data_exc(data, drs):
    """exclude a range from the data
    """
    return np.hstack([data[:, :index_of(data[0], drs[0])],
                      data[:, index_of(data[0], drs[1]) + 1:]])


def update_param_vals(pars, prefix, **kwargs):
    """convenience function to update parameter values
    with keyword arguments"""
    for key, val in list(kwargs.items()):
        pname = "%s%s" % (prefix, key)
        if pname in pars:
            pars[pname].value = val
    return pars


# ##########      peak functions      #################


def gaussian(x, amplitude=1.0, center=0.0, H=1.0):
    """1 dimensional gaussian:
    gaussian(x, amplitude, center, FWHM)
    """
    sigma = H / (2 * np.sqrt(2 * c_ln2))
    x1 = 1.0 * x - center
    return (amplitude / (c_s2pi * sigma)) * np.exp(-x1**2 / (2 * sigma**2))


def lorentzian(x, amplitude=1.0, center=0.0, H=1.0):
    """1 dimensional lorentzian
    lorentzian(x, amplitude, center, FWHM)
    """
    gamma = H / 2.0
    return (amplitude / (1 + ((x - center) / gamma)**2)) /(pi * gamma)


def pvoigt(x, amplitude=1.0, center=0.0, H=1.0, Nu=0.5):
    """1 dimensional pseudo-voigt:
    pvoigt(x, amplitude, center, FWHM, fraction)
       = amplitude*(1-fraction)*gaussion(x, center, sigma_g) +
         amplitude*fraction*lorentzian(x, center, sigma)

    where sigma_g (the sigma for the Gaussian component) is

        sigma_g = sigma / sqrt(2*log(2)) ~= sigma / 1.17741

    so that the Gaussian and Lorentzian components have the
    same FWHM of 2*sigma.
    """
    return ((1.0 - Nu) * gaussian(x, amplitude, center, H) +
            Nu * lorentzian(x, amplitude, center, H))




# from pyXRD.GIIt.psvoigt import psvoigt as pvc
# def pvoigt2(x, amplitude=1.0, center=0.0, H=1.0, Nu=0.5):
#     """1 dimensional pseudo-voigt:
#     pvoigt(x, amplitude, center, sigma, fraction)
#        = amplitude*(1-fraction)*gaussion(x, center, sigma_g) +
#          amplitude*fraction*lorentzian(x, center, sigma)
#
#     where sigma_g (the sigma for the Gaussian component) is
#
#         sigma_g = sigma / sqrt(2*log(2)) ~= sigma / 1.17741
#
#     so that the Gaussian and Lorentzian components have the
#     same FWHM of 2*sigma.
#     """
#     return amplitude*pvc(len(x),(x-center), H, Nu)
###########      Guess and other peak functions      #################


def height_expr(model):
    "return constraint expression for maximum peak height"
    fmt = "{factor:.7f}*{prefix:s}amplitude/max(1.e-15, {prefix:s}H)"
    return fmt.format(factor=model.height_factor, prefix=model.prefix)


def beta_expr(model):
    "return constraint expression for maximum peak height"
    fmt = "max(1.e-15, {prefix:s}H)/{factor:.7f}"
    return fmt.format(factor=model.height_factor, prefix=model.prefix)


def guess_from_peak(model, y, x=None, center=None, HGuess=True, positive=True,
                    prange=None, ampscale=1.0, sigscale=1.0):
    """ guess parameter for peaks type
    estimate amp, cen, sigma for a peak, create params
    Args:
        model (lmfit model): peak model
        y (np.array)  :
        x (peak model):
        center (float): the position of the peak.
                        if not specified it takes take the max of curve
        HGuess: defines what to do to guess
                       [True] search the sigma on  both side and refine center fine hint
                       ['C'] search the sigma on  both side and refine center course hint
                       ['R'] or ['L'] search the sigma on one side doesnt refine center
                       [False]
        positive (bool): if positive menaning a positive max else negative max

    Create model and parameter for a fit
    """

    if x is None:
        return 1.0, 0.0, 1.0

    # to reduce the range
    if not(center):
        center = x[np.argmax(y)]
    min_i, max_i = ran_peak(x, center, range=prange)
    y = y[slice(min_i, max_i)]
    x = x[slice(min_i, max_i)]

    # coarse guess take max after reduced range
    if HGuess == 'C':
        center = x[np.argmax(y)] if positive else x[np.argmin(y)]

    #
    icenter = index_of(x, center)
    ycenter = y[icenter]
    miny, maxy = min(y), max(y)

    halfmax_vals = y > (ycenter + miny) / \
        2.0 if positive else y > (ycenter + maxy) / 2.0
    amp = (ycenter - miny) * 2.0 if positive else -(ycenter - maxy) * 2.0

    i_sigR = icenter + np.argmin(halfmax_vals[icenter:])
    i_sigL = icenter - np.argmin(halfmax_vals[icenter::-1])

    if HGuess == 'R':
        sig = 2 * abs(x[i_sigR] - center)
    elif HGuess == 'L':
        sig = 2 * abs(x[i_sigL] - center)
    else:
        sig = abs(x[i_sigL] - x[i_sigR])
        center = (x[i_sigL] + x[i_sigR]) / 2.

    amp = amp * sig * ampscale / 2.
    sig = sig * sigscale


    if isinstance(model, FingerModel):
        pars = model.make_params(amplitude=amp*2, center=center,  HG=sig/4.0,  HL=sig/4.0)
    else:
        pars = model.make_params(amplitude=amp, center=center, H=sig)
        pars['%sH' % model.prefix].set(min=0.0)
    if positive:
        pars['%samplitude' % model.prefix].set(min=0.0)
    else:
        pars['%samplitude' % model.prefix].set(max=0.0)
    return pars


###########       Model Classes      #################
COMMON_DOC = """

Parameters
----------
Beta = integral breath
independent_vars: list of strings to be set as variable names
missing: None, 'drop', or 'raise'
    None: Do not check for null or missing values.
    'drop': Drop null or missing observations in data.
        Use pandas.isnull if pandas is available; otherwise,
        silently fall back to numpy.isnan.
    'raise': Raise a (more helpful) exception when data contains null
        or missing values.
prefix: string to prepend to paramter names, needed to add two Models that
    have parameter names in common. None by default.
"""



class PolynomialModel(Model):
    __doc__ = "x -> c0 + c1 * x + c2 * x**2 + ... c7 * x**7"
    MAX_DEGREE = 18
    DEGREE_ERR = "degree must be an integer less than %d."

    def __init__(self, degree, *args, **kwargs):
        if not isinstance(degree, int) or degree > self.MAX_DEGREE:
            raise TypeError(self.DEGREE_ERR % self.MAX_DEGREE)

        self.poly_degree = degree
        pnames = ['c%i' % (i) for i in range(degree + 1)]
        kwargs['param_names'] = pnames

        def polynomial(x, c0=0, c1=0, c2=0, c3=0, c4=0, c5=0, c6=0, c7=0,
                       c8=0, c9=0, c10=0, c11=0, c12=0, c13=0, c14=0,
                       c15=0, c16=0, c17=0, c18=0,):
            return np.polyval([c18, c17, c16, c15, c14, c13, c12, c11,
                               c10, c9, c8, c7, c6, c5, c4, c3, c2, c1,
                               c0], x)

        super(PolynomialModel, self).__init__(polynomial, *args, **kwargs)

    def guess(self, data, x=None, points=None, **kwargs):
        """
           fit the best polynomial using np.polyfit
           passing from Points
           if Point is None fitt all point in the data
           data=data
           x=x
         """
        pars = self.make_params()
        if points is not None:
            points = np.array(points)
            indexs = [index_of(x, val) for val in points]
            x = np.take(x, indexs)
            y = np.take(data, indexs)
            out = np.polyfit(x, y, self.poly_degree)
            for i, coef in enumerate(out[::-1]):
                pars['%sc%i' % (self.prefix, i)].set(value=coef)
            return update_param_vals(pars, self.prefix, **kwargs)
        elif x is not None:
            out = np.polyfit(x, data, self.poly_degree)
            for i, coef in enumerate(out[::-1]):
                pars['%sc%i' % (self.prefix, i)].set(value=coef)
        return update_param_vals(pars, self.prefix, **kwargs)


pvoigt_addoc = """
additional parameters defined in the model:
HL = corresponding pure voight lorentzian  FWHM
HG = corresponding pure voight gaussian FWHM

"""
class PseudoVoigtModel(Model):
    __doc__ = pvoigt.__doc__ + COMMON_DOC + pvoigt_addoc

    def __init__(self, *args, **kwargs):
        super(PseudoVoigtModel, self).__init__(pvoigt, *args, **kwargs)
        self.set_param_hint('H', min=0)
        self.set_param_hint('Nu', value=0.5, min=0.0, max=1.0)

        xx = '{prx:s}H*{f1:.7f}/({prx:s}Nu+(1.0-{prx:s}Nu)*{f2:.7f})'.format(
            f1=np.pi / 2, f2=c_f2, prx=self.prefix)
        self.set_param_hint('Beta', expr=xx)

        HL = '(0.72928*{prx:s}Nu +0.19289*{prx:s}Nu**2'.format(prx=self.prefix)
        HL += ' + 0.07783*{prx:s}Nu**3)*{prx:s}H'.format(prx=self.prefix)
        self.set_param_hint('HL', expr=HL)

        HG = '{prx:s}H*( 1 -0.74417*{prx:s}Nu'.format(prx=self.prefix)
        HG += ' -0.24781*{prx:s}Nu**2'.format(prx=self.prefix)
        HG += ' - 0.00810* {prx:s}Nu**3)**0.5'.format(prx=self.prefix)
        self.set_param_hint('HG', expr=HG)

    def guess(self, data, x=None, center=None, negative=False, **kwargs):
        pars = guess_from_peak(self, data, x, center, negative, ampscale=1.00)
        pars['%sNu' % self.prefix].set(value=0.5, min=0.0, max=1.0)
        return update_param_vals(pars, self.prefix, **kwargs)


class PseudoVoigt2Model(Model):
    __doc__ = lorentzian.__doc__ + COMMON_DOC if lorentzian.__doc__ else ""

    def __init__(self, *args, **kwargs):
        super(PseudoVoigt2Model, self).__init__(pvoigt2, *args, **kwargs)
        self.set_param_hint('H', min=0)
        self.set_param_hint('Nu', value=0.5, min=0.0, max=1.0)

        xx = '{prx:s}H*{f1:.7f}/({prx:s}Nu+(1.0-{prx:s}Nu)*{f2:.7f})'.format(
            f1=np.pi / 2, f2=c_f2, prx=self.prefix)
        self.set_param_hint('Beta', expr=xx)

        HL = '(0.72928*{prx:s}Nu +0.19289*{prx:s}Nu**2'.format(prx=self.prefix)
        HL += ' + 0.07783*{prx:s}Nu**3)*{prx:s}H'.format(prx=self.prefix)
        self.set_param_hint('HL', expr=HL)

        HG = '{prx:s}H*( 1 -0.74417*{prx:s}Nu'.format(prx=self.prefix)
        HG += ' -0.24781*{prx:s}Nu**2'.format(prx=self.prefix)
        HG += ' - 0.00810* {prx:s}Nu**3)**0.5'.format(prx=self.prefix)
        self.set_param_hint('HG', expr=HG)

    def guess(self, data, x=None, center=None, negative=False, **kwargs):
        pars = guess_from_peak(self, data, x, center, negative, ampscale=1.00)
        pars['%sNu' % self.prefix].set(value=0.5, min=0.0, max=1.0)
        return update_param_vals(pars, self.prefix, **kwargs)


class FingerModel(Model):
    __doc__ = lorentzian.__doc__ + COMMON_DOC if lorentzian.__doc__ else ""

    def __init__(self, *args, **kwargs):
        super(FingerModel, self).__init__(finger1, *args, **kwargs)

        #self.set_param_hint('HL', min=0)
        #self.set_param_hint('HG', min=0)

        #H = '({prx:s}HG**5 + 2.69269 * {prx:s}HG**4 * {prx:s}HL'.format(prx=self.prefix)
        #H += '+ 2.42843 * {prx:s}HG**3 * {prx:s}HL**2 '.format(prx=self.prefix)
        #H += '+ 4.47163 * {prx:s}HG**2 * {prx:s}HL**3 '.format(prx=self.prefix)
        #H += '+ 0.07842 * {prx:s}HG    * {prx:s}HL**4 '.format(prx=self.prefix)
        #H += '+ {prx:s}HL**5)**(1.0 / 5)'.format(prx=self.prefix)
        #self.set_param_hint('H', expr=H)

        #rat = '({prx:s}HL/{prx:s}H)'.format(prx=self.prefix)
        #Nu = '1.36603*{ra:s} - 0.47719*{ra:s}**2 + 0.11116*{ra:s}**3'.format(ra=rat)
        #self.set_param_hint('Nu', expr=Nu) 

        #xx = '{prx:s}H*{f1:.7f}/({prx:s}Nu+(1.0-{prx:s}Nu)*{f2:.7f})'.format(
        #    f1=np.pi / 2, f2=c_f2, prx=self.prefix)
        #self.set_param_hint('Beta', expr=xx)

    def guess(self, data, x=None, center=None, negative=False, **kwargs):
        pars = guess_from_peak(self, data, x, center, negative, ampscale=1.00)
        return update_param_vals(pars, self.prefix, **kwargs)


class LorentzianModel(Model):
    __doc__ = lorentzian.__doc__ + COMMON_DOC if lorentzian.__doc__ else ""
    height_factor = 2. / np.pi

    def __init__(self, *args, **kwargs):
        super(LorentzianModel, self).__init__(lorentzian, *args, **kwargs)
        self.set_param_hint('H', min=0)
        self.set_param_hint('height', expr=height_expr(self))
        self.set_param_hint('Beta', expr=height_expr(self))

    def guess(self, data, x=None, negative=False, **kwargs):
        pars = guess_from_peak(self, data, x, negative, ampscale=1.25)
        return update_param_vals(pars, self.prefix, **kwargs)


class GaussianModel(Model):
    height_factor = 2.0 * np.sqrt(c_ln2pi)

    def __init__(self, *args, **kwargs):
        super(GaussianModel, self).__init__(gaussian, *args, **kwargs)
        self.set_param_hint('H', min=0)


    def guess(self, data, x=None, negative=False, **kwargs):
        pars = guess_from_peak(self, data, x, negative)
        return update_param_vals(pars, self.prefix, **kwargs)


############################################################################
def create_PicBack(x, y, centers, back, back_degree=1, Guess=True, prg=None,
                   Pconstrain=None, plot=True, model=PseudoVoigtModel):
    """Create model and parameter for a fit
    Create a model and the relate parameters for the fit


    Args:
        x
        y
        centers
        back
        back_degree=1 degree of polinomial used for background
        Guess :Guess [True] or ['C'] stay for course
        prg (float): range to guess the peak
        Pconstrain= peak constrain
                        example
                            constrain  : ex. {'amplitude': {'min':0, 'vary':False},
                                             'H': {'max':2, 'vary':True}}
        plot= if True plot the first guess??
        model= a lmfit compatible model for the peaks default PseudoVoigtModel




    """

    if not prg:
        prg = Gpeak_range
    centers, back = np.asarray(centers), np.asarray(back)

    # Background definitions
    line_mod = PolynomialModel(degree=back_degree, prefix='line_')
    pars = line_mod.guess(data=y, x=x, points=back)
    mod = line_mod

    # utiliy function to check the overimposion of peaks
    def PoR(ii, sig):
        return abs(centers[ii] - (centers[ii + sig])) > prg

    lab = ''
    for i, j in enumerate(centers):
        # print 'peak number', i
        if Guess:
            if i == 0:
                HGuess = True
            else:
                HGuess = PoR(i, -1) or 'R'
            if i == len(centers) - 1:
                pass
            elif PoR(i, +1):
                pass
            else:
                if HGuess:
                    HGuess = 'L'
                else:
                    HGuess = pars[lab + 'H'].value  # H  from previous peak
        #print(HGuess)
        lab = 'pic{:d}_'.format(i)  # define the label name
        P = model(prefix=lab)
        P.set_param_hint('amplitude', min=0)
        if Pconstrain:
            for constr in Pconstrain:
                P.set_param_hint(constr, **Pconstrain[constr])
        pars += P.guess(y, x=x, center=j, HGuess=HGuess)
        mod += P

    if plot:
        plot_guess(x, y, mod, pars)

    return mod, pars


def plot_guess(x, y, model, param):
    Eval = model.eval(param, x=x)
    plt.figure()
    plt.plot(x, y, 'b')
    plt.plot(x, Eval, 'k--')
    plt.legend(['exp', 'ini'])


# peak detection function
def out_result(out, param=None):
    peaks = []
    if param is None:
        param = ['center', 'H', 'HG', 'HL',
                 'amplitude', 'Beta']

    for pic in out.components[1:]:
        picco = {}
        for i in param:
            picco[i] = {'value': out.params[pic.prefix + i].value,
                        'stderr': out.params[pic.prefix + i].stderr}
        peaks.append(picco)
    return peaks


############################################################################
def peakdet(y, delta=0.03, x=None, plot=True, simple=True,
            add_peaks=None, add_valleys=None, lookformax=False):
    """Peak determination routine
    finds the local maxima and minima ("peaks") in the vector y.
    a local minimum or maximumis defined as a the numerical min/max that it is at list
    higher than delta
    It is supposed to start with a minimum

    Args:
        y (np.array type): vector on which seach the maximum and minimum,
                          it is supposed to start with a minimum
        x (np.array type): vector with corresponding x in respect of y
        delta (float): step limit % of (max-min) if negative just absolute value
        bkg_f (float): np.inf  Non ho idea
        plot (bool): create a plot showng valley and peaks
        simple (bool) : if True returns the value of index(x) for peak and valleys
                        if Falsereturns index and value ,
        add_peaks= array to add a peaks
        add_valleys=array to add a valley

    Returns:
        peaks  (1/2D np.array): position /intensity of peaks
        valley (1/2D np.array): position /intensity of valley

    Examples:
    peaks, valleys=FP.peakdet(y, x = x, delta=0.02, plot=True)



    % Converted from MATLAB script at http://billauer.co.il/peakdet.html
    % Eli Billauer, 3.4.05 (Explicitly not copyrighted).
    % This function is released to the public domain; Any use is allowed.
    % quite modified already ; )

    """
    maxtab = []
    mintab = []

    if x is None:
        x = np.arange(len(y))

    y = np.asarray(y)

    if delta:
        if delta > 0:
            delta *= (y.max() - y.min())
        else:
            delta *= -1
    else:
        delta = 0.03 * (y.max() - y.min())

    assert len(y) == len(x), IOError(
        'Input vectors v and x must have same length')

    assert np.isscalar(delta), IOError('Input argument delta must be a scalar')

    mn, mx = np.Inf, -np.Inf
    mnpos, mxpos = np.NaN, np.NaN

    #lookformax = True

    for i, this in enumerate(y):
        if this > mx:
            mx = this
            mxpos = x[i]
        if this < mn:
            mn = this
            mnpos = x[i]

        if lookformax:
            if this < mx - delta:
                # if len(maxtab) == 0:   # add first minimum
                #    mintab.append((mnpos, mn))
                maxtab.append((mxpos, mx))
                mn = this
                mnpos = x[i]
                lookformax = False
        else:
            if this > mn + delta:
                #if mn < mintab[-1][1]:
                mintab.append((mnpos, mn))
                mx = this
                mxpos = x[i]
                lookformax = True

    if not(lookformax):           # add last minimum
        mintab.append((mnpos, mn))

    peaks, valleys = np.array(maxtab).T, np.array(mintab).T

    assert len(peaks) > 1, IOError('Too high delta 0-1')

    if add_peaks:
        for pic in add_peaks:
            if peaks[0][-1] < pic:
                ipic = len(peaks)
            else:
                ipic = np.argmax(peaks > pic)
            ipeak = index_of(x, pic)
            peaks = np.insert(peaks, ipic, [x[ipeak], y[ipeak]], axis=1)

    if add_valleys:
        for val in add_valleys:
            if valleys[0][-1] < val:
                ival = len(peaks)
            else:
                ival = np.argmax(peaks > val)
            ipeak = index_of(x, val)
            peaks = np.insert(peaks, ival, [x[ipeak], y[ipeak]], axis=1)

    if plot:
        plt.figure()
        plt.plot(x, y, label='exp')
        # plt.xlim(18,58)
        plt.plot(peaks[0], peaks[1], 'ro', picker=5)
        plt.plot(valleys[0], valleys[1], 'bo', picker=5)
        plt.legend()

    if simple:
        return peaks[0], valleys[0]
    else:
        return peaks, valleys


def add_peak(peaklist, peak):
    if peak > peaklist[-1]:
        return np.append(peaklist, peak)
    else:
        return np.insert(peaklist, np.argmax(peaklist > peak), peak)


def del_peak(peaklist, peak):
    return np.delete(peaklist, index_of(peaklist, peak))
############################################################################

def JanaPRF(prf, x, y, int_lim=0, plot=True):
    """return hkl and centers
       int_lim = intensity limit

    """
    hkl = HKL()
    prfl = []
    with open('slHMS.prf') as prf:
        while True:
            xx = prf.readline()
            if '999\n' in xx:
                xx = prfl.pop(0)
                prfl = np.loadtxt(prfl)
                break
            else:
                prfl.append(xx)
    pass
    # number of index = indexes
    indexes = int(xx.split()[-1])
    prfl = prfl.compress(prfl[:, -1] > int_lim, axis=0)
    inde = prfl[:, :indexes].astype(int)
    centers = prfl[:, indexes + 2]
    F2 = prfl[:, -1]
    for j, ind in enumerate(inde):
        hkl[tuple(ind)] = {'center': centers[j], 'F2': F2[j]}
    #
    if plot:
        plt.figure()
        plt.plot(x, y)
        hkl.plot(y=y.min() - (y.max() - y.min()) * 0.05)
    return hkl


class HKL(dict):
    """Ordered dictionary containing the HKL
       whe obtained from fit the key are fitted_model and the values are 
       dictionary containing the fitted parameters 
    """

    def limit(self, lmin=-np.inf, lmax=np.inf):
        """create a new HKL class into the limits
        lmin = min
        l,ax = maX
        """
        hkl = HKL()
        for key in list(self.keys()):
            if self[key]['center'] > lmin and self[key]['center'] < lmax:
                hkl[key] = self[key]
        return hkl

    @classmethod
    def from_out(cls, out):
        return cls(__out2hkl__(out))

    def UpdateVal(self, irf):
        """Update values
            if irf is np.array the HKL peak should < than peak used/detected
            attention at the limit
            if out is the result of a fit in ranges lmin lmax:
                xhlr= hkl.limit(lmin ,lmax)
                xhle.UpdateVal(out)
                hkl.update(xhle)
        """
        old_cen = self.getKey('center', all=True)
        if len(old_cen) == 0:               # keeped for compatibility ....
            self.update(__out2hkl__(irf))
            return
        if isinstance(irf, np.ndarray):
            for i, cen in enumerate(old_cen):
                ref = index_of(irf, cen)
                list(self.values())[i].update({'center': irf[ref]})
        elif isinstance(irf, ModelResult):
            irf = __out2hkl__(irf)
            irf_cen = irf.getKey('center')
            for i, cen in enumerate(old_cen):
                ref = index_of(irf_cen, cen)
                list(self.values())[i].update(list(irf.values())[ref])

    def getKey(self, key, all=False):
        '''returns an array witht the values of a key
        '''
        if all:
            return np.array([self[x][key] for x in self]).T
        else:
            out = []
            for x in self:
                try:
                    out.append(self[x][key])
                except KeyError:
                    pass
            return np.array(out).T

    def getIrf(self, keyl=['center', 'H', 'HG', 'HL',
                           'center_stderr', 'H_stderr',
                           'HG_stderr', 'HL_stderr', 'amplitude', 'Beta',
                           'Beta_stderr', 'amplitude_stderr'], exc_peakORprop='peak'):
        """create a dictionary with all interesting values for microstructure
           exc_peakORprop= 'peak' exclude peaks not presenting all keys 
                           'prop' exclude key not present in all peaks

        """
        zzz = {}
        if exc_peakORprop == 'peak':
            for key in keyl:
                zzz[key] = []
            zzz.update({'cry_i': []})
            for x in self:
                try:
                    zz = [self[x][key] for key in keyl]
                    if None in zz:
                        print('problem', x, np.round(self[x]['center'], 2))
                        raise KeyError('one value =0')
                    for i, key in enumerate(keyl):
                        zzz[key].append(zz[i])
                    zzz['cry_i'].append(x)
                except KeyError:
                    pass
            for key in keyl:
                zzz[key] = np.asarray(zzz[key])
        elif exc_peakORprop == 'prop':
            for key in keyl:
                try:
                    zzz[key] = np.asarray([self[x][key] for x in self])
                    if None in zzz[key]:
                        print('problem', key, np.where(zzz[key] == None)) # noqa
                        raise KeyError('one value =0')

                except KeyError:
                    pass
            zzz['cry_i']=[x for x in self]
        return zzz

    def plot(self, y=0):
        fg = plt.gcf()
        cen = self.getKey('center')
        plt.plot(cen, [y] * len(cen), '|', markersize=12, picker=5)
        text = fg.text(0.4, 0, "", va="bottom", ha="left")

        def onpick(event):
            index = list(self.keys())[event.ind[0]]
            text_i = str(index)
            try:
                text_i = '%s %d' % (text_i, self[index]['F2'])
            except KeyError:
                pass
            text.set_text(text_i)
        fg.canvas.mpl_connect('pick_event', onpick)

    """return index of array nearest to a value
    """

    def filter(self, indexcond):
        hkl = HKL()
        for i in self:
            if eval(indexcond):
                hkl.update(i)
        return hkl


def __out2hkl__(out):
    """From the output of a fit (lmfit) create an dict with the peaks
       The peaks in the model should have prefix pic
    """
    data_out = HKL()
    components = [com for com in out.components if 'pic' in com.prefix]
    oup = out.params

    for pic in components:
        data = {}
        for pNam in pic.param_names:
            pNamK = pNam.replace(pic.prefix, '')
            try:
               data.update({pNamK: oup[pNam].value})
            except ValueError:
               print('error', pic.prefix, pNamK)
            data.update({'%s_stderr' % pNamK: oup[pNam].stderr})
        data_out.update({pic: data})
    return data_out

 ##     W                     ################
    # example
    # from pyXRD import FitPeak as FP
    # import numpy as np
    # ex1= np.loadtxt('data.XY', comments='!').T
    # x=ex1[0][685:736]
    # y=ex1[1][685:736]
    # xd=[x[0], x[-1]]
    # Peak1 = FP.PseudoVoigtModel(prefix='p1_')
    # line_mod = FP.PolynomialModel(degree=1, prefix='line_')
    # pars = line_mod.guess(data=y, x=x, points=xd)
    # pars += Peak1.guess(y, x=x, center=24.0)
    # mod = Peak1 + line_mod
    # out = mod.fit(y, pars, x=x, weights=np.sqrt(1/y))

    # x,y,z=FP.data_lim(LaB6,[21.1,140.1]) #140.1
    # peaks, valleys=FP.peakdet(y, x = x, delta=0.02, plot=True)
    # model, param= FP.create_PicBack(x,y, peaks, valleys, back_degree=3,
    #                                 Guess=True, plot=0, Pconstrain=None)
    #
    # %time model.eval(param, x=x)
    # %time out = model.fit(y, param, x=x, weights=1/z)
    # hkl_s = FP.HKL()
    # hkl_s.UpdateVal(out)
    #

    # Lmfit example
    # from lmfit import Model
    #
    # data = loadtxt('model1d_gauss.dat')
    # x = data[:, 0]
    # y = data[:, 1]
    #
    #
    # def gaussian(x, amp, cen, wid):
    #     """1-d gaussian: gaussian(x, amp, cen, wid)"""
    #     return (amp / (sqrt(2*pi) * wid)) * exp(-(x-cen)**2 / (2*wid**2))

    #
    #
    # gmodel = Model(gaussian)
    # gmodel.eval(param, x=x)
    # gmodel.param_names
    # gmodel.independent_vars
    # gmodel.set_param_hint('sigma', min=0)
    # result = gmodel.fit(y, x=x, amp=5, cen=5, wid=1)
