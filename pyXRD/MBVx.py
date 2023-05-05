# cython: infer_types=True
import numpy as np
#cimport cython


#DTYPE = np.intc
#DTYPE2 = np.double_t
#def distances(double [:,:] basis, double [:] x0,double [:,:] x):
def distances(basis, x0, x):
    dist=np.subtract(x,x0)
    dist=np.dot(basis, dist.T).T
    dist*=dist
    disto=np.sqrt(np.sum(dist, axis=1))
    dis_i=np.argsort(disto)
    return disto, dis_i

    
    
#@cython.boundscheck(False)
#@cython.wraparound(False) 
def  BVM(basis, grid_size, labels, xyz, params, dmin, dmax):
#cpdef  BVM(double [:,:] basis, int [:] grid_size, int [:] labels,
#           double [:,:] xyz,   double [:,:] params,  double dmin, double dmax):

    len_d=labels.shape[0]
    xstep= 1.0/grid_size[0]
    ystep= 1.0/grid_size[1]
    zstep= 1.0/grid_size[2]
    xmax = grid_size[0]
    ymax = grid_size[1]
    zmax = grid_size[2]
    #cdef double [:] disto
    #cdef int [:] dist_i 
    #cdef double [:] x0
    grid =  np.zeros([xmax, ymax, xmax], dtype= np.double)
    #cdef double [:,:,:] g = grid   


    
    for x in xrange(xmax):
        for y in xrange(ymax):
            for z in xrange(zmax):
                disto, dis_i=distances(basis, np.array([x*xstep, y*xstep, z*xstep]), xyz)
                if disto[dis_i[0]]< dmin:
                    continue
                elif disto[dis_i[0]]>dmax:
                    continue
                else:
                    for i in xrange(len_d):
                        j= dis_i[i]
                        if disto[j]> dmax:
                            break
                        elif params[labels[j],0]==0:
                            continue                        
                        else:
                            grid[x,y,z]+= np.exp((params[labels[j],0]-disto[j])/params[labels[j],1])
                        pass
                    pass
                pass
            pass
        pass
    return grid
