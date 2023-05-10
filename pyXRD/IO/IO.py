#!/usr/bin/python
"""
pyXRDd.py - A set of python class to convert XRD data
Original author: C PRestipino

Version: 0.1 (some errors may exist!)

bruker format has been translate from cpp to python from library xyconv


varius usefull example
--------------------------------------
coluave=IO.XRDfile()
coluave.info.update(colu.info)
coluave.data=[]
for i in range(0,42,3):
    coluave.data.append(colu.merge(slicei=range(i,i+3), output=True))
    # coluave.data[-1].info.update(colu.data[i].info)
coluave.data.extend(colu.data[42:])
--------------------------------------

ax = gca()
ax.legend_ = None
draw()
"""


import numpy as np
from matplotlib import pylab as plt
from .bkground import spline_bkg
from .parsers import read_raw, read_D1B, read_id22

plt.ion()


def calc_x(start, step, data):
    start, step, = float(start), float(step)
    return np.array([start + step * i for i in np.arange(len(data))])


def set_UXDat(s, x):
    a = x[1:].replace(' ', '').strip().split('=')
    try:
        a, z = a
    except ValueError as rt:
        if len(a) == 1:
            a, z = a[0], None
        else:
            raise rt
    s[a] = z
    return


class XRDdata(np.ndarray):
    """class for import of uxd file

        method defined
        set_info
        def_bkg
        plot
        export
        err seetter


    """
    def __new__(cls, input_array, info=None):
        # Input array is an already formed ndarray instance
        # We first cast to be our class type
        obj = np.asarray(input_array).view(cls)
        # add the new attribute to the created instance
        obj.info = info
        obj.x = obj[:, 0]
        obj.y = obj[:, 1]
        try :
            obj.err = obj[:, 2]
        except:
            pass
        # Finally, we must return the newly created object:
        return obj

    def __array_finalize__(self, obj):
        # see InfoArray.__array_finalize__ for comments
        self.info = getattr(obj, 'info', None)
        self.x = getattr(obj, 'x', None)
        self.y = getattr(obj, 'y', None)

    def set_info(self, lin, val=None):
        """
        """
        if self.info is None:
            self.info = {}
        if val:
            self.info[lin] = val
        else:
            set_UXDat(self.info, lin)

    def plot(self, new=1, cps=False):
        if new:
            plt.figure()
        if cps:
            if self.info['UNIT'] == 'cps':
                plt.plot(self.x, self.cps)

        else:
            plt.errorbar(self.x, self.y, yerr=self.err,
                         capsize=2)
        plt.xlabel(r'2$\theta$ ($\degree$)')
        plt.ylabel('Intensity (counts)')

    def export(self, name, Format='xy', info=None,
               prec=None, bkg=False, inname=False):
        """ export to text function
        Args:
        name (str): basename
        Format (str): available 'xy', fullprof style'FPxy'
        info (str): info to put in the name
        prec (int): precision of the info in the name
        bkg (bool): if background should be subtracted
        inname is ifnfo shoul be in name
        
        Returns:
        bool: The return value. True for success, False otherwise.
        """
        if info:
            if prec is None:
                xx = self.info[info]
            elif prec > 0:
                xx = round(float(self.info[info]), prec)
            else:
                xx = int(round(float(self.info[info]), prec))
            xx = f'_{str(xx)}'
        else:
            xx = ''

        Fheader = ['XYDATA\n', '\n', '\n', '\n', '\n']
        Fcomments = '# '
        ext = Format

        if 'UNIT' in self.info:
            if self.info['UNIT'] == 'cps':
                Fheader[1] = 'UNIT= cps\n'
            elif self.info['UNIT'] == 'counts':
                Fheader[1] = 'UNIT= counts'
        else:
            if 'STEPTIME' in self.info:
                if type(self.info['STEPTIME']) is float:
                    Fheader[1] = 'UNIT= counts, in {:.3f} s\n'.format(
                        self.info['STEPTIME'])

        if bkg:
            Fheader[3] = 'background subtracted'

        if Format == 'FPxy':
            Fcomments = '! '

        if info:
            Fheader[2] = 'TEMP %s\n' % xx[1:]
        ext = 'xye'

        y = self.y
        if bkg and self._bkg:
            if bkg is True:
                y = self.y - self.bkg
            else:
                y = self.y - self.bkg + bkg
        if inname:
            name = '{:s}{:s}.{:s}'.format(name, xx, ext)
        else:
            name = '{:s}.{:s}'.format(name, ext)
        np.savetxt(name, np.vstack([self.x, y, self.err]).T,
                   fmt='%1.10f', header=''.join(Fheader), comments=Fcomments)

    def def_bkg(self):
        if hasattr(self, '_bkg'):
            self._bkg.plotter()
        else:
            self._bkg = spline_bkg(np.vstack([self.x, self.y]))

    @property
    def bkg(self):
        if isinstance(self._bkg, spline_bkg):
            return self._bkg.out(self.x)
        else:
            return self._bkg

    @bkg.setter
    def bkg(self, val):
        self._bkg = val

    @property
    def err(self):
        if not(hasattr(self, '_err')):
            if self.info['UNIT'] == 'counts':
                self._err = self.__cal_err(self.y)
            elif self.info['UNIT'] == 'cps':
                self._err = self.__cal_err(self.y, self.info['STEPTIME'])
        return self._err

    def __cal_err(self, y, time=None):
        if time is None:
            return np.sqrt(y)
        else:
            return np.sqrt(y) / np.sqrt(time)


    @err.setter
    def err(self, val):
        self._err = val

    @property
    def cps(self):
        if self.info['UNIT'] == 'cps':
            return self.y
        elif self.info['UNIT'] == 'counts':
            return self.y / self.info['STEPTIME']


