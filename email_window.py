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
        self.widget = QtGui.QWidget(sendEmail)
        self.widget.setGeometry(QtCore.QRect(50, 30, 431, 361))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.Recipient = QtGui.QHBoxLayout()
        self.Recipient.setObjectName(_fromUtf8("Recipient"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.Recipient.addWidget(self.label)
        self.recipient_txt = QtGui.QLineEdit(self.widget)
        self.recipient_txt.setEnabled(True)
        self.recipient_txt.setObjectName(_fromUtf8("recipient_txt"))
        self.Recipient.addWidget(self.recipient_txt)
        self.verticalLayout.addLayout(self.Recipient)
        self.Subject = QtGui.QHBoxLayout()
        self.Subject.setObjectName(_fromUtf8("Subject"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Subject.addWidget(self.label_2)
        self.subject_text = QtGui.QLineEdit(self.widget)
        self.subject_text.setObjectName(_fromUtf8("subject_text"))
        self.Subject.addWidget(self.subject_text)
        self.verticalLayout.addLayout(self.Subject)
        self.EmailBody = QtGui.QVBoxLayout()
        self.EmailBody.setObjectName(_fromUtf8("EmailBody"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.EmailBody.addWidget(self.label_3)
        self.message_body = QtGui.QTextBrowser(self.widget)
        self.message_body.setReadOnly(False)
        self.message_body.setObjectName(_fromUtf8("message_body"))
        self.EmailBody.addWidget(self.message_body)
        self.verticalLayout.addLayout(self.EmailBody)
        self.widget1 = QtGui.QWidget(sendEmail)
        self.widget1.setGeometry(QtCore.QRect(280, 400, 184, 32))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.buttons = QtGui.QHBoxLayout(self.widget1)
        self.buttons.setObjectName(_fromUtf8("buttons"))
        self.dont_send_btn = QtGui.QPushButton(self.widget1)
        self.dont_send_btn.setObjectName(_fromUtf8("dont_send_btn"))
        self.buttons.addWidget(self.dont_send_btn)
        self.send_btn = QtGui.QPushButton(self.widget1)
        self.send_btn.setObjectName(_fromUtf8("send_btn"))
        self.buttons.addWidget(self.send_btn)
        self.label.raise_()
        self.recipient_txt.raise_()
        self.label_2.raise_()
        self.subject_text.raise_()
        self.label_3.raise_()
        self.message_body.raise_()
        self.dont_send_btn.raise_()
        self.send_btn.raise_()
        self.message_body.raise_()

        self.retranslateUi(sendEmail)
        QtCore.QMetaObject.connectSlotsByName(sendEmail)

    def retranslateUi(self, sendEmail):
        sendEmail.setWindowTitle(_translate("sendEmail", "Send Email", None))
        self.label.setText(_translate("sendEmail", "To:", None))
        self.label_2.setText(_translate("sendEmail", "Subject:", None))
        self.label_3.setText(_translate("sendEmail", "Message:", None))
        self.dont_send_btn.setText(_translate("sendEmail", "Don\'t Send", None))
        self.send_btn.setText(_translate("sendEmail", "Send", None))

