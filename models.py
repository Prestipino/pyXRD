#
#

# import sys
import glob
# import shutil
import numpy as np
import re
import os
import subprocess


# ####### PCR Names
sample = 'fit_lpf109'  # only stuff to touch
Spg = 'SPGR  P -4 3 n'
Biso = 0.5


# to limit to the first n models_filename = glob.glob("models/M*.txt")[:2]
#models_filename = glob.glob("../gen_model/M*.pcr")
#pcr_ener_files = ['ener0.pcr', 'ener1.pcr', 'ener2.pcr', 'ener3.pcr']

######################


def __extra_del_phasexyz(lines, extract=True, Sing_Cry=False):
    '''
    REmove from a pcr files the block of lines
    describing the crystal structure  of the first phase
    Args:
       lines (list):list of the lines of a pcr file 
       extract (bool): if true extract XYZ model
                       if false extract the rest of the file 
    '''
    texto = []
    zcond = 0
    end_cond = '!-------> Scale' if Sing_Cry else '!-------> Profile'

    for i in lines:
        if '!  Data for PHASE number:   1' in i:
            zcond = 1
        if end_cond in i:
            if extract:
                break
            else:
                zcond = 0
        if zcond and extract:
            texto.append(i)
        elif not(zcond) and not(extract):
            texto.append(i)
    return texto


def run_models(models_filename=models_filename,
               pcr_ener_files=pcr_ener_files,
               command=None, Sing_Cry=False, stepwait=3):
    '''
       run fullprof for several structurasl models fro several energy
       input:
          models_filename: list with all the
                           filenames from wich extrat the tructural model
          pcr_ener_files= list with all the
                           filenames from wich insert the tructural model
          command string to insert in command mode for fullprof
          stepwait = numper of paralel process
    '''
    # number of energy
    n_ener = len(pcr_ener_files)
    # utility couners for the wait
    i = 0

    if isinstance(models_filename, str):
        models_filename = [models_filename]

    def o_name(namex):
        return os.path.basename(namex)[:-4]

    # import base pcr
    pcr_ener_inp = []
    inser_in_pcr = []
    for pcr in pcr_ener_files:
        with open(pcr) as pcr_i:
            pcrall = pcr_i.readlines()
        for line_n in range(len(pcrall)):
            if '!  Data for PHASE number:   1' in pcrall[line_n]:
                inser_in_pcr.append(line_n)
        pcrall = __extra_del_phasexyz(pcrall, extract=False, Sing_Cry=Sing_Cry)
        pcr_ener_inp.append(pcrall)
    #

    # start of the cycle
    for mod_name in models_filename:
        print('# %s' % mod_name)
        for ener in range(n_ener):
            # dire = output model directory
            dire = os.path.join(sample, o_name(mod_name))
            pcrname = os.path.join(dire,
                                   o_name(mod_name) + pcr_ener_files[ener])

            # create the dire directory if not existe
            if not os.path.exists(dire):
                os.mkdir(dire)

            # impoer xyz model
            with open(mod_name) as mod_i:
                modxyz = __extra_del_phasexyz(mod_i.readlines(), True)
                #Check if is a new format of pcr 
                if sum([1 if '!Contributions' in ie else 0 for ie in modxyz]):
                    pass
                else:
                    nat = modxyz[5].split()[0]
                    modxyz = __convert_oldxyz2new(modxyz, nat)

                if Sing_Cry:
                    modxyz[9]=   '   4   0    0      0      0\n'

                if command:
                    modxyz[2] = command



            # import base pcr
            pcrall = pcr_ener_inp[ener][:]

            pcrall.insert(inser_in_pcr[ener], ''.join(modxyz))
            pcrall[0] = 'COMM  %s %s' % (
                os.path.basename(mod_name)[:-4], pcrall[0][4:])
            with open(pcrname, 'w') as pcr_i:
                pcr_i.writelines(pcrall)
            # launch fullprof
            if i == 0:
               p = subprocess.Popen(['fp2k.exe', pcrname],
                              creationflags = subprocess.CREATE_NO_WINDOW)
            else :
               xxx=subprocess.Popen(['fp2k.exe', pcrname],
                              creationflags = subprocess.CREATE_NO_WINDOW).pid
            i += 1
            if not(i % stepwait):
                p.wait()
                i=0

    return


