# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Mar 10 11:44:49 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/OCEAN_SMALL_INNO.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName("gridlayout")
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.toolBox = QtGui.QToolBox(self.splitter)
        self.toolBox.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setBaseSize(QtCore.QSize(0, 0))
        self.toolBox.setObjectName("toolBox")
        self.legend_page = QtGui.QWidget()
        self.legend_page.setGeometry(QtCore.QRect(0, 0, 366, 586))
        self.legend_page.setObjectName("legend_page")
        self.gridlayout1 = QtGui.QGridLayout(self.legend_page)
        self.gridlayout1.setMargin(9)
        self.gridlayout1.setSpacing(6)
        self.gridlayout1.setObjectName("gridlayout1")
        self.groupBox = QtGui.QGroupBox(self.legend_page)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.gridlayout1.addWidget(self.groupBox, 0, 0, 1, 1)
        self.toolBox.addItem(self.legend_page, "")
        self.debug_page = QtGui.QWidget()
        self.debug_page.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.debug_page.setObjectName("debug_page")
        self.toolBox.addItem(self.debug_page, "")
        self.frameMap = QtGui.QFrame(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frameMap.sizePolicy().hasHeightForWidth())
        self.frameMap.setSizePolicy(sizePolicy)
        self.frameMap.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameMap.setFrameShadow(QtGui.QFrame.Raised)
        self.frameMap.setObjectName("frameMap")
        self.gridlayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        self.menuInterview = QtGui.QMenu(self.menubar)
        self.menuInterview.setObjectName("menuInterview")
        self.menuMap = QtGui.QMenu(self.menubar)
        self.menuMap.setObjectName("menuMap")
        self.menuUtilities = QtGui.QMenu(self.menubar)
        self.menuUtilities.setObjectName("menuUtilities")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.mpActionZoomOut = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/mActionZoomOut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mpActionZoomOut.setIcon(icon1)
        self.mpActionZoomOut.setObjectName("mpActionZoomOut")
        self.mpActionPan = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/mActionPan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mpActionPan.setIcon(icon2)
        self.mpActionPan.setObjectName("mpActionPan")
        self.mpActionAddRasterLayer = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/mActionAddRasterLayer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mpActionAddRasterLayer.setIcon(icon3)
        self.mpActionAddRasterLayer.setObjectName("mpActionAddRasterLayer")
        self.actionStart_Interview = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/mActionStartEditing.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStart_Interview.setIcon(icon4)
        self.actionStart_Interview.setObjectName("actionStart_Interview")
        self.actionRegion_Tool = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/images/mActionMeasureArea.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRegion_Tool.setIcon(icon5)
        self.actionRegion_Tool.setObjectName("actionRegion_Tool")
        self.actionPolygon_Tool = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/images/mActionCapturePolygon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPolygon_Tool.setIcon(icon6)
        self.actionPolygon_Tool.setObjectName("actionPolygon_Tool")
        self.mpActionZoomIn = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/images/mActionZoomIn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mpActionZoomIn.setIcon(icon7)
        self.mpActionZoomIn.setObjectName("mpActionZoomIn")
        self.mpActionAddVectorLayer = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/images/mActionAddLayer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mpActionAddVectorLayer.setIcon(icon8)
        self.mpActionAddVectorLayer.setObjectName("mpActionAddVectorLayer")
        self.actionPython_Console = QtGui.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/images/mIconProperties.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPython_Console.setIcon(icon9)
        self.actionPython_Console.setObjectName("actionPython_Console")
        self.menuInterview.addAction(self.actionStart_Interview)
        self.menuMap.addAction(self.mpActionAddRasterLayer)
        self.menuMap.addAction(self.mpActionAddVectorLayer)
        self.menuMap.addSeparator()
        self.menuMap.addAction(self.mpActionZoomIn)
        self.menuMap.addAction(self.mpActionZoomOut)
        self.menuMap.addAction(self.mpActionPan)
        self.menuMap.addAction(self.actionRegion_Tool)
        self.menuUtilities.addAction(self.actionPython_Console)
        self.menubar.addAction(self.menuMap.menuAction())
        self.menubar.addAction(self.menuInterview.menuAction())
        self.menubar.addAction(self.menuUtilities.menuAction())

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "OpenOceanMap SOORC Comm.", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.legend_page), QtGui.QApplication.translate("MainWindow", "Legend", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.debug_page), QtGui.QApplication.translate("MainWindow", "Debug", None, QtGui.QApplication.UnicodeUTF8))
        self.menuInterview.setTitle(QtGui.QApplication.translate("MainWindow", "Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.menuMap.setTitle(QtGui.QApplication.translate("MainWindow", "Map", None, QtGui.QApplication.UnicodeUTF8))
        self.menuUtilities.setTitle(QtGui.QApplication.translate("MainWindow", "Utilities", None, QtGui.QApplication.UnicodeUTF8))
        self.mpActionZoomOut.setText(QtGui.QApplication.translate("MainWindow", "Zoom Out", None, QtGui.QApplication.UnicodeUTF8))
        self.mpActionPan.setText(QtGui.QApplication.translate("MainWindow", "Pan", None, QtGui.QApplication.UnicodeUTF8))
        self.mpActionAddRasterLayer.setText(QtGui.QApplication.translate("MainWindow", "Add Raster Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart_Interview.setText(QtGui.QApplication.translate("MainWindow", "Start Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart_Interview.setIconText(QtGui.QApplication.translate("MainWindow", "Start Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStart_Interview.setToolTip(QtGui.QApplication.translate("MainWindow", "Start Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRegion_Tool.setText(QtGui.QApplication.translate("MainWindow", "Region Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPolygon_Tool.setText(QtGui.QApplication.translate("MainWindow", "Polygon Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.mpActionZoomIn.setText(QtGui.QApplication.translate("MainWindow", "Zoom In", None, QtGui.QApplication.UnicodeUTF8))
        self.mpActionAddVectorLayer.setText(QtGui.QApplication.translate("MainWindow", "Add Vector Layer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPython_Console.setText(QtGui.QApplication.translate("MainWindow", "Python Console", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
