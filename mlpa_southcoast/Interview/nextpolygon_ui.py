# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nextpolygon.ui'
#
# Created: Sat Jun 21 03:35:28 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_NextPolygon(object):
    def setupUi(self, NextPolygon):
        NextPolygon.setObjectName("NextPolygon")
        NextPolygon.resize(570,168)
        self.verticalLayout_2 = QtGui.QVBoxLayout(NextPolygon)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtGui.QWidget(NextPolygon)
        self.widget_2.setObjectName("widget_2")
        self.hboxlayout = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setObjectName("hboxlayout")
        self.label_1 = QtGui.QLabel(self.widget_2)
        self.label_1.setMinimumSize(QtCore.QSize(100,0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.hboxlayout.addWidget(self.label_1)
        self.line_1 = QtGui.QLineEdit(self.widget_2)
        self.line_1.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_1.setFont(font)
        self.line_1.setObjectName("line_1")
        self.hboxlayout.addWidget(self.line_1)
        self.verticalLayout.addWidget(self.widget_2)
        self.frame = QtGui.QFrame(NextPolygon)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.habitat_combo_label = QtGui.QLabel(self.frame)
        self.habitat_combo_label.setMinimumSize(QtCore.QSize(100,0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.habitat_combo_label.setFont(font)
        self.habitat_combo_label.setObjectName("habitat_combo_label")
        self.horizontalLayout.addWidget(self.habitat_combo_label)
        self.habitat_combo = QtGui.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.habitat_combo.setFont(font)
        self.habitat_combo.setObjectName("habitat_combo")
        self.habitat_combo.addItem("")
        self.horizontalLayout.addWidget(self.habitat_combo)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.widget = QtGui.QWidget(NextPolygon)
        self.widget.setObjectName("widget")
        self.hboxlayout1 = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.pbnShapeFinished = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnShapeFinished.setFont(font)
        self.pbnShapeFinished.setObjectName("pbnShapeFinished")
        self.hboxlayout1.addWidget(self.pbnShapeFinished)
        self.pbnShapeDiscard = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnShapeDiscard.setFont(font)
        self.pbnShapeDiscard.setObjectName("pbnShapeDiscard")
        self.hboxlayout1.addWidget(self.pbnShapeDiscard)
        self.pbnMoreShapes = QtGui.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnMoreShapes.setFont(font)
        self.pbnMoreShapes.setObjectName("pbnMoreShapes")
        self.hboxlayout1.addWidget(self.pbnMoreShapes)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(NextPolygon)
        QtCore.QMetaObject.connectSlotsByName(NextPolygon)

    def retranslateUi(self, NextPolygon):
        NextPolygon.setWindowTitle(QtGui.QApplication.translate("NextPolygon", "OpenOceanMap - Next Polygon", None, QtGui.QApplication.UnicodeUTF8))
        self.label_1.setText(QtGui.QApplication.translate("NextPolygon", "Weighting (Pennies)", None, QtGui.QApplication.UnicodeUTF8))
        self.habitat_combo_label.setText(QtGui.QApplication.translate("NextPolygon", "Habitat Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.habitat_combo.addItem(QtGui.QApplication.translate("NextPolygon", "Hard Bottom", None, QtGui.QApplication.UnicodeUTF8))
        self.habitat_combo.addItem(QtGui.QApplication.translate("NextPolygon", "New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.habitat_combo.addItem(QtGui.QApplication.translate("NextPolygon", "Soft/Sandy", None, QtGui.QApplication.UnicodeUTF8))
        self.habitat_combo.addItem(QtGui.QApplication.translate("NextPolygon", "Mixed", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnShapeFinished.setText(QtGui.QApplication.translate("NextPolygon", "Finished With Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnShapeDiscard.setText(QtGui.QApplication.translate("NextPolygon", "Discard Last Shape", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnMoreShapes.setText(QtGui.QApplication.translate("NextPolygon", "More Shapes This Fishery", None, QtGui.QApplication.UnicodeUTF8))

