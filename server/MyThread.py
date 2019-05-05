from PyQt5.QtCore import pyqtSignal, QThread

from server.tcpsocket import TcpSocket


class Thread(QThread):

    sign_thread_recv = pyqtSignal(str, str)
    sign_thread_send = pyqtSignal(str, str)

    def __init__(self, socket_id, parent=None):
        super(Thread, self).__init__(parent)
        self.socket_id = socket_id

    def run(self):
        socket = TcpSocket(self.socket_id)
        if not socket.setSocketDescriptor(self.socket_id):
            return
        print("thread")
        socket.sign_recv.connect(self.sign_thread_recv)
        self.sign_thread_send.connect(socket.sign_send)
        self.exec_()
