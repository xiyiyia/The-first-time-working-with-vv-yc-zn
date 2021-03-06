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
import server.server_redis_operation.data_operation.message_pb2 as im_1
import operator as op
import server.server_redis_operation.redis_operation as redis_operation
import server.server_redis_operation.server_message_creat as server_message_creat
import logging

import redis
import server.server_redis_operation.server_redis_pb2 as SRPTB

from server.Tcpserver import Tcpserver
from PyQt5.QtNetwork import QHostAddress

PATH = '~/gayhub/bin/'


class Ui_Server(QObject):
    sign_send = pyqtSignal(str)
    sign_signin = pyqtSignal(str)
    sign_uploadfile = pyqtSignal(str)
    sign_message_deal = pyqtSignal(str)

    def setupUi(self, Server):
        '''
        self.r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=False)
        self.the_user_data = SRPTB.User()
        self.the_user_data.ID = '1024'
        self.the_user_data.PSW = '1024'
        self.the_user_data.IP = '1'
        self.the_user_data.STD = 0
        self.r.set('1024', self.the_user_data.SerializeToString())
        self.r.save()
        '''
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
        self.server_operation(event_msg)


    def check_usr(self, event_msg):
        self.sign_message_deal.emit(event_msg)

    def uploadfile(self, filename):
        Filename = "./server_redis_operation/user_json/"+filename+".json"
        with open(Filename, 'r')as f:
            str1 = f.read()
            r = json.loads(str1)
        event_msg = ['', '']
        event_msg[1] = r
        event_msg[0] = str1.__sizeof__()
        self.sign_send.emit(event_msg)
        f.close()

    def server_start(self):
        self.ss = Tcpserver()
        # 绑定地址，端口
        self.ss.listen(QHostAddress('0.0.0.0'), 10086)
        # tcpServer接受到信息，在界面表示出来，就绑定slot_recv，但是转发那一层就不用在这里表示出来了
        self.ss.sign_server_recv.connect(self.slot_recv)
        self.sign_send.connect(self.ss.sign_server_send)
        print("listen")


    def retranslateUi(self, Server):
        _translate = QtCore.QCoreApplication.translate
        Server.setWindowTitle(_translate("Server", "MainWindow"))

    def slot_recv(self, event_msg):
        self.server_operation(event_msg)



    def slot_send(self, event_msg):
        print("sending……")
        self.sign_send.emit(event_msg)

    def server_operation(self, mes_3):
        logging.basicConfig(level=logging.DEBUG)
        LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
        logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)
        LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
        DATE_FORMAT = "%m/%d/%Y %H:%M:%S %p"

        redis_1 = redis_operation.RedisOperation()
        smc_1 = server_message_creat.ServerMessageCreator()
        json_1 = json_operation.JsonServer()

        mes = im_1.GeneralMessages()
        # mes_4 = str.encode(mes_3[2:])
        mes.ParseFromString(str.encode(mes_3[2:]))
        # print(mes_3[0:2], "00")
        if op.eq(mes_3[0:2], "00"):
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
                        mes_send.DATA = json_1.send_json(mes_data.ID)
                        event_data = mes_send.SerializeToString()
                        event_msg = bytes.decode(event_data)
                        self.slot_send("00" + event_msg)
                        # write json to data(update json)
                    else:
                        mes_send = smc_1.signup(mes, 2)
                        logging.info(mes_send)
                        event_msg = bytes.decode(mes_send.SerializeToString())
                        self.slot_send("00" + event_msg)
                        # send(mes_send, mes.SIP)
                else:
                    mes_send = smc_1.signup(mes, 3)
                    logging.info(mes_send)
                    event_msg = bytes.decode(mes_send.SerializeToString())
                    self.slot_send("00" + event_msg)
            if op.eq(mes.RC, "001001"):
                # signin
                logging.info(mes)
                mes_data = im_1.gm_signup()
                mes_data.ParseFromString(mes.DATA)
                if not redis_1.check_id_exists(mes_data.ID):
                    redis_1.user_login(mes_data.ID, mes_data.PSW)
                    mes_send = smc_1.signup(mes, 1)
                    logging.info(mes_send)
                    json_1.login_json(mes_data.ID)
                    mes_send.DATA = json_1.send_json(mes_data.ID)
                    mes_send_bytes = mes_send.SerializeToString()
                    event_msg = bytes.decode(mes_send_bytes)
                    self.slot_send("00" + event_msg)
                else:
                    mes_send = smc_1.login(mes, 2)
                    logging.info(mes_send)
                    mes_send_bytes = mes_send.SerializeToString()
                    event_msg = bytes.decode(mes_send_bytes)
                    self.slot_send("00" + event_msg)
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
                    mes_send.DATA = json_1.send_json(mes_data.ID)
                    event_msg = bytes.decode(mes_send.SerializeToString())
                    self.slot_send("00" + event_msg)
                    # send(mes_send_SID)
                    # send double json to SID,DID
                if op.eq(mes.SC, '00010'):
                    mes_send_SID = smc_1.add_friend(mes, mes_data, 4)
                    event_msg = bytes.decode(mes_send.SerializeToString())
                    self.slot_send("00" + event_msg)
                    # send(mes_send_SID)

                if redis_1.check_id_exists(mes_data.DID):
                    mes_send_DID = smc_1.add_friend(mes, mes_data, 1)
                    mes_send_bytes = mes_send_DID.SerializeToString()
                    event_msg = bytes.decode(mes_send_bytes)
                    self.slot_send("00" + event_msg)
                    # send(mes_send_DID)

                else:
                    mes_send = smc_1.add_friend(mes, mes_data, 3)
                    logging.info(mes_send)
                    event_msg = bytes.decode(mes_send.SerializeToString())
                    self.slot_send("00" + event_msg)
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
                    mes_send.DATA = json_1.send_json(mes_data.SID)
                    event_msg = bytes.decode(mes_send.SerializeToString())
                    self.slot_send("00" + event_msg)
                    # send(mes_send)
                    # send double json to SID,DID
                else:
                    mes_send = smc_1.add_friend(mes, mes_data, 2)
                    logging.info(mes_send)
                    event_msg = bytes.decode(mes_send.SerializeToString())
                    self.slot_send("00" + event_msg)
                    # send(mes_send)
        else:
            logging.info("啥玩意？")
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

