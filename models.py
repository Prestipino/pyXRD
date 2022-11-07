#
#

# import sys
import glob
import shutil
import numpy as np
import re
import os
import subprocess
import time
import matplotlib.pyplot as plt

# ####### PCR Names
sample = 'fit_lpf109'  # only stuff to touch
Spg = 'P -4 3 n'
Biso = 0.5


# to limit to the first n models_filename = glob.glob("models/M*.txt")[:2]
# models_filename = glob.glob("../gen_model/M*.pcr")
# pcr_ener_files = ['ener0.pcr', 'ener1.pcr', 'ener2.pcr', 'ener3.pcr']

######################


def __extra_del_phasexyz(lines, extract=True):
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
    end_cond1 = '!-------> Scale'
    end_cond2 = '!-------> Profile'

    for i in lines:
        if '!  Data for PHASE number:   1' in i:
            zcond = 1
        if (end_cond1 in i) or (end_cond2 in i):
            if extract:
                break
            else:
                zcond = 0
        if zcond and extract:
            texto.append(i)
        elif not(zcond) and not(extract):
            texto.append(i)
    return texto


def run_models(models, pcr_ener_files, sample,
               newfile=True, pcr_options={},
               commands=None, Sing_Cry=False,
               stepwait=3, stepprint=50,
               force=False, Terminate=True,
               postSi=f'{"0   "*4}\n{" "*18}{"0.00     "*5}',
               postAt=f'{"0   "*4}\n{" "*18}{"0.00     "*5}'):
    '''
       run fullprof for several structurasl models fro several energy
       input:
          models: models object
          pcr_ener_files= list with all the
                           filenames in which insert the tructural model
          sample = directory name
          newfile = if false it just run again on the file
          command string to insert in command mode for fullprof
          stepwait = numper of paralel process

          force = overwrite the directory
          Terminate = force to terminate
    '''

    n_ener = len(pcr_ener_files)
    # import base pcr
    # pcr_ener_inp = list of list contining the pcr lines
    #                apart from struture of phase 1
    # inser_in_pcr = list of the line numbers where insert phase 1 info
    pcr_ener_inp = []
    inser_in_pcr = []
    for pcr in pcr_ener_files:
        with open(pcr) as pcr_i:
            pcr_all = pcr_i.readlines()
            pcr_ener_inp.append(__extra_del_phasexyz(pcr_all, extract=False))
        for line_n, line in enumerate(pcr_all):
            if '!  Data for PHASE number:   1' in line:
                inser_in_pcr.append(line_n)
    pass

    # create directory
    try:
        os.mkdir(sample)
    except FileExistsError as zz:
        if not(newfile):
            pass
        elif force:
            shutil.rmtree(sample)
            os.mkdir(sample)
        else:
            raise FileExistsError(zz)

    # utility counters for the wait
    mod_t = list(range(len(models)))
    old_len = len(mod_t)
    while len(mod_t) > 0:
        i = 0   # used for parallization
        wait = 0.5
        # start of the cycle
        for mod_i in mod_t:
            for ener in range(n_ener):
                # dire = output model directory
                dire = os.path.join(sample, f'mod{mod_i:05d}')
                pcrname = os.path.join(dire, f'm{mod_i:05d}{pcr_ener_files[ener]:s}')

                # create the dire directory if not existe
                if not os.path.exists(dire):
                    os.mkdir(dire)

                if newfile:
                    for line in pcr_ener_inp[ener]:
                        if 'NPATT' in line:
                            n_pattern = int(line.split()[1])
                            break
                    else:
                        n_pattern = 1

                    # import xyz model
                    xyz = models._objipcrxyz(mod_i, patterns=n_pattern,
                                             sincry=Sing_Cry,
                                             commands=commands,
                                             title=f'm{i:04d}',
                                             Rmub=2,
                                             postSi=postSi,
                                             postAt=postAt,
                                             **pcr_options)

                    # import base pcr
                    pcrall = pcr_ener_inp[ener][:]
                    pcrall.insert(inser_in_pcr[ener], ''.join(xyz))
                    pcrall[0] = 'COMM  %s %s' % (f'mod{mod_i:05d}',
                                                 pcrall[0][4:])

                    try:
                        with open(pcrname, 'w') as pcr_i:
                            pcr_i.writelines(pcrall)
                    except PermissionError as PE:
                        print(PE)
                        continue

                # launch fullprof
                # CREATE_NEW_PROCESS_GROUP = 0x00000200
                DETACHED_PROCESS = 0x00000008
                HIGH_PRIORITY_CLASS = 0x00000080
                # CREATE_PROTECTED_PROCESS = 0x00040000

                a = subprocess.Popen(['fp2k.exe', pcrname], creationflags=DETACHED_PROCESS | HIGH_PRIORITY_CLASS)

                i += 1
                if not(i % stepwait):
                    a.wait()

                if not(i % stepprint):
                    print(f'# {mod_i:d}')
                    time.sleep(0.2)

        a.wait()
        time.sleep(0.2)
        good = glob.glob(f'.\\{sample:s}\\**\\*.fst')
        good = set(map(lambda x: int(os.path.basename(x)[1:6]), good))
        mod_t = [i for i in mod_t if i not in good]

        # check divergence
        for i in mod_t:
            outstr = f'mod{i:05d}\\m{i:05d}*.out'
            outfile = glob.glob(f'.\\{sample:s}\\{outstr:s}')[0]
            Divergence = checkDivergence(outfile)
            if Divergence:
                mod_t.remove(i)
                print(i, Divergence)

        if len(mod_t) == 0:
            sum_RF, bad = read_allsum(sample,
                                      Sing_Cry,
                                      p_bad=True,
                                      multi=n_ener > 1)

            if bad:
                mod_t = bad
                if Terminate:
                    continue
                else:
                    return
            RF_name = '_RF2' if Sing_Cry else '_Rbragg'
            models.values_set(sum_RF, sample + RF_name)
            models.values_set(read_allsum(sample, Sing_Cry, chi=True),
                              sample + '_chi2')
            return
        print(len(mod_t))
        if old_len == len(mod_t):
            print(mod_t)
            wait *= 2
            if wait > 5:
                return
        time.sleep(wait)
        old_len = len(mod_t)
    print('End')


