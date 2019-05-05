from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtNetwork import QHostInfo

from client.Qtcpsocket import MyTcpsocket


class Thread(QThread):

    sign_thread_recv = pyqtSignal(str, str)
    sign_thread_send = pyqtSignal(str, str)
    sign_thread_start = pyqtSignal(str)
    hostname = ''

    def _init_(self, parent=None):
        super(QThread, self)._init_(parent)

    def run(self):
        #       获取IP
        socket = MyTcpsocket()
        socket.sign_recv.connect(self.sign_thread_recv)
        self.sign_thread_send.connect(socket.sign_send)

        hostname = QHostInfo.localHostName()
        info = QHostInfo.fromName(hostname)
        self.sign_thread_start.emit(info.addresses()[0].toString())
        self.exec_()



