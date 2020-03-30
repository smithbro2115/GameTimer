# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindowUI.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(187, 249)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.logOutPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.logOutPushButton.setFocusPolicy(QtCore.Qt.NoFocus)
        self.logOutPushButton.setObjectName("logOutPushButton")
        self.verticalLayout.addWidget(self.logOutPushButton)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 3, 1)
        self.viewerWidget = QtWidgets.QWidget(self.centralwidget)
        self.viewerWidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.viewerWidget.sizePolicy().hasHeightForWidth())
        self.viewerWidget.setSizePolicy(sizePolicy)
        self.viewerWidget.setObjectName("viewerWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.viewerWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setVerticalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout.addWidget(self.viewerWidget, 0, 1, 3, 1)
        self.gridLayout.setColumnStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 187, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew_User = QtWidgets.QAction(MainWindow)
        self.actionNew_User.setObjectName("actionNew_User")
        self.actionEdit_User = QtWidgets.QAction(MainWindow)
        self.actionEdit_User.setObjectName("actionEdit_User")
        self.actionDelete_User = QtWidgets.QAction(MainWindow)
        self.actionDelete_User.setObjectName("actionDelete_User")
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.actionGlobal_Settings = QtWidgets.QAction(MainWindow)
        self.actionGlobal_Settings.setObjectName("actionGlobal_Settings")
        self.menuFile.addAction(self.actionNew_User)
        self.menuFile.addAction(self.actionEdit_User)
        self.menuFile.addAction(self.actionDelete_User)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionGlobal_Settings)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Video Game Tracker"))
        self.logOutPushButton.setText(_translate("MainWindow", "Log Out"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew_User.setText(_translate("MainWindow", "New User"))
        self.actionEdit_User.setText(_translate("MainWindow", "Edit User"))
        self.actionDelete_User.setText(_translate("MainWindow", "Delete User"))
        self.action.setText(_translate("MainWindow", "Global Settings"))
        self.actionGlobal_Settings.setText(_translate("MainWindow", "Settings"))
