# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewUserUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(385, 184)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
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
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)
        self.passwordWidget = QtWidgets.QWidget(Dialog)
        self.passwordWidget.setObjectName("passwordWidget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.passwordWidget)
        self.horizontalLayout_9.setContentsMargins(9, 2, -1, 2)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.passwordLabel = QtWidgets.QLabel(self.passwordWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.passwordLabel.setFont(font)
        self.passwordLabel.setObjectName("passwordLabel")
        self.horizontalLayout_9.addWidget(self.passwordLabel)
        self.passwordLineEdit = QtWidgets.QLineEdit(self.passwordWidget)
        self.passwordLineEdit.setText("")
        self.passwordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordLineEdit.setObjectName("passwordLineEdit")
        self.horizontalLayout_9.addWidget(self.passwordLineEdit)
        self.adminCheckBox = QtWidgets.QCheckBox(self.passwordWidget)
        self.adminCheckBox.setObjectName("adminCheckBox")
        self.horizontalLayout_9.addWidget(self.adminCheckBox)
        self.gridLayout.addWidget(self.passwordWidget, 3, 0, 1, 2)
        self.warningTimeWidget = QtWidgets.QWidget(Dialog)
        self.warningTimeWidget.setObjectName("warningTimeWidget")
        self.warningLayout = QtWidgets.QHBoxLayout(self.warningTimeWidget)
        self.warningLayout.setContentsMargins(9, 2, -1, 2)
        self.warningLayout.setObjectName("warningLayout")
        self.label_4 = QtWidgets.QLabel(self.warningTimeWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.warningLayout.addWidget(self.label_4)
        self.warningTimeLineEdit = QtWidgets.QLineEdit(self.warningTimeWidget)
        self.warningTimeLineEdit.setText("")
        self.warningTimeLineEdit.setObjectName("warningTimeLineEdit")
        self.warningLayout.addWidget(self.warningTimeLineEdit)
        self.gridLayout.addWidget(self.warningTimeWidget, 2, 0, 1, 2)
        self.baseTimeWidget = QtWidgets.QWidget(Dialog)
        self.baseTimeWidget.setObjectName("baseTimeWidget")
        self.baseLayout = QtWidgets.QHBoxLayout(self.baseTimeWidget)
        self.baseLayout.setContentsMargins(9, 2, -1, 2)
        self.baseLayout.setObjectName("baseLayout")
        self.baseLabel = QtWidgets.QLabel(self.baseTimeWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.baseLabel.setFont(font)
        self.baseLabel.setObjectName("baseLabel")
        self.baseLayout.addWidget(self.baseLabel)
        self.baseTimeLineEdit = QtWidgets.QLineEdit(self.baseTimeWidget)
        self.baseTimeLineEdit.setText("")
        self.baseTimeLineEdit.setObjectName("baseTimeLineEdit")
        self.baseLayout.addWidget(self.baseTimeLineEdit)
        self.gridLayout.addWidget(self.baseTimeWidget, 1, 0, 1, 2)
        self.nameWidget = QtWidgets.QWidget(Dialog)
        self.nameWidget.setObjectName("nameWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.nameWidget)
        self.horizontalLayout.setContentsMargins(9, 2, -1, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.nameWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.nameLineEdit = QtWidgets.QLineEdit(self.nameWidget)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.horizontalLayout.addWidget(self.nameLineEdit)
        self.gridLayout.addWidget(self.nameWidget, 0, 0, 1, 2)
        self.followGlobalWidget = QtWidgets.QWidget(Dialog)
        self.followGlobalWidget.setObjectName("followGlobalWidget")
        self.followGlobalLayout = QtWidgets.QHBoxLayout(self.followGlobalWidget)
        self.followGlobalLayout.setObjectName("followGlobalLayout")
        self.followGlobalCheckBox = QtWidgets.QCheckBox(self.followGlobalWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.followGlobalCheckBox.setFont(font)
        self.followGlobalCheckBox.setObjectName("followGlobalCheckBox")
        self.followGlobalLayout.addWidget(self.followGlobalCheckBox)
        self.gridLayout.addWidget(self.followGlobalWidget, 4, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "New User"))
        self.acceptPushButton.setText(_translate("Dialog", "Accept"))
        self.cancelPushButton.setText(_translate("Dialog", "Cancel"))
        self.passwordLabel.setText(_translate("Dialog", "Password:"))
        self.adminCheckBox.setText(_translate("Dialog", "Admin"))
        self.label_4.setText(_translate("Dialog", "Warning Time in Minutes:"))
        self.baseLabel.setText(_translate("Dialog", "*Base Amount of Time in Minutes:"))
        self.label_2.setText(_translate("Dialog", "*Name:"))
        self.followGlobalCheckBox.setText(_translate("Dialog", "Follow Global"))