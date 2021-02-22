#!/usr/bin/python
"""
pyXRDd.py - A set of python class to convert XRD data
Original author: C PRestipino

Version: 0.1 (some errors may exist!)

bruker format has been translate from cpp to python from library xyconv


varius usefull example
--------------------------------------
coluave=IO.XRDfile()
coluave.data=[]
for i in range(0,42,3):
    coluave.data.append(colu.merge(slicei=range(i,i+3), output=True))
    coluave.data[-1].info.update(colu.data[i].info)
coluave.data.extend(colu.data[42:])
--------------------------------------

ax = gca()
ax.legend_ = None
draw()
"""


import numpy as np
from matplotlib import pylab as plt
from .parsers import read_raw, read_D1B

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

    """
    def __new__(cls, input_array, info=None):
        # Input array is an already formed ndarray instance
        # We first cast to be our class type
        obj = np.asarray(input_array).view(cls)
        # add the new attribute to the created instance
        obj.info = info
        obj.x = obj[:, 0]
        obj.y = obj[:, 1]
        # Finally, we must return the newly created object:
        return obj

    def __array_finalize__(self, obj):
        # see InfoArray.__array_finalize__ for comments
        self.info = getattr(obj, 'info', None)
        self.x = getattr(obj, 'x', None)
        self.y = getattr(obj, 'y', None)

    def set_info(self, lin, val=None):
        if self.info is None:
            self.info = {}
        if val:
            self.info[lin] = val
        else:
            set_UXDat(self.info, lin)

    def plot(self, new=1):
        plt.figure()
        plt.plot(self.x, self.y)
        plt.xlabel(r'2$\theta$ ($\degree$)')
        plt.ylabel('Intensity (counts)')
        plt.legend()


class XRDfile(dict):
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
        by extension:
            brucker raw V3 V4
            UDX
            XrdML
    """

    def __init__(self, filename=None, format=None, debug=False):
        super(XRDfile, self).__init__()
        self.debug = debug
        if format:
            if format == 'datILL':
                read_D1B(self, filename)
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
            if filename[-3:].upper() == 'SIM':
                print('reading as sim\n')
                try:
                    self._read_sim(filename)
                except Exception as error:
                    print('impossible to open as sim', error)
                    if debug:
                        self._read_sim(filename)
            if filename[-3:].upper() == 'UXD':
                print('reading as UXD\n')
                try:
                    self._read_UDX(filename)
                except Exception as error:
                    print('impossible to open as UXD', error)
                    if debug:
                        self._read_UDX(filename)
            if filename[-3:].upper() == 'RAW':
                print('reading as RAW\n')
                try:
                    read_raw(self, filename)
                    self.data = [XRDfile(i['array'], i['info']) for i in self.data]
                except Exception as error:
                    print('impossible to open as RAW', error)
                    if debug:
                        read_raw(self, filename)
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
        self['filename'] = flines.pop(0)[12:].split()[0].strip()
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
                        self[a] = z
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
        self['filename'] = filename
        self['status'] = root.attrib['status']
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

            y = np.fromstring(scan.find('.//%sintensities' %
                                        name_space).text, sep=' ')
            x = np.linspace(t2sp, t2ep, len(y))

            t2p = scan.find('.//%snonAmbientPoints' % name_space)
            if t2p is not None:
                info[t2p.get('type')] = t2p.find(
                    './%snonAmbientValues' % name_space).text
            self.data.append(XRDdata(np.vstack((x, y)).T, info=info))
        for j, i in enumerate(self.data):
            i.info['index'] = j

    def export(self, root='xrd', Format='xy', info=None, prec=None):
        """
           Export available format
           'xy' simple xy without comments
           'FPxy' xy at the way of FullProf
           info precise if an info must be used in the name
           prec is precision of the info
           ex.
           colu.export(root='colu600T', Format='Fxy', info='TEMPERATURE', prec=1)
        """
        def gen_xx(data):
            if info:
                if prec is None:
                    xx = data.info[info]
                elif prec > 0:
                    xx = round(float(data.info[info]), prec)
                else:
                    xx = int(round(float(data.info[info]), prec))
                xx = '_' + str(xx)
            else:
                xx = ''
            return xx

        Fheader = ''
        Fcomments = '# '
        ext = Format
        if Format == 'FPxy':
            Fcomments = '! '
            Fheader = 'XYDATA\n\n\n\n\n'
            ext = 'xy'

        if len(self.data) == 1:
            xx = gen_xx(self.data[0])
            if Format == 'FPxy':
                Fheader = 'XYDATA\n\nTEMP %s\n\n\n' % xx[1:]
            name = '{:s}{:s}.{:s}'.format(root, xx, ext)
            np.savetxt(name, self.data[0], fmt='%1.10f',
                       header=Fheader, comments=Fcomments)
            return
        width = len(str(len(self.data) - 1))
        for j, i in enumerate(self.data):
            xx = gen_xx(i)
            if Format == 'FPxy':
                name = '{:s}-{:d}'.format(root, j)
                Fheader = 'XYDATA\n\nTEMP %s\n\n\n' % xx[1:]
            else:
                name = '{:s}_{:0{}d}'.format(root, j, width)
            name = '{:s}{:s}.{:s}'.format(name, xx, ext)
            np.savetxt(name, i, fmt='%1.10f',
                       header=Fheader, comments=Fcomments)
        return

    def plot(self, shift=0, start=None, stop=None, info='index', new=True):
        '''plot the different scans
        '''
        if new:
            def onpick(event):
                print('\n{} = {}'.format(info, event.artist.get_label()))
            a = plt.figure()
            a.canvas.mpl_connect('pick_event', onpick)

        for j, i in enumerate(self.data[start:stop]):
            plt.plot(i.x, i.y + j * shift, label=str(i.info[info]), picker=5)
        plt.xlabel(r'2$\theta$ ($\degree$)')
        plt.ylabel('Intensity (counts)')
        if len(self.data[start:stop]) < 11:
            plt.legend()

    def plot_info(self, info, *args, **keyargs):
        '''plot a scan info as function of the scan number
           *args, **keyargs are argument for the plot
        '''
        x = [i.info['index'] for i in self.data]
        y = [float(i.info[info]) for i in self.data]
        plt.plot(x, y, label=info, *args, **keyargs)

    def D2plot(self, log=0, start=None, stop=None, info='index', **keyargs):
        plt.figure()
        data = np.vstack([i.y for i in self.data[start:stop]])
        print(data.shape)
        if log:
            data = np.log(data)
        x = self.data[0].x
        y = [i.info[info] for i in self.data]
        plt.imshow(data, aspect='auto', extent=(x[0], x[-1], y[0], y[-1]), **keyargs)
        plt.xlabel(r'2$\theta$ ($\degree$)')
        plt.ylabel(info)

    def print_info(self, info):
        '''print a scan info as function of the scan number
        '''
        x = [i.info['index'] for i in self.data]
        y = [float(i.info[info]) for i in self.data]
        for i in zip(x, y):
            print(i)

    def merge(self, slicei=None, plot=True, output=False):
        '''merge a set of scan
        slicei = list of xrd dato to be merged
        merge (bool): if true create a self.merged
        '''
        if slicei is None:
            slicei = list(range(len(self.data)))

        data = self.data
        d_inf = {i: {} for i in slicei}

        d_inf['x_max'] = max([data[i].x[-1] for i in slicei])
        d_inf['START'] = min([data[i].x[0] for i in slicei])
        d_inf['STEPSIZE'] = max([data[i].info['STEPSIZE'] for i in slicei])

        x = np.arange(d_inf['START'], d_inf['x_max'], d_inf['STEPSIZE'])

        moretime = len(set([i.info['STEPTIME'] for i in data])) > 1

        for j in slicei:
            d_inf[j]['y'] = np.interp(x, data[j].x, data[j].y,
                                      left=-1, right=-1.0)

            d_inf[j]['time'] = np.where(d_inf[j]['y'] > -1.0, 1.0, 0.0)

            if moretime:
                d_inf[j]['time'] *= data[j].info['STEPTIME']

            d_inf[j]['y'] = np.where(d_inf[j]['y'] > -1, d_inf[j]['y'], 0)

        time_tot = np.sum([d_inf[j]['time'] for j in slicei], axis=0)
        y_tot = np.sum([d_inf[j]['y'] for j in slicei], axis=0)
        y = y_tot / time_tot

        if moretime:
            d_inf['UNIT'] = 'cps'
            d_inf['STEPTIME'] = time_tot
        else:
            d_inf['UNIT'] = 'counts'
            d_inf['STEPTIME'] = time_tot * data[0].info['STEPTIME']
            d_inf['STEPTIME0'] = data[0].info['STEPTIME']

        # remove all the single scan info
        for i in list(d_inf.keys()):
            if isinstance(i, int):
                del d_inf[i]
        if output:
            return XRDdata(np.vstack((x, y)).T, info=d_inf)
        self.merged = XRDdata(np.vstack((x, y)).T, info=d_inf)

        if plot:
            self.plot()
            plt.plot(self.merged.x, self.merged.y, '.-')


