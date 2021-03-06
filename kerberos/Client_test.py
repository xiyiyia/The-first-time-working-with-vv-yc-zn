import gayhub.kerberos.des_encryption as des_en
import gayhub.kerberos.des_decryption as des_de
import gayhub.kerberos.Tstr as tostr
import gayhub.kerberos.UI as ui
import socket
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QLabel, QCheckBox
import sys
import time


class QW(QWidget):
    message1 = ''
    message2_Plaintext = ''
    message2_Ciphertext = ''
    message3 = ''
    message4_Plaintext = ''
    message4_Ciphertext = ''
    message5 = ''
    message6_Plaintext = ''
    message6_Ciphertext = ''


    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #reply = QMessageBox.critical(self, '提醒', '这是一个提醒消息对话框', QMessageBox.Retry , QMessageBox.Retry)
        """msgBox = QMessageBox()
        msgBox.setWindowTitle('提醒')
        msgBox.setText("这是一条来自AS发送到Client的报文！！！")
        msgBox.setStandardButtons(QMessageBox.Retry)
        msgBox.setDefaultButton(QMessageBox.Ignore)
        msgBox.setDetailedText('message2_Plaintext = '+self.message2_Plaintext+ '\n'+ 'Key_client = '+self.Key_client +'message2_Ciphertext = '+self.message2_Ciphertext +'\n\n'+'ticket_tgs_plaintext = '+self.ticket_tgs_Plaintext+'\n'+'ticket_tgs_ciphertext = '+self.ticket_tgs_Ciphertext)
        reply = msgBox.exec()

        if reply == QMessageBox.Ignore:
            self.la.setText('你选择了Ignore！')"""

        self.setGeometry(300, 300, 330, 300)
        self.setWindowTitle('ClientClientClient')
        self.la = QLabel('这里是kerberos验证的加密解密细节呈现'+'\n'+'AS发送到Client的报文', self)
        self.la.move(20, 20)
        self.bt1 = QPushButton('明文密文', self)
        self.bt1.move(120, 80)
        self.bt2 = QPushButton('细节显示', self)
        self.bt2.move(120, 140)
        self.bt3 = QPushButton('来向去向', self)
        self.bt3.move(120, 200)
        self.bt1.clicked.connect(self.aboutMC)
        self.bt2.clicked.connect(self.aboutdetail)
        self.bt3.clicked.connect(self.fromandgoto)

        self.show()
    def aboutMC(self):
        self.form = QWidget()
        self.ui = ui.show_Kerberos()
        self.ui.setupUi(self.form,
                        'message1 = '+self.message1+
                          '\nmessage2_Ciphertext = '+self.message2_Ciphertext+
                          '\nmessage2_Plaintext = '+self.message2_Plaintext+
                          '\nmessage3 = ' + self.message3 +
                          '\nmessage4_Ciphertext = ' + self.message4_Ciphertext +
                          '\nmessage4_Plaintext = ' + self.message4_Plaintext +
                          '\nmessage5 = ' + self.message5 +
                          '\nmessage6_Ciphertext=\n'+self.message6_Ciphertext+
                          '\nmessage6_Plaintext=\n'+self.message6_Plaintext)
        self.form.show()
    def aboutdetail(self):
        self.form = QWidget()
        self.ui = ui.show_Kerberos()
        self.ui.setupUi(self.form,
                          'message1 = ' + self.message1 +
                          '\nmessage2_Ciphertext = ' + self.message2_Ciphertext +
                          '\nmessage2_Plaintext = ' + self.message2_Plaintext +
                          '\nmessage3 = ' + self.message3 +
                          '\nmessage4_Ciphertext = ' + self.message4_Ciphertext +
                          '\nmessage4_Plaintext = ' + self.message4_Plaintext +
                          '\nmessage5 = ' + self.message5 +
                          '\nmessage6_Ciphertext=\n' + self.message6_Ciphertext +
                          '\nmessage6_Plaintext=\n' + self.message6_Plaintext
                          )
        self.form.show()
    def fromandgoto(self):

        QMessageBox.about(self,'来源和去向','这是Client对于加密解密的显示！！！')




def Client_to_AS():
    ip_Client = tostr.get_host_ip()
    ip_Client = tostr.ip_tostr(ip_Client)
    print("ip = ", ip_Client)

    ip_TGS = "192.168.43.203"
    ip_TGS = tostr.ip_tostr(ip_TGS)
    print("ip_TGS = ", ip_TGS)

    ts1 = time.time()
    ts1 = tostr.ts_tostr(ts1)
    print("ts1 = ", ts1)

    #str_ClienttoAS = tostr.IntegrationMessage.ClientAS(ip_Client, ip_TGS, ts1)
    str_ClienttoAS = ip_Client + ip_TGS + ts1
    print("str_Client = ", str_ClienttoAS)

    return str_ClienttoAS


def get_Authencator(Key_ctgs):
    ip_Client = tostr.get_host_ip()
    ip_Client = tostr.ip_tostr(ip_Client)

    AD_c = ip_Client

    ts3 = time.time()
    ts3 = tostr.ts_tostr(ts3)

    authencator = ip_Client + AD_c + ts3
    authencator = des_en.test(authencator, Key_ctgs)

    return authencator,ts3


def Client_to_TGS(ticket_TGS, Key_ctgs):
    ip_Server = '192.168.43.204'  # 如何获取SERVER端的IP呢************************************************

    ip_Server = tostr.ip_tostr(ip_Server)

    Authenticator_c,ts = get_Authencator(Key_ctgs)

    message = ip_Server + ticket_TGS + Authenticator_c
    return message,str(len(ticket_TGS))


