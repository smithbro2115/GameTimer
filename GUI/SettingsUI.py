# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GlobalSettingsUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 200)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.globalTimeLineEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.globalTimeLineEdit.setFont(font)
        self.globalTimeLineEdit.setObjectName("globalTimeLineEdit")
        self.horizontalLayout.addWidget(self.globalTimeLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 7, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.acceptPushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.acceptPushButton.setFont(font)
        self.acceptPushButton.setObjectName("acceptPushButton")
        self.horizontalLayout_5.addWidget(self.acceptPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cancelPushButton.setFont(font)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout_5.addWidget(self.cancelPushButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 9, 0, 1, 1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 6, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.usersPathLineEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.usersPathLineEdit.setFont(font)
        self.usersPathLineEdit.setObjectName("usersPathLineEdit")
        self.horizontalLayout_3.addWidget(self.usersPathLineEdit)
        self.usersPathToolButton = QtWidgets.QToolButton(Dialog)
        self.usersPathToolButton.setObjectName("usersPathToolButton")
        self.horizontalLayout_3.addWidget(self.usersPathToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.globalWarningTimeLineEdit = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.globalWarningTimeLineEdit.setFont(font)
        self.globalWarningTimeLineEdit.setObjectName("globalWarningTimeLineEdit")
        self.horizontalLayout_2.addWidget(self.globalWarningTimeLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Global Settings"))
        self.label.setText(_translate("Dialog", "Global Time in Minutes:"))
        self.acceptPushButton.setText(_translate("Dialog", "Accept"))
        self.cancelPushButton.setText(_translate("Dialog", "Cancel"))
        self.label_4.setText(_translate("Dialog", "Users Path:"))
        self.usersPathToolButton.setText(_translate("Dialog", "..."))
        self.label_2.setText(_translate("Dialog", "Global Warning Time in Minutes:"))
        self.label_3.setText(_translate("Dialog", "Global Settings"))
        self.label_5.setText(_translate("Dialog", "Settings"))