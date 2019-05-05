# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSignal, Qt
import time
from multiprocessing import Process
from client.src.Mythread import Thread
import json


class login(QWidget):

    sign_recv = pyqtSignal(str, str)
    sign_send = pyqtSignal(str, str)
    sign_cmd = pyqtSignal(str)
    sign_getjson = pyqtSignal(str)


    def __init__(self):
        super(login, self).__init__()
        self.setGeometry(300, 300, 400, 247)
        # 登录窗口无边界
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # 登录窗口透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 定义多个空label
        self.label_null1 = QLabel()
        self.label_null2 = QLabel()
        self.label_null3 = QLabel()
        self.label_null4 = QLabel()
        self.label_new = QLabel()
        self.result = ""
        # 定义创建新账户标签并设置信号槽绑定事件
        self.label_new.setText("<a href='#'>注册新用户</a>")
        self.label_new.setStyleSheet('''color: rgb(253,129,53);''')
        self.label_new.linkActivated.connect(self.idnew)
        # 设置隐藏密码RadioButton
        self.btn_check = QRadioButton("显示密码")
        self.btn_check.setStyleSheet('''color: rgb(253,129,53);;''')
        self.btn_check.clicked.connect(self.yanma)
        # 登录与退出按钮，设置按钮颜色及事件绑定
        self.btn_denglu = QPushButton("登录")
        self.btn_quxiao = QPushButton("退出")
        self.btn_denglu.setStyleSheet('''color: white;
                        background-color: rgb(218,181,150);''')
        self.btn_quxiao.setStyleSheet('''color: white;
                        background-color: rgb(218,181,150);''')
        self.btn_denglu.clicked.connect(self.check)
        self.btn_quxiao.clicked.connect(self.quxiao)
        self.thread_start()
        self.sign_cmd.connect(self.check_usr)
        self.sign_getjson.connect(self.getjson)
        # 账号和密码
        self.lineedit_id = QLineEdit()
        self.lineedit_id.setPlaceholderText("账号")
#        self.account = self.lineedit_id.text()
        self.lineedit_password = QLineEdit()
        self.lineedit_password.setEchoMode(QLineEdit.Password)
        self.lineedit_password.setPlaceholderText("密码")
#        self.passwd = self.lineedit_password.text()
        # 布局设置
        layout = QHBoxLayout(self)
        wid_denglu_right = QWidget()
        wid_denglu_left = QLabel()
        g = QGridLayout()
        g.addWidget(self.lineedit_id, 1, 1, 1, 2)
        g.addWidget(self.lineedit_password, 2, 1, 1, 2)
        g.addWidget(self.btn_check, 3, 1)
        g.addWidget(self.btn_denglu, 4, 1)
        g.addWidget(self.btn_quxiao, 4, 2)
        g.addWidget(self.label_null1, 5, 1)
        g.addWidget(self.label_null2, 6, 1)
        g.addWidget(self.label_null3, 7, 1)
        g.addWidget(self.label_null4, 8, 1)
        g.addWidget(self.label_new, 9, 2)
        wid_denglu_right.setLayout(g)
        layout.addWidget(wid_denglu_left)
        layout.addWidget(wid_denglu_right)
        self.setLayout(layout)

    def thread_start(self):
        self.thread = Thread()
        self.thread.hostname = 'localhost'
        self.thread.start()
        self.sign_send.connect(self.thread.sign_thread_send)
        self.thread.sign_thread_recv.connect(self.slot_recv)

        self.thread.sign_thread_start.connect(self.update_name)

    def getjson(self, event_msg):
        Filename = "./"+self.account+".json"
        with open(Filename, 'w+')as f:
            json.dump(event_msg, f, indent=4, ensure_ascii=False)
        f.close()


    # 密码隐藏
    def yanma(self):
        if self.btn_check.isChecked():
            self.lineedit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lineedit_password.setEchoMode(QLineEdit.Password)
    # 登录时核查账号及密码是否正确

    def check_usr(self, str):
        print("check"+self.result)
        if (str == "666666"):
            reply = QMessageBox.warning(self, "!", "登录成功", QMessageBox.Yes)
            # 登录成功
            # 跳转到聊天界面
        else:
            reply = QMessageBox.warning(self, "!", "账号或密码输入错误", QMessageBox.Yes)

    def update_name(self, addr):
        event_msg = ["0", addr]
       # self.sign_send.emit("0000", event_msg)
        print("finish")

    def slot_recv(self, Event_id, Event_msg):
        print("recv now")
        print(Event_msg)
        self.result = Event_msg
        print(self.result)
        if Event_id == '0001':   #登录
            self.sign_cmd.emit(self.result)
        # if(Event_id == '0002'):  #传输json
        #     self.sign_getjson.emit(Event_msg)




    def client_login(self):  # def client_login(self)
        self.account = self.lineedit_id.text()
        self.passwd = self.lineedit_password.text()
        #生成报文
        event_msg = self.account+self.passwd
        #/生成报文
        self.sign_send.emit("0001", event_msg)
        print("send msg")



    def check(self):
        self.client_login()
        print("11"+self.result)

    # 创建新的账号
    def idnew(self):
        self.label_idnew_id = QLabel("账号")
        self.label_idnew_password = QLabel("密码")
        self.lineedit_idnew_id = QLineEdit()

        self.new_account = self.lineedit_idnew_id.text()

        self.lineedit_idnew_password = QLineEdit()

        self.new_passwd = self.lineedit_idnew_password.text()

        self.btn_idnew_quren = QPushButton("注册")
        self.btn_idnew_quren.clicked.connect(self.idnewqueren)
        self.btn_idnew_quxiao = QPushButton("取消")
        self.btn_idnew_quxiao.clicked.connect(self.idnewclose)
        self.idnew = QWidget()
        layout_idnew = QGridLayout()
        layout_idnew.addWidget(self.label_idnew_id, 1, 0)
        layout_idnew.addWidget(self.label_idnew_password, 2, 0)
        layout_idnew.addWidget(self.lineedit_idnew_id, 1, 1, 1, 2)
        layout_idnew.addWidget(self.lineedit_idnew_password, 2, 1, 1, 2)
        layout_idnew.addWidget(self.btn_idnew_quren, 3, 1)
        layout_idnew.addWidget(self.btn_idnew_quxiao, 3, 2)
        self.idnew.setLayout(layout_idnew)
        self.idnew.move(self.pos())
        self.idnew.resize(200, 133)
        self.idnew.setWindowFlags(Qt.FramelessWindowHint)
        self.paintEvent(self)
        self.idnew.setStyleSheet("background-color :rgb(253,216,174)")
        self.idnew.show()
        # 新账号注册的确认

    def idnewqueren(self):
        var = self.client_enroll(self.new_account, self.new_passwd)

        if (var == "0100"):
            replay = QMessageBox.warning(self, "!", "账号存在", QMessageBox.Yes)
        elif var == "0101":
            replay = QMessageBox.warning(self, "!", "密码不符合要求", QMessageBox.Yes)

        elif var == "0102":
            replay = QMessageBox.warning(self, "!", "注册成功", QMessageBox.Yes)
            self.idnew.close()
        replay = QMessageBox.warning(self, "!", "未知错误", QMessageBox.Yes)

    def client_enroll(self, new_account, new_passwd):
        return "fuck off"

    # 添加背景图片
    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("药水哥.jpg")
        painter.drawPixmap(self.rect(), pixmap)

    # 关闭创新账号窗口
    def idnewclose(self):
        self.idnew.close()

    # 取消创建新账号，并退出创建窗口
    def quxiao(self):
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    d = login()
    d.show()
sys.exit(app.exec())
