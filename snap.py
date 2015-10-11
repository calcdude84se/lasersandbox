import pygame
import pygame.camera
from pygame.locals import *

import numpy as np

import scipy.ndimage.filters as filt

import matplotlib.pyplot as plt
import matplotlib.cm as cm

import time

pygame.camera.init()


cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()
cam.get_image()
time.sleep(1)
lfreeimage = cam.get_image()

    
cam.stop()

lfreenpimage = np.frombuffer(lfreeimage.get_buffer(), dtype = np.uint8).reshape(480, 640, 3).astype(np.int)


plt.imshow(lfreenpimage)
plt.show()

