# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drawecotourism.ui'
#
# Created: Sat Apr 04 22:57:29 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DrawEcotourism(object):
    def setupUi(self, DrawEcotourism):
        DrawEcotourism.setObjectName("DrawEcotourism")
        DrawEcotourism.resize(581, 148)
        self.gridlayout = QtGui.QGridLayout(DrawEcotourism)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.widget_2 = QtGui.QWidget(DrawEcotourism)
        self.widget_2.setObjectName("widget_2")
        self.vboxlayout = QtGui.QVBoxLayout(self.widget_2)
        self.vboxlayout.setObjectName("vboxlayout")
        self.type_label = QtGui.QLabel(self.widget_2)
        self.type_label.setMinimumSize(QtCore.QSize(5, 0))
        self.type_label.setMaximumSize(QtCore.QSize(450, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.type_label.setFont(font)
        self.type_label.setAlignment(QtCore.Qt.AlignCenter)
        self.type_label.setObjectName("type_label")
        self.vboxlayout.addWidget(self.type_label)
        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.penny_label = QtGui.QLabel(self.widget_2)
        self.penny_label.setObjectName("penny_label")
        self.hboxlayout.addWidget(self.penny_label)
        self.line_1 = QtGui.QLineEdit(self.widget_2)
        self.line_1.setEnabled(True)
        self.line_1.setMaximumSize(QtCore.QSize(150, 16777215))
        self.line_1.setObjectName("line_1")
        self.hboxlayout.addWidget(self.line_1)
        self.pl_label = QtGui.QLabel(self.widget_2)
        self.pl_label.setMinimumSize(QtCore.QSize(200, 0))
        self.pl_label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.pl_label.setObjectName("pl_label")
        self.hboxlayout.addWidget(self.pl_label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)
        self.vboxlayout.addLayout(self.hboxlayout)
        self.gridlayout.addWidget(self.widget_2, 0, 0, 1, 1)
        self.widget = QtGui.QWidget(DrawEcotourism)
        self.widget.setObjectName("widget")
        self.hboxlayout1 = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout1.setObjectName("hboxlayout1")
        spacerItem1 = QtGui.QSpacerItem(106, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.pbnShapeFinished = QtGui.QPushButton(self.widget)
        self.pbnShapeFinished.setObjectName("pbnShapeFinished")
        self.hboxlayout1.addWidget(self.pbnShapeFinished)
        self.pbnShapeDiscard = QtGui.QPushButton(self.widget)
        self.pbnShapeDiscard.setObjectName("pbnShapeDiscard")
        self.hboxlayout1.addWidget(self.pbnShapeDiscard)
        self.pbnMoreShapes = QtGui.QPushButton(self.widget)
        self.pbnMoreShapes.setObjectName("pbnMoreShapes")
        self.hboxlayout1.addWidget(self.pbnMoreShapes)
        self.gridlayout.addWidget(self.widget, 1, 0, 2, 1)

        self.retranslateUi(DrawEcotourism)
        QtCore.QMetaObject.connectSlotsByName(DrawEcotourism)

    def retranslateUi(self, DrawEcotourism):
        DrawEcotourism.setWindowTitle(QtGui.QApplication.translate("DrawEcotourism", "OpenOceanMap - Next Polygon", None, QtGui.QApplication.UnicodeUTF8))
        self.type_label.setText(QtGui.QApplication.translate("DrawEcotourism", "Type of ecotourism", None, QtGui.QApplication.UnicodeUTF8))
        self.penny_label.setText(QtGui.QApplication.translate("DrawEcotourism", "Weighting (pennies):", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnShapeFinished.setText(QtGui.QApplication.translate("DrawEcotourism", "Finished With Shapes", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnShapeDiscard.setText(QtGui.QApplication.translate("DrawEcotourism", "Discard Last Shape", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnMoreShapes.setText(QtGui.QApplication.translate("DrawEcotourism", "Draw More Shapes...", None, QtGui.QApplication.UnicodeUTF8))

