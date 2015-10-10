import pygame
import pygame.camera
from pygame.locals import *

import numpy as np

import scipy.ndimage.filters as filt

import matplotlib.pyplot as plt
import matplotlib.cm as cm

import time

def waitCountdown():
   for i in range(4, 1, -1):
       time.sleep(1)
       print i




pygame.camera.init()


cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
waitCountdown()
lfreeimage = cam.get_image()

waitCountdown()

video = ["ERROR"] * 100
for i in range(100):
    video[i] = cam.get_image()
    
cam.stop()

lfreenpimage = np.frombuffer(lfreeimage.get_buffer(), dtype = np.uint8).reshape(480, 640, 3)



npvideo = ["error"] * 100
for i in range(100):
    npvideo[i] = np.frombuffer(npimage[i].get_buffer(), dtype = np.uint8).reshape(480, 640, 3)

plt.imshow(lfreenpimage - npvideo[50])

plt.show()