def run_models2(models, pcr_ener_files,
                commands=None, Sing_Cry=False,
                Biso=0.5, stepwait=3):
    '''
       run fullprof for several structurasl models fro several energy
       input:
          models_filename: list with all the
                           filenames from wich extrat the tructural model
          pcr_ener_files= list with all the
                           filenames in which insert the tructural model
          command string to insert in command mode for fullprof
          stepwait = numper of paralel process
    '''
    n_ener = len(pcr_ener_files)
    # utility couners for the wait
    i = 0

    # import base pcr
    # pcr_ener_inp = list of list contining the pcr lines
    #                 apart from struture of phase 1
    # inser_in_pcr = list of the line numbers where insert phase 1 info
    pcr_ener_inp = []
    inser_in_pcr = []
    for pcr in pcr_ener_files:
        with open(pcr) as pcr_i:
            pcr_all = pcr_i.readlines()
            pcr_ener_inp.append(__extra_del_phasexyz(pcr_all, extract=False,
                                                     Sing_Cry=Sing_Cry))
        for line_n, line in enumerate(pcr_all):
            if '!  Data for PHASE number:   1' in line:
                inser_in_pcr.append(line_n)
    pass

    # start of the cycle
    for mod_i in range(len(models)):
        print('# %d' % mod_i)
        for ener in range(n_ener):
            # dire = output model directory
            dire = os.path.join(sample, f'mod{mod_i:05d}')
            pcrname = os.path.join(dire, f'm{i:04d}{pcr_ener_files[ener]:s}')

            # create the dire directory if not existe
            if not os.path.exists(dire):
                os.mkdir(dire)

            # import xyz model
            xyz = models._obji2pcrxyz(mod_i, Spg=Spg, patterns=1, Npr=5,
                                      Biso=Biso, sincry=Sing_Cry,
                                      commands=commands, title=f'm{i:04d}')




            # import base pcr
            pcrall = pcr_ener_inp[ener][:]

            pcrall.insert(inser_in_pcr[ener], ''.join(xyz))
            pcrall[0] = 'COMM  %s %s' % (
                os.path.basename(mod_name)[:-4], pcrall[0][4:])
            with open(pcrname, 'w') as pcr_i:
                pcr_i.writelines(pcrall)
            # launch fullprof
            if i == 0:
               p = subprocess.Popen(['fp2k.exe', pcrname],
                              creationflags = subprocess.CREATE_NO_WINDOW)
            else :
               xxx=subprocess.Popen(['fp2k.exe', pcrname],
                              creationflags = subprocess.CREATE_NO_WINDOW).pid
            i += 1
            if not(i % stepwait):
                p.wait()
                i=0


def gen_names(filebase, ext, start, stop, step):
    nam = []
    for i in np.arange(start, stop, step):
        nam.append("%s%0.2d.pcr" % (filebase, i))
    return nam


def fp2krun(filebase):
    for i in filebase:
        os.system("fp2k %s" % i)
    return


def read_hkl(filename, nline=30):  # nline =number of reflection read
    """
    read hkl from hkl(format 4) from hkl files
    nline = number of reflection
    """
    hkl = {}
    with open(filename, 'r') as hkl_f:
        for i in range(3):
            hkl_f.readline()
        for i in range(nline):
            a = hkl_f.readline().split()
            name = ' '.join(a[:3])
            hkl[name] = float(a[8])
    return hkl


def read_allhkl(npeaks=30):
    '''
    readl all  the hkl files for all the energy

    is based on the idea that files are called modNNNenerN.hkl
    returns a dictionary
    {model:{energy:{khl:f2}}}

    '''
    hkl_mod = {}
    for r, d, f in os.walk(sample):
        for file in f:
            if '.hkl' in file:
                #print(file)
                mod, ener = file.split('ener')
                mod = int(mod[6:])
                ener = int(ener[0])
                if mod in hkl_mod.keys():
                    hkl_mod[mod][ener] = read_hkl(os.path.join(r, file), nline= npeaks)
                else:
                    hkl_mod[mod] = {ener: read_hkl(os.path.join(r, file), nline= npeaks)}
    return hkl_mod


def extract_hkl(hklmod, hkl, ener):
    """
       extract an hkl intensity for all model and one energy
       format hkl = '3 5 7'
    """
    mod_l = np.sort(list(hklmod.keys()))
    hkl_l = []
    for mod in mod_l:
        hkl_l.append(hklmod[mod][ener][hkl])
    return np.vstack((mod_l, hkl_l))


def __convert_oldxyz2new(xyz, nat):
    new_pcr_header = ['!Nat Dis Ang Jbt Isy Str Furth        ATZ     Nvk More\n',
                      '  0   0   0   0   0   0       3160.9280   0   0\n',
                      '!Contributions (0/1) of this phase to the  1 patterns\n',
                      ' 1\n',
                      '!Irf Npr Jtyp  Nsp_Ref Ph_Shift for Pattern#  1\n',
                      '   0   5    0      0      0\n',
                      '! Pr1    Pr2    Pr3   Brind.   Rmua   Rmub   Rmuc     for Pattern#  1\n',
                      '  0.000  0.000  1.000  1.000  0.000  0.000  0.000\n']
    nat = xyz[5].split()[0]
    del xyz[4]
    del xyz[4]
    new_pcr_header[1] = ' %s %s' % (nat, new_pcr_header[1])
    for i in reversed(new_pcr_header):
        xyz.insert(4, i)
    return xyz


