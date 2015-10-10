import threedize as ddd
import numpy.matlib as np

# Prepare data from the camera for use with threedize.threedize_phi_angles

# x is in the half-plane if, in addition to dot(n,x)=0, we have dot(side,x)>=0
class HalfPlane(object):
    def __init__(self, pos, normal, side):
        self.pos = pos
        self.normal = normal
        self.side = side

def calc_phi(xs, ys, ref_pos, ref_side, view, cameraposor, laserpos, lasertheta):
    cref_pos = ddd.unrotate(ref_pos - cameraposor.pos, cameraposor)
    cref_side = ddd.unrotate(ref_side, cameraposor)
    xpos = cref_pos[1, 0]
    ypos = -cref_pos[2, 0]
    side = 
