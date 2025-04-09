"""
   parsed for different format
   raw inspirwed from https://github.com/wojdyr/xylib
"""
import numpy as np
import os


def calc_x(start, step, data):
    start, step, = float(start), float(step)
    return np.array([start + step * i for i in np.arange(len(data))])


def read_ras(filename):
    with open(filename) as ifile:
        ifilecom = [j[1:] for j in ifile.readlines() if j[0] == '*']
    data = np.loadtxt(filename, comments='*')[:, :2]
    meas_dict = dict([j.split()[:2] for j in ifilecom if 'MEAS' in j])
    valkeyn = [i[24:] for i, j in meas_dict.items() if ('AXIS_POS' in i) and ('None' not in j)]
    vmeas_d = {}
    vmeas_d['info_g'] = {}
    for ik in valkeyn:
        name = meas_dict[f'MEAS_COND_AXIS_NAME-{ik}'][1:-1]
        vmeas_d[name] = {'POS': meas_dict[f'MEAS_COND_AXIS_POSITION-{ik}'][1:-1]}
        vmeas_d[name]['INAME'] = meas_dict[f'MEAS_COND_AXIS_NAME_INTERNAL-{ik}'][1:-1]
        if meas_dict[f'MEAS_COND_AXIS_UNIT-{ik}'][1:-1]:
            vmeas_d[name]['unit'] = meas_dict[f'MEAS_COND_AXIS_UNIT-{ik}'][1:-1]
    vmeas_d['SCAN_START_TIME'] = meas_dict['MEAS_SCAN_START_TIME'][1:-1]
    vmeas_d['UNIT'] = meas_dict['MEAS_SCAN_UNIT_Y'][1:-1]
    meas_dict = dict([j.split()[:2] for j in ifilecom if 'HW_' in j])
    vmeas_d['info_g']['ATTACHMENT_NAME'] = meas_dict['HW_ATTACHMENT_NAME'][1:-1]
    vmeas_d['info_g']['CATHODE'] = meas_dict['HW_XG_TARGET_NAME'][1:-1]
    vmeas_d['info_g']['ALPHA1'] = meas_dict['HW_XG_WAVE_LENGTH_ALPHA1']
    vmeas_d['info_g']['ALPHA2'] = meas_dict['HW_XG_WAVE_LENGTH_ALPHA2']

    if [True for i in ifilecom if "VariableSlit" in i]:
        vmeas_d['Var_slit'] = True
    return data, vmeas_d


def read_id22(self, filename):
    if isinstance(filename, str):
        self.data = []
        # print(info, datas.shape)
        self.data.append({'array': np.loadtxt(filename, comments=['#', '!']),
                          'info': {'index': 0, 'UNIT': 'counts', 'STEPTIME': 1}})
    elif isinstance(filename, list):
        self.data = []
        for i, file_names in enumerate(filename):
            try:
                self.data.append({'array': np.loadtxt(file_names, 
                                                      comments=['#', '!']),
                                  'info': {'index': i,
                                           'UNIT': 'counts', 'STEPTIME': 1}})
            except Exception as excep:
                print(f'error for {file_names}\n')
                raise


def read_D1B(self, filename):

    def read_file(file):
        info = {}
        with open(file) as filet:
            a = filet.readlines()
        dato1 = np.loadtxt(a[6:])
        info['title'] = a[0]
        info['INTER'] = a[1]
        for i, j in zip([1, 2, 3], a[2].split()[1:]):
            info['TEMP_%d' % i] = float(j)
        info['COMMENT_1'] = a[3]
        info['COMMENT_2'] = a[4]
        MonTim = a[5].split()[-2:]
        info['Monitor'] = float(MonTim[0])
        info['ConTime'] = float(MonTim[1])
        return dato1, info

    if isinstance(filename, str):
        self.data = []
        datas, info = read_file(filename)
        # print(info, datas.shape)
        self.data.append({'array': datas, 'info': info})

    elif isinstance(filename, list):
        self.data = []
        for i, file_names in enumerate(filename):
            datas, info = read_file(file_names)
            numor = os.path.basename(file_names[:-4])
            info['index'] = i
            if numor.isdecimal():
                info['filenum'] = int(numor)
            self.data.append({'array': datas, 'info': info})


