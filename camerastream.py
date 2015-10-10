import pygame
import pygame.camera
from pygame.locals import *

import numpy as np

import scipy.ndimage.filters as filt

import matplotlib.pyplot as plt
import matplotlib.cm as cm

import time

def waitCountdown():
   for i in range(4, 0, -1):
       time.sleep(1)
       print i




pygame.camera.init()


cam = pygame.camera.Camera("/dev/video1",(640,480))
cam.start()
cam.get_image()
waitCountdown()
lfreeimage = cam.get_image()

waitCountdown()

video = ["ERROR"] * 100
for i in range(100):
    video[i] = cam.get_image()
    
cam.stop()

lfreenpimage = np.frombuffer(lfreeimage.get_buffer(), dtype = np.uint8).reshape(480, 640, 3).astype(np.int)



npvideo = ["error"] * 100
for i in range(100):
    npvideo[i] = np.frombuffer(video[i].get_buffer(), dtype = np.uint8).reshape(480, 640, 3).astype(np.int)


diff = (lfreenpimage - npvideo[50])/2 + 128

diffratio = diff[:,:,2].astype(np.float) / (diff[:,:,0] + diff[:,:,1] + diff[:,:,2])

if __name__ == "__main__":
    plt.imshow(diff[:,:,2].astype(np.float) / (diff[:,:,0] + diff[:,:,1] + diff[:,:,2]))
    plt.colorbar()
    plt.show()
