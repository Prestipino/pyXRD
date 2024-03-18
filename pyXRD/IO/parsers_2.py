"""
   parsed for different format
   raw inspirwed from https://github.com/wojdyr/xylib
"""
import numpy as np
import os


def calc_x(start, step, data):
    start, step, = float(start), float(step)
    return np.array([start + step * i for i in np.arange(len(data))])


def read_raw(self, filename):
    read_i = lambda arr : np.frombuffer(bfile[arr:], dtype=np.uint32, count=1)[0] # noqa
    read_d = lambda arr : np.frombuffer(bfile[arr:], dtype=np.float64, count=1)[0] # noqa
    read_f = lambda arr : np.frombuffer(bfile[arr:], dtype=np.float32, count=1)[0] # noqa
    read_s = lambda arr, nby: bfile[arr:arr+nby].decode('ascii').rstrip('\x00') # noqa

    self.data = []

    with open(filename, 'rb') as filex:
        bfile = filex.read()
    head = bfile[:4].decode('ascii')
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
        setlf.info['Version']= read_s(0, 7)   # version complet
        filex.read(4)   # results in 65519??             ## address 
        # file_status=read_uint32_le()
        # status=["done", "active", "aborted", "interrupted"]
        # self.file_status=status[file_status]
        self.info["MEASURE_DATE"] = read_s(12, 12)        # address 12# noqa E510
        self.info["MEASURE_TIME"] = read_s(24, 10)        # address 24->34# noqa E510
        self.info['SCAN_cnt_0'] = read_i(36)      # noqa
        self.info['SCAN_cnt']   = read_i(40)      # noqa
        self.info['SCAN_cnt2']  = read_i(44)      # noqa
        self.info['RUNTIME']    = read_f(48)      # maybe done address 48 52# noqa E510
        self.info['RUNTIME2']   = read_f(48)      # maybe done address 52 56# noqa E510
        #future_info  = read_i()                 # maybe done val 1409  address 56 60   # noqa E510
        #filex.read(3)                                   # maybe done  address 60 61                  # noqa E510

        pos = 61
        while True:
            code = read_i(pos)                                 # offset x->x+4  # noqa E510
            if code in [0, 160]:
                pos += 4
                break
            len_seg =  read_i(pos+4)                         # offset 4->8  # noqa E510
            if code == 10:
                key = read_s(pos + 12, 24)
                self.info[key] = read_s(pos+36, len_seg - 36 ) # noqa E510
                pos += len_seg
            elif code == 30:
                self.info["V4_INF_STAGE_CODE"]    = read_i(pos+12)    # noqa
                self.info['GONIOMETER_RADIUS']    = read_f(pos+24)/2  # noqa
                self.info["V4_INF_FIXED_DIVSLIT"] = read_f(pos+36)    # noqa
                self.info["FIXED_ANTISLIT"]       = read_f(pos+60)    # noqa
                self.info["FIXED_DSLIT"]          = read_f(pos+64)    # noqa
                self.info["ALPHA_AVERAGE"]        = read_d(pos+72)    # noqa
                self.info["ALPHA1"]               = read_d(pos+80)    # noqa
                self.info["ALPHA2"]               = read_d(pos+88)    # noqa
                self.info["BETA"]                 = read_d(pos+96)    # noqa
                self.info["ALPHA_RATIO"]          = read_d(pos+104)   # noqa
                self.info["Anode"]           =  read_s(pos+116, 4)    # noqa
                self.info["W_UNIT"]          =  read_s(pos+120, 4)    # noqa
                pos += len_seg
            elif code == 60:
                pos += len_seg
            elif code == 5:
                pos += len_seg
            else:
                print('unknown code', code)
                raise ValueError('unknown code')

        for cur_range in range(self.info['SCAN_cnt']):
            print(cur_range, pos)
            blkmeta = {}
            blkmeta['SCAN_step1']         = read_i(pos+4)    # noqa
            blkmeta['SCAN_step2']         = read_i(pos+8)    # noqa
            blkmeta['ADDITIONALDETECTOR'] = read_i(pos+24)   # noqa                
            blkmeta['SCAN_type']        = read_s(pos+32, 24) # address 32@@@@@@@@@@ # noqa
            # print filex.tell(), 'should be 642+68 710'
            blkmeta["TIMESTARTED"]     = read_f(pos+68)       # noqa
            blkmeta["START"]           = read_d(pos+72)       # not sure result=10 # noqa
            blkmeta["STEPSIZE"]        = read_d(pos+80)       # noqa
            blkmeta["STEPS"]           = read_i(pos+88)       # address 88@@@@@@@@@ # noqa
            blkmeta["STEPTIME"]        = read_f(pos+92)       # address 92@@@@@@@@@@ # noqa
            blkmeta["KV"]              = read_f(pos+100)              # address 100@@@@@@@@@ # noqa
            blkmeta["MA"]              = read_f(pos+104)              # address 104@@@@@@@@@ # noqa
            blkmeta["RANGE_WL"]        = read_d(pos+112)              # address 112@@@@@@@@@ # noqa
            datum_size      = read_i(pos+136)     # noqa
            hdr_size        = read_i(pos+140)                            # address 140@@@@@@@@#  equal to 0??? # noqa

            pos += 160

            next_data = pos + hdr_size
            while hdr_size > 0:
                code    = read_i(pos)        # noqa E510
                len_seg = read_i(pos+4)      # noqa E510
                if code == 10:
                    key = read_s(pos + 12, 24)
                    self.info[key] = read_s(pos+36, len_seg - 36 ) # noqa E510
                    pos += len_seg
                    hdr_size -= len_seg
                if code == 110:
                    blkmeta["PSD2THETA"]        = read_d(pos+8)              # address 8 @@@@@@@@@@@ # noqa
                    blkmeta["PSDCHANNEL1"]      = read_i(pos+16)          # address 16 @@@@@@@@@@@ # noqa
                    blkmeta["PSDAPERTURE"]      = read_f(pos+20)             # address 20 @@@@@@@@@@@ # noqa
                    blkmeta["PSDTYPE"]          = read_i(pos+24)          # address 24 @@@@@@@@@@@ # noqa
                    blkmeta["PSDFIXED"]         = read_f(pos+4)             # address 28 @@@@@@@@@@@ # noqa 
                    pos += len_seg
                    hdr_size -= len_seg
                if code == 50:
                    # int 2                                                 # address 8 @@@@@@@@@@@ # noqa
                    key  = read_s(pos+12:, 24)                               # address 12 @@@@@@@@@@@ # noqa
                    blkmeta[f"START_{key}"]      = read_d(56)          # address 56 @@@@@@@@@@@ # noqa
                pos += len_seg
                hdr_size -= len_seg
                if code == 300:
                    blkmeta["HRXRD"] =[]                                       # address 8 @@@@@@@@@@@ # noqa
                    blkmeta["HRXRD"].append(read_s(pos, 24))
                    blkmeta["HRXRD"].append(read_d(52))
                    blkmeta["HRXRD"].append(read_d(60))
                    blkmeta["HRXRD"].append(read_d(80))
                    blkmeta["HRXRD"].append(read_d(88))
                    blkmeta["HRXRD"].append(read_d(96))
                    blkmeta["HRXRD"].append(read_d(104))
                    blkmeta["HRXRD"].append(read_i(112))
                    blkmeta["HRXRD"].append(read_d(116))
                    blkmeta["HRXRD"].append(read_d(124))
                    blkmeta["HRXRD"].append(read_d(132))
                    blkmeta["HRXRD"].append(read_d(204))
                    blkmeta["HRXRD"].append(read_d(212))
                    blkmeta["HRXRD"].append(read_d(220))
                pos += len_seg
                hdr_size -= len_seg
            pass
            y = np.frombuffer(bfile[next_data:], dtype=np.float32, count=blkmeta["STEPS"])
            x = calc_x(blkmeta["START"], blkmeta["STEPSIZE"], y)
            # print len(x), len(y)
            # print 'shape',x.shape , y.shape
            self.data.append({'array': np.vstack((x, y)).T,
                              'info': blkmeta})

for j, i in enumerate(self.data):
    i['info']['index'] = j
    i['info']['UNIT'] = 'counts'