class XRDfile(object):
    """class for import of xrd file
    class for import of xrd file derived by dict()
    values of the dictionary
    contains general info for the acquisition

    Attr:
        debug        : if one stop the reading
        file_status  : file status active done..
        version      : version of the orginal file
        data         : list with the scans
        merged       : list of x,y merged

    Methods:
        export
        plot
        plot_info
        print_info
        merge

    available format:
        by format keyword:
            'datILL'
            'datID22'
            'XY'
            'XYE'
        by extension:
            brucker raw V3 V4
            UDX
            XrdML
    """

    def __init__(self, filename=None, format=None, debug=False):
        # +super(XRDfile, self).__init__()
        self.debug = debug
        self.info = {}
        if format:
            if format.upper() == 'DATILL':
                read_D1B(self, filename)
                self.data = [XRDdata(i['array'], i['info']) for i in self.data]
            if format.upper() in ['DATID22', 'XY', 'XYE']:
                read_id22(self, filename)
                self.data = [XRDdata(i['array'], i['info']) for i in self.data]
        elif filename:
            if filename[-5:].upper() == 'XRDML':
                print('reading as XrdML (Panalytical)\n')
                try:
                    self._read_XrdML(filename)
                except Exception as error:
                    print('impossible to open as XrdML', error)
                    if debug:
                        self._read_XrdML(filename)
            elif filename[-3:].upper() == 'SIM':
                print('reading as sim\n')
                try:
                    self._read_sim(filename)
                except Exception as error:
                    print('impossible to open as sim', error)
                    if debug:
                        self._read_sim(filename)
            elif filename[-3:].upper() == 'UXD':
                print('reading as UXD\n')
                try:
                    self._read_UDX(filename)
                except Exception as error:
                    print('impossible to open as UXD', error)
                    if debug:
                        self._read_UDX(filename)
            elif filename[-3:].upper() == 'RAW':
                print('reading as RAW\n')
                #try:
                read_raw(self, filename)
                self.data = [XRDdata(i['array'],
                                     i['info']) for i in self.data]
                # except Exception as error:
                #     print('impossible to open as RAW', error)
                #     if debug:
                #         read_raw(self, filename)
            else:
                print('unknown format')

    def _read_sim(self, filename):
        with open(filename, 'r') as filex:
            flines = filex.readlines()
        start, step, stop, name = flines[0].split()
        start, step, stop = list(map(float, [start, step, stop]))
        y = np.array([])
        for lin in flines[1:]:
            y = np.append(y, np.fromstring(lin, sep=' '))
        x = np.arange(start, stop + step / 2., step)
        self.data = [XRDdata(np.vstack((x, y)).T)]

    def _read_UDX(self, filename):
        with open(filename, 'r') as filex:
            flines = filex.readlines()
        self.info['filename'] = flines.pop(0)[12:].split()[0].strip()
        self.data = []
        data = list()
        info = dict()
        flines.reverse()
        section = 'data_n'

        for lin in flines:
            if [x for x in ['Unknown', 'None'] if x in lin] or not(lin.strip()):
                continue
            elif lin[0] == '_':
                if section == 'General':
                    set_UXDat(self, lin)
                elif section == 'data_n':
                    section = 'data_i'
                elif section == 'data_i':
                    set_UXDat(info, lin)
            elif lin[0] == ';':
                if 'Data for' in lin:
                    data.reverse()
                    for i in ["START", "STEPSIZE", "STEPTIME"]:
                        info[i] = float(info[i])
                    x = calc_x(info["START"], info["STEPSIZE"], data)
                    data = np.vstack((x, np.loadtxt(data))).T
                    self.data.insert(0, XRDdata(data, info=info))
                    info, data, section = {}, [], 'General'
                else:
                    try:
                        a, z = lin[1:].strip().split()
                        self.info[a] = z
                    except Exception:
                        pass

            else:
                data.append(lin)
                section = 'data_n'
        if section == 'data_n':
            raise ValueError('no data readed')
        pass
        for j, i in enumerate(self.data):
            i.info['index'] = j

    def _read_XrdML(self, filename):
        import xml.etree.ElementTree as ET
        tree = ET.parse(filename)
        root = tree.getroot()
        name_space = root.tag[0:root.tag.find('}')] + '}'
        self.info['filename'] = filename
        self.info['status'] = root.attrib['status']
        self.data = []
        xrdmes = root.find(name_space + 'xrdMeasurement')
        scans = xrdmes.findall(name_space + 'scan')
        for scan in scans:
            info = dict()
            info['startTimeStamp'] = scan.find(
                './/%sstartTimeStamp' % name_space).text
            t2p = scan.find('.//*[@axis="2Theta"]')
            t2sp = float(t2p.find('{:s}startPosition'.format(name_space)).text)
            t2ep = float(t2p.find('{:s}endPosition'.format(name_space)).text)

            info['STEPTIME'] = float(
                scan.find('.//%scommonCountingTime' % name_space).text)
            intensity = scan.find('.//%sintensities' % name_space)
            info['UNIT'] = intensity.get('unit')
            y = np.fromstring(intensity.text, sep=' ')
            x = np.linspace(t2sp, t2ep, len(y))

            t2p = scan.find('.//%snonAmbientPoints' % name_space)
            if t2p is not None:
                info[t2p.get('type')] = t2p.find(
                    './%snonAmbientValues' % name_space).text
            self.data.append(XRDdata(np.vstack((x, y)).T, info=info))
        for j, i in enumerate(self.data):
            i.info['index'] = j

    def export(self, root='xrd', Format='xy', info=None, prec=None,
               inname=False):
        """
           Export available format
           'xy' simple xy without comments
           'FPxy' xy at the way of FullProf
           'block'  datablock of y
           info precise if an info must be used in the name
           prec is precision of the info
           ex.
           colu.export(root='colu600T', Format='FPxy',
                       info='TEMPERATURE', prec=1)
        """

        if len(self.data) == 1:
            self.data[0].export(root, Format=Format, info=info, prec=prec)
            return
        width = len(str(len(self.data) - 1))
        if Format == 'block':
            data = np.vstack([i.cps for i in self.data])
            np.savetxt(root,data)
        for j, i in enumerate(self.data):
            if Format == 'FPxy':
                name = '{:s}-{:d}'.format(root, j)
            else:
                name = '{:s}_{:0{}d}'.format(root, j, width)
            i.export(name, Format=Format, info=info, prec=prec, inname=inname)
        return

    def plot(self, shift=0, start=None, stop=None, info='index',
             new=True):
        '''plot the different scans
        '''
        if new:
            def onpick(event):
                print('\n{} = {}'.format(info, event.artist.get_label()))
            a = plt.figure()
            a.canvas.mpl_connect('pick_event', onpick)

        for j, i in enumerate(self.data[start:stop]):
            if i.info['UNIT'] == 'counts':
                y = i.y / i.info['STEPTIME']
            else:
                y = i.y
            plt.plot(i.x, y + j * shift, label=str(i.info[info]),
                     picker=True, pickradius=5)
        plt.xlabel(r'2$\theta$ ($\degree$)')
        plt.ylabel('Intensity (cps)')
        if len(self.data[start:stop]) < 11:
            plt.legend()

    def plot_info(self, info, new=1, *args, **keyargs):
        '''plot a scan info as function of the scan number
           *args, **keyargs are argument for the plot

           ex:
           -------------------
           ele1.plot_info('TEMPERATURE')
        '''
        if new:
            plt.figure()
        x = [i.info['index'] for i in self.data]
        y = [float(i.info[info]) for i in self.data]
        plt.plot(x, y, label=info, *args, **keyargs)

    def D2plot(self, log=0, start=None, stop=None, info='index', **keyargs):
        plt.figure()
        data = np.vstack([i.cps for i in self.data[start:stop]])
        data = np.flip(data, axis=0)
        print(data.shape)
        if log:
            data = np.log(data)
        x = self.data[0].x
        y = [i.info[info] for i in self.data[start:stop]]
        plt.imshow(data, aspect='auto', extent=(
            x[0], x[-1], y[0], y[-1]), **keyargs)
        plt.xlabel(r'2$\theta$ ($\degree$)')
        plt.ylabel(info)

    def get_info(self, info):
        '''print a scan info as function of the scan number
        '''
        x = [i.info['index'] for i in self.data]
        y = [float(i.info[info]) for i in self.data]
        for i in zip(x, y):
            print(i)
        return y


    def merge(self, slicei=None, plot=True, output=False):
        '''merge a set of scan
        slicei = list of xrd dato to be merged
        merge (bool): if true create a self.merged
        '''
        if slicei is None:
            slicei = list(range(len(self.data)))

        setdata = [self.data[i] for i in slicei]

        merged = merge_XRD(setdata, plot=plot)
        if output:
            return merged
        self.merged = merged

    def peak_intensity(self, xmin, xmax, start=None, stop=None,
                       plot=True, info=None):
        x = [i.info['index'] for i in self.data]
        axmin = np.searchsorted(self.data[start:stop][0].x, xmin)
        axmax = np.searchsorted(self.data[start:stop][0].x, xmax)
        step = (xmax - xmin) / 2

        def integP(i):
            fp = np.trapz(i.y[axmin:axmax], i.x[axmin:axmax])
            return fp - (step * (i.y[axmin] + i.y[axmax]))

        y = [integP(i) for i in self.data[start:stop]]

        if plot:
            c1 = 'tab:blue'
            fig, ax1 = plt.subplots()
            ax1.plot(x, y, '.-', color=c1)
            ax1.set_xlabel('index')
            ax1.set_ylabel('integrated intensity')
            if info:
                c2 = 'tab:red'
                ax1.tick_params(axis='y', labelcolor=c1)
                ax1.set_ylabel('integrated intensity', color=c1)
                ax2 = ax1.twinx()
                ax2.plot(x,
                         [float(i.info[info]) for i in self.data[start:stop]],
                         '-', color=c2)
                ax2.set_ylabel(info, color=c2)
                ax2.tick_params(axis='y', labelcolor=c2)
            plt.title(f'range {xmin}--{xmax}')
        return np.vstack((x, y))


