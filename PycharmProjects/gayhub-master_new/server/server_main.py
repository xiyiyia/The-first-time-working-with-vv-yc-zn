# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'server_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import pyqtSignal, QObject, QDataStream, QFile, Qt
import json
import server.server_redis_operation.json_operation as json_operation
import server.server_redis_operation.data_operation.intergrated_message as intergrated_message
import server.server_redis_operation.data_operation.message_pb2 as message_pb2
import operator as op
import server.server_redis_operation.redis_operation as redis_operation
import server.server_redis_operation.server_message_creat as server_message_creat
import logging

from server.Tcpserver import Tcpserver
from PyQt5.QtNetwork import QHostAddress

PATH = '~/gayhub/bin/'


class Ui_Server(QObject):
    sign_send = pyqtSignal(str, str)
    sign_signin = pyqtSignal(str)
    sign_uploadfile = pyqtSignal(str)
    sign_message_deal = pyqtSignal(str)

    def setupUi(self, Server):
        Server.setObjectName("Server")
        Server.resize(431, 322)
        self.centralwidget = QtWidgets.QWidget(Server)
        self.centralwidget.setObjectName("centralwidget")
        self.server_start()
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
        self.sign_message_deal.connect(self.server_pack)
        self.sign_signin.connect(self.check_usr)
        self.sign_uploadfile.connect(self.uploadfile)
        self.retranslateUi(Server)
        QtCore.QMetaObject.connectSlotsByName(Server)

    def server_pack(self, event_msg):
        try1 = message_pb2.GeneralMessages()
        try1_data = message_pb2.gm_signup()
        try1_data.ID = '1024'
        try1_data.PSW = '12345'
        data_1 = try1_data.SerializeToString()
        try1.RC = '000001'
        try1.SC = '00000'
        try1.DT = '00'
        try1.DATA = data_1
        try1.SIP = '192.168.1.100'
        try1.DIP = '192.168.1.101'
        data_2 = try1.SerializeToString()
        bs = str(data_2, encoding="utf8")
        self.server_operation("00"+bs)


    def check_usr(self, event_msg):
        #生成报文
        # self.account = event_msg[0]
        # self.passwd = event_msg[1]
        # self.textBrowser.append("account:" + self.account + "passwd:" + self.passwd)
        #/ 生成报文
        # 这里要数据库比对
        self.sign_message_deal.emit(event_msg)
        # event_msg = ['1', 'success']
        # self.slot_send("0001", event_msg)
        # self.sign_uploadfile.emit(self.account)

    def uploadfile(self, filename):
        Filename = "./server_redis_operation/user_json/"+filename+".json"
        with open(Filename, 'r')as f:
            str1 = f.read()
            r = json.loads(str1)
        event_msg = ['', '']
        event_msg[1] = r
        event_msg[0] = str1.__sizeof__()
        self.sign_send.emit("0002", event_msg)
        f.close()

    def server_start(self):
        self.ss = Tcpserver()
        # 绑定地址，端口
        self.ss.listen(QHostAddress('0.0.0.0'), 10086)
        # tcpServer接受到信息，在界面表示出来，就绑定slot_recv，但是转发那一层就不用在这里表示出来了
        self.ss.sign_server_recv.connect(self.slot_recv)
        self.sign_send.connect(self.ss.sign_send)
        print("listen")


    def retranslateUi(self, Server):
        _translate = QtCore.QCoreApplication.translate
        Server.setWindowTitle(_translate("Server", "MainWindow"))

    def slot_recv(self, event_id, event_msg):
        print("finish")
        print(event_msg)
        if event_id =="0001" :
            self.sign_signin.emit(event_msg)


    def slot_send(self, event_id, event_msg):
        print("sending……")
        print(event_msg)
        self.sign_send.emit(event_id, event_msg)

    def server_operation(self, mes_3):
        logging.basicConfig(level=logging.DEBUG)
        LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
        logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)
        LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
        DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

        # message = recv()
        # message = type1 + message1
        redis_1 = redis_operation.RedisOperation()
        im_1 = message_pb2
        smc_1 = server_message_creat.ServerMessageCreator()
        json_1 = json_operation.JsonServer()

        mes = im_1.GeneralMessages()
        mes_1 = mes_3
        mes_4 = bytes(mes_3[2:], encoding="utf8")
        mes.ParseFromString(mes_4)
        print(mes_1[0:2], "00")
        if op.eq(mes_1[0:2], "00"):
            # mes = im_1.GeneralMessages()
            mes_send = im_1.GeneralMessages()
            # mes_data = im_1.signup()
            mes_send_DID = im_1.GeneralMessages()

            # mes.ParseFromString(message1)
            if op.eq(mes.RC, "000001"):
                # signup
                logging.info(mes)
                mes_data = im_1.gm_signup()
                mes_data.ParseFromString(str.encode(mes.DATA))
                if redis_1.check_id_exists(mes_data.ID):
                    if redis_1.check_signup(mes_data.ID, mes_data.PSW):
                        mes_send = smc_1.signup(mes, 1)
                        redis_1.std_signup(mes_data.ID, mes_data.PSW)
                        logging.info(mes_send)
                        json_1.update_json(mes_data.ID)
                        # send(mes_send, mes.SIP)
                        mes_send_bytes = mes_send.SerializeToString()
                        event_msg = [bytes.decode(mes_send_bytes), "1"]
                        self.slot_send("0001", event_msg)
                        # send json
                    else:
                        mes_send = smc_1.signup(mes, 2)
                        logging.info(mes_send)
                        mes_send_bytes = mes_send.SerializeToString()
                        event_msg = [bytes.decode(mes_send_bytes), "1"]
                        self.slot_send("0001", event_msg)
                        # send(mes_send, mes.SIP)
                else:
                    mes_send = smc_1.signup(mes, 3)
                    logging.info(mes_send)
                    mes_send_bytes = mes_send.SerializeToString()
                    event_msg = [bytes.decode(mes_send_bytes), "1"]
                    self.slot_send("0001", event_msg)
            if op.eq(mes.RC, "001001"):
                # signin
                logging.info(mes)
                mes_data = im_1.gm_signup()
                mes_data.ParseFromString(mes.DATA)
                if not redis_1.check_id_exists(mes_data.ID):
                    redis_1.user_login(mes_data.ID, mes_data.PSW)
                    mes_send = smc_1.signup(mes, 1)
                    logging.info(mes_send)
                    # send(mes_send, mes.SIP)
                    mes_send_bytes = mes_send.SerializeToString()
                    event_msg = [bytes.decode(mes_send_bytes), "1"]
                    self.slot_send("0001", event_msg)
                    # send json
                else:
                    mes_send = smc_1.login(mes, 2)
                    logging.info(mes_send)
                    mes_send_bytes = mes_send.SerializeToString()
                    event_msg = [bytes.decode(mes_send_bytes), "1"]
                    self.slot_send("0001", event_msg)
            if op.eq(mes.RC, "000010"):
                # add friend
                logging.info(mes)
                mes_data = im_1.gm_friend()
                mes_data.ParseFromString(mes.DATA)
                if op.eq(mes.SC, '66666'):
                    mes_send_SID = smc_1.add_friend(mes, mes_data, 2)
                    json_1.add_friend_json(mes_data.SID, mes_data.DID)
                    json_1.update_json(mes_data.SID)
                    json_1.update_json(mes_data.DID)
                    # send(mes_send_SID)
                    # send double json to SID,DID
                if op.eq(mes.SC, '00010'):
                    mes_send_SID = smc_1.add_friend(mes, mes_data, 4)
                    # send(mes_send_SID)

                if redis_1.check_id_exists(mes_data.DID):
                    mes_send_DID = smc_1.add_friend(mes, mes_data, 1)
                    # send(mes_send_DID)

                else:
                    mes_send = smc_1.add_friend(mes, mes_data, 3)
                    logging.info(mes_send)
                    # send(mes_send)
            if op.eq(mes.RC, '000011'):
                # delete friend
                logging.info(mes)
                mes_data = im_1.GeneralMessages()
                mes_data.ParseFromString(mes.DATA)

                if redis_1.check_id_exists(mes_data.DID):
                    mes_send = smc_1.delete_friend(mes, 1)
                    json_1.add_friend_json(mes_data.SID, mes_data.DID)
                    json_1.update_json(mes_data.SID)
                    json_1.update_json(mes_data.DID)
                    # send(mes_send)
                    # send double json to SID,DID
                else:
                    mes_send = smc_1.add_friend(mes, mes_data, 2)
                    logging.info(mes_send)
                    # send(mes_send)
            '''
            if op.eq(mes.RC, '010001'):
            if op.eq(mes.RC, '010001'):
            if op.eq(mes.RC, '010001'):
            if op.eq(mes.RC, '010001'):
            '''
        '''
        if op.eq(type, '01'):
            mes = im_1.ClientAS()
        if op.eq(type, '02'):
            mes = im_1.AuthenticatorC3()
        if op.eq(type, '03'):
            mes = im_1.ClientV()
        if op.eq(type, '04'):
            mes = im_1.AuthenticatorC5()
        if op.eq(type, '05'):
            mes = im_1.VClient()
        if op.eq(type, '06'):
            mes = im_1.ClientTGS()
        if op.eq(type, '07'):
            mes = im_1.TGSClient()
        if op.eq(type, '08'):
            mes = im_1.Ticketv()
        if op.eq(type, '09'):
            mes = im_1.ASClient()
        if op.eq(type, '10'):
            mes = im_1.Tickettgs()
        '''


if __name__ == "__main__":
            app = QApplication(sys.argv)
            mainWindow = QMainWindow()
            ui = Ui_Server()
            ui.setupUi(mainWindow)
            mainWindow.show()
            sys.exit(app.exec_())

