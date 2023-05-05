from numpy import pi, sqrt
import numpy as np
import matplotlib.pyplot as plt

from lmfit.model import Model

c_ln2 = np.log(2.0)
c_ln2pi = c_ln2 / np.pi
c_s2pi = np.sqrt(2 * pi)
c_f2 = np.sqrt(c_ln2 * np.pi)

Gpeak_range = 0.5
G_Hrange = 8

###########       Util functions      #################


def index_of(arr, val):
    """return index of array nearest to a value
    """
    if val < min(arr):
        return 0
    return np.abs(arr - val).argmin()


def ran_peak(x, center, range=None):
    """returns the index before and after center
       use a fixed range defined as global1 in the module
    """
    if not range:
        range = Gpeak_range
    return index_of(x, center - range), index_of(x, center + range) + 1


def data_lim(data, drs):
    return data[:, index_of(data[0], drs[0]): index_of(data[0], drs[1]) + 1]


def update_param_vals(pars, prefix, **kwargs):
    """convenience function to update parameter values
    with keyword arguments"""
    for key, val in list(kwargs.items()):
        pname = "%s%s" % (prefix, key)
        if pname in pars:
            pars[pname].value = val
    return pars


###########      Microstructure related functions      #################


def tan_d(x):
    return np.tan(np.radians(x))


def cos_d(x):
    return np.cos(np.radians(x))


def sin_d(x):
    return np.cos(np.radians(x - 90))

###########      Pseudo voight functions      #################


def GammaG(x, U=0, V=0, W=0, Ig=0):
    """dependency of FWHM2 of the gasussian part of profile
       params:
       x: 2 theta
       U : strain gaussian
       V : V value
       W : value
       Ig  : size gaussian

       returns the   FWHM2  respect to 2T     
    """
    theta = np.array(x) / 2.0
    G2 = U * tan_d(theta)**2 + V * tan_d(theta) + W + (Ig / (cos_d(theta)**2))
    return np.sqrt(G2)


def GammaL(x, X, Y):
    """dependency of FWHM of the lorentzian part of profile
       params:
       x:  2 theta
       X : strain gaussian
       Y : size lorentzian

       returns the   FWHM2  respect to T     
    """
    theta = x / 2.0
    return X * tan_d(theta) + (Y / cos_d(theta))


def getH(Hg, Hl):
    return (Hg**5 + 2.69269 * Hg**4 * Hl + 2.42843 * Hg**3 * Hl**2 + 4.47163 * Hg**2 * Hl**3 + 0.07842 * Hg * Hl**4 + Hl**5)**(1.0 / 5)


def getNu(Hl, H):
    rat = Hl / H
    return 1.36603 * rat - 0.47719 * rat**2 + 0.11116 * rat**3


def getB(H, Nu):
    return (H * (np.pi / 2)) / (Nu + (1.0 - Nu) * c_f2)

# ##   from fit to irf ######


def get_irf(out):
    """The peaks in the model should have prefix pic
    """
    data = dict()
    prefixs = [com.prefix for com in out.components if 'pic' in com.prefix]
    par_inf = ['center', 'H', 'HG', 'HL']

    def adst(i): return '{:s}_stderr'.format(i)

    for i in par_inf:
        data.update({i: np.array([])})
        data.update({adst(i): np.array([])})

    for pre in prefixs:
        for par in par_inf:
            par_s = out.params['{:s}{:s}'.format(pre, par)]
            data[par] = np.append(data[par], par_s.value)
            data[adst(par)] = np.append(data[adst(par)], par_s.stderr)
    for key, item in list(data.items()):
        data[key] = np.asarray(item)
    return data


def append_irf(data_old, data_new):
    for key in list(data_new.keys()):
        data_old[key] = np.hstack((data_old[key], data_new[key]))


