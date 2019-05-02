# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat2.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time

class fuck(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(446, 382)
        self.yourmessage = QtWidgets.QTextEdit(Form)
        self.yourmessage.setGeometry(QtCore.QRect(30, 250, 371, 91))
        self.yourmessage.setObjectName("yourmessage")
        self.friendIP = QtWidgets.QLineEdit(Form)
        self.friendIP.setGeometry(QtCore.QRect(280, 34, 151, 21))
        self.friendIP.setObjectName("friendIP")
        self.miwen = QtWidgets.QLineEdit(Form)
        self.miwen.setGeometry(QtCore.QRect(280, 84, 151, 21))
        self.miwen.setObjectName("miwen")
        self.key = QtWidgets.QLineEdit(Form)
        self.key.setGeometry(QtCore.QRect(280, 134, 151, 21))
        self.key.setObjectName("key")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 67, 17))
        self.label.setObjectName("label")
        self.send_btn = QtWidgets.QPushButton(Form)
        self.send_btn.setGeometry(QtCore.QRect(300, 350, 89, 25))
        self.send_btn.setObjectName("send_btn")
        self.send_btn.clicked.connect(self.send_click)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(310, 10, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(320, 60, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(320, 110, 67, 17))
        self.label_4.setObjectName("label_4")
        self.history_message = QtWidgets.QTextBrowser(Form)
        self.history_message.setGeometry(QtCore.QRect(25, 40, 251, 191))
        self.history_message.setObjectName("history_message")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "聊天界面"))
        self.send_btn.setText(_translate("Form", "发送"))
        self.label_2.setText(_translate("Form", "好友IP"))
        self.label_3.setText(_translate("Form", "密文"))
        self.label_4.setText(_translate("Form", "秘钥"))

    def send_click(self):

        self.message = "your message "+time.asctime( time.localtime(time.time()) )+'\n'+self.yourmessage.toPlainText()
        self.history_message.append(self.message)
        self.yourmessage.clear()
        #sendmessage to friend !!!!!!!!!!!!!!!!!!!!!! 补充在这里

    """
    receive other's message
    
    self.message = "friend's message "+time.asctime( time.localtime(time.time()) )+'\n'+self.friendmessage
    
    """

    def load_info(self):
        #self.miwen.setText(加密函数)
        #self.key.setText(秘钥)
        #self.friendIP.setText(IP)
        pass
"""
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = fuck()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
"""