def read_raw(self, filename):
    read_uint32_le = lambda : np.fromfile(filex, dtype=np.uint32, count=1)[0] # noqa
    read_dbl_le    = lambda : np.fromfile(filex, dtype=np.float64, count=1)[0] # noqa
    read_flt_le    = lambda : np.fromfile(filex, dtype=np.float32, count=1)[0] # noqa
    read_str       = lambda nby : filex.read(nby).decode('ascii').rstrip('\x00') # noqa
    self.data = []

    with open(filename, 'rb') as filex:
        head = filex.read(4).decode('ascii')
        print(head)
        if head == "RAW ":
            self.version = "ver. 1"
        elif head == "RAW2":
            self.version = "ver. 2"
        elif head == "RAW1":
            subv = filex.read(3).decode('ascii')
            if subv == ".01":
                self.version = "ver. 3"
        elif (head == "RAW4"):
            self.version = "ver. 4"
        else:
            print("no format detected")
        print('head= ', head)
        if self.version == "ver. 3":
            filex.seek(8)
            file_status = read_uint32_le()
            status = ["done", "active", "aborted", "interrupted"]
            self.file_status = status[file_status]
            self.info['SCAN_cnt'] = read_uint32_le()
            self.info["MEASURE_DATE"]                = read_str(10)     ## address 16 # noqa
            self.info["MEASURE_TIME"]                = read_str(10)     ## address 26 # noqa
            self.info["USER"]                        = read_str(72)     # address 36 # noqa
            self.info["SITE"]                        = read_str(218)    # address 108 # noqa
            self.info["SAMPLE_ID"]                   = read_str(60)     ## address 326 # noqa
            self.info["COMMENT"]                     = read_str(160)    # address 386 # noqa
            self.info["bug"]                         = filex.read(2)      #apparently there is a bug in docs, 386+160 != 548 # noqa
            self.info["goniometer_code"]             = read_uint32_le()   # address 548 # noqa
            self.info["goniometer stage code"]       = filex.read(4)      # address 552 # noqa
            self.info["sample loader code"]          = filex.read(4)      # address 556 # noqa
            self.info["goniometer controller code"]  = filex.read(4)      # address 560 # noqa
            self.info["(R4)_goniometer_radius"]      = filex.read(4)      # address 564 # noqa
            self.info["(R4) fixed divergence"]       = filex.read(4)      # address 568 # noqa
            self.info["(R4) fixed sample slit"]      = filex.read(4)      # address 572 # noqa
            self.info["primary Soller slit"]         = filex.read(4)      # address 576 # noqa
            self.info["primary monochromator"]       = filex.read(4)      # address 580 # noqa
            self.info["(R4) fixed antiscatter"]      = filex.read(4)      # address 584 # noqa
            self.info["(R4) fixed detector slit"]    = filex.read(4)      # address 588 # noqa
            self.info["secondary Soller slit"]       = filex.read(4)      # address 592 # noqa
            self.info["fixed thin film attachment"]  = filex.read(4)      # address 596 # noqa
            self.info["beta filter"]                 = filex.read(4)      # address 600 # noqa
            self.info["secondary monochromator"]     = filex.read(4)      # address 604 # noqa

            self.info["ANODE_MATERIAL"]              = read_str(4)  # address 608      # noqa
            filex.read(4); # unused                      # address 612            # noqa
            self.info["ALPHA_AVERAGE"]               = read_dbl_le() # address 616      # noqa
            self.info["ALPHA1"]                      = read_dbl_le()        # address 624    # noqa
            self.info["ALPHA2"]                      = read_dbl_le()        # address 632    # noqa
            self.info["BETA"]                        = read_dbl_le()          # address 640  # noqa
            self.info["ALPHA_RATIO"]                 = read_dbl_le()   # address 648    # noqa
            filex.read(4); # (C4) unit name              # address 656             # noqa
            filex.read(4); # (R4) intensity beta:a1      # address 660             # noqa
            self.info["measurement time"]            = read_flt_le() # address 664      # noqa
            filex.read(43); # unused                     # address 668             # noqa
            filex.read(1); # hardware dependency ...     # address 711             # noqa
            #print filex.tell()        #  start first  pattern comments
            #we start from 712

            for cur_range in range(self.info['SCAN_cnt']):
                try:
                    # print cur_range
                    blkmeta = {}                        # empty dictionary for utility use
                    header_len = read_uint32_le()     # address 0
                    # print header_len
                    blkmeta["STEPS"] = read_uint32_le() # address 4 # noqa
                    blkmeta["START_THETA"] = read_dbl_le()  # address 8 # noqa
                    blkmeta["START_2THETA"] = read_dbl_le()  # address 16

                    filex.read(8); # Chi drive start         # address 24 # noqa
                    filex.read(8); # Phi drive start         # address 32 # noqa
                    filex.read(8); # x drive start           # address 40 # noqa
                    filex.read(8); # y drive start           # address 48 # noqa
                    filex.read(8); # z drive start           # address 56 # noqa
                    filex.read(8);                            # address 64 # noqa
                    filex.read(6);                            # address 72 # noqa
                    filex.read(2); # unused                  # address 78 # noqa
                    filex.read(8); # (R8) variable antiscat. # address 80 # noqa
                    filex.read(6);                            # address 88 # noqa
                    filex.read(2); # unused                  # address 94 # noqa
                    filex.read(4); # detector code           # address 96 # noqa
                    blkmeta["HIGH_VOLTAGE"] = read_flt_le() # address 100 # noqa
                    blkmeta["AMPLIFIER_GAIN"] = read_flt_le()  # 104
                    blkmeta["DISCRIMINATOR_1_LOWER_LEVEL"] = read_flt_le()  # 108
                    filex.read(4);       #full to investigate # address 112 # noqa
                    filex.read(4);                            # address 116 # noqa
                    filex.read(8);                            # address 120 # noqa
                    filex.read(4);                            # address 128 # noqa
                    filex.read(4);                            # address 132 # noqa
                    filex.read(5);                            # address 136 # noqa
                    filex.read(3); # unused                  # address 141 # noqa
                    filex.read(8);                            # address 144 # noqa
                    filex.read(8);                            # address 152 # noqa
                    filex.read(8);                            # address 160 # noqa
                    filex.read(4);                            # address 168 # noqa
                    filex.read(4); # unused                   # address 172 # noqa
                    blkmeta["STEPSIZE"] = read_dbl_le()      # address 176 # noqa
                    filex.read(8);                            # address 184 # noqa
                    blkmeta["STEPTIME"] = read_flt_le()  # address 192 # noqa
                    filex.read(4);                            # address 196 # noqa
                    filex.read(4);                            # address 200 # noqa
                    blkmeta["TIMESTARTED"] =read_flt_le()     # address 204 # noqa
                    blkmeta["ROTATION_SPEEDrpm"] = read_flt_le()  # 208
                    blkmeta["TEMPERATURE"] = read_flt_le()    # address 212 # noqa
                    blkmeta["TEMP_RATE"] =read_flt_le()       # address 216 # noqa
                    blkmeta["TEMP_DELAY"] =read_flt_le()      # address 220 # noqa
                    blkmeta["GENERATOR_VOLTAGE"] = read_uint32_le()  # 224
                    blkmeta["GENERATOR_CURRENT"] = read_uint32_le()  # 228
                    filex.read(4);                            # address 232 # noqa
                    filex.read(4); # unused                   # address 236 # noqa
                    blkmeta["USED_LAMBDA"] = read_dbl_le()    # address 240 # noqa
                    filex.read(4);                            # address 248 # noqa
                    filex.read(4);    #used                     # address 252 # noqa
                    supplementary_headers_size = read_uint32_le() # address 256 # noqa
                    filex.read(4);                            # address 260 # noqa
                    filex.read(4);                            # address 264 # noqa
                    filex.read(4);  # unused                  # address 268 # noqa
                    filex.read(8);                            # address 272 # noqa
                    filex.read(24); # unused                 # address 280 # noqa
                    # assert(filex.tellg() == 712 + (cur_range + 1) * header_len);
                except Exception as frase:
                    print('pippp in header', cur_range)
                    print(frase)
                    print('just before ', filex.tell())
                    print(supplementary_headers_size)
                    if self.debug:
                        raise frase

                if (supplementary_headers_size > 0):
                    filex.read(supplementary_headers_size)

                y = np.fromfile(filex, dtype=np.float32, count=blkmeta["STEPS"])
                x = calc_x(blkmeta["START_2THETA"], blkmeta["STEPSIZE"], y)

                try:
                    # print filex.tell()   start numeber for pattern
                    self.data.append({'array': np.vstack((x, y)).T,
                                      'info': blkmeta})

                except Exception as frase:
                    print('pippp in array', cur_range)
                    print('shape x, y ', x.shape, y.shape)
                    print(type(frase))
                    print('just before ', filex.tell())
                    print(supplementary_headers_size)
                    if self.debug:
                        raise frase
        pass

        if self.version == "ver. 4":
            filex.seek(0)
            filex.read(8)   # version complet
            filex.read(4)   # results in 65519??             ## address 
            # file_status=read_uint32_le()
            # status=["done", "active", "aborted", "interrupted"]
            # self.file_status=status[file_status]
            self.info["MEASURE_DATE"] = read_str(12)        # address 12# noqa E510
            self.info["MEASURE_TIME"] = read_str(12)        # address 24->36# noqa E510
            self.info['SCAN_cnt_0'] = read_uint32_le()      # maybe start or soller 36 40# noqa E510
            self.info['SCAN_cnt'] = read_uint32_le()        # address 40 44# noqa E510
            self.info['SCAN_cnt2'] = read_uint32_le()       # maybe done address 44 48# noqa E510
            self.info['RUNTIME'] = read_flt_le()            # maybe done address 48 52# noqa E510
            self.info['RUNTIME2'] = read_flt_le()           # maybe done address 52 56# noqa E510
            future_info  = read_uint32_le()                 # maybe done val 1409  address 56 60   # noqa E510
            filex.read(3)                                   # maybe done  address 60 62                  # noqa E510

            while True:
                code = read_uint32_le()                                 # offset x->x+4  # noqa E510
                if code in [0, 160]:
                    break
                len_seg = read_uint32_le()                              # offset 4->8  # noqa E510
                if code == 10:
                    read_int()                                           #skip 8 -12  # noqa E510
                    key = filex.read(24).decode('ascii').strip('\x00')   # key 12-36  # noqa E510
                    self.info[key] = filex.read(len_seg - 36).decode('ascii').strip('\x00') # noqa E510
                elif code == 30:
                    read_int()                                           #skip 8 -12    # noqa E510
                    self.info["V4_INF_STAGE_CODE"]  = read_uint32_le()   # val 12-16  # noqa E510
                    read_int()                                           #skip 16-20  # noqa E510
                    read_int()                                           #skip 20-24  # noqa E510
                    self.info['GONIOMETER_RADIUS'] =  read_flt_le()/2    # val 24-28  # noqa E510
                    read_int()                                           #skip 28-32  # noqa E510
                    read_int()                                           #skip 32-36  # noqa E510
                    self.info["V4_INF_FIXED_DIVSLIT"] = read_flt_le()    # val 36-40  # noqa E510
                    filex.read(20)
                    self.info["FIXED_ANTISLIT"] = read_flt_le()           # val 60-64  # noqa E510
                    self.info["FIXED_DSLIT"]  = read_flt_le()             # val 64-68  # noqa E510
                    self.info["ALPHA_AVERAGE"]= read_dbl_le()             # val 64-68  # noqa E510
                    self.info["ALPHA1"]       = read_dbl_le()              # val 64-68  # noqa E510
                    self.info["ALPHA2"]       = read_dbl_le()              # val 64-68  # noqa E510
                    self.info["BETA"]         = read_dbl_le()            # val 64-68  # noqa E510
                    self.info["ALPHA_RATIO"]  = read_dbl_le()             #val 64-68   # noqa E510
                    read_uint32_le()
                    self.info["Anode"] = bfile[x+116:x+120].decode('ascii').strip('\x00')  # noqa E510
                    self.info["W_UNIT"] = bfile[x+120:x+124].decode('ascii').strip('\x00') # noqa E510 
                elif code == 5:
                    filex.read(len_seg - 8)
                else:
                    print('unknown code', code)
                    raise ValueError('unknown code')



            # val = read_uint32_le()                                          # # address 452@@@@@@  10
            # n_charl = read_uint32_le()                                      # # address 456@@@@@@  50
            # n_char = filex.read(n_charl - 8).decode('ascii')                  # # address 288@@@@@@
            # code = n_char[4:28].rstrip('\x00')
            # value = n_char[28:].strip('\x00')
            # self.info["OSUSER"] = value

            # val = read_uint32_le()                                          # # address 502@@@@@@  10
            # n_charl = read_uint32_le()                                      # # address 506@@@@@@  49
            # n_char = filex.read(n_charl - 8).decode('ascii')                      # # address 510@@@@@@
            # code = n_char[4:28].rstrip('\x00')
            # value = n_char[28:].strip('\x00')
            # self.info["USER"] = value

            # val = read_uint32_le()                                          # # address 551@@@@@@  10
            # n_charl = read_uint32_le()                                      # # address 555@@@@@@  42
            # n_char = filex.read(n_charl - 8).decode('ascii')                  # # address 288@@@@@@
            # code = n_char[4:28].rstrip('\x00')
            # value = n_char[28:].strip('\x00')
            # self.info["SITE"] = value

            # val = read_uint32_le()                                          # # address 593@@@@@@  10
            # n_charl = read_uint32_le()                                      # # address 597@@@@@@  49
            # n_char = filex.read(n_charl - 8).decode('ascii')                  # # address 601@@@@@@
            # code = n_char[4:28].rstrip('\x00')
            # value = n_char[28:].strip('\x00')
            # self.info["SAMPLEID"] = value

            for cur_range in range(self.info['SCAN_cnt']):
                print(cur_range)
                blkmeta = {}
                val = read_uint32_le()
                blkmeta['SCAN_step1']         =read_uint32_le()            # address  4@@@@@@@@@@@ # noqa
                blkmeta['SCAN_step2']         =read_uint32_le()            # address  8@@@@@@@@@@@ # noqa
                read_uint32_le()                                      # 8  # address 12@@@@@@@@@@@ # noqa
                read_uint32_le()
                read_uint32_le()
                blkmeta['ADDITIONALDETECTOR']         =read_uint32_le()            # address  8@@@@@@@@@@@ # noqa                
                #print filex.tell(), 'should be 642+36 678'
                read_uint32_le()
                blkmeta['SCAN_type']        =filex.read(24).decode('ascii').strip('\00') # address 32@@@@@@@@@@ # noqa
                read_flt_le()                                           # 0 ? # addr 56 # noqa  
                read_flt_le()                                           # 0 ? # addr 60 # noqa  
                read_flt_le()                                           # 392 ? # addr 64 # noqa  
                # print filex.tell(), 'should be 642+68 710'
                blkmeta["TIMESTARTED"]     =read_flt_le()               # address 68@@@@@@@@@@ # noqa
                blkmeta["START"]           = read_dbl_le()              # address 72@@@@@@@@@@______not sure result=10 # noqa
                blkmeta["STEPSIZE"]        = read_dbl_le()              # address 80@@@@@@@@@@ # noqa
                blkmeta["STEPS"]           = read_uint32_le()           # address 88@@@@@@@@@ # noqa
                blkmeta["STEPTIME"]   = read_flt_le()                   # address 92@@@@@@@@@@ # noqa
                read_flt_le()
                blkmeta["KV"]              = read_flt_le()              # address 100@@@@@@@@@ # noqa
                blkmeta["MA"]              = read_flt_le()              # address 104@@@@@@@@@ # noqa
                read_flt_le()                                           # address 108@@@@@@@@@ equal to 0??? # noqa
                blkmeta["RANGE_WL"]        = read_dbl_le()              # address 112@@@@@@@@@ # noqa
                read_flt_le()                                           # address 120@@@@@@@@#  equal to 0??? # noqa
                read_flt_le()                   #  equal to 0???        # address 124 # noqa
                read_flt_le()                   #  equal to 1???        # address 128 # noqa
                read_flt_le()                   #  equal to 0???        # address 132 # noqa
                read_flt_le()                                           # address 136@@@@@@@@#  equal to 0??? # noqa
                read_flt_le()                                           # address 140@@@@@@@@#  equal to 0??? # noqa
                read_flt_le()                   #  equal to 0???        # address 144@@@@@@@@ # noqa
                filex.read(20)
                blkmeta["PSD2THETA"]        =read_dbl_le()              # address 168 @@@@@@@@@@@ # noqa
                blkmeta["PSDCHANNEL1"]      = read_uint32_le()          # address 176 @@@@@@@@@@@ # noqa
                blkmeta["PSDAPERTURE"]      = read_flt_le()             # address 180 @@@@@@@@@@@ # noqa
                blkmeta["PSDTYPE"]          = read_uint32_le()          # address 184 @@@@@@@@@@@ # noqa
                blkmeta["PSDFIXED"]         = read_flt_le()             # address 188 @@@@@@@@@@@ # noqa

                # #blkmeta["TEMPCONTROL"] = 2
                filex.read(52)
                blkmeta["TEMPCONTROL"]      = read_uint32_le()          # address 244@@@@@@@@ # noqa
                blkmeta["TEMPSTAGE"]        = read_flt_le()             # address 248@@@@@@@@ # noqa
                blkmeta["TEMPSENSOR"]       = read_flt_le()             # address 252@@@@@@@@ # noqa
                blkmeta["TEMPERATURE"]      = read_flt_le()             # adresss 256@@@@@@@@@@@@@@ # noqa
                blkmeta["TEMPRATE"]         = read_flt_le()             # adresss 260@@@@@@@@@@@@@@ # noqa
                blkmeta["TEMPDELAY"]        = read_flt_le()             # adresss 264@@@@@@@@@@@@@@ # noqa
                blkmeta["TEMPRAMPFLAG"]     = read_flt_le()             # adresss 268@@@@@@@@@@@@@@ # noqa

                filex.read(56)
                # print filex.tell(), 'should be 642+328 970'
                blkmeta["THETA"]   = read_dbl_le()                      # adresss 328@@@@?????@@@@@@10 # noqa
                filex.read(84)                                            # adresss 336@@@@?????@@@@@@10 # noqa
                blkmeta["2THETA"]   = read_dbl_le()                     # adresss 420@@@@?????@@@@@@ # noqa
                filex.read(32)                                          # adresss 428@@@@?????@@@@@@ # noqa
                read_uint32_le()  #92                                   # adresss 460@@@@?????@@@@@@ # noqa
                read_uint32_le()  #7                                    # adresss 464@@@@?????@@@@@@ # noqa
                filex.read(92)
                blkmeta["DETECTOR"] =       read_str(80)                 # adresss 560@@@@?????@@@@@@ # noqa
                read_uint32_le()                                         # address  640 @@@@@@@@@@@@@@@@@@@@ # noqa
                read_uint32_le()                                         # address  644 @@@@@@@@@@@@@@@@@@@@ # noqa
                # print filex.tell(), 'should be 648+642 1290'
                blkmeta["DETECTORHV"] =     read_flt_le()                # address  648 @@@@@@@@@@@@@@@@@@@@ # noqa
                blkmeta["AMPLIFIER_GAIN"] = read_flt_le()                # adresss 652@@@@@@@@@@@@@@@@@@@@ # noqa
                blkmeta["DETECTORLLD1"]   = read_flt_le()                # adresss 656@@@@@@@@@@@@@@@@@@@@ # noqa
                blkmeta["DETECTORWW1"]    = read_flt_le()                # adresss 660@@@@@@@@@@@@@@@@@@@@ # noqa
                blkmeta["DETECTORLLD2"]   = read_flt_le()                # adresss 664 # noqa
                blkmeta["DETECTORWW2"]    = read_flt_le()                # adresss 668 # noqa
                blkmeta["DETECTORPS"]     = read_flt_le()                # adresss 672@@@@@@@@@@@@@@@@@@@@ # noqa
                blkmeta["DETECTORDT"]     = read_flt_le()                # adresss 676@@@@@@@@@@@@@@@@@@@@ # noqa
                read_uint32_le()
                # if cur_range==0:
                #    assert filex.tell() == 1326
                y = np.fromfile(filex, dtype=np.float32, count=blkmeta["STEPS"])
                x = calc_x(blkmeta["START"], blkmeta["STEPSIZE"], y)
                # print len(x), len(y)
                # print 'shape',x.shape , y.shape
                self.data.append({'array': np.vstack((x, y)).T,
                                  'info': blkmeta})

                # except Exception as x:
                # print 'pippp'
                # print 'just before ',filex.tell()
                # print x
                # break
                # print supplementary_headers_size
    for j, i in enumerate(self.data):
        i['info']['index'] = j
        i['info']['UNIT'] = 'counts'
