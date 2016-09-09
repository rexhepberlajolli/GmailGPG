# -*- coding: utf-8 -*-

import os
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from PyQt4 import QtCore, QtGui

try:
    serveri = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setFixedSize(1047, 576)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-300, -110, 1461, 691))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("ux/bg.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 0, 351, 121))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("ux/Gmail-logo.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color: rgb(30, 237, 255);"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 20, 281, 31))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("../app/images/message_bar.png")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.emailfield = QtGui.QLineEdit(self.centralwidget)
        self.emailfield.setGeometry(QtCore.QRect(160, 20, 270, 30))
        self.emailfield.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.emailfield.setObjectName(_fromUtf8("emailfield"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(_fromUtf8("color: rgb(30, 237, 255);"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 70, 281, 31))
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("../app/images/message_bar.png")))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.passwordfiled = QtGui.QLineEdit(self.centralwidget)
        self.passwordfiled.setGeometry(QtCore.QRect(160, 70, 270, 30))
        self.passwordfiled.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.passwordfiled.setObjectName(_fromUtf8("passwordfiled"))
        self.passwordfiled.setEchoMode(QtGui.QLineEdit.Password)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-30, 100, 1121, 31))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 140, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("color: rgb(30, 237, 255);"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(160, 140, 271, 31))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setPixmap(QtGui.QPixmap(_fromUtf8("../app/images/message_bar.png")))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.subjectfield = QtGui.QLineEdit(self.centralwidget)
        self.subjectfield.setGeometry(QtCore.QRect(160, 140, 270, 30))
        self.subjectfield.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.subjectfield.setObjectName(_fromUtf8("subjectfield"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(570, 140, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(_fromUtf8("color: rgb(30, 237, 255);"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(620, 140, 281, 31))
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setPixmap(QtGui.QPixmap(_fromUtf8("../app/images/message_bar.png")))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.tofield = QtGui.QLineEdit(self.centralwidget)
        self.tofield.setGeometry(QtCore.QRect(620, 140, 270, 30))
        self.tofield.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.tofield.setObjectName(_fromUtf8("tofield"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(60, 180, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(_fromUtf8("color: rgb(30, 237, 255);"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-40, 280, 271, 321))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("ux/gnupg.png")))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.msgfield = QtGui.QTextEdit(self.centralwidget)
        self.msgfield.setGeometry(QtCore.QRect(110, 220, 911, 281))
        self.msgfield.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);"))
        self.msgfield.setObjectName(_fromUtf8("msgfield"))
        self.loginbutton = QtGui.QPushButton(self.centralwidget)
        self.loginbutton.setGeometry(QtCore.QRect(480, 40, 121, 51))
        self.loginbutton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("ux/login.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.loginbutton.setIcon(icon)
        self.loginbutton.setIconSize(QtCore.QSize(100, 100))
        self.loginbutton.setFlat(True)
        self.loginbutton.setObjectName(_fromUtf8("loginbutton"))
        self.sendbutton = QtGui.QPushButton(self.centralwidget)
        self.sendbutton.setGeometry(QtCore.QRect(880, 510, 121, 51))
        self.sendbutton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("ux/send-button.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sendbutton.setIcon(icon1)
        self.sendbutton.setIconSize(QtCore.QSize(200, 150))
        self.sendbutton.setFlat(True)
        self.sendbutton.setObjectName(_fromUtf8("sendbutton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.loginbutton.clicked.connect(self.login)
        self.sendbutton.clicked.connect(self.sendmail)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_4.setText(_translate("MainWindow", "Email Address :", None))
        self.label_6.setText(_translate("MainWindow", "Password :", None))
        self.label_8.setText(_translate("MainWindow", "Subject :", None))
        self.label_10.setText(_translate("MainWindow", "To :", None))
        self.label_12.setText(_translate("MainWindow", "Message :", None))

        self.subjectfield.setDisabled(True)
        self.tofield.setDisabled(True)
        self.msgfield.setDisabled(True)
        self.sendbutton.setDisabled(True)

    def login(self):
        usr = str(self.emailfield.text())
        pw = str(self.passwordfiled.text())
        try :
            serveri.login(usr,pw)
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(_fromUtf8("ux/logout.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.loginbutton.setIcon(icon2)
            self.subjectfield.setDisabled(False)
            self.tofield.setDisabled(False)
            self.msgfield.setDisabled(False)
            self.sendbutton.setDisabled(False)
        except smtplib.SMTPAuthenticationError :
            print "Authentication Failed"

    def sendmail(self):
        mesazhi = self.msgfield.toPlainText()
        sub = str(self.subjectfield.text())
        recp = str(self.tofield.text())
        os.system("rm msgtoencrypt")
        os.system("rm msgtoencrypt.asc")
        unenc = open("msgtoencrypt", "w")
        unenc.write(mesazhi)
        unenc.close()
        os.system("gpg --armor --encrypt -r %s msgtoencrypt" % recp)
        with open("msgtoencrypt.asc", "r") as myfile:
            data = myfile.read()
        msg = MIMEMultipart()
        msg['From'] = str(self.emailfield.text())
        msg['Subject'] = str(self.subjectfield.text())
        msg['To'] = str(self.tofield.text())
        msg.attach(MIMEText(data, 'plain'))
        text = msg.as_string()
        serveri.sendmail(str(self.emailfield.text()), str(self.tofield.text()), text)
        print "Message Sent"





if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
