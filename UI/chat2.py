# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat2.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time
import socket
def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

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
        self.getyourname = QtWidgets.QLineEdit(Form)
        self.getyourname.setGeometry(QtCore.QRect(10, 14, 71, 21))
        self.getyourname.setObjectName("lineEdit")
        self.getyourname.setPlaceholderText("您的名字")
        self.getfriendname = QtWidgets.QLineEdit(Form)
        self.getfriendname.setGeometry(QtCore.QRect(100, 14, 81, 21))
        self.getfriendname.setObjectName("lineEdit_2")
        self.getfriendname.setPlaceholderText("好友的名字")

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

    #   self.sign_slot.emit('000000'+self.yourmessage.toPlainText()+get_host_ip()+self.show_friendIP())
        self.show_miwen(self.yourmessage.toPlainText())
        self.show_friendIP()
        self.show_key()
        self.yourmessage.clear()
        #sendmessage to friend !!!!!!!!!!!!!!!!!!!!!! 补充在这里

    def show_friendIP(self):
        self.myname = self.getyourname.text()
        self.friendname = self.getfriendname.text()
    #   open myname.json     比如2016.json
    #   通过用户名得到相应的IP
    #   myIP 和 friend_IP
    #   self.friendIP.setText(friendname_IP)
    #   return self.friend_IP
        pass

    def show_miwen(self,msg):
        #self.miwen.setText("加密msg")
        pass

    def show_key(self):
        #self.key.setText("key")
        pass

    def slot_rec(self,msg):            #接受从服务区发来的消息
        msg_1 = msg                    #分离报文 分离出从好友那里发送来的消息
        self.history_message.append('From'+self.friendname+time.asctime( time.localtime(time.time()) )+'\n'+self.msg_1)

    """
    receive other's message
    
    self.message = "friend's message "+time.asctime( time.localtime(time.time()) )+'\n'+self.friendmessage
    
    """

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