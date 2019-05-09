# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI-kerboros.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys


class show_Kerberos(object):
    def setupUi(self, Form,msg):
        Form.setObjectName("Form")
        Form.resize(359, 290)
        self.msg = msg
        self.textBrowser = QTextBrowser(Form)
        self.textBrowser.setGeometry(QRect(20, 20, 321, 211))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton =QPushButton(Form)
        self.pushButton.setGeometry(QRect(140, 250, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)
        self.textBrowser.append(self.msg)
        self.pushButton.clicked.connect(Form.close)

    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Kerberos"))
        self.pushButton.setText(_translate("Form", "确定"))

if __name__ == '__main__':
    # 创建页面实例对象
    app = QApplication(sys.argv)
    form = QWidget()
    ui= show_Kerberos()
    msg='asdasfr\ngargera\nhaerh\nerhae\nrhegdfvgrehes\nhehrtj\nrjrtnstbr\ntrthrstjrjrjs\nthbsrtbtrhsthsh\ndfbsdb\ndbdtshd\nrshsdr\nhbdf'
    ui.setupUi(form,msg)
    form.show()

    sys.exit(app.exec_())
