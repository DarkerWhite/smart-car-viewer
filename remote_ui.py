# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\remote_ui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_RemoteCamera(object):
    def setupUi(self, RemoteCamera):
        RemoteCamera.setObjectName("RemoteCamera")
        RemoteCamera.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(RemoteCamera)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 591))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(220, 530, 351, 29))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_remote_listen_address = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_remote_listen_address.setFont(font)
        self.label_remote_listen_address.setObjectName("label_remote_listen_address")
        self.horizontalLayout.addWidget(self.label_remote_listen_address)
        self.edit_remote_listen_address = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.edit_remote_listen_address.setObjectName("edit_remote_listen_address")
        self.horizontalLayout.addWidget(self.edit_remote_listen_address)
        self.button_remote_listen_address = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_remote_listen_address.setFont(font)
        self.button_remote_listen_address.setObjectName("button_remote_listen_address")
        self.horizontalLayout.addWidget(self.button_remote_listen_address)
        self.label_get_remote = QtWidgets.QLabel(self.tab)
        self.label_get_remote.setGeometry(QtCore.QRect(10, 10, 771, 511))
        self.label_get_remote.setStyleSheet("background-color: rgb(193, 193, 193);")
        self.label_get_remote.setFrameShape(QtWidgets.QFrame.Box)
        self.label_get_remote.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_get_remote.setLineWidth(1)
        self.label_get_remote.setText("")
        self.label_get_remote.setObjectName("label_get_remote")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(220, 10, 351, 29))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_remote_send_address = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_remote_send_address.setFont(font)
        self.label_remote_send_address.setObjectName("label_remote_send_address")
        self.horizontalLayout_2.addWidget(self.label_remote_send_address)
        self.edit_remote_send_address = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.edit_remote_send_address.setObjectName("edit_remote_send_address")
        self.horizontalLayout_2.addWidget(self.edit_remote_send_address)
        self.button_remote_send_address = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.button_remote_send_address.setFont(font)
        self.button_remote_send_address.setObjectName("button_remote_send_address")
        self.horizontalLayout_2.addWidget(self.button_remote_send_address)
        self.textEdit = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 761, 501))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.tabWidget.addTab(self.tab_2, "")
        RemoteCamera.setCentralWidget(self.centralwidget)

        self.retranslateUi(RemoteCamera)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(RemoteCamera)

    def retranslateUi(self, RemoteCamera):
        _translate = QtCore.QCoreApplication.translate
        RemoteCamera.setWindowTitle(_translate("RemoteCamera", "Remote Camera"))
        self.label_remote_listen_address.setText(_translate("RemoteCamera", "Listening Address"))
        self.button_remote_listen_address.setText(_translate("RemoteCamera", "Start Listening"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("RemoteCamera", "Server Side"))
        self.label_remote_send_address.setText(_translate("RemoteCamera", "Sending Address"))
        self.button_remote_send_address.setText(_translate("RemoteCamera", "Start Sending"))
        self.textEdit.setHtml(_translate("RemoteCamera", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\';\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("RemoteCamera", "Client Side"))

