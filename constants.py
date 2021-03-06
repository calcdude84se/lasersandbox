import threedize as ddd
import camera_to_threedize as c23d
import numpy as np

camerapos = ddd.coord(20, 42, 46)
camera_phi = -np.pi*78/180 # TODO this is wrong
cameraposor = ddd.Posor(camerapos, -np.pi/2, camera_phi, 0)

laserpos = ddd.coord(0, 0, 61) # x-coord should not matter
lasertheta = np.pi/2

ref_half_plane = c23d.HalfPlane(ddd.coord(33, 0, 18), # y-coord should not matter
                                ddd.coord(0, 0, 1),
                                ddd.coord(1, 0, 0))

view = ddd.View(319.5, 239.5, 245, 25 * np.pi / 180)

def default_threedize_phi_angles(data):
    """Calculate the array of x-y-z triples associated with the list of arrays of
pixel triples data taken by the configuration defined by the constants in this
module."""
    return c23d.threedize_phi_angles(data, ref_half_plane, view, cameraposor, laserpos, lasertheta)
