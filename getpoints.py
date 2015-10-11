import numpy as np

import scipy.ndimage.filters as filt

import matplotlib.pyplot as plt
import matplotlib.cm as cm

import camerastream as camst

import pickle

from mpl_toolkits.mplot3d import Axes3D
def getpoints(diffratio):
    image = []
    minarray = []
    flatpoints = []
    angles = []
    nonconfarray = []
    #construct mins array

    for onediffpic in diffratio:
        typicalbright = np.sum(onediffpic, axis = 0) / 480
    
        nonconfidences = np.min(onediffpic, axis = 0) / typicalbright
        nonconfarray += [nonconfidences]
        mins = np.argmin(onediffpic, axis = 0)
        minarray += [mins]
    
        flat_representative = mins[570]
        angles += [flat_representative]
    
    nminarray = np.array(minarray)

    nminarray = filt.gaussian_filter(nminarray, 1)
    npangles = np.array(angles)
    npangles = filt.gaussian_filter(npangles, 1)
    for j in range(camst.ROWNUM):
        mins, nonconfidences, flat_representative = nminarray[j], nonconfarray[j], npangles[j]
    
        realmins = []
        for i in range(640):
           if nonconfidences[i] < .9:
               realmins += [[i, mins[i]]]
               flatpoints += [[i, mins[i], flat_representative]]
        image += [realmins]
    

    
    
    
        nonconfidences = np.min(onediffpic, axis = 0) / typicalbright
    
    npimage = np.array(image)
    npangles = np.array(angles)
    pointcloud = np.array(flatpoints)
    sss = np.array(minarray)
    
    plt.plot(pointcloud[:,0] + .5 * pointcloud[:,2] , pointcloud[:,1] + .5 * pointcloud[:,2], ",")
   
    plt.show()

    PackedData = [(angle, np.array(array)) for angle, array in zip(angles, image)]
    with open("Data", "w") as f:
        pickle.dump(PackedData, f)
    
    list_of_rows_with_same_laser = [np.array(array) for array in image]
    return list_of_rows_with_same_laser
    

if __name__ == "__main__":
   
   plt.imshow(diffratio[50])
   plt.plot(minarray[50])
   plt.show()
   plt.plot(pointcloud[:,0] + .5 * pointcloud[:,2] , pointcloud[:,1] + .5 * pointcloud[:,2], ",")
   
   plt.show()
   


    




