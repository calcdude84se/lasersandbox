import threedize as ddd
import numpy.matlib as np

# Prepare data from the camera for use with threedize.threedize_phi_angles

# x is in the half-plane if, in addition to dot(n,x)=0, we have dot(side,x)>=0
class HalfPlane(object):
    def __init__(self, pos, normal, side):
        self.pos = pos
        self.normal = normal
        self.side = side

def calc_phi(xys, ref_half_plane, view, cameraposor, laserpos, lasertheta):
    cref_pos = ddd.unrotate(ref_half_plane.pos - cameraposor.pos, cameraposor)
    cref_side = ddd.unrotate(ref_half_plane.side, cameraposor)
    # TODO less copy-pasta
    cpos = np.array([cref_pos[1, 0], -cref_pos[2, 0]])
    cside = np.array([cref_side[1, 0], -cref_side[2, 0]])
    dxys = xys - cpos
    dot_products = np.array(np.mat(cside) * np.mat(dxys).transpose())[0]
    good_dxys = dxys[dot_products >= 0]
    
