import numpy.matlib as np

# Take 2 numpy arrays, xs and ys, along with the view, represented as an object
# with minx, maxx, miny, maxy, xangle, yangle, and two objects camerapos, with
# x, y, z, theta, phi, and psi, and laserpos, with x, y, z, theta, and phi.
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
def 3dize(xs, ys, view, camerapos, laserpos):
    plane = calc_plane(laserpos)
    rays = calc_rays(xs, ys, view)
    rot_rays = rotate(rays, camerapos)
    3d_points = intersect(plane, camerapos, rot_rays)
    return 3d_points

class Plane(object):
    def __init__(self, x, y, z, dx, dy, dz):
        self.x = x
        self.y = y
        self.z = z
        self.dx = dx
        self.dy = dy
        self.dz = dz

# Take a pos object and return another object with point x, y, z and normal dx,
# dy, dz
def calc_plane(pos):
    normal = np.mat([[1, 0, 0]], dtype=np.float).transpose()
    rot_normal = rotate(normal, pos)
    return Plane(pos.x, pos.y, pos.z, rot_normal[0, 0], rot_normal[1, 0], rot_normal[2, 0])