##########################################################################
def read_allsum(splity='ener', chi=False):
    '''
    readl all  the hkl files for all the energy

    is based on the idea that files are called modNNNenerN.hkl
    returns a dictionary
    {model:{energy:{khl:f2}}}

    '''
    bad=[]
    sum_mod = {}
    for r, d, f in os.walk(sample):
        for file in f:
            if '.sum' in file:
                mod, ener = file.split(splity)
                mod = int(re.search(r'[A-Za-z_\-]*(\d{1,4})', mod)[1])
                try:
                    if ener[0]=='.':
                        sum_mod[mod] = read_sumSC(os.path.join(r, file), pr=0)
                        continue
                    elif ener[0] in [str(i) for i in range(10)]:    
                        ener = int(ener[0])
                    if mod in list(sum_mod.keys()):
                        sum_mod[mod][ener] = read_sum(os.path.join(r, file), pr=0, chi=chi)
                    else:
                        sum_mod[mod] = {ener: read_sum(os.path.join(r, file), pr=0, chi=chi)}
                        continue
                except Exception as E:
                    print(file)
                    print(E)
                    bad.append(mod-1)
                    break
    assert len(sum_mod)>0, 'empty database'
    if len(bad)>0:
    	print(repr(bad))
    return sum_mod


def read_all_Rbrag_super(list_hkl):
    def R(z):
        return [abs(i['Icalc'] - ['Iobs']) / i['Sigma'] for i in list(z.values())]
    Rbragg_mod = {}
    hkl_out = {}
    for r, d, f in os.walk(sample):
        for file in f:
            if '.out' in file:
                mod, ener = file.split('ener')
                mod = int(mod[3:])
                ener = int(ener[0])

                a = outfile(os.path.join(r, file))
                a.extr_hkl()
                z = {i: a.phases[1][1]['hkl'][i] for i in list_hkl}
                if mod in list(Rbragg_mod.keys()):
                    hkl_out[mod][ener] = z
                    Rbragg_mod[mod][ener] = np.sum(R(z))
                else:
                    hkl_out[mod] = {ener: z}
                    Rbragg_mod[mod] = {ener: np.sum(R(z))}
    return hkl_out, Rbragg_mod


class outfile():
    def __init__(self, out_filename):
        with open(out_filename) as outfile:
            self.outlines = outfile.readlines()

        self.phases_sec = {}
        Nph = None
        for i, line in enumerate(self.outlines):
            if not Nph:
                Nph = re.search(r' => Number of phases:\s*(\d)', line)
            if '=>  Parameter shifts set to zero' in line:
                start_final = i
                break
        for i, line in enumerate(self.outlines[start_final:]):
            a = re.search(r' => Phase\s*(\d{1,2})\s*Name:\s*(.*)', line)
            if a:
                n_p = int(a.group(1))
                self.phases_sec[n_p] = {'name': a.group(2).rstrip(),
                                        'line0': i + start_final}
                if n_p > 1:
                    self.phases_sec[n_p - 1]['line-1'] = i + start_final - 1
            if 'BRAGG R-Factors and weight fractions' in line:
                self.phases_sec[n_p]['line-1'] = i + start_final - 2
                end_final = i + start_final - 2
                break
        self.start_final = start_final
        self.end_final = end_final
        self.phases = {}

    def extr_hkl(self, phase_i, pattern):
        hkl = {}
        sline = self.phases_sec[phase_i]['line0']
        eline = self.phases_sec[phase_i]['line-1']
        for i, line in enumerate(self.outlines[sline:eline]):
            a = re.search(r'Pattern#\s*%d\s*Phase No.:\s*%d' %
                          (phase_i, pattern), line)
            if a:
                sline_hkl = i + sline
                break
        for i, line in enumerate(self.outlines[sline_hkl + 3:eline]):
            if not(line.strip()):
                continue
            if 'No.  Code' in line:
                continue
            if '---' in line:
                break
            stringa = line.split()
            name = ' '.join(stringa[2:5])
            hkl[name] = {'Icalc': float(stringa[9]),
                         'Iobs': float(stringa[10]),
                         'Sigma': float(stringa[11])}

        self.phases = {1: {1: {'hkl': hkl}}}
        return


def read_sum(sum_file, pr=True, chi=False):
    '''pr if 1 print
    '''
    with open(sum_file) as ourfile:
        sumlines = ourfile.readlines()
    for sum_line in sumlines:
        a = re.search(r'=.*Bragg R-factor: *(\d{1,2}\.\d*).*V', sum_line)
        if a is not None:
            if pr:
               print(a.group())
            Rbragg = float(a.group(1))
        a = re.search(r'Reduced Chi-square :\s*(\d{1,2}\.\d*).*', sum_line)
        if a is not None:
            if pr:
                print('=>', a.group())
            chi2 = float(a.group(1))
    if chi:
        return  chi2
    else:
        return Rbragg


def read_sumSC(sum_file, pr=True):
    with open(sum_file) as ourfile:
        sumlines = ourfile.readlines()
    for sum_line in sumlines:
        a = re.search(r'RF2 -factor : *(\d{1,2}\.\d*).*', sum_line)
        if a is not None:
            if pr:
               print(a.group())
            Rbragg = float(a.group(1))
        a = re.search(r'Chi2\(Intens\): *(\d{1,2}\.\d*).*', sum_line)
        if a is not None:
            if pr:
                print('=>', a.group())
            chi2 = float(a.group(1))
    return Rbragg   #, chi2