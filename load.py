# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'load.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(616, 420)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setStyleSheet("QGroupBox{border:0px;background-color:#4683ff;}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setContentsMargins(20, 9, 20, 20)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/MainSources/Wlogo.png"))
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setStyleSheet("")
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{color:#ffffff;}")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.label3 = QtWidgets.QLabel(self.groupBox_2)
        self.label3.setStyleSheet("QLabel{color:#ffffff;}")
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setObjectName("label3")
        self.verticalLayout_3.addWidget(self.label3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setMinimumSize(QtCore.QSize(130, 125))
        self.groupBox_3.setStyleSheet("QGroupBox{background-color:#2d72ff;}")
        self.groupBox_3.setTitle("")
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap(":/MainSources/manage.png"))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.label10 = QtWidgets.QLabel(self.groupBox_3)
        self.label10.setStyleSheet("QLabel{color:#bdd2ff;}")
        self.label10.setAlignment(QtCore.Qt.AlignCenter)
        self.label10.setWordWrap(True)
        self.label10.setObjectName("label10")
        self.verticalLayout_8.addWidget(self.label10)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setMinimumSize(QtCore.QSize(130, 125))
        self.groupBox_4.setStyleSheet("QGroupBox{background-color:#2d72ff;}")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/MainSources/patientt.png"))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label11 = QtWidgets.QLabel(self.groupBox_4)
        self.label11.setStyleSheet("QLabel{color:#bdd2ff;}")
        self.label11.setAlignment(QtCore.Qt.AlignCenter)
        self.label11.setObjectName("label11")
        self.verticalLayout_4.addWidget(self.label11)
        self.horizontalLayout_3.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setMinimumSize(QtCore.QSize(130, 125))
        self.groupBox_5.setStyleSheet("QGroupBox{background-color:#2d72ff;}")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_5)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/MainSources/report.png"))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label13 = QtWidgets.QLabel(self.groupBox_5)
        self.label13.setStyleSheet("QLabel{color:#bdd2ff;}")
        self.label13.setAlignment(QtCore.Qt.AlignCenter)
        self.label13.setObjectName("label13")
        self.verticalLayout_5.addWidget(self.label13)
        self.horizontalLayout_3.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_6.setMinimumSize(QtCore.QSize(130, 125))
        self.groupBox_6.setStyleSheet("QGroupBox{background-color:#2d72ff;}")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_9 = QtWidgets.QLabel(self.groupBox_6)
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/MainSources/doctor.png"))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_7.addWidget(self.label_9)
        self.label12 = QtWidgets.QLabel(self.groupBox_6)
        self.label12.setStyleSheet("QLabel{color:#bdd2ff;}")
        self.label12.setAlignment(QtCore.Qt.AlignCenter)
        self.label12.setObjectName("label12")
        self.verticalLayout_7.addWidget(self.label12)
        self.horizontalLayout_3.addWidget(self.groupBox_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.looop = QtWidgets.QLabel(self.groupBox)
        self.looop.setObjectName("looop")
        self.horizontalLayout_2.addWidget(self.looop)
        self.msg = QtWidgets.QLabel(self.groupBox)
        self.msg.setStyleSheet("QLabel{color:#bdd2ff;}")
        self.msg.setObjectName("msg")
        self.horizontalLayout_2.addWidget(self.msg)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "DOCTOR CLINIC"))
        self.label3.setText(_translate("MainWindow", "مرحبا بك، فى تطبيق إدارة العيادة"))
        self.label10.setText(_translate("MainWindow", "MANAGEMENT & SCHEDULE"))
        self.label11.setText(_translate("MainWindow", "PATIENT DATA"))
        self.label13.setText(_translate("MainWindow", "REPORTS"))
        self.label12.setText(_translate("MainWindow", "HEALTH RESULTS"))
        self.looop.setText(_translate("MainWindow", "TextLabel"))
        self.msg.setText(_translate("MainWindow", "جارى فتح التطبيق"))
import sources_rc
