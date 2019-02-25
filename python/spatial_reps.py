
from numpy import sin, cos, pi
import numpy as N

def rotate_x(alpha):
    """
    Generate a rotation matrix around the x axis.
    
    Arguments: 
    alpha - angle of rotation, counterclockwise when X points toward you, in [rad]
    
    Returns:
    a matrix object (note, not an array object) with the 4x4 transformation 
    matrix.
    """
    ca = cos(alpha)
    sa = sin(alpha)
    return N.matrix([[1, 0,	0,	0],
        [0, ca, -sa, 0],
        [0, sa, ca, 0],
        [0, 0, 0, 1]])

def rotate_y(alpha):
    """
    Generate a rotation matrix around the y axis.
    
    Arguments: 
    alpha - angle of rotation, counterclockwise when X points toward you, in [rad]
    
    Returns:
    a matrix object (note, not an array object) with the 4x4 transformation 
    matrix.
    """
    ca = cos(alpha)
    sa = sin(alpha)
    return N.matrix([[ca, 0,	sa,	0],
        [0, 1, 0, 0],
        [-sa, 0, ca, 0],
        [0, 0, 0, 1]])

def rotate_z(alpha):
    """
    Generate a rotation matrix around the z axis.
    
    Arguments: 
    alpha - angle of rotation, counterclockwise when X points toward you, in [rad]
    
    Returns:
    a matrix object (note, not an array object) with the 4x4 transformation 
    matrix.
    """
    ca = cos(alpha)
    sa = sin(alpha)
    return N.matrix([[ca, -sa,	0,	0],
        [sa, ca, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]])

def translate(x, y, z):
    """Homogenous transformation matrix representing a translation by x,y,z."""
    return N.mat("1 0 0 %f; 0 1 0 %f; 0 0 1 %f; 0 0 0 1" % (x, y, z))

def projection_in_vrc(viewpoint, points):
    """
    Calculates the projection of points relative to the xy plane.
    Arguments: 
    viewpoint - the coordinates of the view point in the View
        Reference Coordinates (VRC).
    points - the points to be projected, in VRC. Quaternions.
    
    Returns: the projected points (with z=0).
    """
    # We know how to do this when viewpoint = (0, 0, 0), so we'll move
    # everything accordingly:
    T = translate(viewpoint[0], viewpoint[1], viewpoint[2]);
    
    # Distance of the plane from the view is viewpoint[2], hence the basic
    # projection is:
    Pr = N.mat("""1 0 0 0;
          0 1 0 0;
          0 0 1 0;
          0 0 """ + str(-1./viewpoint[2]) + " 0 ")
     
    basic = Pr*T.I*points
    
    # Adjust sizes and translate back:
    proj = []
    for bs in basic.T:
        proj.append(T*bs.T/bs[0,2])
    
    return N.array(proj)

def get_plane(plane_name):
    """
    Returns a transformation matrix representing a frame where the requested
    plane is normal to the frame's Z axis. The frame is tailored for viewing
    an object graphically, maintaining the proper 'up', 'down', etc.
    
    Arguments:
    plane_name - one of the predefined names of planes, 'XY', 'YZ' and 'XZ'. any
        other name would give a plane for isometric view.
    """
    if plane_name == 'XY':
        return rotate_y(pi)*rotate_z(pi)
    if plane_name == 'YZ':
        return rotate_y(pi/2)*rotate_z(pi/2)*translate(0, 0, -40)
    if plane_name == 'XZ':
        return rotate_x(pi/2)*rotate_y(pi)
    # Else, isometric view:
    return rotate_z(pi/4)*rotate_y(pi)*rotate_x(-pi/3)*translate(0,0,-100)
