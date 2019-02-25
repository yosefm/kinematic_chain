# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cranesim_base.ui'
#
# Created: Thu Jun 18 12:00:52 2009
#      by: PyQt4 UI code generator 4.4.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CraneViewer(object):
    def setupUi(self, CraneViewer):
        CraneViewer.setObjectName("CraneViewer")
        CraneViewer.resize(517, 571)
        self.verticalLayout = QtGui.QVBoxLayout(CraneViewer)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(CraneViewer)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.theta1 = QtGui.QDoubleSpinBox(CraneViewer)
        self.theta1.setMinimum(-180.0)
        self.theta1.setMaximum(180.0)
        self.theta1.setObjectName("theta1")
        self.horizontalLayout.addWidget(self.theta1)
        self.label_2 = QtGui.QLabel(CraneViewer)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.d2 = QtGui.QDoubleSpinBox(CraneViewer)
        self.d2.setSingleStep(0.1)
        self.d2.setObjectName("d2")
        self.horizontalLayout.addWidget(self.d2)
        self.label_3 = QtGui.QLabel(CraneViewer)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.d3 = QtGui.QDoubleSpinBox(CraneViewer)
        self.d3.setSingleStep(0.1)
        self.d3.setObjectName("d3")
        self.horizontalLayout.addWidget(self.d3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtGui.QLabel(CraneViewer)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.sel_view = QtGui.QComboBox(CraneViewer)
        self.sel_view.setObjectName("sel_view")
        self.sel_view.addItem(QtCore.QString())
        self.sel_view.addItem(QtCore.QString())
        self.sel_view.addItem(QtCore.QString())
        self.sel_view.addItem(QtCore.QString())
        self.horizontalLayout_2.addWidget(self.sel_view)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.crane_view = QtGui.QGraphicsView(CraneViewer)
        self.crane_view.setObjectName("crane_view")
        self.verticalLayout.addWidget(self.crane_view)

        self.retranslateUi(CraneViewer)
        QtCore.QMetaObject.connectSlotsByName(CraneViewer)

    def retranslateUi(self, CraneViewer):
        CraneViewer.setWindowTitle(QtGui.QApplication.translate("CraneViewer", "Crane Simulator", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CraneViewer", "Rotation (degrees):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CraneViewer", "Carriage distance:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CraneViewer", "Hook extension", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CraneViewer", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.sel_view.setItemText(0, QtGui.QApplication.translate("CraneViewer", "Isometric", None, QtGui.QApplication.UnicodeUTF8))
        self.sel_view.setItemText(1, QtGui.QApplication.translate("CraneViewer", "XY", None, QtGui.QApplication.UnicodeUTF8))
        self.sel_view.setItemText(2, QtGui.QApplication.translate("CraneViewer", "YZ", None, QtGui.QApplication.UnicodeUTF8))
        self.sel_view.setItemText(3, QtGui.QApplication.translate("CraneViewer", "XZ", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    CraneViewer = QtGui.QWidget()
    ui = Ui_CraneViewer()
    ui.setupUi(CraneViewer)
    CraneViewer.show()
    sys.exit(app.exec_())

