# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectfishery.ui'
#
# Created: Sat Jun 21 03:35:29 2008
#      by: PyQt4 UI code generator 4.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectFishery(object):
    def setupUi(self, SelectFishery):
        SelectFishery.setObjectName("SelectFishery")
        SelectFishery.resize(840,429)
        self.verticalLayout_5 = QtGui.QVBoxLayout(SelectFishery)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtGui.QWidget(SelectFishery)
        self.widget.setObjectName("widget")
        self.hboxlayout = QtGui.QHBoxLayout(self.widget)
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(9)
        self.hboxlayout.setObjectName("hboxlayout")
        self.fishery_text = QtGui.QLabel(self.widget)
        self.fishery_text.setObjectName("fishery_text")
        self.hboxlayout.addWidget(self.fishery_text)
        self.fishery_comboBox = QtGui.QComboBox(self.widget)
        self.fishery_comboBox.setObjectName("fishery_comboBox")
        self.fishery_comboBox.addItem("")
        self.hboxlayout.addWidget(self.fishery_comboBox)
        self.horizontalLayout_3.addWidget(self.widget)
        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.groupBox = QtGui.QGroupBox(SelectFishery)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtGui.QFrame(self.groupBox)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.p1 = QtGui.QCheckBox(self.frame)
        self.p1.setObjectName("p1")
        self.verticalLayout.addWidget(self.p1)
        self.p2 = QtGui.QCheckBox(self.frame)
        self.p2.setObjectName("p2")
        self.verticalLayout.addWidget(self.p2)
        self.p3 = QtGui.QCheckBox(self.frame)
        self.p3.setObjectName("p3")
        self.verticalLayout.addWidget(self.p3)
        self.p4 = QtGui.QCheckBox(self.frame)
        self.p4.setObjectName("p4")
        self.verticalLayout.addWidget(self.p4)
        self.p5 = QtGui.QCheckBox(self.frame)
        self.p5.setObjectName("p5")
        self.verticalLayout.addWidget(self.p5)
        self.p6 = QtGui.QCheckBox(self.frame)
        self.p6.setObjectName("p6")
        self.verticalLayout.addWidget(self.p6)
        self.p7 = QtGui.QCheckBox(self.frame)
        self.p7.setObjectName("p7")
        self.verticalLayout.addWidget(self.p7)
        self.p8 = QtGui.QCheckBox(self.frame)
        self.p8.setObjectName("p8")
        self.verticalLayout.addWidget(self.p8)
        self.p9 = QtGui.QCheckBox(self.frame)
        self.p9.setObjectName("p9")
        self.verticalLayout.addWidget(self.p9)
        self.p10 = QtGui.QCheckBox(self.frame)
        self.p10.setObjectName("p10")
        self.verticalLayout.addWidget(self.p10)
        self.p11 = QtGui.QCheckBox(self.frame)
        self.p11.setObjectName("p11")
        self.verticalLayout.addWidget(self.p11)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_3 = QtGui.QFrame(self.groupBox)
        self.frame_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.p12 = QtGui.QCheckBox(self.frame_3)
        self.p12.setObjectName("p12")
        self.verticalLayout_2.addWidget(self.p12)
        self.p13 = QtGui.QCheckBox(self.frame_3)
        self.p13.setObjectName("p13")
        self.verticalLayout_2.addWidget(self.p13)
        self.p14 = QtGui.QCheckBox(self.frame_3)
        self.p14.setObjectName("p14")
        self.verticalLayout_2.addWidget(self.p14)
        self.p15 = QtGui.QCheckBox(self.frame_3)
        self.p15.setObjectName("p15")
        self.verticalLayout_2.addWidget(self.p15)
        self.p16 = QtGui.QCheckBox(self.frame_3)
        self.p16.setObjectName("p16")
        self.verticalLayout_2.addWidget(self.p16)
        self.p17 = QtGui.QCheckBox(self.frame_3)
        self.p17.setObjectName("p17")
        self.verticalLayout_2.addWidget(self.p17)
        self.p18 = QtGui.QCheckBox(self.frame_3)
        self.p18.setObjectName("p18")
        self.verticalLayout_2.addWidget(self.p18)
        self.p19 = QtGui.QCheckBox(self.frame_3)
        self.p19.setObjectName("p19")
        self.verticalLayout_2.addWidget(self.p19)
        self.p20 = QtGui.QCheckBox(self.frame_3)
        self.p20.setObjectName("p20")
        self.verticalLayout_2.addWidget(self.p20)
        self.p21 = QtGui.QCheckBox(self.frame_3)
        self.p21.setObjectName("p21")
        self.verticalLayout_2.addWidget(self.p21)
        self.p22 = QtGui.QCheckBox(self.frame_3)
        self.p22.setObjectName("p22")
        self.verticalLayout_2.addWidget(self.p22)
        self.horizontalLayout.addWidget(self.frame_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_2 = QtGui.QFrame(self.groupBox)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.p23 = QtGui.QCheckBox(self.frame_2)
        self.p23.setObjectName("p23")
        self.verticalLayout_3.addWidget(self.p23)
        self.p24 = QtGui.QCheckBox(self.frame_2)
        self.p24.setObjectName("p24")
        self.verticalLayout_3.addWidget(self.p24)
        self.p25 = QtGui.QCheckBox(self.frame_2)
        self.p25.setObjectName("p25")
        self.verticalLayout_3.addWidget(self.p25)
        self.p26 = QtGui.QCheckBox(self.frame_2)
        self.p26.setObjectName("p26")
        self.verticalLayout_3.addWidget(self.p26)
        self.p27 = QtGui.QCheckBox(self.frame_2)
        self.p27.setObjectName("p27")
        self.verticalLayout_3.addWidget(self.p27)
        self.p28 = QtGui.QCheckBox(self.frame_2)
        self.p28.setObjectName("p28")
        self.verticalLayout_3.addWidget(self.p28)
        self.p29 = QtGui.QCheckBox(self.frame_2)
        self.p29.setObjectName("p29")
        self.verticalLayout_3.addWidget(self.p29)
        self.verticalLayout_4.addWidget(self.frame_2)
        spacerItem1 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtGui.QWidget(SelectFishery)
        self.widget_2.setObjectName("widget_2")
        self.hboxlayout1 = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setMargin(9)
        self.hboxlayout1.setObjectName("hboxlayout1")
        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem2)
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
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Lobster (Trap)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Squid (Seine)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Coastal Pelagics (Seine)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Urchin (Diving)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Spot Prawn (Trap)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Nearshore Rockfish (Hook-Line)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "NearshoreRockfish (Trap)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Deeper Nearshore Rockfish (Hook-Line)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Deeper Nearshore Rockfish (Trap)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "California Halibut (Hook-Line)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "California Halibut (Gillnet)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Rock Crab (Trap)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Shark-Swordfish (Hook-Line)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Shark-Swordfish (Gillnet)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Sea Cucumber (Diving)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Tuna (Hook-Line)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "Thornyhead (Hook-Line)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "White Seabass (Hook-Line)", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.addItem(QtGui.QApplication.translate("SelectFishery", "White Seabass (Gillnet)", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("SelectFishery", "Select Permits for this fishery:", None, QtGui.QApplication.UnicodeUTF8))
        self.p1.setText(QtGui.QApplication.translate("SelectFishery", "Deeper Nearshore Species Permit", None, QtGui.QApplication.UnicodeUTF8))
        self.p2.setText(QtGui.QApplication.translate("SelectFishery", "Drift Gillnet Sharks - Swordfish Permit", None, QtGui.QApplication.UnicodeUTF8))
        self.p3.setText(QtGui.QApplication.translate("SelectFishery", "Dungeness Crab Vessel (Nonresident)", None, QtGui.QApplication.UnicodeUTF8))
        self.p4.setText(QtGui.QApplication.translate("SelectFishery", "Dungeness Crab Vessel (Resident)", None, QtGui.QApplication.UnicodeUTF8))
        self.p5.setText(QtGui.QApplication.translate("SelectFishery", "Federal (HMS) Permit - Thresher Shark", None, QtGui.QApplication.UnicodeUTF8))
        self.p6.setText(QtGui.QApplication.translate("SelectFishery", "Federal Coastal Pelagic Species Permit", None, QtGui.QApplication.UnicodeUTF8))
        self.p7.setText(QtGui.QApplication.translate("SelectFishery", "Federal Limited Entry Fixed Gear Permit", None, QtGui.QApplication.UnicodeUTF8))
        self.p8.setText(QtGui.QApplication.translate("SelectFishery", "Federal Limited Entry Trap Permit", None, QtGui.QApplication.UnicodeUTF8))
        self.p9.setText(QtGui.QApplication.translate("SelectFishery", "Gill/Trammel Net Permit", None, QtGui.QApplication.UnicodeUTF8))
        self.p10.setText(QtGui.QApplication.translate("SelectFishery", "Herring Gillnet (Nonresident)", None, QtGui.QApplication.UnicodeUTF8))
        self.p11.setText(QtGui.QApplication.translate("SelectFishery", "Herring Gillnet (Resident)", None, QtGui.QApplication.UnicodeUTF8))
        self.p12.setText(QtGui.QApplication.translate("SelectFishery", "Market Squid Brail Permit (Nontransferable)", None, QtGui.QApplication.UnicodeUTF8))
        self.p13.setText(QtGui.QApplication.translate("SelectFishery", "Market Squid Brail Permit (Transferable)", None, QtGui.QApplication.UnicodeUTF8))
        self.p14.setText(QtGui.QApplication.translate("SelectFishery", "Market Squid Light Boat Owner", None, QtGui.QApplication.UnicodeUTF8))
        self.p15.setText(QtGui.QApplication.translate("SelectFishery", "Market Squid Light Boat Permit (Nontransferable)", None, QtGui.QApplication.UnicodeUTF8))
        self.p16.setText(QtGui.QApplication.translate("SelectFishery", "Market Squid Vessel (Nontransferable)", None, QtGui.QApplication.UnicodeUTF8))
        self.p17.setText(QtGui.QApplication.translate("SelectFishery", "Market Squid Vessel (Transferable)", None, QtGui.QApplication.UnicodeUTF8))
        self.p18.setText(QtGui.QApplication.translate("SelectFishery", "Nearshore Fishery Bycatch", None, QtGui.QApplication.UnicodeUTF8))
        self.p19.setText(QtGui.QApplication.translate("SelectFishery", "Nearshore Fishery Bycatch (Nontransferable)", None, QtGui.QApplication.UnicodeUTF8))
        self.p20.setText(QtGui.QApplication.translate("SelectFishery", "Nearshore Fishery Permit", None, QtGui.QApplication.UnicodeUTF8))
        self.p21.setText(QtGui.QApplication.translate("SelectFishery", "Nearshore Fishery Permit - North Coast", None, QtGui.QApplication.UnicodeUTF8))
        self.p22.setText(QtGui.QApplication.translate("SelectFishery", "Nearshore Fishery Permit - North-Central Coast", None, QtGui.QApplication.UnicodeUTF8))
        self.p23.setText(QtGui.QApplication.translate("SelectFishery", "Nearshore Fishery Permit - South Coast", None, QtGui.QApplication.UnicodeUTF8))
        self.p24.setText(QtGui.QApplication.translate("SelectFishery", "Nearshore Fishery Permit - South-Central Coast", None, QtGui.QApplication.UnicodeUTF8))
        self.p25.setText(QtGui.QApplication.translate("SelectFishery", "Nearshore Fishery Trap Endorsement", None, QtGui.QApplication.UnicodeUTF8))
        self.p26.setText(QtGui.QApplication.translate("SelectFishery", "Open Access", None, QtGui.QApplication.UnicodeUTF8))
        self.p27.setText(QtGui.QApplication.translate("SelectFishery", "Salmon Enhancement Stamp", None, QtGui.QApplication.UnicodeUTF8))
        self.p28.setText(QtGui.QApplication.translate("SelectFishery", "Salmon Vessel Permit", None, QtGui.QApplication.UnicodeUTF8))
        self.p29.setText(QtGui.QApplication.translate("SelectFishery", "Sea Urchin Diving Permit", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFisheryFinished.setText(QtGui.QApplication.translate("SelectFishery", "Finished With Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnStartShapes.setText(QtGui.QApplication.translate("SelectFishery", "Start Drawing Shapes", None, QtGui.QApplication.UnicodeUTF8))

