
from PyQt5.QtNetwork import QTcpSocket, QAbstractSocket
from PyQt5.QtCore import QDataStream, pyqtSignal, QByteArray, QIODevice

PORT = 10086
SIZE_OF_UINT16 = 2


class MyTcpsocket(QTcpSocket):
    sign_send = pyqtSignal(str)
    sign_recv = pyqtSignal(str)
    MIP = ''

    def __init__(self, parent=None):
        super(MyTcpsocket, self).__init__(parent)
        self.connectToHost('localhost', PORT)
        self.readyRead.connect(self.slot_receive)
        self.sign_send.connect(self.slot_send)

    def slot_receive(self):
        print("recv")
        min_block_size = SIZE_OF_UINT16
        while self.state() == QAbstractSocket.ConnectedState:
            stream = QDataStream(self)

            if self.bytesAvailable() >= min_block_size:
                nextblock_size = stream.readUInt16()

            else:
                break
            if nextblock_size < min_block_size:
                break
            # Event_id = stream.readQString()
            Event_msg = stream.readQString()
            print(Event_msg)
            self.sign_recv.emit(Event_msg)

    def slot_send(self, event_msg):
        reply = QByteArray()
        stream = QDataStream(reply, QIODevice.WriteOnly)
        stream.writeUInt16(0)
        # stream.writeQString(event_id)
        stream.writeQString(event_msg)
        stream.writeUInt16(0)
        stream.device().seek(0)
        stream.writeUInt16(reply.size() - SIZE_OF_UINT16)
        self.write(reply)
