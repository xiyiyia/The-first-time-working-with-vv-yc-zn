from PyQt5.QtNetwork import QTcpServer
from PyQt5.QtCore import pyqtSignal, pyqtSlot


from server.MyThread import Thread

PATH = "~/gay/hub/bin"


class Tcpserver(QTcpServer):

    sign_server_recv = pyqtSignal(str, str)
    sign_send = pyqtSignal(str, str)

    def __init__(self, parent=None):
        super(Tcpserver, self).__init__(parent)
        self.sip_list = []
       # self.sign_server_recv.connect(self.slot_recv)

    def incomingConnection(self, sip_voidptr):
        if sip_voidptr not in self.sip_list:
            self.sip_list.append(sip_voidptr)
            # 开启一个线程
        print("incoming")
        self.thread = Thread(sip_voidptr)
        self.thread.start()
        # thread中接受信息的信号连接到tcpServer中的接受信号
        self.thread.sign_thread_recv.connect(self.sign_server_recv)
        # 转发信号要连接到各个线程中的发送信号
        self.sign_send.connect(self.thread.sign_thread_send)

    # def slot_recv(self, event_id, event_msg):
    #     print("thread",event_msg)
    #     self.sign_send.emit(event_id, event_msg)

