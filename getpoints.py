import numpy as np

import scipy.ndimage.filters as filt

import matplotlib.pyplot as plt
import matplotlib.cm as cm

import camerastream as camst

import pickle

from mpl_toolkits.mplot3d import Axes3D

image = []
simage = []
flatpoints = []
angles = []
for onediffpic in camst.diffratio:
    typicalbright = np.sum(onediffpic, axis = 0) / 480

    nonconfidences = np.min(onediffpic, axis = 0) / typicalbright

    mins = np.argmin(onediffpic, axis = 0)
    flat_representative = mins[600]
    realmins = []
    for i in range(640):
       if nonconfidences[i] < .9:
           realmins += [[i, mins[i]]]
           flatpoints += [[i, mins[i], flat_representative]]
    image += [realmins]
    angles += [flat_representative]
    simage += [mins]
    
    
npimage = np.array(image)
npangles = np.array(angles)
pointcloud = np.array(flatpoints)
sss = np.array(simage)

PackedData = [(angle, np.array(array)) for angle, array in zip(angles, image)]
with open("Data", "w") as f:
   pickle.dump(PackedData, f)

if __name__ == "__main__":
   plt.plot(pointcloud[:,0] + .5 * pointcloud[:,2] , pointcloud[:,1] + .5 * pointcloud[:,2], "-")
   
   plt.show()
   


    




