from numpy import pi
import numpy as np
import matplotlib.pyplot as plt

try:
    from matplotlib.widgets import TextBox
except Exception as e:
    pass

from uncertainties import unumpy

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

def uplot(x, y, fmt='', *args, **kwargs):
    """Wrapper for plt.plot that handles ufloat arrays"""
    from uncertainties import unumpy
    if hasattr(y, 'dtype') and y.dtype == object and all(hasattr(val, 'nominal_value') for val in y):
        y_nom = unumpy.nominal_values(y)
        y_err = unumpy.std_devs(y)
    else:
        y_nom = y
        y_err = None
    if hasattr(x, 'dtype') and x.dtype == object and all(hasattr(val, 'nominal_value') for val in x):
        x_nom = unumpy.nominal_values(x)
        x_err = unumpy.std_devs(x)
    else:
        x_nom = x
        x_err = None
    if (x_err or y_err) is None:
        return plt.plot(x, y, fmt, *args, **kwargs)
    
    return plt.errorbar(x_nom, y_nom, yerr=y_err, xerr=x_err, fmt= fmt, *args, **kwargs)

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
    Args:
        data (np.array): 2D array with the first row as x values
        drs (list or np.array): two values defining the range to limit the data

    returns:
        np.array: 2D array with the data limited to the range defined by drs
    """
    try:
        totranspose = data.shape[0] > data.shape[1]
    except IndexError:
        totranspose = False
    if totranspose:
        data = data.T
    data =data[:, index_of(data[0], drs[0]): index_of(data[0], drs[1]) + 1]
    return data 
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

def plot_guess(x, y, model, param):
    Eval = model.eval(param, x=x)
    plt.figure()
    plt.plot(x, y, 'b')
    plt.plot(x, Eval, 'k--')
    plt.legend(['exp', 'ini'])


# peak detection function
def out_result(out, param=None):
    '''return a list of dict with the peak parameters
    Args:   
        out (lmfit.model.ModelResult): the result of a fit
        param (list or str): list of parameters to return 
                if None return all the parameters 
    Returns:
        peaks (list of dict): list of dict with the peak parameters
        peaks (np.array): if param is str return a 1D array with the parameters
    '''
    peaks = []
    numeric = False
    if param is None:
        param = ['center', 'H', 'HG', 'HL',
                 'amplitude', 'Beta']
    if isinstance(param, str):
        param = [param]
        numeric = True
    for pic in out.components[1:]:
        picco = {}
        for i in param:
            picco[i] = {'value': out.params[pic.prefix + i].value,
                        'stderr': out.params[pic.prefix + i].stderr}
        peaks.append(picco)
    if numeric:
        values = np.array([picco[param[0]]['value'] for picco in peaks])
        errors = np.array([picco[param[0]]['stderr'] for picco in peaks])
        return unumpy.uarray(values, errors)
        
    return peaks


############################################################################
