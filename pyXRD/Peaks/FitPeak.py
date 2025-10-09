from numpy import pi
import numpy as np
import matplotlib.pyplot as plt

try:
    from matplotlib.widgets import TextBox
except Exception as e:
    pass

from uncertainties import unumpy
from .PeaksModels import PseudoVoigtModel, FingerModel, LorentzianModel, PolynomialModel, GaussianModel

# from indexed import IndexedOrderedDict as ODict

from lmfit.model import Model, ModelResult
from tqdm import tqdm

##########################################################################################################################
from numpy import pi
import numpy as np
import matplotlib.pyplot as plt

try:
    from matplotlib.widgets import TextBox
except Exception as e:
    pass

from uncertainties import unumpy

# from indexed import IndexedOrderedDict as ODict


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

def uplot(*args, fmt='', **kwargs):
    """
    Enhanced plotting function that works like plt.plot() but automatically handles uncertainties.
    
    Usage:
        uplot(y, fmt='', **kwargs)           # plot y versus index
        uplot(x, y, fmt='', **kwargs)        # plot y versus x
        uplot(x, y, fmt, **kwargs)           # plot with format string
        uplot(x, y, fmt, label='data')       # with additional kwargs
    
    Handles both regular arrays and ufloat arrays seamlessly.
    """
    # Extract arguments similar to plt.plot()
    if len(args) == 0:
        raise ValueError("uplot requires at least 1 argument")
    
    # Determine if we have (y) or (x, y) calling pattern
    if len(args) == 1:
        y = args[0]
        x = np.arange(len(y)) if hasattr(y, '__len__') else None
        args = args[1:]
    else:
        if isinstance(args[1],(list,tuple, np.ndarray)):
            x, y = args[:2]
            args = args[2:]
        else:
            y = args[0]
            x = np.arange(len(y)) if hasattr(y, '__len__') else None
            args = args[1:]

    
    # Handle format string if provided as third argument
    if args and isinstance(args[0], str):
        fmt = args[0]
        args = args[1:]
    
    # Process uncertainties in x and y
    def process_uncertainties(arr):
        if arr is None:
            return None, None
        if hasattr(arr, 'dtype') and arr.dtype == object and all(hasattr(val, 'nominal_value') for val in arr):
            return unumpy.nominal_values(arr), unumpy.std_devs(arr)
        return arr, None
    
    x_nom, x_err = process_uncertainties(x)
    y_nom, y_err = process_uncertainties(y)
    
    # Determine if we need error bars
    has_errors = (x_err is not None) or (y_err is not None)
    
    # Plot with appropriate function
    if not has_errors:
        # Regular plot
        return plt.plot(x_nom, y_nom, fmt, *args, **kwargs)
    else:
        # Errorbar plot
        eb = plt.errorbar(x_nom, y_nom, yerr=y_err, xerr=x_err, 
                         fmt=fmt if fmt else '-',  # Use 'none' if no fmt to show only errorbars
                         *args, **kwargs)
        
        # Apply format string components to errorbar markers/lines
        if fmt:
            markers = {'o', 's', '^', 'D', 'v', '>', '<', 'p', '*', 'h', 'H', '+', 'x', 'X', 'd'}
            line_styles = {'-', '--', '-.', ':', ''}
            
            for char in fmt:
                if char in markers:
                    eb[-1][0].set_marker(char)  # Set marker style
                elif char in line_styles:
                    eb[0].set_linestyle(char)  # Set line style
        
        return eb

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

