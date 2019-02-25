import numpy as N

class Link(object):
    """
    Holds the geometry and topology (vertices and lines) describing the link 
    visually, as well as the frame stating how the link axes are changed 
    relative to the earlier link. 
    
    The non-constant change from previous link is represented externally to the 
    link using the Denavitt-Hartenberg (DH) method. For this the link holds the
    type of connection with the previous one - either revolute or prizmatic 
    (sliding).
    """
    def __init__(self, frame, geometry, faces, is_revolute):
        self._frame = N.mat(frame, dtype=N.float)
        self._geometry = N.mat(geometry, dtype=N.float)
        self._faces = N.mat(faces - 1) # Indexes adjusted to Python indexing
        self._rev = is_revolute
    
    # Accessors:
    def is_revolute(self):
        return self._rev
    
    def get_frame(self):
        return self._frame
    
    def get_geometry(self):
        return self._geometry
    
    def get_faces(self):
        return self._faces

class Connector(object):
    """Not yet used for anything"""
    def __init__(self, state, geometry, topology):
        self._state = N.array(state, dtype=N.float)
        self._geom = N.mat(geometry, dtype=N.float)
        self._topo = N.mat(topology)

class KinematicChain(object):
    """
    Holds a series of links in the order they are connected, as well as their DH
    vector, representing the variable state.
    """
    def __init__(self, links, state, connectors):
        self._links = links
        self._state = N.array(state, dtype=N.float).flatten()
        self._conns = connectors
    
    def get_links(self):
        return self._links
    
    def get_state(self):
        return self._state
    
    def set_state_of_link(self, link_idx, new_state):
        self._state[link_idx] = new_state
    
