# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication
import data_operation.intergrated_message as intergrated_message
import operator as op


class Ui_Server(object):
    def setupUi(self, Server):
        Server.setObjectName("Server")
        Server.resize(431, 322)
        self.centralwidget = QtWidgets.QWidget(Server)
        self.centralwidget.setObjectName("centralwidget")

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 601, 371))
        self.textBrowser.setObjectName("textBrowser")

        self.textBrowser.append("1")  # 文本框逐条添加数据
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)  # 文本框显示到底部

        Server.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Server)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 431, 23))
        self.menubar.setObjectName("menubar")
        Server.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Server)
        self.statusbar.setObjectName("statusbar")
        Server.setStatusBar(self.statusbar)

        self.retranslateUi(Server)
        QtCore.QMetaObject.connectSlotsByName(Server)

    def screen_out(self, message, type1):

        if op.eq(type1, '00'):
            mes = intergrated_message.general_messages()
        if op.eq(type1, '01'):
            mes = intergrated_message.ClientAS()
        if op.eq(type1, '02'):
            mes = intergrated_message.AuthenticatorC3()
        if op.eq(type1, '03'):
            mes = intergrated_message.ClientV()
        if op.eq(type1, '04'):
            mes = intergrated_message.AuthenticatorC5()
        if op.eq(type1, '05'):
            mes = intergrated_message.VClient()
        if op.eq(type1, '06'):
            mes = intergrated_message.ClientTGS()
        if op.eq(type1, '07'):
            mes = intergrated_message.TGSClient()
        if op.eq(type1, '08'):
            mes = intergrated_message.Ticketv()
        if op.eq(type1, '09'):
            mes = intergrated_message.ASClient()
        if op.eq(type1, '10'):
            mes = intergrated_message.Tickettgs()

        mes.ParseFromString(message)
        self.textBrowser.append(mes + "\n\n")  # 文本框逐条添加数据
        self.textBrowser.moveCursor(self.textBrowser.textCursor().End)  # 文本框显示到底部

    def retranslateUi(self, Server):
        _translate = QtCore.QCoreApplication.translate
        Server.setWindowTitle(_translate("Server", "MainWindow"))


if __name__ == "__main__":
            app = QApplication(sys.argv)
            mainWindow = QMainWindow()
            ui = Ui_Server()
            ui.setupUi(mainWindow)
            mainWindow.show()
            sys.exit(app.exec_())