# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdminUserWidgetUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(706, 450)
        Form.setMinimumSize(QtCore.QSize(700, 450))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(15, 0, 9, 0)
        self.gridLayout.setHorizontalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.line = QtWidgets.QFrame(Form)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 0, 2, 1)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setEnabled(True)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 42))
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.userLabel = QtWidgets.QLabel(self.widget)
        self.userLabel.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.userLabel.setFont(font)
        self.userLabel.setStyleSheet("")
        self.userLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.userLabel.setObjectName("userLabel")
        self.horizontalLayout.addWidget(self.userLabel)
        self.horizontalLayout.setStretch(0, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout.addWidget(self.widget, 0, 1, 1, 2)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setHorizontalSpacing(6)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.reportTableWidget = QtWidgets.QTableWidget(Form)
        self.reportTableWidget.setMinimumSize(QtCore.QSize(450, 0))
        self.reportTableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.reportTableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.reportTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.reportTableWidget.setObjectName("reportTableWidget")
        self.reportTableWidget.setColumnCount(4)
        self.reportTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.reportTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.reportTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.reportTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.reportTableWidget.setHorizontalHeaderItem(3, item)
        self.gridLayout_6.addWidget(self.reportTableWidget, 0, 1, 1, 1)
        self.userSelectionWidget = QtWidgets.QWidget(Form)
        self.userSelectionWidget.setMinimumSize(QtCore.QSize(175, 0))
        self.userSelectionWidget.setMaximumSize(QtCore.QSize(250, 16777215))
        self.userSelectionWidget.setObjectName("userSelectionWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.userSelectionWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.newUserPushButton = QtWidgets.QPushButton(self.userSelectionWidget)
        self.newUserPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.newUserPushButton.setObjectName("newUserPushButton")
        self.gridLayout_3.addWidget(self.newUserPushButton, 6, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.userSelectionWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_3.addWidget(self.line_2, 5, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.editUserPushButton = QtWidgets.QPushButton(self.userSelectionWidget)
        self.editUserPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.editUserPushButton.setObjectName("editUserPushButton")
        self.horizontalLayout_2.addWidget(self.editUserPushButton)
        self.deleteUserPushButton = QtWidgets.QPushButton(self.userSelectionWidget)
        self.deleteUserPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.deleteUserPushButton.setObjectName("deleteUserPushButton")
        self.horizontalLayout_2.addWidget(self.deleteUserPushButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.modifyTimePushButton = QtWidgets.QPushButton(self.userSelectionWidget)
        self.modifyTimePushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.modifyTimePushButton.setObjectName("modifyTimePushButton")
        self.gridLayout_3.addWidget(self.modifyTimePushButton, 3, 0, 1, 1)
        self.userReportPushButton = QtWidgets.QPushButton(self.userSelectionWidget)
        self.userReportPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.userReportPushButton.setObjectName("userReportPushButton")
        self.gridLayout_3.addWidget(self.userReportPushButton, 4, 0, 1, 1)
        self.gridLayout_6.addWidget(self.userSelectionWidget, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_6, 1, 1, 1, 2)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 9)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.userLabel.setText(_translate("Form", "User:"))
        item = self.reportTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Date"))
        item = self.reportTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Time Played"))
        item = self.reportTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Time Limit"))
        item = self.reportTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Surplus Time"))
        self.newUserPushButton.setText(_translate("Form", "New User"))
        self.editUserPushButton.setText(_translate("Form", "Edit User"))
        self.deleteUserPushButton.setText(_translate("Form", "Delete User"))
        self.modifyTimePushButton.setText(_translate("Form", "Modify Today\'s Time Limit"))
        self.userReportPushButton.setText(_translate("Form", "User Report"))