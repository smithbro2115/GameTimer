# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PathNotFoundUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 160)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.descriptionLabel = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.gridLayout.addWidget(self.descriptionLabel, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.retryPushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.retryPushButton.setFont(font)
        self.retryPushButton.setDefault(True)
        self.retryPushButton.setObjectName("retryPushButton")
        self.horizontalLayout_5.addWidget(self.retryPushButton)
        self.newPathPushButton = QtWidgets.QPushButton(Dialog)
        self.newPathPushButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.newPathPushButton.setFont(font)
        self.newPathPushButton.setObjectName("newPathPushButton")
        self.horizontalLayout_5.addWidget(self.newPathPushButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.closePushButton = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.closePushButton.setFont(font)
        self.closePushButton.setObjectName("closePushButton")
        self.horizontalLayout_5.addWidget(self.closePushButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Path Not Found"))
        self.descriptionLabel.setText(_translate("Dialog", "The users path specified; [path], could not be found. If you are using a external or network drive, make sure that it is connected and then try again. Or select a new path."))
        self.retryPushButton.setText(_translate("Dialog", "Retry"))
        self.newPathPushButton.setText(_translate("Dialog", "New Path"))
        self.closePushButton.setText(_translate("Dialog", "Close"))
        self.label_2.setText(_translate("Dialog", "Path Not Found"))
