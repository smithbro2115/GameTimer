# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ModifyTimeDialogUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(296, 157)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 3)
        self.timeSpinBox = QtWidgets.QSpinBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timeSpinBox.setFont(font)
        self.timeSpinBox.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhTime)
        self.timeSpinBox.setMinimum(-86400)
        self.timeSpinBox.setMaximum(86400)
        self.timeSpinBox.setObjectName("timeSpinBox")
        self.gridLayout.addWidget(self.timeSpinBox, 5, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.userLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.userLabel.setFont(font)
        self.userLabel.setObjectName("userLabel")
        self.horizontalLayout.addWidget(self.userLabel)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 5, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.timeLineEdit = QtWidgets.QLineEdit(Dialog)
        self.timeLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.timeLineEdit.setText("")
        self.timeLineEdit.setObjectName("timeLineEdit")
        self.horizontalLayout_2.addWidget(self.timeLineEdit)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 3)
        self.gridLayout.setColumnStretch(0, 1)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Modify Time"))
        self.label.setText(_translate("Dialog", "Enter the amount you want to modify by. Negative numbers are also allowed"))
        self.timeSpinBox.setSuffix(_translate("Dialog", " Minutes"))
        self.userLabel.setText(_translate("Dialog", "Modifying User\'s Time"))
        self.label_2.setText(_translate("Dialog", "Time Left: "))
        self.label_3.setText(_translate("Dialog", "Minutes"))
