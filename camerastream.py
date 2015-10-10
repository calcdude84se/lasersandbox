import pygame
import pygame.camera
from pygame.locals import *

import numpy as np

import scipy.ndimage.filters as filt

import matplotlib.pyplot as plt
import matplotlib.cm as cm

pygame.camera.init()


cam = pygame.camera.Camera("/dev/video0",(640,480))
cam.start()

image = cam.get_image()
cam.stop()

npimages = np.frombuffer(image.get_buffer(), dtype = np.uint8).reshape(480, 640, 3)

plt.imshow(npimages)
plt.show()
