import numpy.matlib as np

# To use:
# - Call threedize(xs, ys, view, cameraposor, laserposor), where:
#   - xs and ys are numpy arrays
#   - view is created with View
#   - the *posors are created with Posor(pos, theta, phi, psi)
#     - pos is created with coords

class Posor(object):
    def __init__(self, pos, theta, phi, psi):
        self.pos = pos
        self.theta = theta
        self.phi = phi
        self.psi = psi

class View(object):
    def __init__(self, centerx, centery, dist, angle):
        self.centerx = centerx
        self.centery = centery
        self.dist = dist
        self.angle = angle

# Take 2 numpy arrays, xs and ys, along with the view, represented as an object
# with centerx, centery, dist, angle, and two objects camerapos, with
# pos, theta, phi, and psi, and laserpos, with pos, theta, and phi.
# Return 3 numpy arrays, giving the corresponding points in absolute coördinates

# Laser starts out as the plane with normal y = z = 0.  Orientation is created
# in the following way: Start by looking along the positive x axis, with z up.
# Rotate theta radians clockwise along the z axis, towards positive y.  Rotate
# phi radians upwards along the new y axis, towards positive z.  Finally, rotate
# psi radians counterclockwise along the new x axis, towards positive z.

# The transformation from camera coördinates to absolute coördinates is then
# given by the matrix product:
# [ cos th -sin th 0 ] [ cos ph 0 -sin ph ] [ 1      0       0 ]
# [ sin th  cos th 0 ] [      0 1       0 ] [ 0 cos ps -sin ps ]
# [      0       0 1 ] [ sin ph 0  cos ph ] [ 0 sin ps  cos ps ]
def threedize(xs, ys, view, cameraposor, laserposor):
    plane = calc_plane(laserposor)
    rays = calc_rays(xs, ys, view)
    rot_rays = rotate(rays, cameraposor)
    3d_points = intersect(plane, cameraposor.pos, rot_rays)
    return tuple(3d_points)

class Plane(object):
    def __init__(self, pos, normal):
        self.pos = pos
        self.normal = normal

# Take a posor object and return another object with point x, y, z and normal
# dx, dy, dz
def calc_plane(posor):
    normal = rotate(coord(1, 0, 0), posor)
    return Plane(posor.pos, normal)

# points is a matrix
def rotate(points, posor):
    rot_matrix = calc_rot_matrix(posor)
    return rot_matrix * points

def calc_rays(xs, ys, view):
    something = view.dist/np.tan(view.angle)
    cxs = xs - view.centerx
    cys = ys - view.centery
    return np.mat([np.full(len(xs), something), cxs, -cys], dtype=np.float)

def calc_rot_matrix(posor):
    th = posor.theta
    theta = np.mat([[np.cos(th), -np.sin(th), 0],
                    [np.sin(th), np.cos(th), 0],
                    [0, 0, 1]], dtype=np.float)
    ph = posor.phi
    phi = np.mat([[np.cos(ph), 0, -np.sin(ph)],
                  [0, 1, 0],
                  [np.sin(ph), 0, np.cos(ph)]], dtype=np.float)
    ps = posor.psi
    psi = np.mat([[1, 0, 0],
                  [0, np.cos(ps), -np.sin(ps)],
                  [0, np.sin(ps), np.cos(ps)]], dtype=np.float)
    return theta * phi * psi

def intersect(plane, ray_pos, rays):
    nt = plane.normal.transpose()
    rel = np.array(rays.transpose()) * np.array((nt * (plane.pos - ray_pos))[0, 0] / np.array(nt * rays)[0])
    array = np.array(ray_pos.transpose())[0] + rel
    return np.matrix(array).transpose()

def coord(*args):
    return np.mat([args], dtype=np.float).transpose()
