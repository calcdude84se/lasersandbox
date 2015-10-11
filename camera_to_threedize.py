import threedize as ddd
import numpy.matlib as np
import numpy.linalg as npl

# Prepare data from the camera for use with threedize.threedize_phi_angles
def threedize_phi_angles(data, ref_half_plane, view, cameraposor, laserpos, lasertheta):
    return ddd.threedize_phi_angles(tag_data(data, ref_half_plane, view, cameraposor, laserpos, lasertheta),
                                 view, cameraposor, laserpos, lasertheta)

# x is in the half-plane if, in addition to dot(n,x)=0, we have dot(side,x)>=0
class HalfPlane(object):
    def __init__(self, pos, normal, side):
        self.pos = pos
        self.normal = normal
        self.side = side

class NoReferenceException(Exception): pass

def calc_phi(xys, ref_half_plane, view, cameraposor, laserpos, lasertheta):
    cref_pos = ddd.unrotate(ref_half_plane.pos - cameraposor.pos, cameraposor)
    cref_side = ddd.unrotate(ref_half_plane.side, cameraposor)
    # TODO less copy-pasta
    cpos = np.array([cref_pos[1, 0], -cref_pos[2, 0]]) / cref_pos[0, 0] * ddd.view_number(view) \
           + np.array([view.centerx, view.centery])
    cside = np.array([cref_side[1, 0], -cref_side[2, 0]])
    dxys = xys - cpos
    dot_products = np.array(np.mat(cside) * np.mat(dxys).T)[0]
    good_xys = xys[dot_products >= 0]
    if len(good_xys) == 0:
        raise NoReferenceException()
    threepoints = ddd.threedize_plane(good_xys, view, cameraposor, ref_half_plane)
    return calc_phi_points(threepoints, laserpos, lasertheta)

def calc_phi_points(points, laserpos, lasertheta):
    plane_line = ddd.coord(-np.sin(lasertheta), np.cos(lasertheta), 0)
    normals = np.cross(np.array(plane_line.T)[0], points - np.array(laserpos.T)[0])
    return calc_phi_norm(np.average(normals / npl.norm(normals), axis = 0))

def calc_phi_norm(norm):
    return np.arctan2(norm[2], npl.norm(norm[:2]))

def tag_data(data, ref_half_plane, view, cameraposor, laserpos, lasertheta):
    result = []
    for xys in data:
        if len(xys) == 0:
            continue
        try:
            result.append((calc_phi(xys, ref_half_plane, view,
                                    cameraposor, laserpos, lasertheta),
                           xys))
        except NoReferenceException:
            pass
    return result
