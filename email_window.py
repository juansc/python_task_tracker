# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'email_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
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

class Ui_sendEmail(object):
    def setupUi(self, sendEmail):
        sendEmail.setObjectName(_fromUtf8("sendEmail"))
        sendEmail.resize(543, 446)
        sendEmail.setMaximumSize(QtCore.QSize(543, 446))
        self.layoutWidget = QtGui.QWidget(sendEmail)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 30, 431, 361))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Recipient = QtGui.QHBoxLayout()
        self.Recipient.setObjectName(_fromUtf8("Recipient"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.Recipient.addWidget(self.label)
        self.recipient_text = QtGui.QLineEdit(self.layoutWidget)
        self.recipient_text.setEnabled(True)
        self.recipient_text.setObjectName(_fromUtf8("recipient_text"))
        self.Recipient.addWidget(self.recipient_text)
        self.verticalLayout.addLayout(self.Recipient)
        self.Subject = QtGui.QHBoxLayout()
        self.Subject.setObjectName(_fromUtf8("Subject"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Subject.addWidget(self.label_2)
        self.subject_text = QtGui.QLineEdit(self.layoutWidget)
        self.subject_text.setObjectName(_fromUtf8("subject_text"))
        self.Subject.addWidget(self.subject_text)
        self.verticalLayout.addLayout(self.Subject)
        self.EmailBody = QtGui.QVBoxLayout()
        self.EmailBody.setObjectName(_fromUtf8("EmailBody"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.EmailBody.addWidget(self.label_3)
        self.message_body = QtGui.QTextBrowser(self.layoutWidget)
        self.message_body.setReadOnly(False)
        self.message_body.setObjectName(_fromUtf8("message_body"))
        self.EmailBody.addWidget(self.message_body)
        self.verticalLayout.addLayout(self.EmailBody)
        self.layoutWidget1 = QtGui.QWidget(sendEmail)
        self.layoutWidget1.setGeometry(QtCore.QRect(280, 400, 184, 32))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.buttons = QtGui.QHBoxLayout(self.layoutWidget1)
        self.buttons.setObjectName(_fromUtf8("buttons"))
        self.dont_send_btn = QtGui.QPushButton(self.layoutWidget1)
        self.dont_send_btn.setObjectName(_fromUtf8("dont_send_btn"))
        self.buttons.addWidget(self.dont_send_btn)
        self.send_btn = QtGui.QPushButton(self.layoutWidget1)
        self.send_btn.setObjectName(_fromUtf8("send_btn"))
        self.buttons.addWidget(self.send_btn)

        self.retranslateUi(sendEmail)
        QtCore.QMetaObject.connectSlotsByName(sendEmail)

    def retranslateUi(self, sendEmail):
        sendEmail.setWindowTitle(_translate("sendEmail", "Send Email", None))
        self.label.setText(_translate("sendEmail", "To:", None))
        self.label_2.setText(_translate("sendEmail", "Subject:", None))
        self.label_3.setText(_translate("sendEmail", "Message:", None))
        self.dont_send_btn.setText(_translate("sendEmail", "Don\'t Send", None))
        self.send_btn.setText(_translate("sendEmail", "Send", None))

