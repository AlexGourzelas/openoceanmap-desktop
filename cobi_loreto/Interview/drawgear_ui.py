# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'drawgear.ui'
#
# Created: Mon Aug  4 16:27:26 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_DrawGear(object):
    def setupUi(self, DrawGear):
        DrawGear.setObjectName("DrawGear")
        DrawGear.resize(QtCore.QSize(QtCore.QRect(0,0,452,239).size()).expandedTo(DrawGear.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(DrawGear)
        self.vboxlayout.setObjectName("vboxlayout")

        self.widget_2 = QtGui.QWidget(DrawGear)
        self.widget_2.setObjectName("widget_2")

        self.hboxlayout = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout.setObjectName("hboxlayout")

        self.type_label = QtGui.QLabel(self.widget_2)
        self.type_label.setMinimumSize(QtCore.QSize(200,0))
        self.type_label.setMaximumSize(QtCore.QSize(500,16777215))

        font = QtGui.QFont()
        font.setPointSize(14)
        self.type_label.setFont(font)
        self.type_label.setObjectName("type_label")
        self.hboxlayout.addWidget(self.type_label)

        self.penny_label = QtGui.QLabel(self.widget_2)
        self.penny_label.setObjectName("penny_label")
        self.hboxlayout.addWidget(self.penny_label)

        self.line_1 = QtGui.QLineEdit(self.widget_2)
        self.line_1.setEnabled(True)
        self.line_1.setMaximumSize(QtCore.QSize(200,16777215))
        self.line_1.setObjectName("line_1")
        self.hboxlayout.addWidget(self.line_1)

        self.pl_label = QtGui.QLabel(self.widget_2)
        self.pl_label.setMinimumSize(QtCore.QSize(50,0))
        self.pl_label.setMaximumSize(QtCore.QSize(50,16777215))
        self.pl_label.setObjectName("pl_label")
        self.hboxlayout.addWidget(self.pl_label)
        self.vboxlayout.addWidget(self.widget_2)

        self.groupBox = QtGui.QGroupBox(DrawGear)
        self.groupBox.setObjectName("groupBox")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.groupBox)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.s5 = QtGui.QCheckBox(self.groupBox)
        self.s5.setObjectName("s5")
        self.vboxlayout1.addWidget(self.s5)

        self.s2 = QtGui.QCheckBox(self.groupBox)
        self.s2.setObjectName("s2")
        self.vboxlayout1.addWidget(self.s2)

        self.s3 = QtGui.QCheckBox(self.groupBox)
        self.s3.setObjectName("s3")
        self.vboxlayout1.addWidget(self.s3)
        self.hboxlayout1.addLayout(self.vboxlayout1)

        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.s4 = QtGui.QCheckBox(self.groupBox)
        self.s4.setObjectName("s4")
        self.vboxlayout2.addWidget(self.s4)

        self.s1 = QtGui.QCheckBox(self.groupBox)
        self.s1.setObjectName("s1")
        self.vboxlayout2.addWidget(self.s1)

        self.s6 = QtGui.QCheckBox(self.groupBox)
        self.s6.setObjectName("s6")
        self.vboxlayout2.addWidget(self.s6)
        self.hboxlayout1.addLayout(self.vboxlayout2)

        self.vboxlayout3 = QtGui.QVBoxLayout()
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.s7 = QtGui.QCheckBox(self.groupBox)
        self.s7.setObjectName("s7")
        self.vboxlayout3.addWidget(self.s7)

        spacerItem = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout3.addItem(spacerItem)
        self.hboxlayout1.addLayout(self.vboxlayout3)
        self.vboxlayout.addWidget(self.groupBox)

        self.widget = QtGui.QWidget(DrawGear)
        self.widget.setObjectName("widget")

        self.hboxlayout2 = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout2.setObjectName("hboxlayout2")

        spacerItem1 = QtGui.QSpacerItem(196,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem1)

        self.pbnShapeFinished = QtGui.QPushButton(self.widget)
        self.pbnShapeFinished.setObjectName("pbnShapeFinished")
        self.hboxlayout2.addWidget(self.pbnShapeFinished)

        self.pbnShapeDiscard = QtGui.QPushButton(self.widget)
        self.pbnShapeDiscard.setObjectName("pbnShapeDiscard")
        self.hboxlayout2.addWidget(self.pbnShapeDiscard)

        self.pbnMoreShapes = QtGui.QPushButton(self.widget)
        self.pbnMoreShapes.setObjectName("pbnMoreShapes")
        self.hboxlayout2.addWidget(self.pbnMoreShapes)
        self.vboxlayout.addWidget(self.widget)

        self.retranslateUi(DrawGear)
        QtCore.QMetaObject.connectSlotsByName(DrawGear)

    def retranslateUi(self, DrawGear):
        DrawGear.setWindowTitle(QtGui.QApplication.translate("DrawGear", "OpenOceanMap - Next Polygon", None, QtGui.QApplication.UnicodeUTF8))
        self.penny_label.setText(QtGui.QApplication.translate("DrawGear", "Weighting (pennies):", None, QtGui.QApplication.UnicodeUTF8))
        self.pl_label.setText(QtGui.QApplication.translate("DrawGear", "remaining", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DrawGear", "Check which types of species are caught in this area:", None, QtGui.QApplication.UnicodeUTF8))
        self.s5.setText(QtGui.QApplication.translate("DrawGear", "Benthic fish", None, QtGui.QApplication.UnicodeUTF8))
        self.s2.setText(QtGui.QApplication.translate("DrawGear", "Coastal reef fish", None, QtGui.QApplication.UnicodeUTF8))
        self.s3.setText(QtGui.QApplication.translate("DrawGear", "Deep reef fish", None, QtGui.QApplication.UnicodeUTF8))
        self.s4.setText(QtGui.QApplication.translate("DrawGear", "Migratory fish", None, QtGui.QApplication.UnicodeUTF8))
        self.s1.setText(QtGui.QApplication.translate("DrawGear", "Sharks and Skates", None, QtGui.QApplication.UnicodeUTF8))
        self.s6.setText(QtGui.QApplication.translate("DrawGear", "Shrimp", None, QtGui.QApplication.UnicodeUTF8))
        self.s7.setText(QtGui.QApplication.translate("DrawGear", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnShapeFinished.setText(QtGui.QApplication.translate("DrawGear", "Finished With Shapes", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnShapeDiscard.setText(QtGui.QApplication.translate("DrawGear", "Discard Last Shape...", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnMoreShapes.setText(QtGui.QApplication.translate("DrawGear", "Draw More Shapes...", None, QtGui.QApplication.UnicodeUTF8))

