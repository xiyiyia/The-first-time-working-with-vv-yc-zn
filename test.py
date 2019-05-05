import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import chat2
from PyQt5.QtCore import pyqtSignal, Qt
import time
from multiprocessing import Process
from client.src.Mythread import Thread
import json

account = ''
passwd = ''
# 主页

# class MainPage(QWidget):
#
#
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(500, 50, 0, 0)
#         self.setWindowTitle('')
#         self.setWindowIcon(QIcon('icon.jpg'))
#         self.resize(300, 300)
#         self.loginButton = QPushButton(self)
#         self.loginButton.setText("登陆")  # text
#         self.loginButton.setIcon(QIcon("close.png"))  # icon
#         self.loginButton.setShortcut('Ctrl+D')  # shortcut key
#         self.loginButton.clicked.connect(self.close)
#         self.loginButton.setToolTip("Login")  # Tool tip
#         self.loginButton.move(50, 100)
#
#         self.registerButton = QPushButton(self)
#         self.registerButton.setText("注册")  # text
#         self.registerButton.setIcon(QIcon("close.png"))  # icon
#         self.registerButton.setShortcut('Ctrl+D')  # shortcut key
#         self.registerButton.clicked.connect(self.close)
#         self.registerButton.setToolTip("Register")  # Tool tip
#         self.registerButton.move(150, 100)
#         self.show()
#     # 跳转到登陆界面


class Login(QWidget):

    sign_recv = pyqtSignal(str, object)
    sign_send = pyqtSignal(str, object)
    sign_cmd = pyqtSignal(str)
    sign_getjson = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        self.initUI()

    def __init__(self):
        super(Login, self).__init__()
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
        Filename = "./" + self.account + ".json"
        with open(Filename, 'w+')as f:
            json.dump(event_msg[1], f, indent=4, ensure_ascii=False)
        f.close()

        # 密码隐藏

    def yanma(self):
        if self.btn_check.isChecked():
            self.lineedit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lineedit_password.setEchoMode(QLineEdit.Password)
        # 登录时核查账号及密码是否正确

    def check_usr(self, str):
        print("check" + self.result)
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
        self.result = Event_msg[0]
        print(self.result)
        if Event_id == '0001':  # 登录
            self.sign_cmd.emit(self.result)
        # if(Event_id == '0002'):  #传输json
        #     self.sign_getjson.emit(Event_msg)

    def client_login(self):  # def client_login(self)
        account = self.lineedit_id.text()
        passwd = self.lineedit_password.text()
        event_msg = [account, passwd]
        self.sign_send.emit("0001", event_msg)
        print("send msg")

    def check(self):
        self.client_login()
        print("11" + self.result)

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
            reply = QMessageBox.warning(self, "!", "账号存在", QMessageBox.Yes)
        elif var == "0101":
            reply = QMessageBox.warning(self, "!", "密码不符合要求", QMessageBox.Yes)

        elif var == "0102":
            reply = QMessageBox.warning(self, "!", "注册成功", QMessageBox.Yes)
            self.idnew.close()
        reply = QMessageBox.warning(self, "!", "未知错误", QMessageBox.Yes)

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


