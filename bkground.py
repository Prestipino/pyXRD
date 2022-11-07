from numpy import pi
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
from scipy.interpolate import UnivariateSpline



min_bkg=False

c_ln2 = np.log(2.0)
c_ln2pi = c_ln2 / np.pi
c_s2pi = np.sqrt(2 * pi)
c_f2 = np.sqrt(c_ln2 * np.pi)


class polyfitFig:
    def __init__(self, data, bkpos=40):
        '''
           bkpos=origin of the polynomial see fullprof manual
        '''
        poly_degree = str(6)
        initial_text = poly_degree
        self.Bkpos = bkpos

        self.fig, self.ax = plt.subplots()

        plt.subplots_adjust(bottom=0.2)
        # data line
        self.l, = plt.plot(data[0], data[1], 'k')
        # bkg line
        self.b, = plt.plot([], [], 'r')
        self.polyl, = plt.plot([], [], 'o')

        plt.xlabel('2$\Theta$($\degree$)')
        plt.ylabel('Intensity (Counts)')

        def onpick(event):
            if not(event.inaxes == self.ax):
                return
            if plt.get_current_fig_manager().toolbar.mode != '':
                return
            xpoly = self.polyl.get_xdata()
            ypoly = self.polyl.get_ydata()
            if event.button < 3:
                i = np.searchsorted(xpoly, event.xdata)
                xpoly = np.insert(xpoly, i, event.xdata)
                if event.button == 2:
                    ypoly = np.insert(ypoly, i, data[1][i])
                elif event.button == 1:
                    ypoly = np.insert(ypoly, i, event.ydata)
            if event.button == 3:
                i = (np.abs(xpoly - event.xdata)).argmin()
                xpoly = np.delete(xpoly, i)
                ypoly = np.delete(ypoly, i)
            self.polyl.set_xdata(xpoly)
            self.polyl.set_ydata(ypoly)
            plt.draw()
            if len(xpoly) > 3:
                submit(text_box.text)
        # cid = fig.canvas.mpl_connect('button_press_event', onclick)

        def submit(text):
            xpoly = self.polyl.get_xdata()
            ypoly = self.polyl.get_ydata()
            poly_degree = min(eval(text), len(xpoly) - 1)
            xpoly = xpoly / self.Bkpos - 1
            self.out = np.poly1d(np.polyfit(xpoly, ypoly, poly_degree))
            self.b.set_ydata(self.out(data[0] / self.Bkpos - 1))
            self.b.set_xdata(data[0])
            plt.draw()
            return

        self.fig.canvas.mpl_connect('button_press_event', onpick)
        axbox = plt.axes([0.25, 0.02, 0.1, 0.055])
        text_box = TextBox(axbox, 'Poly degree', initial=initial_text)
        text_box.on_submit(submit)

    def debye(self, r, B, wv):
        self.r = r
        self.B = B
        if hasattr(self, 'D'):
            pass
        else:
            self.D, = self.ax.plot([], [])
        Q = 4 * np.pi * np.sin(self.l.get_xdata() * np.pi / 360.0) / wv
        self.df = np.zeros(len(Q))
        for ri, bi in zip(r, B):
            self.df += bi * np.sin(Q * ri) / Q * ri

        self.D.set_xdata(self.l.get_xdata())
        self.D.set_ydata(self.df)
        plt.draw()
        return


class spline_bkg:
    '''interactive background for difficult background
    '''

    def __init__(self, data):
        if isinstance(data, str):
            data = np.loadtxt(data).T
        self.data = data

        self.fig, self.ax = plt.subplots()
        # data line
        self.li, = plt.plot(data[0], data[1], 'k')
        # self.li = plt.errorbar(x=data[0], y=data[1], yerr=data[2],
        #                        fmt='k', capsize=3)
        self.b, = plt.plot([], [], 'r')
        self.polyl, = plt.plot([], [], 'o')

        plt.xlabel('2$\Theta$($\degree$)')
        plt.ylabel('Intensity (Counts)')

        def onpick(event):
            if not(event.inaxes == self.ax):
                return
            if plt.get_current_fig_manager().toolbar.mode != '':
                return
            xpoly = self.polyl.get_xdata()
            ypoly = self.polyl.get_ydata()
            if event.button < 3:
                i = np.searchsorted(xpoly, event.xdata)
                xpoly = np.insert(xpoly, i, event.xdata)
                if event.button == 2:
                    ypoly = np.insert(ypoly, i, data[1][i])
                elif event.button == 1:
                    ypoly = np.insert(ypoly, i, event.ydata)
            if event.button == 3:
                i = (np.abs(xpoly - event.xdata)).argmin()
                xpoly = np.delete(xpoly, i)
                ypoly = np.delete(ypoly, i)
            self.polyl.set_xdata(xpoly)
            self.polyl.set_ydata(ypoly)
            plt.draw()
            if len(xpoly) > 3:
                submit()
        # cid = fig.canvas.mpl_connect('button_press_event', onclick)

        def submit():
            xpoly = self.polyl.get_xdata()
            ypoly = self.polyl.get_ydata()
            self.out = UnivariateSpline(xpoly, ypoly)
            self.b.set_ydata(self.out(data[0]))
            self.b.set_xdata(data[0])
            self.ax.draw_artist(self.b)
            return

        self.fig.canvas.mpl_connect('button_press_event', onpick)

    def get_signal(self):
        bkg = self.out(self.data[0])
        if min_bkg:
            minus = min(bkg)
        else:
            minus = 0
        y = self.data[1] - bkg + minus
        return np.vstack([self.data[0], y])

    def save_signal(self, filname, shift=0):
        data = self.get_signal()
        data[1] = data[1] + shift
        np.savetxt(filname, data.T)

    def save_bkgpoints(self, filname):
        xpoly = self.polyl.get_xdata()
        ypoly = self.polyl.get_ydata()
        np.savetxt(filname, np.vstack((xpoly, ypoly)).T)

