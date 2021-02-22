import numpy as np
import struct

formatbyte = '''
Format  C Type                  Python type         Standard size
x       pad byte                no value
c       char                    bytes of length 1       1
b       signed char             integer                 1
B       unsigned char           integer                 1
?       _Bool                   bool                    1   (1)
h       short                   integer                 2   (3)
H       unsigned short          integer                 2   (3)
i       int                     integer                 4   (3)
I       unsigned int            integer                 4   (3)
l       long                    integer                 4   (3)
L       unsigned long           integer                 4   (3)
q       long long               integer                 8   (2), (3)
Q       unsigned long long      integer                 8   (2), (3)
n       ssize_t                 integer                     (4)
N       size_t                  integer                     (4)
e       (7)                     float                   2   (5)
f       float                   float                   4   (5)
d       double                  float                   8   (5)
s       char[]                  bytes
p       char[]                  bytes
P       void *                  integer                     (6)'''


byte_size = {
    'c': 1,
    'b': 1,
    'B': 1,
    '?': 1,
    'h': 2,
    'H': 2,
    'i': 4,
    'I': 4,
    'l': 4,
    'L': 4,
    'q': 8,
    'Q': 8,
    'e': 2,
    'f': 4,
    'd': 8
}


def read_uint32_le(filex):
    return np.fromfile(filex, dtype=np.uint32, count=1)[0]


def read_dbl_le(filex):
    return np.fromfile(filex, dtype=np.float64, count=1)[0]


def read_flt_le(filex):
    return np.fromfile(filex, dtype=np.float32, count=1)[0]


def search_value(filex_s, value, fmt):
    for i in range(len(filex_s)):
        for f in fmt:
            j = i + byte_size[f]
            if struct.unpack(filex_s[i:j], f) == value:
                print(i)
