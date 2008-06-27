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
from other_ui import Ui_Other

from Util.common_functions import *

# General system includes
import sys

class OtherGui(QDialog, Ui_Other):
    def __init__(self, parent, flags, prevGUI=None):
        QDialog.__init__(self, parent.mainwindow, flags)
        self.setupUi(self)
        self.parent = parent
        self.prevGUI = prevGUI

    def on_pbnSelectOther_released(self):

        #interviewInfo2 = self.parent.interviewInfo2
        #interviewInfo2.append(["e_v_len", self.vessel_length_line.text()])
        #interviewInfo2.append(["e_v_motor", self.vessel_motor_line.text()])
        #interviewInfo2.append(["e_v_cap", self.haul_capacity_line.text()])
        #interviewInfo2.append(["e_v_homep", self.home_port_line.text()])
        #interviewInfo2.append(["e_trabajos", self.workers_line.text()])


        self.close()
        # this is a special case: we only assume on type of 'other' income
        from drawshapes import DrawShapesGui
        flags = Qt.WindowTitleHint | Qt.WindowSystemMenuHint | Qt.WindowMaximizeButtonHint 
        wnd = DrawShapesGui(self.parent,flags)
        wnd.show()

    def on_pbnCancel_clicked(self):
        self.close()
        # stop interview process
        self.parent.resetInterview("Cancelled out of Other Income interview...")