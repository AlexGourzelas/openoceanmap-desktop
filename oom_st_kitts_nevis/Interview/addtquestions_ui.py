# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addtquestions.ui'
#
# Created: Thu Apr 29 10:51:23 2010
#      by: PyQt4 UI code generator 4.4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_AdditionalQuestions(object):
    def setupUi(self, AdditionalQuestions):
        AdditionalQuestions.setObjectName("AdditionalQuestions")
        AdditionalQuestions.setWindowModality(QtCore.Qt.WindowModal)
        AdditionalQuestions.resize(520, 367)
        self.horizontalLayout_3 = QtGui.QHBoxLayout(AdditionalQuestions)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_4 = QtGui.QGroupBox(AdditionalQuestions)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_57 = QtGui.QWidget(self.groupBox_4)
        self.widget_57.setObjectName("widget_57")
        self.verticalLayout_28 = QtGui.QVBoxLayout(self.widget_57)
        self.verticalLayout_28.setSpacing(4)
        self.verticalLayout_28.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.widget_58 = QtGui.QWidget(self.widget_57)
        self.widget_58.setObjectName("widget_58")
        self.horizontalLayout_37 = QtGui.QHBoxLayout(self.widget_58)
        self.horizontalLayout_37.setSpacing(4)
        self.horizontalLayout_37.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        self.label_42 = QtGui.QLabel(self.widget_58)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.horizontalLayout_37.addWidget(self.label_42)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem)
        self.yrs_fishing_line = QtGui.QLineEdit(self.widget_58)
        self.yrs_fishing_line.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.yrs_fishing_line.setFont(font)
        self.yrs_fishing_line.setObjectName("yrs_fishing_line")
        self.horizontalLayout_37.addWidget(self.yrs_fishing_line)
        self.verticalLayout_28.addWidget(self.widget_58)
        self.verticalLayout.addWidget(self.widget_57)
        self.widget_65 = QtGui.QWidget(self.groupBox_4)
        self.widget_65.setObjectName("widget_65")
        self.verticalLayout_32 = QtGui.QVBoxLayout(self.widget_65)
        self.verticalLayout_32.setSpacing(4)
        self.verticalLayout_32.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.widget_66 = QtGui.QWidget(self.widget_65)
        self.widget_66.setObjectName("widget_66")
        self.horizontalLayout_40 = QtGui.QHBoxLayout(self.widget_66)
        self.horizontalLayout_40.setSpacing(4)
        self.horizontalLayout_40.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        self.label_46 = QtGui.QLabel(self.widget_66)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.horizontalLayout_40.addWidget(self.label_46)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_40.addItem(spacerItem1)
        self.pct_house_inc = QtGui.QLineEdit(self.widget_66)
        self.pct_house_inc.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pct_house_inc.setFont(font)
        self.pct_house_inc.setObjectName("pct_house_inc")
        self.horizontalLayout_40.addWidget(self.pct_house_inc)
        self.verticalLayout_32.addWidget(self.widget_66)
        self.verticalLayout.addWidget(self.widget_65)
        self.widget_59 = QtGui.QWidget(self.groupBox_4)
        self.widget_59.setObjectName("widget_59")
        self.verticalLayout_29 = QtGui.QVBoxLayout(self.widget_59)
        self.verticalLayout_29.setSpacing(4)
        self.verticalLayout_29.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.widget_60 = QtGui.QWidget(self.widget_59)
        self.widget_60.setObjectName("widget_60")
        self.horizontalLayout_38 = QtGui.QHBoxLayout(self.widget_60)
        self.horizontalLayout_38.setSpacing(4)
        self.horizontalLayout_38.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        self.label_43 = QtGui.QLabel(self.widget_60)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.horizontalLayout_38.addWidget(self.label_43)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem2)
        self.num_dependents = QtGui.QLineEdit(self.widget_60)
        self.num_dependents.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.num_dependents.setFont(font)
        self.num_dependents.setObjectName("num_dependents")
        self.horizontalLayout_38.addWidget(self.num_dependents)
        self.verticalLayout_29.addWidget(self.widget_60)
        self.verticalLayout.addWidget(self.widget_59)
        self.widget_61 = QtGui.QWidget(self.groupBox_4)
        self.widget_61.setObjectName("widget_61")
        self.verticalLayout_30 = QtGui.QVBoxLayout(self.widget_61)
        self.verticalLayout_30.setSpacing(4)
        self.verticalLayout_30.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.widget_62 = QtGui.QWidget(self.widget_61)
        self.widget_62.setObjectName("widget_62")
        self.horizontalLayout_39 = QtGui.QHBoxLayout(self.widget_62)
        self.horizontalLayout_39.setSpacing(4)
        self.horizontalLayout_39.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        self.label_44 = QtGui.QLabel(self.widget_62)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.horizontalLayout_39.addWidget(self.label_44)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem3)
        self.num_crew = QtGui.QLineEdit(self.widget_62)
        self.num_crew.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.num_crew.setFont(font)
        self.num_crew.setObjectName("num_crew")
        self.horizontalLayout_39.addWidget(self.num_crew)
        self.verticalLayout_30.addWidget(self.widget_62)
        self.verticalLayout.addWidget(self.widget_61)
        self.widget_63 = QtGui.QWidget(self.groupBox_4)
        self.widget_63.setObjectName("widget_63")
        self.verticalLayout_31 = QtGui.QVBoxLayout(self.widget_63)
        self.verticalLayout_31.setSpacing(4)
        self.verticalLayout_31.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.widget_64 = QtGui.QWidget(self.widget_63)
        self.widget_64.setObjectName("widget_64")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_64)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_45 = QtGui.QLabel(self.widget_64)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.horizontalLayout_2.addWidget(self.label_45)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.how_crew_paid = QtGui.QComboBox(self.widget_64)
        self.how_crew_paid.setMinimumSize(QtCore.QSize(150, 0))
        self.how_crew_paid.setMaximumSize(QtCore.QSize(150, 16777215))
        self.how_crew_paid.setObjectName("how_crew_paid")
        self.how_crew_paid.addItem(QtCore.QString())
        self.how_crew_paid.setItemText(0, "")
        self.how_crew_paid.addItem(QtCore.QString())
        self.how_crew_paid.addItem(QtCore.QString())
        self.how_crew_paid.addItem(QtCore.QString())
        self.horizontalLayout_2.addWidget(self.how_crew_paid)
        self.verticalLayout_31.addWidget(self.widget_64)
        self.verticalLayout.addWidget(self.widget_63)
        self.widget_32 = QtGui.QWidget(self.groupBox_4)
        self.widget_32.setObjectName("widget_32")
        self.verticalLayout_16 = QtGui.QVBoxLayout(self.widget_32)
        self.verticalLayout_16.setSpacing(4)
        self.verticalLayout_16.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.widget_34 = QtGui.QWidget(self.widget_32)
        self.widget_34.setObjectName("widget_34")
        self.horizontalLayout_25 = QtGui.QHBoxLayout(self.widget_34)
        self.horizontalLayout_25.setSpacing(4)
        self.horizontalLayout_25.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_30 = QtGui.QLabel(self.widget_34)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_25.addWidget(self.label_30)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem5)
        self.verticalLayout_16.addWidget(self.widget_34)
        self.verticalLayout.addWidget(self.widget_32)
        self.widget_35 = QtGui.QWidget(self.groupBox_4)
        self.widget_35.setObjectName("widget_35")
        self.verticalLayout_17 = QtGui.QVBoxLayout(self.widget_35)
        self.verticalLayout_17.setSpacing(4)
        self.verticalLayout_17.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.widget_36 = QtGui.QWidget(self.widget_35)
        self.widget_36.setObjectName("widget_36")
        self.horizontalLayout_26 = QtGui.QHBoxLayout(self.widget_36)
        self.horizontalLayout_26.setSpacing(4)
        self.horizontalLayout_26.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem6)
        self.label_31 = QtGui.QLabel(self.widget_36)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_26.addWidget(self.label_31)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem7)
        self.captain_shares = QtGui.QLineEdit(self.widget_36)
        self.captain_shares.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.captain_shares.setFont(font)
        self.captain_shares.setObjectName("captain_shares")
        self.horizontalLayout_26.addWidget(self.captain_shares)
        self.verticalLayout_17.addWidget(self.widget_36)
        self.verticalLayout.addWidget(self.widget_35)
        self.widget_24 = QtGui.QWidget(self.groupBox_4)
        self.widget_24.setObjectName("widget_24")
        self.verticalLayout_14 = QtGui.QVBoxLayout(self.widget_24)
        self.verticalLayout_14.setSpacing(4)
        self.verticalLayout_14.setContentsMargins(4, 2, 4, 2)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.widget_26 = QtGui.QWidget(self.widget_24)
        self.widget_26.setObjectName("widget_26")
        self.horizontalLayout_23 = QtGui.QHBoxLayout(self.widget_26)
        self.horizontalLayout_23.setSpacing(4)
        self.horizontalLayout_23.setContentsMargins(4, 0, 4, 0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem8)
        self.label_28 = QtGui.QLabel(self.widget_26)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_23.addWidget(self.label_28)
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem9)
        self.crew_shares = QtGui.QLineEdit(self.widget_26)
        self.crew_shares.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.crew_shares.setFont(font)
        self.crew_shares.setObjectName("crew_shares")
        self.horizontalLayout_23.addWidget(self.crew_shares)
        self.verticalLayout_14.addWidget(self.widget_26)
        self.verticalLayout.addWidget(self.widget_24)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem10)
        self.button_box = QtGui.QWidget(self.groupBox_4)
        self.button_box.setObjectName("button_box")
        self.horizontalLayout = QtGui.QHBoxLayout(self.button_box)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.pbnCancel = QtGui.QPushButton(self.button_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnCancel.setFont(font)
        self.pbnCancel.setObjectName("pbnCancel")
        self.horizontalLayout.addWidget(self.pbnCancel)
        spacerItem12 = QtGui.QSpacerItem(50, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.pbnFinished = QtGui.QPushButton(self.button_box)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pbnFinished.setFont(font)
        self.pbnFinished.setObjectName("pbnFinished")
        self.horizontalLayout.addWidget(self.pbnFinished)
        self.verticalLayout.addWidget(self.button_box)
        self.horizontalLayout_3.addWidget(self.groupBox_4)

        self.retranslateUi(AdditionalQuestions)
        QtCore.QMetaObject.connectSlotsByName(AdditionalQuestions)
        AdditionalQuestions.setTabOrder(self.yrs_fishing_line, self.pct_house_inc)
        AdditionalQuestions.setTabOrder(self.pct_house_inc, self.num_dependents)
        AdditionalQuestions.setTabOrder(self.num_dependents, self.num_crew)
        AdditionalQuestions.setTabOrder(self.num_crew, self.how_crew_paid)
        AdditionalQuestions.setTabOrder(self.how_crew_paid, self.captain_shares)
        AdditionalQuestions.setTabOrder(self.captain_shares, self.crew_shares)
        AdditionalQuestions.setTabOrder(self.crew_shares, self.pbnFinished)
        AdditionalQuestions.setTabOrder(self.pbnFinished, self.pbnCancel)

    def retranslateUi(self, AdditionalQuestions):
        AdditionalQuestions.setWindowTitle(QtGui.QApplication.translate("AdditionalQuestions", "OpenOceanMap - Additional Questions", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(QtGui.QApplication.translate("AdditionalQuestions", "10. Years fishing experience:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_46.setText(QtGui.QApplication.translate("AdditionalQuestions", "11. % of total household income from fishing:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setText(QtGui.QApplication.translate("AdditionalQuestions", "12. How many people live in your household, including yourself:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_44.setText(QtGui.QApplication.translate("AdditionalQuestions", "13. Average number of crew per trip (not including yourself):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_45.setText(QtGui.QApplication.translate("AdditionalQuestions", "14. How are crewmembers paid:", None, QtGui.QApplication.UnicodeUTF8))
        self.how_crew_paid.setItemText(1, QtGui.QApplication.translate("AdditionalQuestions", "Salary", None, QtGui.QApplication.UnicodeUTF8))
        self.how_crew_paid.setItemText(2, QtGui.QApplication.translate("AdditionalQuestions", "Share of revenue", None, QtGui.QApplication.UnicodeUTF8))
        self.how_crew_paid.setItemText(3, QtGui.QApplication.translate("AdditionalQuestions", "Share of catch", None, QtGui.QApplication.UnicodeUTF8))
        self.label_30.setText(QtGui.QApplication.translate("AdditionalQuestions", "15. After expenses (like gas) have been paid, what percentage does", None, QtGui.QApplication.UnicodeUTF8))
        self.label_31.setText(QtGui.QApplication.translate("AdditionalQuestions", "the captain get:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("AdditionalQuestions", "the crewmembers get:", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnCancel.setText(QtGui.QApplication.translate("AdditionalQuestions", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.pbnFinished.setText(QtGui.QApplication.translate("AdditionalQuestions", "Continue", None, QtGui.QApplication.UnicodeUTF8))