def plot_irf(data, key=None):
    """plot an irf (a dictionary with key 
    'center', 'H', 'HG', 'HL','amplitude', 'Beta',
    and their error
                           ]
    """
    plt.figure()
    if key is None:
        key = ['H', 'HG', 'HL']
    for i in key:
        plt.errorbar(data['center'], data[i],
                     yerr=data[i + '_stderr'],
                     fmt='.', capsize=6, label=i)
    plt.legend()
    plt.xlabel(r'2$\theta$($\degree$)')
    plt.ylabel(r'FWHM 2$\theta$($\degree$)')


def deconv_IRF(data, Gfunc, Lfunc):
    theta2 = data['center']
    HG = data['HG']
    HL = data['HL']

    data['HGd'] = np.sqrt(HG**2 - Gfunc(theta2)**2)
    data['HLd'] = HL - Lfunc(theta2)
    data['Hd'] = getH(HG, HL)
    data['Nud'] = getNu(data['HLd'], data['Hd'])
    data['Beta_d'] = getB(data['Hd'], data['Nud'])


def plot_WillHall(data, typo='Beta_d', err=None):
    plt.figure()
    fg = plt.gcf()
    y = np.radians(data[typo]) / 2.0 * cos_d(data['center'] / 2.0)
    x = sin_d(data['center'] / 2.0)
    if err is not None:
        err = np.radians(err) / 2.0 * cos_d(data['center'] / 2.0)
    plt.errorbar(x, y, fmt='xb', picker=5, yerr=err, capsize=6)
    text = fg.text(0.2, 0, "", va="bottom", ha="left")
    plt.subplots_adjust(bottom=0.15)

    def onpick(event):
        t_ind = str(data['cry_i'][event.ind[0]])
        t_cen = str(np.round(data['center'][event.ind[0]], 2))
        t_amp = str(np.round(data['amplitude'][event.ind[0]], 2))

        try:
            text_i = '%s cen=%s amp=%s' % (t_ind, t_cen, t_amp)
        except KeyError:
            pass
        text.set_text(text_i)
    fg.canvas.mpl_connect('pick_event', onpick)
    plt.xlabel(r'sin($\theta$)')
    plt.ylabel(r'$B$cos($\theta$)($rad$)')
    plt.title('plot_WillHall')



##           Model Classes      #################


class CagliotiG(Model):
    """docstring for Caglioti
    model to fit gaussina H evolution as afunction of 
    """

    def __init__(self, *args, **kwargs):
        super(CagliotiG, self).__init__(GammaG, *args, **kwargs)
        self.set_param_hint('U', min=0,)
        self.set_param_hint('V', max=1,)
        self.set_param_hint('W', min=0,)
        # if 'Ig' in kwargs:
        #    if not(kwargs['Ig']):
        #        self.set_param_hint('Ig', value=0, min=0, vary=False)
        #        return
        self.set_param_hint('Ig', value=0, min=0)

    def guess(self, data, x, **kwargs):
        """
           quando ho tempo e voglia
        """
        theta = x / 2
        w = data[0]**2
        v = data.min()**2 - w
        v /= tan_d(theta[data.argmin()])
        u = data.max()**2 - (GammaG(theta[data.argmax()], U=0, W=w, V=v))**2
        u /= tan_d(theta[data.argmax()])**2
        pars = self.make_params(U=u, V=v, W=w, Ig=0)
        return update_param_vals(pars, self.prefix, **kwargs)


class L_model(Model):
    """docstring for Caglioti"""

    def __init__(self, *args, **kwargs):
        super(L_model, self).__init__(GammaL, *args, **kwargs)
        self.set_param_hint('X', min=0, vary=1)
        self.set_param_hint('Y', min=0, vary=1)


def plot_guess(x, y, model, param):
    Eval = model.eval(param, x=x)
    plt.figure()
    plt.plot(x, y, 'b')
    plt.plot(x, Eval, 'k--')
    plt.legend(['exp', 'ini'])