class chatPage(QMainWindow):
    inputSigal = pyqtSignal(str)
    sendMesSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(800, 50, 0, 0)
        self.setWindowTitle('')
        self.setWindowIcon(QIcon('icon.jpg'))
        self.resize(300, 600)
        # 设置中心窗口
        componudWidget = QWidget()
        layout = QGridLayout()
        self.inputText = QTextEdit("输入聊天信息")
        self.inputText.resize(100, 100)
        self.friend_IP = QLineEdit()
        self.friend_IP.setPlaceholderText("好友IP")
        self.miwen = QLineEdit()
        self.miwen.setPlaceholderText("密文")
        self.key = QLineEdit()
        self.key.setPlaceholderText("秘钥")
        self.inputConButton = QPushButton("发送消息")
        self.inputCanBUtton = QPushButton("取消发送")
        self.showText = QTextEdit("message is here")
        self.showText.resize(100, 100)

        layout.addWidget(self.showText)
        layout.addWidget(self.inputText)
        layout.addWidget(self.friend_IP)
        layout.addWidget(self.miwen)
        layout.addWidget(self.key)
        layout.addWidget(self.inputConButton)
        layout.addWidget(self.inputCanBUtton)

        componudWidget.setLayout(layout)
        self.setCentralWidget(componudWidget)
        # 创建触发事件
        self.exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Exit application')
        self.exitAction.triggered.connect(qApp.quit)
        self.indivChatA = QAction(QIcon('exit.png'), '开始聊天', self)
        self.indivChatA.setShortcut("开始聊天")
        self.groupChatA = QAction(QIcon('exit.png'), '创建一个群聊', self)
        self.groupChatA.setShortcut("创建群聊")
        self.eGroupChatA = QAction(QIcon('exit.png'), '开始加入一个群聊', self)
        self.eGroupChatA.setShortcut("加入群聊")
        self.aGroupChatA = QAction(QIcon('exit.png'), '添加一个群聊', self)
        self.aGroupChatA.setShortcut("添加群聊")
        self.upFileA = QAction(QIcon('exit.png'), '上传文件', self)
        self.upFileA.setShortcut("上传文件")
        self.getHelpA = QAction(QIcon('exit.png'), '帮助', self)
        self.getHelpA.setShortcut("帮助")
        # 添加菜单
        self.chat = self.menuBar().addMenu("聊天")
        self.indivChat = self.chat.addMenu("选择个体聊天")
        self.groupChat = self.chat.addMenu("创建群聊")
        self.enterGC = self.chat.addMenu("加入群聊")
        self.addGC = self.chat.addMenu("添加群聊")
        self.up = self.menuBar().addMenu("上传文件")
        self.help = self.menuBar().addMenu("帮助")
        self.chooseUser = self.menuBar().addMenu("选择聊天对象")
        self.quit = self.menuBar().addMenu("退出系统")
        # 为菜单添加Action
        self.indivChat.addAction(self.indivChatA)  # 添加个体聊天Action
        self.groupChat.addAction(self.groupChatA)  # 群聊Action
        self.enterGC.addAction(self.eGroupChatA)  # 加入群聊Action
        self.addGC.addAction(self.aGroupChatA)  # 添加群聊Action
        self.up.addAction(self.upFileA)  # 上传文件Action
        self.help.addAction(self.getHelpA)  # 帮助Action
        # 添加信号槽
        self.inputConButton.clicked.connect(self.sendMessage)
        self.inputCanBUtton.clicked.connect(self.sendMessage)
        self.indivChatA.triggered.connect(lambda: self.emitChatSiganl("cp"))  # 个体聊天触发事件
        self.groupChatA.triggered.connect(lambda: self.emitChatSiganl("cg"))  # 群聊触发事件
        self.eGroupChatA.triggered.connect(lambda: self.emitChatSiganl("eg"))  # 加入一个群聊
        self.aGroupChatA.triggered.connect(lambda: self.emitChatSiganl("ag"))  # 添加一个群聊
        self.upFileA.triggered.connect(self.openFile)  # 上传文件触发事件
        self.getHelpA.triggered.connect(lambda: self.emitChatSiganl("h"))  # 获取帮助触发事件
        self.quit.addAction(self.exitAction)

    def handle_click(self):
        self.showText.setText("聊天内容")
        if not self.isVisible():
            self.show()

    def emitChatSiganl(self, signal):
        self.inputSigal.emit(signal)
        print("lunched now")

    def sendMessage(self):
        message = str(self.inputText.toPlainText())
        target = "max"
        chat(target, message)
        print(message)
        print("message has emited")

    def setText(self, message):
        print(message)
        self.showText.setText(message)

        print(message)

    def openFile(self):
        fileName, filetype = QFileDialog.getOpenFileName(self,
                                                         "选择文件路径",
                                                         "H:/",
                                                         "All Files (*);;Text Files (*.txt)")
        print(fileName)
        target = "max"
        file = open(fileName)
        print("文件打开成功")
        data = file.read(1024)
        print("文件读取成功")
        #sendFile(target, data)
        print("文件发送成功")
        print(fileName)


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(495, 405)

        self.listWidget = QListWidget(Form)
        self.listWidget.setGeometry(QRect(220, 50, 261, 311))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemClicked.connect(self.click_item)
        self.load_friend()
        self.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        #self.listWidget.customContextMenuRequested[QPoint].connect(self.rightMenu)


        self.label = QLabel(Form)
        self.label.setGeometry(QRect(320, 20, 81, 21))
        self.label.setObjectName("label")
        self.dateTimeEdit = QDateTimeEdit(Form)

        self.dateTimeEdit.setGeometry(QRect(10, 20, 194, 26))
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setFrame(False)
        self.dateTimeEdit.setDate(QDate.currentDate())
        self.dateTimeEdit.setTime(QTime.currentTime())
        self.welcome_label = QLabel(Form)
        self.welcome_label.setGeometry(QRect(40, 60, 141, 31))
        self.welcome_label.setObjectName("welcome_label")
        self.id_label = QLabel(Form)
        self.id_label.setGeometry(QRect(70, 100, 67, 17))


        self.id_label.setObjectName("id_label")
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setPlaceholderText("添加好友")
        self.lineEdit.setGeometry(QRect(10, 150, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QPushButton(Form)
        self.pushButton.setGeometry(QRect(140, 150, 61, 21))
        self.pushButton.setObjectName("pushButton")



        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
        '''
        def rightMenu(self):
            rightMenu = QMenu(self.listWidget)
            removeAction = QAction(u"删除好友", triggered=self.delete_friend)
            rightMenu.addAction(removeAction)
    
            addAction = QAction(u"发起聊天",  triggered=self.start2chat)  # 也可以指定自定义对象事件
            rightMenu.addAction(addAction)
            rightMenu.exec_(QCursor.pos())
        '''

    def click_item(self,item):
        QMessageBox.information(self.listWidget, "ListWidget", "你选择了: " + item.text())

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "好友列表"))
        self.welcome_label.setText(_translate("Form", "welcome to gayhub"))
        self.pushButton.setText(_translate("Form", "确定"))


    def load_friend(self):
        #read account.json
        #test
        self.listWidget.addItem("2016 192.168.0.0 1")
        self.listWidget.addItem("2017 192.168.0.1 1")
        self.listWidget.addItem("2018 192.168.0.2 1")


    def delete_friend(self):
        #print(self.listWidget.clicked.text())
        #send friend's account to server
        #load client.json
        #self.listWidget.addItem("account ip sip")
        pass

    def start2chat(self):
        pass



    def add_friend(self):
        # send friend's account to server
        # load client.json
        # self.listWidget.addItem("account ip sip")
        pass