def Client_to_Server(ticket_Server, Key_cv):
    Authencator_c,ts5 = get_Authencator(Key_cv)

    message = ticket_Server + Authencator_c
    return message, len(ticket_Server),ts5


def CLIENT():
    Key_c = 'abcdefg'  # Key_Client
    message1 = Client_to_AS()
    QW.message1 = message1
    localhost = socket.gethostname()
    port_AS = 10000
    port_TGS = 10001
    port_Server = 10002
    print("mesage1 = ", message1)

    """s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((localhost,port_AS))
    s.send(message1.encode('utf-8'))
    message2 = s.recv(1024)
    message2 = message2.decode()
    print("message2 = ",message2)
    s.close()
    """

    message2 = 'D3A41D74DCE667CAD3D397336CC8B2EE06A8308066127732963DDC58C3F3DF748B228F7BA7E3BE4498B3A781D438F4A6D937FF4846783646DCB15C599E2C137B4C6BD9E917992E6C1DE2F71066632786C9ECEE38802F6F2F16D117AF055D5D2BBA65D636AC72197B2D153F9464FCC9D25297DE32E7C88507BF8D27EC72472C15F4E418C00D3AE157D17B2A230E64D2A84AA3FCDF931C1BC5D1250522F2248F8D63D6C82291CEF3855D2734C685D0EDF2277144ED594DE71E9694E606D0D8AFB4AD0E6439F7333D2E47AAA1EB7B5E0CDCE9AB683C1432B9B0'
    QW.message2_Ciphertext = message2
    message2 = des_de.test(message2, Key_c)
    QW.message2_Plaintext = message2
    print("message2 = ", message2)
    Key_ctgs = message2[0:7]
    print("Key_ctgs = ", Key_ctgs)

    ip_TGS_fromAS = message2[7:22]
    ip_TGS_fromAS = tostr.takeout(ip_TGS_fromAS)
    print("ip_TGS = ", ip_TGS_fromAS)

    ts2 = message2[22:40]
    ts2 = tostr.takeout(ts2)
    ts2 = float(ts2)
    print("ts2 = ", ts2)

    lifetime2 = message2[40:48]
    lifetime2 = tostr.takeout_0(lifetime2)
    print("lifetime2 = ", lifetime2)

    ticket_TGS = message2[48:]
    print("ticket_TGS = ", ticket_TGS)
    # 给TGS发送报文

    message3,lenofticket_tgs = Client_to_TGS(ticket_TGS,Key_ctgs)
    print("message3 = ", message3)
    QW.message3 = message3
    print("lenofticket = ", lenofticket_tgs)
    # 发送报文到TGS，再把lenofticket也发送过去
    """tgs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("1")
    tgs.connect(("localhost", port_TGS))
    print("2")
    tgs.send(message3.encode('utf-8'))
    print("3")
    time.sleep(1)
    tgs.send(lenofticket_tgs.encode('utf-8'))
    message4 = tgs.recv(1024)
    message4 = message4.decode()
    print("message4 = ", message4)
    tgs.close()"""
    # 从TGS接收到message4
    message4 = '60E1C1DEE89D50B5D76FA69341FB845BEA16784472B24B617BE5BA3DC2EEF8361EBB8BC4B2E29F03245E7E6D4E1E395DCA003EA2D338A5B8ED4513868C3B44B6D97E9E0137F47BB9FAA319BB4DFAD05F12B14A2E081ED644BDEC148EF5C878E63995026084D974DE320273D2B4FFC3C2D688C2A4A4946A5C65197A570A5E4DA5F7242F37BD68F4A85DCED3BFB43AA654A51CD2E64D6242A64FBAEFFB277B8AC7F0049D4E7C2692584AF898BD0826F7C9BA2EFDF1DD8A8262CC130C743E83F60867D77BE9F9CC2B0E7358F0ED7796932F'
    QW.message4_Ciphertext = message4
    message4 = des_de.test(message4, Key_ctgs)
    QW.message4_Plaintext = message4
    message4 = tostr.takeout(message4)
    print("message4 = ", message4)
    lenofmessage4 = len(message4)
    Key_cv = message4[0:7]
    print("Key_cv = ", Key_cv)

    ip_Server = message4[7:22]
    ip_Server = tostr.takeout(ip_Server)
    print("ip_Server = ", ip_Server)

    ts4 = message4[22:40]
    ts4 = tostr.takeout(ts4)
    print("ts4 = ", ts4)

    ticket_Server = message4[40:lenofmessage4]

    print("ticket_Server = ", ticket_Server)

    message5, lenofticket_server, ts5 = Client_to_Server(ticket_Server, Key_cv)
    QW.message5 = message5
    lenofticket_server = str(lenofticket_server)
    ts5 = tostr.takeout(ts5)
    ts5 = float(ts5)
    print("message5 = ", message5)
    print("lenofticket_server = ", lenofticket_server)
    print("ts5 = ", ts5)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect(("localhost", port_Server))
    server.send(message5.encode('utf-8'))
    time.sleep(1)
    server.send(lenofticket_server.encode('utf-8'))
    message6 = server.recv(1024)
    message6 = message6.decode()
    print("message6 = ", message6)
    server.close()
    QW.message6_Ciphertext = message6
    message6 = des_de.test(message6, Key_cv)
    QW.message6_Plaintext = message6
    ts6 = tostr.takeout(message6)
    ts6 = float(ts6)
    print("ts6 = ", ts6)

    if 1 == ts6-ts5:
        print("Get server authentication!!!")
    else:
        print("The authentication of server is wrong!!!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    CLIENT()
    qw = QW()
    sys.exit(app.exec())