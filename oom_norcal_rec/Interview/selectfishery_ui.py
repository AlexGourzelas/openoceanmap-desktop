# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectfishery.ui'
#
# Created: Mon Mar 09 15:04:47 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectFishery(object):
    def setupUi(self, SelectFishery):
        SelectFishery.setObjectName("SelectFishery")
        SelectFishery.resize(459, 121)
        self.verticalLayout_5 = QtGui.QVBoxLayout(SelectFishery)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtGui.QWidget(SelectFishery)
        self.widget.setObjectName("widget")
        self.hboxlayout = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setContentsMargins(9, 9, 9, 0)
        self.hboxlayout.setObjectName("hboxlayout")
        self.fishery_text = QtGui.QLabel(self.widget)
        self.fishery_text.setMinimumSize(QtCore.QSize(160, 0))
        self.fishery_text.setMaximumSize(QtCore.QSize(160, 16777215))
        self.fishery_text.setObjectName("fishery_text")
        self.hboxlayout.addWidget(self.fishery_text)
        self.fishery_comboBox = QtGui.QComboBox(self.widget)
        self.fishery_comboBox.setObjectName("fishery_comboBox")
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.hboxlayout.addWidget(self.fishery_comboBox)
        self.horizontalLayout_3.addWidget(self.widget)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtGui.QWidget(SelectFishery)
        self.widget_2.setObjectName("widget_2")
        self.hboxlayout1 = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setMargin(9)
        self.hboxlayout1.setObjectName("hboxlayout1")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem1)
        self.pbnFisheryFinished = QtGui.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnFisheryFinished.setFont(font)
        self.pbnFisheryFinished.setObjectName("pbnFisheryFinished")
        self.hboxlayout1.addWidget(self.pbnFisheryFinished)
        self.pbnStartShapes = QtGui.QPushButton(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnStartShapes.setFont(font)
        self.pbnStartShapes.setObjectName("pbnStartShapes")
        self.hboxlayout1.addWidget(self.pbnStartShapes)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SelectFishery)
        QtCore.QMetaObject.connectSlotsByName(SelectFishery)

    def retranslateUi(self, SelectFishery):
        SelectFishery.setWindowTitle(QtGui.QApplication.translate("SelectFishery", "OpenOceanMap - Select Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_text.setText(QtGui.QApplication.translate("SelectFishery", "Select Fishery :", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(0, QtGui.QApplication.translate("SelectFishery", "Dungeness Crab", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(1, QtGui.QApplication.translate("SelectFishery", "Groundfish / Bottom Fishing", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(2, QtGui.QApplication.translate("SelectFishery", "Halibut", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(3, QtGui.QApplication.translate("SelectFishery", "Salmon", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(4, QtGui.QApplication.translate("SelectFishery", "Tuna", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFisheryFinished.setText(QtGui.QApplication.translate("SelectFishery", "Finished With Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnStartShapes.setText(QtGui.QApplication.translate("SelectFishery", "Start Drawing Shapes", None, QtGui.QApplication.UnicodeUTF8))

