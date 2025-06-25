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

    if isinstance(filename, memoryview):
        bfile = filename.tobytes()
    if isinstance(filename, str):
        with open(filename, 'rb') as filex:
            bfile = filex.read()


    head = bfile[:4].decode('ascii')
    if head == "RAW ":
        self.version = "ver. 1"
    elif head == "RAW2":
        self.version = "ver. 2"
    elif head == "RAW1":
        subv = read_s(4,3)
        if subv == ".01":
            self.version = "ver. 3"
    elif (head == "RAW4"):
        self.version = "ver. 4"
    else:
        print("no format detected")
    print('head= ', head)
    if self.version == "ver. 3":
        offset = 8
        file_status = read_i(offset)
        status = ["done", "active", "aborted", "interrupted"]
        self.file_status = status[file_status]
        self.info['SCAN_cnt'] = read_i(12)
        self.info["MEASURE_DATE"]                = read_s( 16, 10)     ## address 16 # noqa
        self.info["MEASURE_TIME"]                = read_s( 26, 10)     ## address 26 # noqa
        self.info["USER"]                        = read_s(36 , 72)     # address 36 # noqa
        self.info["SITE"]                        = read_s(108, 218)    # address 108 # noqa
        self.info["SAMPLE_ID"]                   = read_s( 32, 60)     ## address 326 # noqa
        self.info["COMMENT"]                     = read_s(386, 160)    # address 386 # noqa
        #self.info["bug"]                         = filex.read(2)      #apparently there is a bug in docs, 386+160 != 548 # noqa
        self.info["goniometer_code"]             = read_i( 548)       # address 548 # noqa
        self.info["goniometer stage code"]       = read_i(552)        # address 552 # noqa
        self.info["sample loader code"]          = read_i(556)        # address 556 # noqa
        self.info["goniometer controller code"]  = read_i(560)        # address 560 # noqa
        self.info["(R4)_goniometer_radius"]      = read_i(564)        # address 564 # noqa
        self.info["(R4) fixed divergence"]       = read_i(568)        # address 568 # noqa
        self.info["(R4) fixed sample slit"]      = read_i(572)        # address 572 # noqa
        self.info["primary Soller slit"]         = read_i(576)        # address 576 # noqa
        self.info["primary monochromator"]       = read_i(580)        # address 580 # noqa
        self.info["(R4) fixed antiscatter"]      = read_i(584)        # address 584 # noqa
        self.info["(R4) fixed detector slit"]    = read_i(588)        # address 588 # noqa
        self.info["secondary Soller slit"]       = read_i(592)        # address 592 # noqa
        self.info["fixed thin film attachment"]  = read_i(596)        # address 596 # noqa
        self.info["beta filter"]                 = read_i(600)        # address 600 # noqa
        self.info["secondary monochromator"]     = read_i(604)        # address 604 # noqa

        self.info["ANODE_MATERIAL"]              = read_s(608, 4)  # address 608      # noqa
        #filex.read(4); # unused                      # address 612            # noqa
        self.info["ALPHA_AVERAGE"]               = read_i(616)        # address 616      # noqa
        self.info["ALPHA1"]                      = read_i(624)        # address 624    # noqa
        self.info["ALPHA2"]                      = read_i(632)        # address 632    # noqa
        self.info["BETA"]                        = read_i(640)        # address 640  # noqa
        self.info["ALPHA_RATIO"]                 = read_i(648)           # address 648    # noqa
        #filex.read(4); # (C4) unit name              # address 656             # noqa
        #filex.read(4); # (R4) intensity beta:a1      # address 660             # noqa
        self.info["measurement time"]            = read_f(664)           # address 664      # noqa
        #filex.read(43); # unused                     # address 668             # noqa
        #filex.read(1); # hardware dependency ...     # address 711             # noqa
        #print filex.tell()        #  start first  pattern comments
        #we start from 712
        
        offset =712
        datum_size = 4
        for cur_range in range(self.info['SCAN_cnt']):
            try:
                # print cur_range
                blkmeta = {}                        # empty dictionary for utility use
                header_len = read_i(offset)     # address 0
                # print header_len
                blkmeta["STEPS"] =        read_i(offset + 4)  # address 4 # noqa
                blkmeta["START_THETA"] =  read_d(offset + 8)  # address 8 # noqa
                blkmeta["START_2THETA"] = read_d(offset + 16) # address 16

                blkmeta["CHI_START"] = read_d(offset + 24)  # address 24 # noqa
                blkmeta["Phi_START"] = read_d(offset + 32)  # address 32 # noqa

                blkmeta["X_START"] =    read_d(offset + 40)  # address 40 # noqa
                blkmeta["Y_START"] =    read_d(offset + 48)  # address 48 # noqa
                blkmeta["Z_START"] =    read_d(offset + 56)  # address 56 # noqa
                blkmeta["DIVERGENCE"] = read_d(offset + 64)  # address 64 # noqa
                blkmeta["DIVER_MODE"] = read_s(offset + 72, 6) # address 72 # noqa
                 #filex.read(2); # unused                    # address 78 # noqa
                blkmeta["ANTISCATTER"] = read_d(offset + 80) # address 80 # noqa
                blkmeta["ANTISCAT_MODE"] = read_s(offset + 88, 6) # address 88 # noqa
                #filex.read(2); # unused                     # address 94 # noqa
                blkmeta['det_code']  = read_i(offset + 96)   # address 96 # noqa
                blkmeta["HIGH_VOLTAGE"] =   read_f(offset +100)  # address 100 # noqa
                blkmeta["AMPLIFIER_GAIN"] = read_f(offset +104)  # 104
                blkmeta["DISCRIMINATOR_1_LOWER_LEVEL"] = read_f(offset +108)  # 108
                #filex.read(4);       #full to investigate # address 112 # noqa
                #filex.read(4);                            # address 116 # noqa
                #filex.read(8);                            # address 120 # noqa
                #filex.read(4);                            # address 128 # noqa
                #filex.read(4);                            # address 132 # noqa
                blkmeta["Detectype"] : read_s(offset + 136, 5)  # address 136 # noqa
                #filex.read(3); # unused                   # address 141 # noqa
                #filex.read(8);                            # address 144 # noqa
                #filex.read(8);                            # address 152 # noqa
                #filex.read(8);                            # address 160 # noqa
                #filex.read(4);       maybe counts         # address 168 # noqa
                #filex.read(4); # unused                   # address 172 # noqa
                blkmeta["STEPSIZE"] = read_d(offset +176)   # address 176 # noqa
                #filex.read(8);                              # address 184 # noqa
                blkmeta["STEPTIME"] = read_f(offset +192)  # address 192 # noqa
                #filex.read(4);                            # address 196 # noqa
                #filex.read(4);                            # address 200 # noqa
                blkmeta["TIMESTARTED"] =read_f(offset + 204 )          # address 204  # noqa
                blkmeta["ROTATION_SPEEDrpm"] = read_f(offset + 208 )   # address 208  # noqa
                blkmeta["TEMPERATURE"] = read_f(offset + 212 )         # address 212  # noqa
                blkmeta["TEMP_RATE"] =read_f(offset + 216 )            # address 216  # noqa
                blkmeta["TEMP_DELAY"] =read_f(offset + 220 )           # address 220  # noqa
                blkmeta["GENERATOR_VOLTAGE"] = read_i(offset +224)  # 224
                blkmeta["GENERATOR_CURRENT"] = read_i(offset +228)  # 228
                #filex.read(4);                            # address 232 # noqa
                #filex.read(4); # unused                   # address 236 # noqa
                blkmeta["USED_LAMBDA"] = read_d(offset + 240)    # address 240 # noqa
                #filex.read(4);                            # address 248 # noqa
                #filex.read(4);    #used    4 val          # address 252 # noqa
                supplementary_headers_size = read_i(offset + 256) # address 256 # noqa
                #filex.read(4);                            # address 260 # noqa
                #filex.read(4);                            # address 264 # noqa
                #filex.read(4);  # unused                  # address 268 # noqa
                #filex.read(8);                            # address 272 # noqa
                #filex.read(24); # unused                 # address 280 # noqa
                # assert(filex.tellg() == 712 + (cur_range + 1) * header_len);
            except Exception as frase:
                print('pippp in header', cur_range)
                print(frase)
                print('just before ', filex.tell())
                print(supplementary_headers_size)
                if self.debug:
                    raise frase

            next_data = offset + header_len


            if (supplementary_headers_size > 0):
                next_data += supplementary_headers_size
                

            y = np.frombuffer(bfile[next_data:], dtype=np.float32, count=blkmeta["STEPS"])
            x = calc_x(blkmeta["START_2THETA"], blkmeta["STEPSIZE"], y)
            SS
            print('shape x, y ', x.shape, y.shape)
            offset = next_data + 4 * blkmeta["STEPS"]

            try:
                # print filex.tell()   start numeber for pattern
                self.data.append({'array': np.vstack((x, y)).T,
                                  'info': blkmeta})
                print('shape x, y ', x.shape, y.shape)

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
        self.info['Version']= read_s(0, 7)   # version complet
        # file_status=read_uint32_le()
        # status=["done", "active", "aborted", "interrupted"]
        # self.file_status=status[file_status]
        self.info["MEASURE_DATE"] = read_s(12, 12)        # address 12# noqa E510
        self.info["MEASURE_TIME"] = read_s(24, 10)        # address 24->34# noqa E510
        self.info['SCAN_cnt_0'] = read_i(36)      # noqa
        self.info['SCAN_cnt']   = read_i(40)      # noqa
        self.info['SCAN_cnt2']  = read_i(44)      # noqa
        self.info['RUNTIME']    = read_f(48)      # maybe done address 48 52# noqa E510
        self.info['RUNTIME2']   = read_f(52)      # maybe done address 52 56# noqa E510
        future_info  =read_i(56)                  # maybe done val 1409  address 56 60   # noqa E510
        #filex.read(3)                                   # maybe done  address 60 61                  # noqa E510
        #print(bfile[arr:3])
        #print('future_info', future_info) # noqa E510



        pos = 61
        while True:
            code = read_i(pos)                                 # offset x->x+4  # noqa E510
            if code in [0, 160]:
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
            # print(cur_range, pos)
            blkmeta = {}
            blkmeta['SCAN_step1']         = read_i(pos+4)    # noqa
            blkmeta['SCAN_step2']         = read_i(pos+8)    # noqa
            blkmeta['ADDITIONALDETECTOR'] = read_i(pos+24)   # noqa                
            blkmeta['SCAN_type']        = read_s(pos+32, 24) # address 32@@@@@@@@@@ # noqa
            # print filex.tell(), 'should be 642+68 710'
            blkmeta["TIMESTARTED"]     = read_f(pos+68)       # noqa
            blkmeta["START"]           = read_d(pos+72)       # not sure result=10 # noqa
            blkmeta["STEPSIZE"]        = read_d(pos+80)       # 88 # noqa
            blkmeta["STEPS"]           = read_i(pos+88)       # address 88@@@@@@@@@ # noqa
            blkmeta["STEPTIME"]        = read_f(pos+92)       # address 92@@@@@@@@@@ # noqa
            blkmeta["KV"]              = read_f(pos+100)              # address 100@@@@@@@@@ # noqa
            blkmeta["MA"]              = read_f(pos+104)              # address 104@@@@@@@@@ # noqa
            blkmeta["RANGE_WL"]        = read_d(pos+112)              # address 112@@@@@@@@@ # noqa
            datum_size      = read_i(pos+136)                         # address 136@@@@@@@@#  equal to 0??? # noqa
            hdr_size        = read_i(pos+140)                         # address 140@@@@@@@@#  equal to 0??? # noqa
            pos += 160

            next_data = pos + hdr_size
            # print(pos, 'next_data', next_data)
            while hdr_size > 0:
                code    = read_i(pos)        # noqa E510
                len_seg = read_i(pos+4)      # noqa E510
                if code == 10:
                    key = read_s(pos + 12, 24)
                    self.info[key] = read_s(pos+36, len_seg - 36 ) # noqa E510
                    pos += len_seg
                    hdr_size -= len_seg
                elif code == 110:
                    blkmeta["PSD2THETA"]        = read_d(pos+8)              # address 8 @@@@@@@@@@@ # noqa
                    blkmeta["PSDCHANNEL1"]      = read_i(pos+16)          # address 16 @@@@@@@@@@@ # noqa
                    blkmeta["PSDAPERTURE"]      = read_f(pos+20)             # address 20 @@@@@@@@@@@ # noqa
                    blkmeta["PSDTYPE"]          = read_i(pos+24)          # address 24 @@@@@@@@@@@ # noqa
                    blkmeta["PSDFIXED"]         = read_f(pos+4)             # address 28 @@@@@@@@@@@ # noqa 
                    pos += len_seg
                    hdr_size -= len_seg
                elif code == 50:
                    # int 2 
                    un = read_i(pos + 8)
                    key  = read_s(pos+12, 24)                               # address 12 @@@@@@@@@@@ # noqa
                    un2 = read_i(pos + 52)
                    blkmeta[f"START_{key}"]      = read_d(pos+56)          # address 56 @@@@@@@@@@@ # noqa
                    pos += len_seg
                    hdr_size -= len_seg
                elif code == 300:
                    blkmeta["HRXRD"] =[]                                       # address 8 @@@@@@@@@@@ # noqa
                    blkmeta["HRXRD"].append(read_s(pos + 8, 24))
                    blkmeta["HRXRD"].append(read_d(pos + 52))
                    blkmeta["HRXRD"].append(read_d(pos + 60))
                    blkmeta["HRXRD"].append(read_d(pos + 80))
                    blkmeta["HRXRD"].append(read_d(pos + 88))
                    blkmeta["HRXRD"].append(read_d(pos + 96))
                    blkmeta["HRXRD"].append(read_d(pos + 104))
                    blkmeta["HRXRD"].append(read_i(pos + 112))
                    blkmeta["HRXRD"].append(read_d(pos + 116))
                    blkmeta["HRXRD"].append(read_d(pos + 124))
                    blkmeta["HRXRD"].append(read_d(pos + 132))
                    blkmeta["HRXRD"].append(read_d(pos + 204))
                    blkmeta["HRXRD"].append(read_d(pos + 212))
                    blkmeta["HRXRD"].append(read_d(pos + 220))
                    pos += len_seg
                    hdr_size -= len_seg
                else:
                    print('unknown code', code)
                    raise ValueError('unknown code')
            pass
            assert(datum_size == 4)
            y = np.frombuffer(bfile[next_data:], dtype=np.float32, count=blkmeta["STEPS"])
            x = calc_x(blkmeta["START"], blkmeta["STEPSIZE"], y)


            try:
                # print filex.tell()   start numeber for pattern
                self.data.append({'array': np.vstack((x, y)).T,
                                    'info': blkmeta})

            except Exception as frase:
                print('pippp in array', cur_range)
                print('shape x, y ', x.shape, y.shape)
                print(type(frase))
                print('just before ', filex.tell())
                if self.debug:
                    raise fras
            

            pos += datum_size * blkmeta["STEPS"]

    for j, i in enumerate(self.data):
        i['info']['index'] = j
        i['info']['UNIT'] = 'counts'