def merge_XRD(slicei, plot=True):
    """
    merge several patters
    keepinf metadata information
    only tewsted with raw brucker file

    to see with the experiment done for pierric

    Args:
        slice = list of XRDdata
    """

    d_inf = {}
    d_inf.update(slicei[0].info)

    one_x = all([np.array_equal(slicei[0].x, i.x) for i in slicei])

    if one_x:
        d_inf.info['STEPTIME'] = np.sum([j.info['STEPTIME']
                                         for j in slicei], axis=0)
        x = slicei[0].x
        y = np.sum([j.y for j in slicei], axis=0)
        d_inf.info['UNIT'] = 'counts'

    else:
        d_inf['x_max'] = np.round(max([i.x[-1] for i in slicei]), 7)
        d_inf['START'] = np.round(min([i.x[0] for i in slicei]), 7)
        d_inf['STEPSIZE'] = max([i.info['STEPSIZE'] for i in slicei])
        d_inf['STEPSIZE'] = np.round(d_inf['STEPSIZE'], 7)

        x = np.arange(d_inf['START'],
                      d_inf['x_max'] + d_inf['STEPSIZE'] / 2,
                      d_inf['STEPSIZE'])

        y, time = np.zeros((2, *x.shape))

        for j in slicei:
            j_y = np.interp(x, j.x, j.y,
                            left=-1, right=-1.0)
            y += np.where(j_y > -1, j_y, 0)

            time += np.where(j_y > -1, j.info['STEPTIME'], 0)
        d_inf['UNIT'] = 'cps'

        while True:
            if time[-1] == 0:
                time = time[:-1]
                x = x[:-1]
                y = y[:-1]
            else:
                break

        d_inf['STEPTIME'] = time
        y /= time

    merged = XRDdata(np.vstack((x, y)).T, info=d_inf)

    if plot:
        for j, i in enumerate(slicei):
            plt.plot(i.x, i.y/i.info['STEPTIME'], label=str(j))
        plt.plot(merged.x, merged.y+max(merged.y), '.-')

    return merged


