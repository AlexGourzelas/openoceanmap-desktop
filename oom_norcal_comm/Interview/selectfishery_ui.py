# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectfishery.ui'
#
# Created: Mon Jun 15 14:14:30 2009
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_SelectFishery(object):
    def setupUi(self, SelectFishery):
        SelectFishery.setObjectName("SelectFishery")
        SelectFishery.resize(477, 401)
        self.verticalLayout = QtGui.QVBoxLayout(SelectFishery)
        self.verticalLayout.setObjectName("verticalLayout")
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
        self.fishery_comboBox.setItemText(0, "")
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.fishery_comboBox.addItem(QtCore.QString())
        self.hboxlayout.addWidget(self.fishery_comboBox)
        self.horizontalLayout_3.addWidget(self.widget)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.widget_4 = QtGui.QWidget(SelectFishery)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_12 = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_7 = QtGui.QLabel(self.widget_4)
        self.label_7.setMinimumSize(QtCore.QSize(160, 0))
        self.label_7.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_12.addWidget(self.label_7)
        self.fishery_yrs_exp = QtGui.QLineEdit(self.widget_4)
        self.fishery_yrs_exp.setMinimumSize(QtCore.QSize(40, 0))
        self.fishery_yrs_exp.setMaximumSize(QtCore.QSize(40, 16777215))
        self.fishery_yrs_exp.setObjectName("fishery_yrs_exp")
        self.horizontalLayout_12.addWidget(self.fishery_yrs_exp)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.horizontalLayout_11.addWidget(self.widget_4)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.widget_8 = QtGui.QWidget(SelectFishery)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout_20 = QtGui.QHBoxLayout(self.widget_8)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_11 = QtGui.QLabel(self.widget_8)
        self.label_11.setMinimumSize(QtCore.QSize(160, 0))
        self.label_11.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_20.addWidget(self.label_11)
        self.fishery_effort = QtGui.QLineEdit(self.widget_8)
        self.fishery_effort.setMinimumSize(QtCore.QSize(250, 0))
        self.fishery_effort.setMaximumSize(QtCore.QSize(250, 16777215))
        self.fishery_effort.setObjectName("fishery_effort")
        self.horizontalLayout_20.addWidget(self.fishery_effort)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem2)
        self.horizontalLayout_19.addWidget(self.widget_8)
        self.verticalLayout.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.widget_7 = QtGui.QWidget(SelectFishery)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_18 = QtGui.QHBoxLayout(self.widget_7)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_10 = QtGui.QLabel(self.widget_7)
        self.label_10.setMinimumSize(QtCore.QSize(160, 0))
        self.label_10.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_18.addWidget(self.label_10)
        self.fishery_traps_hooks = QtGui.QLineEdit(self.widget_7)
        self.fishery_traps_hooks.setMinimumSize(QtCore.QSize(40, 0))
        self.fishery_traps_hooks.setMaximumSize(QtCore.QSize(40, 16777215))
        self.fishery_traps_hooks.setObjectName("fishery_traps_hooks")
        self.horizontalLayout_18.addWidget(self.fishery_traps_hooks)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem3)
        self.horizontalLayout_17.addWidget(self.widget_7)
        self.verticalLayout.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.widget_6 = QtGui.QWidget(SelectFishery)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_16 = QtGui.QHBoxLayout(self.widget_6)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_9 = QtGui.QLabel(self.widget_6)
        self.label_9.setMinimumSize(QtCore.QSize(160, 0))
        self.label_9.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_16.addWidget(self.label_9)
        self.fishery_perc_income = QtGui.QLineEdit(self.widget_6)
        self.fishery_perc_income.setMinimumSize(QtCore.QSize(40, 0))
        self.fishery_perc_income.setMaximumSize(QtCore.QSize(40, 16777215))
        self.fishery_perc_income.setObjectName("fishery_perc_income")
        self.horizontalLayout_16.addWidget(self.fishery_perc_income)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem4)
        self.horizontalLayout_15.addWidget(self.widget_6)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.widget_5 = QtGui.QWidget(SelectFishery)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_14 = QtGui.QHBoxLayout(self.widget_5)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_8 = QtGui.QLabel(self.widget_5)
        self.label_8.setMinimumSize(QtCore.QSize(160, 0))
        self.label_8.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_14.addWidget(self.label_8)
        self.fishery_avg_price = QtGui.QLineEdit(self.widget_5)
        self.fishery_avg_price.setMinimumSize(QtCore.QSize(40, 0))
        self.fishery_avg_price.setMaximumSize(QtCore.QSize(40, 16777215))
        self.fishery_avg_price.setObjectName("fishery_avg_price")
        self.horizontalLayout_14.addWidget(self.fishery_avg_price)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem5)
        self.horizontalLayout_13.addWidget(self.widget_5)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.widget_3 = QtGui.QWidget(SelectFishery)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtGui.QLabel(self.widget_3)
        self.label.setMinimumSize(QtCore.QSize(160, 0))
        self.label.setMaximumSize(QtCore.QSize(160, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.fishery_hist_avg_price = QtGui.QLineEdit(self.widget_3)
        self.fishery_hist_avg_price.setMinimumSize(QtCore.QSize(40, 0))
        self.fishery_hist_avg_price.setMaximumSize(QtCore.QSize(40, 16777215))
        self.fishery_hist_avg_price.setObjectName("fishery_hist_avg_price")
        self.horizontalLayout_4.addWidget(self.fishery_hist_avg_price)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.horizontalLayout_5.addWidget(self.widget_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtGui.QWidget(SelectFishery)
        self.widget_2.setObjectName("widget_2")
        self.hboxlayout1 = QtGui.QHBoxLayout(self.widget_2)
        self.hboxlayout1.setSpacing(6)
        self.hboxlayout1.setMargin(9)
        self.hboxlayout1.setObjectName("hboxlayout1")
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem7)
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
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(SelectFishery)
        QtCore.QMetaObject.connectSlotsByName(SelectFishery)

    def retranslateUi(self, SelectFishery):
        SelectFishery.setWindowTitle(QtGui.QApplication.translate("SelectFishery", "OpenOceanMap - Select Fishery", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_text.setText(QtGui.QApplication.translate("SelectFishery", "Select Fishery :", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(1, QtGui.QApplication.translate("SelectFishery", "Dungeness Crab - trap", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(2, QtGui.QApplication.translate("SelectFishery", "Groundfish - trawl", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(3, QtGui.QApplication.translate("SelectFishery", "Groundfish - hook & line", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(4, QtGui.QApplication.translate("SelectFishery", "Hagfish - trap", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(5, QtGui.QApplication.translate("SelectFishery", "Halibut - longline", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(6, QtGui.QApplication.translate("SelectFishery", "Lingcod - hook & line", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(7, QtGui.QApplication.translate("SelectFishery", "Prawn - trap", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(8, QtGui.QApplication.translate("SelectFishery", "Sablefish (Blackcod) - longline", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(9, QtGui.QApplication.translate("SelectFishery", "Sablefish (Blackcod) - trap", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(10, QtGui.QApplication.translate("SelectFishery", "Salmon - troll", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(11, QtGui.QApplication.translate("SelectFishery", "Shrimp - trawl", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(12, QtGui.QApplication.translate("SelectFishery", "Tuna - jig", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(13, QtGui.QApplication.translate("SelectFishery", "Tuna - pole", None, QtGui.QApplication.UnicodeUTF8))
        self.fishery_comboBox.setItemText(14, QtGui.QApplication.translate("SelectFishery", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("SelectFishery", "Years experience in fishery:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("SelectFishery", "Fishing effort:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("SelectFishery", "Traps/Hooks:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("SelectFishery", "Percent income from this fishery:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("SelectFishery", "Average price:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("SelectFishery", "Historic average price:", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFisheryFinished.setText(QtGui.QApplication.translate("SelectFishery", "Finished With Interview", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnStartShapes.setText(QtGui.QApplication.translate("SelectFishery", "Start Drawing Shapes", None, QtGui.QApplication.UnicodeUTF8))

