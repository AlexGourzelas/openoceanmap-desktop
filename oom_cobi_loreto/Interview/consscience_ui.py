# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'consscience.ui'
#
# Created: Mon Mar 30 16:28:06 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ConsScience(object):
    def setupUi(self, ConsScience):
        ConsScience.setObjectName("ConsScience")
        ConsScience.resize(764, 486)
        self.verticalLayout_5 = QtGui.QVBoxLayout(ConsScience)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.vessel_info = QtGui.QGroupBox(ConsScience)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.vessel_info.setFont(font)
        self.vessel_info.setObjectName("vessel_info")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.vessel_info)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home_port_5 = QtGui.QWidget(self.vessel_info)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.home_port_5.setFont(font)
        self.home_port_5.setObjectName("home_port_5")
        self.hboxlayout = QtGui.QHBoxLayout(self.home_port_5)
        self.hboxlayout.setSpacing(4)
        self.hboxlayout.setMargin(4)
        self.hboxlayout.setObjectName("hboxlayout")
        self.employee_text = QtGui.QLabel(self.home_port_5)
        self.employee_text.setMinimumSize(QtCore.QSize(150, 0))
        self.employee_text.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.employee_text.setFont(font)
        self.employee_text.setObjectName("employee_text")
        self.hboxlayout.addWidget(self.employee_text)
        self.comboBox = QtGui.QComboBox(self.home_port_5)
        self.comboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem(QtCore.QString())
        self.comboBox.addItem(QtCore.QString())
        self.comboBox.addItem(QtCore.QString())
        self.comboBox.addItem(QtCore.QString())
        self.comboBox.addItem(QtCore.QString())
        self.comboBox.addItem(QtCore.QString())
        self.hboxlayout.addWidget(self.comboBox)
        self.verticalLayout_2.addWidget(self.home_port_5)
        self.vessel_length = QtGui.QWidget(self.vessel_info)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.vessel_length.setFont(font)
        self.vessel_length.setObjectName("vessel_length")
        self.hboxlayout1 = QtGui.QHBoxLayout(self.vessel_length)
        self.hboxlayout1.setSpacing(4)
        self.hboxlayout1.setMargin(4)
        self.hboxlayout1.setObjectName("hboxlayout1")
        self.add_info_text = QtGui.QLabel(self.vessel_length)
        self.add_info_text.setMinimumSize(QtCore.QSize(150, 0))
        self.add_info_text.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_info_text.setFont(font)
        self.add_info_text.setObjectName("add_info_text")
        self.hboxlayout1.addWidget(self.add_info_text)
        self.add_info_line = QtGui.QLineEdit(self.vessel_length)
        self.add_info_line.setEnabled(True)
        self.add_info_line.setMinimumSize(QtCore.QSize(200, 0))
        self.add_info_line.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.add_info_line.setFont(font)
        self.add_info_line.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.add_info_line.setObjectName("add_info_line")
        self.hboxlayout1.addWidget(self.add_info_line)
        self.verticalLayout_2.addWidget(self.vessel_length)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addWidget(self.vessel_info)
        self.groupBox = QtGui.QGroupBox(ConsScience)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_9 = QtGui.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_10 = QtGui.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self._14 = QtGui.QHBoxLayout()
        self._14.setObjectName("_14")
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setMinimumSize(QtCore.QSize(280, 0))
        self.label_12.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self._14.addWidget(self.label_12)
        self.focus_coast_reef = QtGui.QLineEdit(self.groupBox)
        self.focus_coast_reef.setEnabled(True)
        self.focus_coast_reef.setMinimumSize(QtCore.QSize(30, 0))
        self.focus_coast_reef.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.focus_coast_reef.setFont(font)
        self.focus_coast_reef.setObjectName("focus_coast_reef")
        self._14.addWidget(self.focus_coast_reef)
        self.verticalLayout_10.addLayout(self._14)
        self._15 = QtGui.QHBoxLayout()
        self._15.setObjectName("_15")
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setMinimumSize(QtCore.QSize(280, 0))
        self.label_13.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self._15.addWidget(self.label_13)
        self.focus_deep_reef = QtGui.QLineEdit(self.groupBox)
        self.focus_deep_reef.setEnabled(True)
        self.focus_deep_reef.setMinimumSize(QtCore.QSize(30, 0))
        self.focus_deep_reef.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.focus_deep_reef.setFont(font)
        self.focus_deep_reef.setObjectName("focus_deep_reef")
        self._15.addWidget(self.focus_deep_reef)
        self.verticalLayout_10.addLayout(self._15)
        self._16 = QtGui.QHBoxLayout()
        self._16.setObjectName("_16")
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setMinimumSize(QtCore.QSize(280, 0))
        self.label_14.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self._16.addWidget(self.label_14)
        self.focus_soft = QtGui.QLineEdit(self.groupBox)
        self.focus_soft.setEnabled(True)
        self.focus_soft.setMinimumSize(QtCore.QSize(30, 0))
        self.focus_soft.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.focus_soft.setFont(font)
        self.focus_soft.setObjectName("focus_soft")
        self._16.addWidget(self.focus_soft)
        self.verticalLayout_10.addLayout(self._16)
        self._17 = QtGui.QHBoxLayout()
        self._17.setObjectName("_17")
        self.label_15 = QtGui.QLabel(self.groupBox)
        self.label_15.setMinimumSize(QtCore.QSize(280, 0))
        self.label_15.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self._17.addWidget(self.label_15)
        self.focus_pelagic = QtGui.QLineEdit(self.groupBox)
        self.focus_pelagic.setEnabled(True)
        self.focus_pelagic.setMinimumSize(QtCore.QSize(30, 0))
        self.focus_pelagic.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.focus_pelagic.setFont(font)
        self.focus_pelagic.setObjectName("focus_pelagic")
        self._17.addWidget(self.focus_pelagic)
        self.verticalLayout_10.addLayout(self._17)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self._18 = QtGui.QHBoxLayout()
        self._18.setObjectName("_18")
        self.focus_migratory = QtGui.QLabel(self.groupBox)
        self.focus_migratory.setMinimumSize(QtCore.QSize(280, 0))
        self.focus_migratory.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.focus_migratory.setFont(font)
        self.focus_migratory.setObjectName("focus_migratory")
        self._18.addWidget(self.focus_migratory)
        self.focus_migratory_2 = QtGui.QLineEdit(self.groupBox)
        self.focus_migratory_2.setEnabled(True)
        self.focus_migratory_2.setMinimumSize(QtCore.QSize(30, 0))
        self.focus_migratory_2.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.focus_migratory_2.setFont(font)
        self.focus_migratory_2.setObjectName("focus_migratory_2")
        self._18.addWidget(self.focus_migratory_2)
        self.verticalLayout_9.addLayout(self._18)
        self._19 = QtGui.QHBoxLayout()
        self._19.setObjectName("_19")
        self.label_17 = QtGui.QLabel(self.groupBox)
        self.label_17.setMinimumSize(QtCore.QSize(280, 0))
        self.label_17.setMaximumSize(QtCore.QSize(280, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self._19.addWidget(self.label_17)
        self.focus_turtles = QtGui.QLineEdit(self.groupBox)
        self.focus_turtles.setEnabled(True)
        self.focus_turtles.setMinimumSize(QtCore.QSize(30, 0))
        self.focus_turtles.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.focus_turtles.setFont(font)
        self.focus_turtles.setObjectName("focus_turtles")
        self._19.addWidget(self.focus_turtles)
        self.verticalLayout_9.addLayout(self._19)
        spacerItem2 = QtGui.QSpacerItem(20, 5, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_21 = QtGui.QLabel(self.groupBox)
        self.label_21.setMinimumSize(QtCore.QSize(80, 0))
        self.label_21.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.verticalLayout_3.addWidget(self.label_21)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_23 = QtGui.QLabel(self.groupBox)
        self.label_23.setMinimumSize(QtCore.QSize(80, 0))
        self.label_23.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_3.addWidget(self.label_23)
        self.focus_other_1_name = QtGui.QLineEdit(self.groupBox)
        self.focus_other_1_name.setEnabled(True)
        self.focus_other_1_name.setMinimumSize(QtCore.QSize(100, 0))
        self.focus_other_1_name.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.focus_other_1_name.setFont(font)
        self.focus_other_1_name.setObjectName("focus_other_1_name")
        self.horizontalLayout_3.addWidget(self.focus_other_1_name)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_22 = QtGui.QLabel(self.groupBox)
        self.label_22.setMinimumSize(QtCore.QSize(140, 0))
        self.label_22.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_4.addWidget(self.label_22)
        self.focus_other_1_interest = QtGui.QLineEdit(self.groupBox)
        self.focus_other_1_interest.setEnabled(True)
        self.focus_other_1_interest.setMinimumSize(QtCore.QSize(30, 0))
        self.focus_other_1_interest.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.focus_other_1_interest.setFont(font)
        self.focus_other_1_interest.setObjectName("focus_other_1_interest")
        self.horizontalLayout_4.addWidget(self.focus_other_1_interest)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.verticalLayout_9.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_24 = QtGui.QLabel(self.groupBox)
        self.label_24.setMinimumSize(QtCore.QSize(80, 0))
        self.label_24.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_4.addWidget(self.label_24)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_25 = QtGui.QLabel(self.groupBox)
        self.label_25.setMinimumSize(QtCore.QSize(80, 0))
        self.label_25.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_5.addWidget(self.label_25)
        self.focus_other_2_name = QtGui.QLineEdit(self.groupBox)
        self.focus_other_2_name.setEnabled(True)
        self.focus_other_2_name.setMinimumSize(QtCore.QSize(100, 0))
        self.focus_other_2_name.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.focus_other_2_name.setFont(font)
        self.focus_other_2_name.setObjectName("focus_other_2_name")
        self.horizontalLayout_5.addWidget(self.focus_other_2_name)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_26 = QtGui.QLabel(self.groupBox)
        self.label_26.setMinimumSize(QtCore.QSize(140, 0))
        self.label_26.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_6.addWidget(self.label_26)
        self.focus_other_2_interest = QtGui.QLineEdit(self.groupBox)
        self.focus_other_2_interest.setEnabled(True)
        self.focus_other_2_interest.setMinimumSize(QtCore.QSize(30, 0))
        self.focus_other_2_interest.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.focus_other_2_interest.setFont(font)
        self.focus_other_2_interest.setObjectName("focus_other_2_interest")
        self.horizontalLayout_6.addWidget(self.focus_other_2_interest)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.verticalLayout_9.addLayout(self.verticalLayout_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout_9)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.groupBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.button_box = QtGui.QWidget(ConsScience)
        self.button_box.setObjectName("button_box")
        self.hboxlayout2 = QtGui.QHBoxLayout(self.button_box)
        self.hboxlayout2.setObjectName("hboxlayout2")
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem4)
        self.pbnSelectConsScience = QtGui.QPushButton(self.button_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnSelectConsScience.setFont(font)
        self.pbnSelectConsScience.setObjectName("pbnSelectConsScience")
        self.hboxlayout2.addWidget(self.pbnSelectConsScience)
        self.verticalLayout_5.addWidget(self.button_box)

        self.retranslateUi(ConsScience)
        QtCore.QMetaObject.connectSlotsByName(ConsScience)

    def retranslateUi(self, ConsScience):
        ConsScience.setWindowTitle(QtGui.QApplication.translate("ConsScience", "OpenOceanMap - Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.vessel_info.setTitle(QtGui.QApplication.translate("ConsScience", "Conservationist / Scientist Information", None, QtGui.QApplication.UnicodeUTF8))
        self.employee_text.setText(QtGui.QApplication.translate("ConsScience", "Type of Specialist:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("ConsScience", "Academic", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("ConsScience", "Non-Governmental Organization", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("ConsScience", "Government (Municipal)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("ConsScience", "Government (State)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(4, QtGui.QApplication.translate("ConsScience", "Government (Federal)", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(5, QtGui.QApplication.translate("ConsScience", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.add_info_text.setText(QtGui.QApplication.translate("ConsScience", "Additional info:", None, QtGui.QApplication.UnicodeUTF8))
        self.add_info_line.setText(QtGui.QApplication.translate("ConsScience", "add info yo", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("ConsScience", "Areas of Focus:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ConsScience", "What percent interest do you have in each activity? (Must add up to 100)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("ConsScience", "Coastal reef ecosystem - fish and invertebrates:", None, QtGui.QApplication.UnicodeUTF8))
        self.focus_coast_reef.setText(QtGui.QApplication.translate("ConsScience", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("ConsScience", "Deep sea reef ecosystem - fish and invertebrates:", None, QtGui.QApplication.UnicodeUTF8))
        self.focus_deep_reef.setText(QtGui.QApplication.translate("ConsScience", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("ConsScience", "Soft bottom - sand, mud, etc:", None, QtGui.QApplication.UnicodeUTF8))
        self.focus_soft.setText(QtGui.QApplication.translate("ConsScience", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("ConsScience", "Small pelagics - sardines, anchovy, etc:", None, QtGui.QApplication.UnicodeUTF8))
        self.focus_pelagic.setText(QtGui.QApplication.translate("ConsScience", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.focus_migratory.setText(QtGui.QApplication.translate("ConsScience", "Migratory fish - tuna, swordfish, sailfish:", None, QtGui.QApplication.UnicodeUTF8))
        self.focus_migratory_2.setText(QtGui.QApplication.translate("ConsScience", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("ConsScience", "Sea turtles:", None, QtGui.QApplication.UnicodeUTF8))
        self.focus_turtles.setText(QtGui.QApplication.translate("ConsScience", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("ConsScience", "Other focus #1:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("ConsScience", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("ConsScience", "% interest:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("ConsScience", "Other focus #2:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("ConsScience", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("ConsScience", "% interest:", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnSelectConsScience.setText(QtGui.QApplication.translate("ConsScience", "Start Drawing Shapes", None, QtGui.QApplication.UnicodeUTF8))

