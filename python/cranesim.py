
from PyQt4 import QtCore, QtGui
from cranesim_base import Ui_CraneViewer

import kinematic_chain as KC
import spatial_reps as SP
import object_reps
import scipy.io
import numpy as N

class CraneViewer(QtGui.QWidget, Ui_CraneViewer):
    """
    Implements a main window showing a crane which can rotate about its axis, 
    and move the cart and hook.
    
    Loads the crane geometry from a specially structured Matlab file that was 
    carried over fron the "good old days".
    
    The geometric work-horse is show_kinematic_chain(), and the connection to
    crane variables is through redraw_crane()
    """
    def __init__(self, crane_file='../crane.mat', parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(parent)
        self._crane = self.load_crane(crane_file)
        self.crane_view.setTransform(QtGui.QTransform(1, 0, 0, -1, 0, 0))
        
        # Interactions with GUI controls:
        QtCore.QObject.connect(self.sel_view, \
            QtCore.SIGNAL("currentIndexChanged(int)"), self.redraw_crane)
        QtCore.QObject.connect(self.theta1, \
            QtCore.SIGNAL("valueChanged(double)"), self.change_crane_rot)
        QtCore.QObject.connect(self.d2, \
            QtCore.SIGNAL("valueChanged(double)"), self.change_cart_pos)
        QtCore.QObject.connect(self.d3, \
            QtCore.SIGNAL("valueChanged(double)"), self.change_hook_extension)
        
    def load_crane(self, crane_file):
        """
        Converts a mat-file representation of a crane to a proper KinematicChain
        object and sub-objects.
        
        Arguments: the mat-file name
        Returns: a KinematicChain object with all links etc. in place.
        """
        mat_structure = scipy.io.loadmat(crane_file)
        links = []
        for link in mat_structure['crane']['links'][0,0]:
            links.append(KC.Link(link['frame'][0], link['geometry'][0], link['faces'][0], link['is_revolute'][0]))

        connectors = []
        for cn in mat_structure['crane']['connectors'][0,0]:
            connectors.append(KC.Connector(cn['state'][0], cn['geometry'][0], cn['topo'][0]))
        
        return KC.KinematicChain(links, mat_structure['crane']['state'][0,0], connectors)
    
    def show_kinematic_chain(self, geom_maker=lambda points: points.T):
        """
        Goes over each link in the chain, calculates its transformation relative
        to the global coordinates (using the accumulated transformation and the 
        link's oun transformation), and draws the transformed link.
        
        Arguments:
        geom_maker - a function that transforms the points from the global 
            coordinates to camera coordinates. Takes a row of points and returns
            a column of points.
        """
        scene = QtGui.QGraphicsScene()
        
        links = self._crane.get_links()
        moving_frame = links[0].get_frame().copy()
        state = self._crane.get_state().tolist() # To be used as a stack
        # Save some data for the connectors (not yet implemented):
        frames = [moving_frame]
        
        # Draw first link:
        points = moving_frame*links[0].get_geometry()
        self.body_from_topo(geom_maker(points), object_reps.topo_from_faces(links[0].get_faces()), scene)
        
        # Following links:
        for link in links[1:]:
            # Generate a transformation representing the position of the link:
            if link.is_revolute():
                # Link rotates around the Z axis:
                moving_frame *= SP.rotate_z(state[0])
            else:
                # Link moves along the Z axis:
                moving_frame *= SP.translate(0, 0, state[0])
            moving_frame *= link.get_frame()
            
            frames.append(moving_frame)
            state.pop(0)
            
            # Draw link:
            points = moving_frame*link.get_geometry()
            self.body_from_topo(geom_maker(points), \
                object_reps.topo_from_faces(link.get_faces()), scene)
        
        # Finalize by fitting the result in the view.
        self.crane_view.setScene(scene)
        self.crane_view.fitInView(scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)
        self._scene = scene # Otherwise it is destroyed, go figure.
        
    def redraw_crane(self):
        """
        Create the correct camera and view plane, then call draw.
        """
        self._eye = N.r_[0., 0, -100]
        plane = SP.get_plane(self.sel_view.currentText())
        geom_maker = lambda points: SP.projection_in_vrc(self._eye, plane.I*points)
        self.show_kinematic_chain(geom_maker)
        
    def body_from_topo(self, geom, topo, scene, colour='b'):
        """
        Draws a given body in the graphics scene, as a parallel projection on the xy plane.
        
        Arguments: 
        geom - a column of points belonging to the body.
        topo - a column of indices pairs defining pairs of points to connect 
            with a line. The indices point to elements of geom. For example, 
            [3, 6] will connect the 4th point in geom to the seventh (and vice 
            versa).
        scene - a QGraphicsScene object that will hold the new lines.
        """
        for t in topo:
            t = N.int_(t)
            scene.addLine(geom[t[0], 0], geom[t[0], 1], geom[t[1], 0], geom[t[1], 1])
    
    # The following 3 just access the crane's corresponding state variables 
    # separately.
    def change_crane_rot(self, new_rot):
        self._crane.set_state_of_link(0, new_rot*N.pi/180)
        self.redraw_crane()
    
    def change_cart_pos(self, new_pos):
        self._crane.set_state_of_link(1, new_pos)
        self.redraw_crane()
    
    def change_hook_extension(self, new_ext):
        self._crane.set_state_of_link(2, new_ext)
        self.redraw_crane()
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    window = QtGui.QWidget()
    ui = CraneViewer(parent=window)
    window.show()
    ui.redraw_crane()
    sys.exit(app.exec_())
