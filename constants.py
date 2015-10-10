import threedize as ddd
import camera_to_threedize as c23d
import numpy as np

camerapos = ddd.coords(20, 37, 47)
camera_phi = -np.pi/2 # TODO this is wrong
cameraposor = ddd.Posor(camerapos, np.pi, camera_phi, 0)

laserpos = ddd.coords(0, 0, 59.5) # x-coord should not matter
lasertheta = 0

ref_half_plane = c23d.HalfPlane(ddd.coords(36, 0, 18.5), # y-coord should not matter
                                ddd.coords(0, 0, 1),
                                ddd.coords(1, 0, 0))

view = ddd.View(319.5, 239.5, 490, 25 * np.pi / 180)