# creationflags=subprocess.DETACHED_PROCESS
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

##########################################################################
def read_phase1_parall(sample):
    sum_mod = []
    for file in glob.glob(f'.\\{sample:s}\\**\\*.out'):
        sum_mod.append(read_phase1par(file))
    return sum_mod


def read_phase1par(out_file, buf_size=8192):
    parameters={}
    with open(out_file) as fh:
        segment = None
        offset = 0
        fh.seek(0, os.SEEK_END)
        file_size = remaining_size = fh.tell()
        while remaining_size > 0:
            offset = min(file_size, offset + buf_size)
            fh.seek(file_size - offset)
            buffer = fh.read(min(remaining_size, buf_size))
            remaining_size -= buf_size
            cond1 = 'SYMBOLIC NAMES' in buffer
            cond2 = 'AND SIGMA' in buffer
            if cond1 or cond2:
                fh.seek(file_size - offset)
                break
        while True:
            line = fh.readline()

            if '>  Parameter number' in line:
                pa = re.split(r'[ (]{1,}', line)
                parameters[pa[6]] = [float(pa[7]), float(pa[9])]
            if '=> Number of bytes' in line:
                break
    return parameters

############################################################################
def read_allsum(sample, Sing_Cry=0, chi=False, p_bad=False, multi=False):
    '''
    readl all  the hkl files for all the energy

    could read multi run (multi=True) in such case 
    is based on the idea that files are called modNNN{splity:s}N.sum

    one multipatternpcr
    returns a dictionary
    {model:{energy:{khl:f2}}}

    '''
    bad = []
    sum_mod = []
    for file in glob.glob(f'.\\{sample:s}\\**\\*.sum'):
        f_bname = os.path.basename(file)
        mod = int(f_bname[1:6])
        try:
            if multi:
                ener = int(f_bname[-5:-4])
                if mod < len(sum_mod):

                    sum_mod[mod][ener] = read_sum(file, pr=0, chi=chi)
                else:
                    sum_mod.append({ener: read_sum(file, pr=0, chi=chi)})

            if Sing_Cry:
                sum_mod.append(read_sumSC(file, pr=0, chi=chi))

            else:
                rr = read_sumMP(file, pr=False, chi=chi)
                if rr == []:
                    raise ValueError
                    #rr = [np.NaN] * len(sum_mod[-1])
                sum_mod.append(rr)

        except Exception:
            if checkDivergence(file[:-3] + 'out'):
                sum_mod.append(None)
            else:
                bad.append(mod)
    # if len(bad) > 0:
        # print(len(bad), repr(bad))
    assert len(sum_mod) > 0, 'empty database'
    if p_bad:

        return sum_mod, bad
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


def checkDivergence(outfile):
    with open(outfile) as out:
        outlines = out.readlines()[-20:]
    for line in outlines:
        if 'Strong DIVERGENCE' in line:
            return 'Strong DIVERGENCE'
        if 'Singular matrix!!' in line:
            return 'Singular matrix!!'
        if 'WARNING, Scale factor <0, fixed to 1.E-10' in line:
            return 'WARNING, Scale factor <0, fixed to 1.E-10'
    else:
        return False