class fuck(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(446, 382)
        self.history_message = QTextEdit(Form)
        self.history_message.setGeometry(QRect(30, 30, 231, 211))
        self.history_message.setObjectName("history_message")
        self.yourmessage = QTextEdit(Form)
        self.yourmessage.setGeometry(QRect(30, 250, 371, 91))
        self.yourmessage.setObjectName("yourmessage")
        self.friendIP = QLineEdit(Form)
        self.friendIP.setGeometry(QRect(280, 34, 151, 21))
        self.friendIP.setObjectName("friendIP")
        self.miwen = QLineEdit(Form)
        self.miwen.setGeometry(QRect(280, 84, 151, 21))
        self.miwen.setObjectName("miwen")
        self.key = QLineEdit(Form)
        self.key.setGeometry(QRect(280, 134, 151, 21))
        self.key.setObjectName("key")
        self.label = QLabel(Form)
        self.label.setGeometry(QRect(30, 10, 67, 17))
        self.label.setObjectName("label")
        self.send_btn = QPushButton(Form)
        self.send_btn.setGeometry(QRect(300, 350, 89, 25))
        self.send_btn.setObjectName("send_btn")
        self.send_btn.clicked.connect(self.send_click)
        self.label_2 = QLabel(Form)
        self.label_2.setGeometry(QRect(310, 10, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel(Form)
        self.label_3.setGeometry(QRect(320, 60, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QLabel(Form)
        self.label_4.setGeometry(QRect(320, 110, 67, 17))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "聊天界面"))
        self.send_btn.setText(_translate("Form", "发送"))
        self.label_2.setText(_translate("Form", "好友IP"))
        self.label_3.setText(_translate("Form", "密文"))
        self.label_4.setText(_translate("Form", "秘钥"))

    def send_click(self):
        #send to my friend
        self.message = self.yourmessage.toPlainText()
        self.yourmessage.insertPlainText(self.message+'\n')
        self.history_message.setText(self.message+'\n')

if __name__ == '__main__':
    # 创建页面实例对象
    app = QApplication(sys.argv)
    #mp = MainPage()  # 主页
    lg = Login()  # 登陆界面
    lg.show()
    #mp.loginButton.clicked.connect(lg.handle_click)
    #mp.loginButton.clicked.connect(mp.hide)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)

    form1 = QWidget()
    ui1 = chat2.fuck()
    ui1.setupUi(form1)


    #re = Register()  # 注册界面
    cp = chatPage()  # 聊天界面


    def rightMenu():
        rightMenu = QMenu(ui.listWidget)
        removeAction = QAction(u"删除好友", triggered=ui.delete_friend)
        rightMenu.addAction(removeAction)

        addAction = QAction(u"发起聊天", triggered=form1.show)  # 也可以指定自定义对象事件
        rightMenu.addAction(addAction)
        rightMenu.exec_(QCursor.pos())

    ui.listWidget.customContextMenuRequested[QPoint].connect(rightMenu)



    #myInputData = inputData()
    #myGetData = getData()
    #mydata = getdata()
    # 将信号绑定到槽
   # mydata.getDataSignal.connect(cp.setText)
    #cp.inputSigal.connect(myInputData.setTarget)

    #mp.registerButton.clicked.connect(re.handle_click)
    #mp.registerButton.clicked.connect(mp.hide)

    lg.btn_denglu.clicked.connect(Form.show)

    #re.confirmButton.clicked.connect(re.sendData)
    #re.confirmButton.clicked.connect(cp.handle_click)
    #lg.cancelButton.clicked.connect(QCoreApplication.quit)

   # cp.sendMesSignal.connect(myInputData.setMessage)
    # 与服务器建立连接，获取链接对象
    #tcpCliSock.connect(ADDR)
    #print('Connected with server')
   # mydata.start()
    sys.exit(app.exec_())