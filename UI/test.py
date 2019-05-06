import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import chat2
import socket

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


class Login(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
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
        # 账号和密码
        self.lineedit_id = QLineEdit()
        self.lineedit_id.setPlaceholderText("账号")
        self.account = self.lineedit_id.text()
        self.lineedit_password = QLineEdit()
        self.lineedit_password.setEchoMode(QLineEdit.Password)
        self.lineedit_password.setPlaceholderText("密码")
        self.passwd = self.lineedit_password.text()
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
        # 密码隐藏

    def yanma(self):
        if self.btn_check.isChecked():
            self.lineedit_password.setEchoMode(QLineEdit.Normal)
        else:
            self.lineedit_password.setEchoMode(QLineEdit.Password)
        # 登录时核查账号及密码是否正确

    def check(self):
        self.passwd = self.lineedit_password.text()
        self.account = self.lineedit_id.text()
    #   self.sign_slot.emit("000001"+self.account,self.passwd,get_host_ip())
        print("000001"+self.account,self.passwd,get_host_ip())

##########################################################################################

    def slot_recv(self,msg):
        msg_2 = msg #获取状态码
        if(msg_2=='666666'):            #这个成功分为登录成功和注册成功 登录成功则self.show() 注册成功则self.idnewclose()
            replay = QMessageBox.warning(self, "!", "成功", QMessageBox.Yes) #这里可以加入kerberos的字符串
            self.close()
            self.idnewclose()
        if (msg_2 == '00100'):
            replay = QMessageBox.warning(self, "!", "账号不存在", QMessageBox.Yes)
            quit()
        if (msg_2 == '00001'):
            replay = QMessageBox.warning(self, "!", "账号密码错误", QMessageBox.Yes)
            quit()
        if (msg_2 == '00011'):
            replay = QMessageBox.warning(self, "!", "账号已存在", QMessageBox.Yes)
            quit()
        replay = QMessageBox.warning(self, "!", "未知错误", QMessageBox.Yes)

    ##########################################################################################

    # 创建新的账号
    def idnew(self):
        self.hide()
        self.label_idnew_id = QLabel("账号")
        self.label_idnew_password = QLabel("密码")
        self.lineedit_idnew_id = QLineEdit()

        self.lineedit_idnew_password = QLineEdit()


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
        self.new_account = self.lineedit_idnew_id.text()
        self.new_passwd = self.lineedit_idnew_password.text()
    #   self.sign_slot('001001'+ self.new_account, self.new_passwd, get_host_ip())





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

    def handle_click(self):
        if not self.isVisible():
            self.show()




class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(495, 405)

        self.listWidget = QListWidget(Form)
        self.listWidget.setGeometry(QRect(220, 50, 261, 311))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.itemClicked.connect(self.click_item)

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

        self.getname_line = QLineEdit(Form)
        self.getname_line.setGeometry(QRect(40, 60, 141, 31))
        self.getname_line.setObjectName("get_name")
        self.getname_line.setPlaceholderText("请输入账号名")
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
        self.pushButton.clicked.connect(self.add_friend)

        self.load_friend()


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    """
    def rightMenu(self):
        rightMenu = QMenu(self.listWidget)
        removeAction = QAction(u"删除好友", triggered=self.delete_friend)
        rightMenu.addAction(removeAction)

        addAction = QAction(u"发起聊天",  triggered=self.start2chat)  # 也可以指定自定义对象事件
        rightMenu.addAction(addAction)
        rightMenu.exec_(QCursor.pos())
    """

    def click_item(self,item):
        QMessageBox.information(self.listWidget, "ListWidget", "你选择了: " + item.text())

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "好友列表"))
        #self.welcome_label.setText(_translate("Form", "welcome to gayhub"))
        self.pushButton.setText(_translate("Form", "确定"))


    def load_friend(self):
        #read account.json
        #test
        #把json文件中的好友信息全部读到列表中
        self.myname = self.getname_line.text()
        #open self.myname.json
        #self.listWidget.addItem(account + IP + SIP)   用空格分开
        self.listWidget.addItem("2016 192.168.0.0 1")
        self.listWidget.addItem("2017 192.168.0.1 1")
        self.listWidget.addItem("2018 192.168.0.2 1")


    def delete_friend(self,item):
        #row = self.listWidget.currentRow()
        print(self.listWidget.currentItem().text())
        self.str = self.listWidget.currentItem().text()
        self.del_name = self.str.split(" ")[0]
        print(self.del_name)
        #########self.sign_slot.emit("000011"+self.del_name+get_host_ip())

        #send friend's account to server
        #load client.json
        #self.listWidget.addItem("account ip sip")


    def start2chat(self):
        self.str = self.listWidget.currentItem().text()
        self.chat_friend = self.str.split(" ")[0]
        self.friend_IP = self.str.split(" ")[2]



    def add_friend(self):

        self.addfriend_name = self.lineEdit.text()
    #   self.sign_slot.emit('000010'+self.addfriend_name,get_host_ip())
    #   self.listWidget.addItem("account ip sip")
        pass



    ######################################################################################
    def slot_recv(self,msg):
        msg_1 = msg             #处理报文 分离出状态码
        if (msg_1 == '666666'):
            replay = QMessageBox.warning(self, "!", "成功", QMessageBox.Yes)
            self.load_friend()  #只要是成功就要更新好友列表
        if (msg_1 == '00100'):
            replay = QMessageBox.warning(self, "!", "账号不存在", QMessageBox.Yes)
            #这个是添加好友 账号不存在 可以继续输入正确账号
        if (msg_1 == '00010'):
            replay = QMessageBox.warning(self, "!", "好友请求被拒绝", QMessageBox.Yes)
        replay = QMessageBox.warning(self, "!", "未知错误"+msg_1, QMessageBox.Yes)
    ######################################################################################



if __name__ == '__main__':
    # 创建页面实例对象
    app = QApplication(sys.argv)
    #mp = MainPage()  # 主页
    lg = Login()  # 登陆界面
    lg.show()
    print("lg "+lg.account)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)

    form1 = QWidget()
    ui1 = chat2.fuck()
    ui1.setupUi(form1)



    def rightMenu():
        rightMenu = QMenu(ui.listWidget)
        removeAction = QAction(u"删除好友", triggered=ui.delete_friend)
        rightMenu.addAction(removeAction)

        addAction = QAction(u"发起聊天", triggered=form1.show)  # 也可以指定自定义对象事件
        rightMenu.addAction(addAction)
        rightMenu.exec_(QCursor.pos())

    ui.listWidget.customContextMenuRequested[QPoint].connect(rightMenu)


    lg.btn_denglu.clicked.connect(Form.show)


    sys.exit(app.exec_())
