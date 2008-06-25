#---------------------------------------------------------------------
# 
# OpenOceanMap - An Open Source GIS tool for performing interviews
# to obtain socio-economic data using spatial information.
# 
# Copyright (C) 2007  Ecotrust
# Copyright (C) 2007  Aaron Racicot
# 
#---------------------------------------------------------------------
# 
# licensed under the terms of GNU GPL 2
# 
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
# 
#---------------------------------------------------------------------


# PyQt4 includes for python bindings to QT
from PyQt4.QtCore import *
from PyQt4.QtGui import *
# QGIS bindings for mapping functions
from qgis.core import *
from qgis.gui import *
# Custom Tools
from Tools.polygontool import *


# UI specific includes
from selectfishery_ui import Ui_SelectFishery
from nextpolygon_ui import Ui_NextPolygon

from Util.common_functions import *

# General system includes
import sys

class SelectFisheryGui(QDialog, Ui_SelectFishery):
    def __init__(self, parent, flags):
        QDialog.__init__(self, parent.mainwindow, flags)
        self.setupUi(self)
        self.parent = parent

    def on_pbnStartShapes_released(self):
        #Get fishery value
        cur_fishery = self.fishery_comboBox.currentText()
        if not cur_fishery:
            QMessageBox.warning(self, "Fishery Error", "Please select a fishery")
            return 
        else:
            self.parent.currentFishery = cur_fishery
            
        self.close()
        mc = self.parent.canvas      
        self.p = PolygonTool(mc,self.parent)
        QObject.connect(self.p.o, SIGNAL("finished()"), self.nextPolygon)
        self.saveTool = mc.mapTool()
        mc.setMapTool(self.p)
            
    def on_pbnFisheryFinished_released(self):
        self.parent.pennies_left = 100; 
        self.close()
        capture_string = QString("Finished with fishery interview...")
        self.parent.parent.statusbar.showMessage(capture_string)
        
        # add some features# add some features
        for capPolyRub in self.parent.capturedPolygonsRub:
            capPolyRub.reset()
        #self.parent.parent.interviewInProgress = False
        #self.parent.parent.interviewSaveTool = None
        self.parent.currentCommFish = False
        self.parent.currentCommSport = False
        self.parent.currentPrivateFish = False

        if self.parent.currentEcotourism:
            from ecotourism import EcotourismWindowGui
            flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
            wnd = EcotourismWindowGui(self.parent,flags)
            wnd.show()    

        #self.parent.currentConsScience = False
        #self.parent.currentOther = False
        self.parent.canvas.setMapTool(self.parent.parent.toolZoomIn)

    def on_pbnGearFinished_released(self):
        self.parent.pennies_left = 100;
        self.close()
        capture_string = QString("Finished with gear types...")
        self.parent.parent.statusbar.showMessage(capture_string)

        from fisherswindow import FishersWindowGui
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = FishersWindowGui(self.parent,flags)
        wnd.show()

        # add some features
        for capPolyRub in self.parent.capturedPolygonsRub:
            capPolyRub.reset()
        self.parent.canvas.setMapTool(self.parent.parent.toolZoomIn)

    def nextPolygon(self):
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = NextPolygonGui(self.parent,flags,self.parent.pennies_left)
        wnd.show()

class NextPolygonGui(QDialog, Ui_NextPolygon):
    def __init__(self, parent, flags, pennies_left):
        QDialog.__init__(self, parent.mainwindow, flags)
        self.setupUi(self)
        self.parent = parent
        self.discardLast = False
        self.pennies_left = pennies_left
        self.pl_label.setText("  "+str(self.pennies_left)+" left")
        if pennies_left == 0:
            self.pbnMoreShapes.setDisabled(True)

    #Called when "More Shapes this fishery" button pressed        
    def on_pbnMoreShapes_released(self):
        if not self.discardLast:
            num_pennies = self.line_1.text()
            if not num_pennies:
                QMessageBox.warning(self, "Pennies Error", "Missing penny value")
                return
            elif not strIsInt(num_pennies):
                QMessageBox.warning(self, "Pennies Error", "Penny value must be a number (no decimals)")
                return
            elif num_pennies == '0':
                QMessageBox.warning(self, "Pennies Error", "Please add a penny value")
                return
            elif int(num_pennies) > self.pennies_left:
                QMessageBox.warning(self, "Pennies Error", "You don't have that many pennies left")
                return
            else:
                self.parent.pennies_left = self.pennies_left - int(num_pennies)
                self.parent.capturedPolygonsPennies.append(num_pennies)

            self.parent.capturedPolygonsFishery.append(self.parent.currentFishery)
            #self.parent.capturedPolygonsHabitat.append(self.habitat_combo.currentText())
            #self.parent.capturedPolygonsPermits.append(self.parent.currentPermits)

        self.close()

        #Check if this fishery should be done (no pennies left)
        if self.parent.pennies_left == 0:
            QMessageBox.warning(self, "Pennies Error", "You are out of pennies.  This fishery is now done.")
            self.parent.interviewEnd()
        else:
            mc = self.parent.canvas      
            self.p = PolygonTool(mc,self.parent)
            QObject.connect(self.p.o, SIGNAL("finished()"), self.nextPolygon)
            self.saveTool = mc.mapTool()
            mc.setMapTool(self.p)
            
    def on_pbnShapeDiscard_released(self):
        # Dump the last shape...
        self.parent.capturedPolygons.pop()
        rub = self.parent.capturedPolygonsRub.pop()
        rub.reset()
        # Grey out the button...
        self.pbnShapeDiscard.setEnabled(False)
        self.discardLast = True
            
    #"Finished with Fishery" button clicked
    def on_pbnShapeFinished_released(self):
        if not self.discardLast:
            num_pennies = self.line_1.text()
            if not num_pennies:
                QMessageBox.warning(self, "Pennies Error", "Missing penny value")
                return
            elif not strIsInt(num_pennies):
                QMessageBox.warning(self, "Pennies Error", "Penny value must be a number (no decimals)")
                return
            elif num_pennies == '0':
                QMessageBox.warning(self, "Pennies Error", "Please add a penny value")
                return
            elif int(num_pennies) > self.parent.pennies_left:
                QMessageBox.warning(self, "Pennies Error", "You don't have that many pennies left")
                return
            elif int(num_pennies) < self.parent.pennies_left:
                QMessageBox.warning(self, "Pennies Error", "You would still have pennies left.  Please enter a larger penny value or draw additional shapes")
                return
            else:
                self.parent.capturedPolygonsPennies.append(num_pennies)
                        
            self.parent.capturedPolygonsFishery.append(self.parent.currentFishery)
            #self.parent.capturedPolygonsHabitat.append(self.habitat_combo.currentText())
            #self.parent.capturedPolygonsPermits.append(self.parent.currentPermits)
        self.close()
        self.parent.interviewEnd()

    def nextPolygon(self):
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = NextPolygonGui(self.parent,flags,self.parent.pennies_left)
        wnd.show()
