# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogInUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(344, 125)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.userLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.userLabel.setFont(font)
        self.userLabel.setText("")
        self.userLabel.setObjectName("userLabel")
        self.gridLayout.addWidget(self.userLabel, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(3)
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
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.widget)
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.horizontalLayout.addWidget(self.passwordLineEdit)
        self.gridLayout.addWidget(self.widget, 2, 0, 1, 1)
        self.msgLabel = QtWidgets.QLabel(Dialog)
        self.msgLabel.setStyleSheet("color: red;")
        self.msgLabel.setText("")
        self.msgLabel.setObjectName("msgLabel")
        self.gridLayout.addWidget(self.msgLabel, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Log in"))
        self.acceptPushButton.setText(_translate("Dialog", "Accept"))
        self.cancelPushButton.setText(_translate("Dialog", "Cancel"))
        self.label_2.setText(_translate("Dialog", "Password:"))
