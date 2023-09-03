# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1099, 841)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_1 = QtWidgets.QVBoxLayout()
        self.verticalLayout_1.setObjectName("verticalLayout_1")
        self.sensorReadingBox = QtWidgets.QGroupBox(self.centralwidget)
        self.sensorReadingBox.setObjectName("sensorReadingBox")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.sensorReadingBox)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.groupBox_2 = QtWidgets.QGroupBox(self.sensorReadingBox)
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ultrasonicLbl = QtWidgets.QLabel(self.groupBox_2)
        self.ultrasonicLbl.setObjectName("ultrasonicLbl")
        self.horizontalLayout_4.addWidget(self.ultrasonicLbl)
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_3.setReadOnly(True)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_4.addWidget(self.spinBox_3)
        self.gridLayout_11.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.sensorReadingBox)
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.currentLbl = QtWidgets.QLabel(self.groupBox_3)
        self.currentLbl.setObjectName("currentLbl")
        self.horizontalLayout_5.addWidget(self.currentLbl)
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_4.setReadOnly(True)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout_5.addWidget(self.spinBox_4)
        self.gridLayout_12.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(self.sensorReadingBox)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.voltageLbl = QtWidgets.QLabel(self.groupBox)
        self.voltageLbl.setObjectName("voltageLbl")
        self.horizontalLayout_6.addWidget(self.voltageLbl)
        self.spinBox_5 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_5.setReadOnly(True)
        self.spinBox_5.setObjectName("spinBox_5")
        self.horizontalLayout_6.addWidget(self.spinBox_5)
        self.gridLayout_13.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.verticalLayout_7.addWidget(self.groupBox)
        self.gridLayout_10.addLayout(self.verticalLayout_7, 0, 0, 1, 1)
        self.verticalLayout_1.addWidget(self.sensorReadingBox)
        self.ipTasksBox = QtWidgets.QGroupBox(self.centralwidget)
        self.ipTasksBox.setObjectName("ipTasksBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.ipTasksBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.task1Btn = QtWidgets.QPushButton(self.ipTasksBox)
        self.task1Btn.setObjectName("task1Btn")
        self.verticalLayout.addWidget(self.task1Btn)
        self.task2Btn = QtWidgets.QPushButton(self.ipTasksBox)
        self.task2Btn.setObjectName("task2Btn")
        self.verticalLayout.addWidget(self.task2Btn)
        self.task3Btn = QtWidgets.QPushButton(self.ipTasksBox)
        self.task3Btn.setObjectName("task3Btn")
        self.verticalLayout.addWidget(self.task3Btn)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_1.addWidget(self.ipTasksBox)
        self.horizontalLayout.addLayout(self.verticalLayout_1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cameraFeedBox = QtWidgets.QGroupBox(self.centralwidget)
        self.cameraFeedBox.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.cameraFeedBox.setObjectName("cameraFeedBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.cameraFeedBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.camerFeed = QtWidgets.QLabel(self.cameraFeedBox)
        self.camerFeed.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.camerFeed.setAlignment(QtCore.Qt.AlignCenter)
        self.camerFeed.setObjectName("camerFeed")
        self.verticalLayout_3.addWidget(self.camerFeed)
        self.screenShotBtn = QtWidgets.QPushButton(self.cameraFeedBox)
        self.screenShotBtn.setObjectName("screenShotBtn")
        self.verticalLayout_3.addWidget(self.screenShotBtn)
        self.gridLayout_5.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.cameraFeedBox)
        self.teamLogoBox = QtWidgets.QGroupBox(self.centralwidget)
        self.teamLogoBox.setTitle("")
        self.teamLogoBox.setObjectName("teamLogoBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.teamLogoBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.logoLbl = QtWidgets.QLabel(self.teamLogoBox)
        self.logoLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.logoLbl.setObjectName("logoLbl")
        self.gridLayout_6.addWidget(self.logoLbl, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.teamLogoBox)
        self.motionControlBox = QtWidgets.QGroupBox(self.centralwidget)
        self.motionControlBox.setObjectName("motionControlBox")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.motionControlBox)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.leftBtn = QtWidgets.QPushButton(self.motionControlBox)
        self.leftBtn.setObjectName("leftBtn")
        self.horizontalLayout_3.addWidget(self.leftBtn)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.forwardBtn = QtWidgets.QPushButton(self.motionControlBox)
        self.forwardBtn.setObjectName("forwardBtn")
        self.verticalLayout_8.addWidget(self.forwardBtn)
        self.backwardBtn = QtWidgets.QPushButton(self.motionControlBox)
        self.backwardBtn.setObjectName("backwardBtn")
        self.verticalLayout_8.addWidget(self.backwardBtn)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.rightBtn = QtWidgets.QPushButton(self.motionControlBox)
        self.rightBtn.setObjectName("rightBtn")
        self.horizontalLayout_3.addWidget(self.rightBtn)
        self.gridLayout_8.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.motionControlBox)
        self.verticalLayout_2.setStretch(0, 4)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.speedControlBox = QtWidgets.QGroupBox(self.centralwidget)
        self.speedControlBox.setObjectName("speedControlBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.speedControlBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.speedSpinBox = QtWidgets.QSpinBox(self.speedControlBox)
        self.speedSpinBox.setReadOnly(False)
        self.speedSpinBox.setMaximum(255)
        self.speedSpinBox.setObjectName("speedSpinBox")
        self.gridLayout_3.addWidget(self.speedSpinBox, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lowSpeedRadioBtn = QtWidgets.QRadioButton(self.speedControlBox)
        self.lowSpeedRadioBtn.setAutoFillBackground(False)
        self.lowSpeedRadioBtn.setCheckable(True)
        self.lowSpeedRadioBtn.setChecked(False)
        self.lowSpeedRadioBtn.setAutoExclusive(True)
        self.lowSpeedRadioBtn.setObjectName("lowSpeedRadioBtn")
        self.horizontalLayout_2.addWidget(self.lowSpeedRadioBtn)
        self.midSpeedRadioBtn = QtWidgets.QRadioButton(self.speedControlBox)
        self.midSpeedRadioBtn.setCheckable(True)
        self.midSpeedRadioBtn.setObjectName("midSpeedRadioBtn")
        self.horizontalLayout_2.addWidget(self.midSpeedRadioBtn)
        self.highSpeedRadioBtn = QtWidgets.QRadioButton(self.speedControlBox)
        self.highSpeedRadioBtn.setCheckable(True)
        self.highSpeedRadioBtn.setObjectName("highSpeedRadioBtn")
        self.horizontalLayout_2.addWidget(self.highSpeedRadioBtn)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.speedControlBox)
        self.motionModeBox = QtWidgets.QGroupBox(self.centralwidget)
        self.motionModeBox.setObjectName("motionModeBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.motionModeBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.radioButton_5 = QtWidgets.QRadioButton(self.motionModeBox)
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout_5.addWidget(self.radioButton_5)
        self.radioButton_4 = QtWidgets.QRadioButton(self.motionModeBox)
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout_5.addWidget(self.radioButton_4)
        self.spinBox_2 = QtWidgets.QSpinBox(self.motionModeBox)
        self.spinBox_2.setObjectName("spinBox_2")
        self.verticalLayout_5.addWidget(self.spinBox_2)
        self.gridLayout_7.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.motionModeBox)
        self.connectivityBox = QtWidgets.QGroupBox(self.centralwidget)
        self.connectivityBox.setObjectName("connectivityBox")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.connectivityBox)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.connectivityBox)
        self.radioButton_7.setCheckable(False)
        self.radioButton_7.setObjectName("radioButton_7")
        self.verticalLayout_6.addWidget(self.radioButton_7)
        self.radioButton_6 = QtWidgets.QRadioButton(self.connectivityBox)
        self.radioButton_6.setCheckable(False)
        self.radioButton_6.setObjectName("radioButton_6")
        self.verticalLayout_6.addWidget(self.radioButton_6)
        self.gridLayout_9.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.connectivityBox)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sensorReadingBox.setTitle(_translate("MainWindow", "Sensor Readings"))
        self.ultrasonicLbl.setText(_translate("MainWindow", "UltraSonic"))
        self.currentLbl.setText(_translate("MainWindow", "Current"))
        self.voltageLbl.setText(_translate("MainWindow", "Voltage"))
        self.ipTasksBox.setTitle(_translate("MainWindow", "IP Tasks"))
        self.task1Btn.setText(_translate("MainWindow", "Task 1"))
        self.task2Btn.setText(_translate("MainWindow", "Task 2"))
        self.task3Btn.setText(_translate("MainWindow", "Task 3"))
        self.cameraFeedBox.setTitle(_translate("MainWindow", "Camera Feed"))
        self.camerFeed.setText(_translate("MainWindow", "Camera Feed will be placed here"))
        self.screenShotBtn.setText(_translate("MainWindow", "Screen Shot"))
        self.logoLbl.setText(_translate("MainWindow", "Team Logo will be placed here"))
        self.motionControlBox.setTitle(_translate("MainWindow", "Motion Control"))
        self.leftBtn.setText(_translate("MainWindow", "Left"))
        self.forwardBtn.setText(_translate("MainWindow", "Forward"))
        self.backwardBtn.setText(_translate("MainWindow", "Backward"))
        self.rightBtn.setText(_translate("MainWindow", "Right"))
        self.speedControlBox.setTitle(_translate("MainWindow", "Speed Control"))
        self.lowSpeedRadioBtn.setText(_translate("MainWindow", "Low"))
        self.midSpeedRadioBtn.setText(_translate("MainWindow", "Mid"))
        self.highSpeedRadioBtn.setText(_translate("MainWindow", "High"))
        self.motionModeBox.setTitle(_translate("MainWindow", "Motion Mode"))
        self.radioButton_5.setText(_translate("MainWindow", "Manual"))
        self.radioButton_4.setText(_translate("MainWindow", "Autonomous (specify distance to wall)"))
        self.connectivityBox.setTitle(_translate("MainWindow", "Connectivity"))
        self.radioButton_7.setText(_translate("MainWindow", "Connected"))
        self.radioButton_6.setText(_translate("MainWindow", "Disconnected"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