############################################################################
def create_PicBack(x, y, centers, back, back_int=None, back_degree=1, Guess=True, prg=None,
                   Pconstrain=None, plot=True, model=PseudoVoigtModel):
    """Create model and parameter for a fit
    Create a model and the relate parameters for the fit


    Args:
        x   (np.array): x values of the data
        y   (np.array): data to fit
        centers = list of centers of the peaks
        back = list of points to use for background
        back_int=None: background intensity if None use y values at back points
        back_degree=1 degree of polinomial used for background
        Guess :Guess [True] or ['C'] stay for course
        prg (float): range to used to estimate if a peak is superimposed usend in guest
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
    if back_int is None:
        pars = line_mod.guess(data=y, x=x, points=back)
    else:
        pars = line_mod.guess(data=back_int, x=back)
    if len(pars) == 0:
        raise ValueError('No background points found in data')
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
    if param is None:
        param = ['center', 'H', 'HG', 'HL',
                 'amplitude', 'Beta']
    if isinstance(param, str):
        param = [param]


    if isinstance(out, list):
        if len(param) ==1:
            return np.vstack([out_result(i, param=param) for i in out]).T
        else:
            return np.vstack([out_result(i, param=param) for i in out])

    for pic in out.components[1:]:
        picco = []
        for i in param:
            picco.append(unumpy.uarray(out.params[pic.prefix + i].value, 
                                       out.params[pic.prefix + i].stderr))  
        peaks.append(picco)

    Dtype = [(pic.prefix + i, object  ) for pic in out.components[1:] for i in param]
    struc_arr = np.rec.array(sum(peaks, []) , dtype=Dtype)

    if len(param) ==1:
        return  np.array(struc_arr.tolist(), dtype=object)
    return struc_arr


############################################################################
def sequential_fit(data_list, model, pars, start=0, stop=-1, xstart=None, xstop=None, ran_var=False):
    '''Fit a list of datasets sequentially using a model and parameters
    Args:
        data_list (list): list of dataset indices to fit    
        model (lmfit.model.Model): the model to fit
        pars (lmfit.Parameters): the parameters for the model
        start (int): starting index in data_list
        stop (int): ending index in data_list
        xstart (int): starting index in the x data
        xstop (int): ending index in the x data
        range_var : bool, optional If True, xstart and xstop are relative to peak center (default: False).
    Returns:
        out (list): list of ModelResult objects for each fit
       
    Notes
    -----
    - When range_var=True, xstart and xstop are relative to the peak center from parameters.
    - Each fit after the first uses the parameters from the previous fit as starting values.
    """


    '''
    out = []
    index = []
    if ran_var:
        xstart = pars['pic0_center'].value - xstart
        xstop =  xstop - pars['pic0_center'].value
    for i, data in tqdm(enumerate(data_list[start:stop]), total=len(data_list[start:stop]), desc="Fitting datasets"):
        if i !=0:
            pars = out[-1].params.copy()
        if ran_var :
            x,y,z  = data_lim(data, [pars['pic0_center'].value - xstart,
                                        pars['pic0_center'].value + xstop])
        else:
            x,y,z = data_lim(data,[xstart, xstop])
       
        out.append( model.fit(y, x=x, params=pars, weights=1/z))
        index.append(i + start)
    return out, index


def sequential_1P(data_list, start=0, stop=-1, peak=None, ranges=None, ran_var=True):
    '''Fit a list of datasets sequentially for 1 peak data
    Args:

    '''
    index = []
    out = []
    if peak is None:
        if hasattr(ranges, '__iter__'):
            x,y,z  = data_lim(data_list[0], [ranges[0], ranges[1]])
            peak = x[[np.argmax(y)]]
        else:
            peak = x[[np.argmax(y)]]
    else:
        if isinstance(ranges, (int, float)):
            ranges = [peak - ranges, peak + ranges]

    if ran_var:
        if hasattr(ranges, '__iter__'):
            xstart = peak - ranges[0]
            xstop =  ranges[1] - peak
        else:
            xstart =  -ranges
            xstop = ranges

    x,y,z  = data_lim(data_list[0], [ranges[0], ranges[1]])     
    model =  create_PicBack(x, y, [peak], [y[0], y[-1]])

    for i, data in tqdm(enumerate(data_list[start:stop]), total=len(data_list[start:stop]), desc="Fitting datasets"):
        if i !=0:
            pars = out[-1].params.copy()
            if ran_var :
                x,y,z  = data_lim(data, [pars['pic0_center'].value - xstart,
                                         pars['pic0_center'].value + xstop])
            else:
                x,y,z = data_lim(data,ranges)
        out.append( model.fit(y, x=x, params=pars, weights=1/z))
        index.append(i + start)
    return out, index    

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
