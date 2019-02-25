import numpy as N

def topo_from_faces(faces):
    """
    Determines the body's topology, given its faces. 
    
    Arguments: 
    faces - a list of faces in the format described in visible_lines.m
    
    Returns: A column of topology pairs.
    """
    topo = set()
    for face in faces:
        # All faces are the same length. faces with less vertices are
        # padded with NaN, which we remove here:
        face = face[~N.isnan(face)].A[0]
        rotary = N.r_[face, face[0]]
        
        for ii in xrange(len(face)):
            new = (face[ii], rotary[ii+1])
            
            # Add the line to the topology if it's not there already.
            topo.add(new)
    
    return N.vstack([t for t in topo])
    
def visible_lines(geom, faces, viewpoint):
    """
    Select the visible lines of a body. A line is visible if it is on at
    least one visible face, i.e. a face whose normal vector is pointing
    no more than pi/2 radians away from the eye.
    
    Arguments: 
    geom - a column of the vertices making up the body.
    faces - a collum of faces. Each face represented as a row of vertices in an 
        order that is counterclockwise when looking from the face's normal to 
        the face.
    viewpoint - the point where the camera is located.
    
    Returns: a column of topology pairs (see body_from_topo() in cranesim.py)
    """
    
    visible_faces = [];
    geom = geom[:, :2]; # get rid of homogenous form.
    for face in faces:
        u = geom[face[1]] - geom[face[0]]
        v = geom[face[2]] - geom[face[1]]
        
        view_vect = viewpoint - geom[face[1]]
        if (N.dot(N.cross(u,v), view_vect) >= 0):
            visible_faces.append(face)
    
    return topo_from_faces(N.array(visible_faces))
