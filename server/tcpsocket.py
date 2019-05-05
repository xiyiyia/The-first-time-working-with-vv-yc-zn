from PyQt5.QtNetwork import QTcpSocket, QAbstractSocket
from PyQt5.QtCore import QDataStream, pyqtSignal, QByteArray, QIODevice

SIZE_OF_UINT16 = 2


class TcpSocket(QTcpSocket):

    sign_recv = pyqtSignal(str, str)
    sign_send = pyqtSignal(str, str)

    def __init__(self, socket_id, parent=None):
        super(TcpSocket, self).__init__(parent)
        self.socket_id = socket_id

        # 监听端口，有信息过来就触发该信号
        self.readyRead.connect(self.slot_readyRead)
        # 该信号被触发就会激活发送函数
        self.sign_send.connect(self.slot_send)

    def slot_readyRead(self):
        # 定义最小接受长度
        print("come")
        min_block_size = SIZE_OF_UINT16

        while self.state() == QAbstractSocket.ConnectedState:
            stream = QDataStream(self)
            # 如果可接受字符串比这个更小就直接丢弃
            if self.bytesAvailable() >= min_block_size:
                # 读取接下来信息流的长度，因为信息流第一个位置写入的是长度，为UInt16类型
                nextblock_size = stream.readUInt16()
            else:
                break
            # 如果 nextblock_size 比这个还小说明接受错误
            if nextblock_size <= min_block_size:
                break
            event_id = stream.readQString()
            event_msg = stream.readQString()
            self.sign_recv.emit(event_id, event_msg)

    def slot_send(self, event_id, event_msg):
        print("send")
        print(event_msg)
        # 定义一个字节列表
        reply = QByteArray()
        # 使用QDateaStream向列表写入
        stream = QDataStream(reply, QIODevice.WriteOnly)
        # 为什么接受的最小长度是2个字节，是因为这里收尾都写入了0
        stream.writeUInt16(0)
        stream.writeQString(event_id)
        stream.writeQString(event_msg)
        stream.writeUInt16(0)

        # 寻找到首部的0，写入字节流的真实长度
        stream.device().seek(0)
        stream.writeUInt16(reply.size() - SIZE_OF_UINT16)

        # 发送
        self.write(reply)
