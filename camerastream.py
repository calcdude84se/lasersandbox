import pygame
import pygame.camera
from pygame.locals import *

import numpy as np

import scipy.ndimage.filters as filt

import matplotlib.pyplot as plt
import matplotlib.cm as cm

import time

import serialConnection

def waitCountdown():
   for i in range(4, 0, -1):
       time.sleep(1)
       #print i

ROWNUM = 100


pygame.camera.init()


cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()

def getCamStream():
    cam.get_image()
    waitCountdown()
    lfreeimage = cam.get_image()

    waitCountdown()

    serialConnection.activate("go!")
    time.sleep(.7)
    video = ["ERROR"] * ROWNUM
    for i in range(ROWNUM):
        video[i] = cam.get_image()
        print "say frame: " , i


    lfreenpimage = np.frombuffer(lfreeimage.get_buffer(), dtype = np.uint8).reshape(480, 640, 3).astype(np.int)



    npvideo = ["error"] * ROWNUM
    for i in range(ROWNUM):
        npvideo[i] = np.frombuffer(video[i].get_buffer(), dtype = np.uint8).reshape(480, 640, 3).astype(np.int)


    diff = [ (lfreenpimage - npvideo_frame)/2 + 128 for npvideo_frame in npvideo ] 


    diffratio = [diff_el[:,:,2].astype(np.float) / (diff_el[:,:,0] + diff_el[:,:,1] + diff_el[:,:,2]) for diff_el in diff]

    mid = diffratio[50]

    plt.imshow(diffratio[50])
    plt.show()
    return diffratio

if __name__ == "__main__":
    plt.imshow(mid)
    plt.colorbar()
    plt.show()