def read_sumMP(sum_file, pr=True, chi=False):
    '''read multipattern out
        pr if 1 print
    '''
    with open(sum_file) as ourfile:
        sumlines = ourfile.readlines()
    Rbragg = []
    chi2 = np.NaN
    for sum_line in sumlines:
        a = re.search(r'=.*Bragg R-factor: * (\d{1,3}\.\d*).*V', sum_line)
        if a is None:
            a = re.search(r'RF2 -factor : *(\d{1,2}\.\d*).*', sum_line)
            b = re.search(r'RF2 -factor : *(NaN).*', sum_line)
            if b is not None:
                Rbragg.append(None)
                continue
        if a is not None:
            if pr:
                print(a.group())
            Rbragg.append(float(a.group(1)))
            continue
        a = re.search(r'.*weigthed Chi2 \(Brag.*\s* (\d{1,5}\.\d*E?\+?\d*).*', sum_line)
        if a is not None:
            if pr:
                print('=>', a.group(), a.group(1))
            chi2 = float(a.group(1))
            if chi:
                break
            continue

    if chi:
        return chi2
    else:
        return Rbragg

def read_sum(sum_file, pr=True, chi=False):
    '''pr if 1 print
    '''
    with open(sum_file) as ourfile:
        sumlines = ourfile.readlines()
    for sum_line in sumlines:
        a = re.search(r'=.*Bragg R-factor: *(\d{1,3}\.\d*).*V', sum_line)
        if a is not None:
            if pr:
               print(a.group())
            Rbragg = float(a.group(1))
        a = re.search(r'Reduced Chi-square :\s*(\d{1,3}\.\d*).*', sum_line)
        if a is not None:
            if pr:
                print('=>', a.group())
            chi2 = float(a.group(1))
    if chi:
        return chi2
    else:
        return Rbragg

def read_sumSC(sum_file, pr=True, chi=False):
    with open(sum_file) as ourfile:
        sumlines = ourfile.readlines()
    for sum_line in sumlines:
        a = re.search(r'RF2 -factor : *(\d{1,2}\.\d*).*', sum_line)
        b = re.search(r'RF2 -factor : *(NaN).*', sum_line)
        if a is not None:
            if pr:
                print(a.group())
            RF2 = float(a.group(1))
        if b is not None:
            RF2 = None

        a = re.search(r'Chi2\(Intens\): *(\d{1,2}\.\d*).*', sum_line)
        b = re.search(r'Chi2\(Intens\): *(NaN).*', sum_line)
        if a is not None:
            if pr:
                print('=>', a.group())
            chi2 = float(a.group(1))
        if b is not None:
            chi2 = None

    if chi:
        return chi2
    else:
        return RF2

def scatter_site(atom, site, ReSC, Mod_str, label=''):
    """ hl =high limit for test
    """
    plt.xlabel('model nb.')
    plt.title('%s %s' % (label, site))
    if isinstance(ReSC, str):
        plt.ylabel(ReSC)
        ReSC = getattr(Mod_str, ReSC)
    ReSC = np.array(ReSC)
    for i in range(Mod_str.wiks[site]['m'] + 1):
        cond = '== %d' % i  # Define condition
        Mod_i = Mod_str.filter(site, atom, cond, N=1)
        i_legend = '%s %s:%d' % (atom, site, i)  # Define label
        if len(Mod_i) > 0:
            plt.scatter(Mod_i, ReSC[Mod_i], marker='s', label=i_legend)
    plt.legend()












def reverse_readline(filename, buf_size=8192):
    import os
    """A generator that returns the lines of a file in reverse order"""
    with open(filename) as fh:
        segment = None
        offset = 0
        fh.seek(0, os.SEEK_END)
        file_size = remaining_size = fh.tell()
        while remaining_size > 0:
            offset = min(file_size, offset + buf_size)
            fh.seek(file_size - offset)
            buffer = fh.read(min(remaining_size, buf_size))
            remaining_size -= buf_size
            lines = buffer.split('\n')
            # The first line of the buffer is probably not a complete line so
            # we'll save it and append it to the last line of the next buffer
            # we read
            if segment is not None:
                # If the previous chunk starts right from the beginning of line
                # do not concat the segment to the last line of new chunk.
                # Instead, yield the segment first 
                if buffer[-1] != '\n':
                    lines[-1] += segment
                else:
                    yield segment
            segment = lines[0]
            for index in range(len(lines) - 1, 0, -1):
                if lines[index]:
                    yield lines[index]
        # Don't yield None if the file was empty
        if segment is not None:
            yield segment