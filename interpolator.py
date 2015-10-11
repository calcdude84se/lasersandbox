import numpy as np
import scipy.spatial
import scipy.ndimage.filters as filt

import matplotlib.pyplot as plt

def interpolate(xmesh, ymesh, pointcloud):
    shape = xmesh.shape
   
    mytree = scipy.spatial.cKDTree(pointcloud[:,:2])
    
    xflat = xmesh.flatten()
    yflat = ymesh.flatten()
    
    _, indecies = mytree.query(np.array([xflat, yflat]).transpose())
    
    z = pointcloud[indecies, 2]
    
    z = z.reshape(shape)
    
    #z = filt.gaussian_filter(z, 2)
    
    return z, mytree





def test():
    xarray = np.linspace(-5, 5, 30)
    yarray = np.linspace(-5, 5, 30)
    
    xmesh, ymesh = np.meshgrid(xarray, yarray)
    
    xpoint = np.random.ranf(400)*10 -5
    ypoint = np.random.ranf(400)*10 -5
    zpoint = xpoint**2 + ypoint **2
    
    pointcloud = np.array([xpoint, ypoint, zpoint]).transpose()
    
    zarray , mytree = interpolate(xmesh, ymesh, pointcloud)
    #zarray = filt.gaussian_filter(zarray, 4)
    return zarray
    
    
    
if __name__ == "__main__":
    z = test()
    plt.imshow(z)
    plt.show()
    
    