def merge_XRD(slicei):
    """merge several patters
    keepinf metadata information 
    only tewsted with raw brucker file 

    to see with the experiment done for pierric

    Args:
        slice = list of XRDdata
    """
    qnt = list(range(len(slicei)))

    d_inf = {i: {} for i in qnt}

    d_inf['x_max'] = max([i.info['x_max'] for i in slicei])
    d_inf['START'] = min([i.info['START'] for i in slicei])
    d_inf['STEPSIZE'] = max([i.info['STEPSIZE'] for i in slicei])

    x = np.arange(d_inf['START'], d_inf['x_max'], d_inf['STEPSIZE'])

    time = slicei[0].info['STEPTIME']
    moretime = sum(sum([i.info['STEPTIME'] != time for i in slicei]))

    for j in qnt:
        d_inf[j]['y'] = np.interp(x, slicei[j].x, slicei[j].y,
                                  left=-1, right=-1.0)

        d_inf[j]['time'] = np.where(d_inf[j]['y'] > -1.0, 1.0, 0.0)

        if moretime:
            d_inf[j]['time'] *= np.interp(x, slicei[j].x, slicei[j].info['STEPTIME'],
                                          left=-1, right=-1.0)

        d_inf[j]['y'] = np.where(d_inf[j]['y'] > -1, d_inf[j]['y'], 0)

    time_tot = np.sum([d_inf[j]['time'] for j in qnt], axis=0)
    y_tot = np.sum([d_inf[j]['y'] for j in qnt], axis=0)
    y = y_tot / time_tot

    if moretime:
        d_inf['UNIT'] = 'cps'
        d_inf['STEPTIME'] = time_tot
    else:
        d_inf['UNIT'] = 'counts'
        d_inf['STEPTIME'] = time_tot * time
        d_inf['STEPTIME0'] = time

    # remove all the single scan info
    for i in list(d_inf.keys()):
        if isinstance(i, int):
            del d_inf[i]

    merged = XRDdata(np.vstack((x, y)).T, info=d_inf)

    plt.figure()
    for j, i in enumerate(slicei):
        plt.plot(i.x, i.y, label=str(j))

    plt.plot(merged.x, merged.y, '.-', label='merged')
    plt.legend()
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
                    self[a] = int(b)
                elif a in ['D(calc)', 'Vol', 'Formula Wt']:
                    self[a] = float(b)
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
                        self['Atoms'] = atoms
                    else:
                        while True:
                            a, b = read_par(next(txt))
                            if a in ['Std._Notes']:
                                c, self[a], = a, b
                                break
                else:
                    self[a] = b
            else:
                self[c] = '{}\n{}'.format(self[c], b)
        self['Symmetry'] = self['Symmetry'].split('\n')
        self['Symmetry'] = [x.split(' ' * 3)[-1] for x in self['Symmetry']]
        return


def convert_raw(item):
    a = XRDfile(item)
    a.export(root=item[:-4])


if __name__ == '__main__':
    import sys
    print('Number of pattern to convert:', len(sys.argv) - 1)
    for item in sys.argv[1:]:
        convert_raw(item)
