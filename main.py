import numpy as np
import matplotlib.pyplot as plt

import time

import getpoints
import camerastream
import constants    #Jonathan's magic package

import interpolator

import toMinecraft

while True:
    inn = raw_input()
    
    
    if inn[0] == "c":
        print inn[1:]
        break
        
        
        
    reload(constants)
    reload(interpolator)
    reload(toMinecraft)
    diffratio = camerastream.getCamStream()
    print "say doing minfind"
    pixel_coords_rows = getpoints.getpoints(diffratio)
        
    


    print "say doing jonathan transform"
    pointcloud = constants.default_threedize_phi_angles(pixel_coords_rows)
    
    plt.plot(pointcloud[:,0], pointcloud[:,1])
    plt.title("tranformed pointcloud")
    plt.show()
    
    xspace = np.linspace(4, 40, 60)
    yspace = np.linspace(18, 44, int(60 * (44 - 18) / 36.))
    
    xmesh, ymesh = np.meshgrid(xspace, yspace)
    print "say interpolating pointcloud"
    zmesh, _ = interpolator.interpolate(xmesh, ymesh, pointcloud)
    print "say making string"
    string = toMinecraft.createString(zmesh)
    plt.imshow(zmesh)
    plt.show()
    print "say writing to minecraft"
    for line in string.split("\n"):
        print(line)
    print "say done making commands"
    

    
