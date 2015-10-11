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
    
    return z, mytree





if __name__ == "__main__":
    xarray = np.linspace(-5, 5, 400)
    yarray = np.linspace(-5, 5, 400)
    
    xmesh, ymesh = np.meshgrid(xarray, yarray)
    
    xpoint = np.random.ranf(400)*10 -5
    ypoint = np.random.ranf(400)*10 -5
    zpoint = xpoint**2 + ypoint **2
    
    pointcloud = np.array([xpoint, ypoint, zpoint]).transpose()
    
    zarray , mytree = interpolate(xmesh, ymesh, pointcloud)
    zarray = filt.gaussian_filter(zarray, 4)
    plt.imshow(zarray)
    plt.show()
    
    
    
    
    
    
    





