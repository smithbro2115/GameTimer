# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CrashReportUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(543, 294)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.reportTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.reportTextEdit.setObjectName("reportTextEdit")
        self.gridLayout.addWidget(self.reportTextEdit, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.sendPushButton = QtWidgets.QPushButton(Dialog)
        self.sendPushButton.setObjectName("sendPushButton")
        self.horizontalLayout.addWidget(self.sendPushButton)
        self.cancelPushButton = QtWidgets.QPushButton(Dialog)
        self.cancelPushButton.setObjectName("cancelPushButton")
        self.horizontalLayout.addWidget(self.cancelPushButton)
        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Crash Report"))
        self.label_2.setText(_translate("Dialog", "We have gathered data about the crash and will submit a crash report. If you could write down exactly what were doing when the program crashed, it would greatly help to fix the issue."))
        self.label.setText(_translate("Dialog", "Screen Time Tracker Crashed"))
        self.sendPushButton.setText(_translate("Dialog", "Send"))
        self.cancelPushButton.setText(_translate("Dialog", "Cancel"))