class STRfile(dict):
    """ALLOWS TO READ STR file from ICSD
    """

    def __init__(self, filename=None, debug=False):
        super(STRfile, self).__init__()
        if filename:
            if filename[-3:].upper() == 'TXT':
                print('reading as txt icsd\n')
                try:
                    self.read_txt(filename)
                except Exception as error:
                    print('impossible to open as txt')
                    if debug:
                        self.read_txt(filename)

        pass

    def read_txt(self, filename):
        def read_par(s):
            return s[:12].strip().replace(' ', '_'), s[12:].strip()

        def form_s(s):
            try:
                s = int(s)
            except ValueError:
                try:
                    s = float(s)
                except:
                    pass
            return s

        with open(filename, 'r') as filex:
            txt = iter(filex.readlines()[3:])

        c = ''
        for line in txt:
            # print line
            try:
                a, b = read_par(line)
            except IndexError:
                a = ''

            if a:
                c = a
                if a in ['Coll_Code', 'Z', 'SG_Number']:
                    self.info[a] = int(b)
                elif a in ['D(calc)', 'Vol', 'Formula Wt']:
                    self.info[a] = float(b)
                elif a in ['Unit_Cell']:
                    pass
                if 'Atom' in a:
                    if 'Std._Cell' in self:
                        atoms = []
                        keys = line.split()
                        keys.insert(3, 'MULT')
                        while True:
                            a = txt.next().replace('++', '+').split()
                            if 'end' in a[0]:
                                break
                            else:
                                a = list(zip(keys, list(map(form_s, a))))
                                atoms.append(dict(a))
                        self.info['Atoms'] = atoms
                    else:
                        while True:
                            a, b = read_par(next(txt))
                            if a in ['Std._Notes']:
                                c, self.info[a], = a, b
                                break
                else:
                    self.info[a] = b
            else:
                self.info[c] = '{}\n{}'.format(self.info[c], b)
        self.info['Symmetry'] = self.info['Symmetry'].split('\n')
        self.info['Symmetry'] = [x.split(' ' * 3)[-1]
                                 for x in self.info['Symmetry']]
        return


def convert_raw(item):
    a = XRDfile(item)
    a.export(root=item[:-4])


if __name__ == '__main__':
    import sys
    print('Number of pattern to convert:', len(sys.argv) - 1)
    for item in sys.argv[1:]:
        convert_raw(item)
