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

class Ui_SendEmail(object):
    def setupUi(self, SendEmail):
        SendEmail.setObjectName(_fromUtf8("SendEmail"))
        SendEmail.resize(692, 448)
        self.layoutWidget = QtGui.QWidget(SendEmail)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 20, 611, 396))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(36, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.recipient_text = QtGui.QLineEdit(self.layoutWidget)
        self.recipient_text.setObjectName(_fromUtf8("recipient_text"))
        self.horizontalLayout_4.addWidget(self.recipient_text)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem1 = QtGui.QSpacerItem(34, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.cc_text = QtGui.QLineEdit(self.layoutWidget)
        self.cc_text.setObjectName(_fromUtf8("cc_text"))
        self.horizontalLayout_3.addWidget(self.cc_text)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_4 = QtGui.QLabel(self.layoutWidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        spacerItem2 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.bcc_text = QtGui.QLineEdit(self.layoutWidget)
        self.bcc_text.setObjectName(_fromUtf8("bcc_text"))
        self.horizontalLayout_2.addWidget(self.bcc_text)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem3 = QtGui.QSpacerItem(6, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.subject_text = QtGui.QLineEdit(self.layoutWidget)
        self.subject_text.setObjectName(_fromUtf8("subject_text"))
        self.horizontalLayout.addWidget(self.subject_text)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_5 = QtGui.QLabel(self.layoutWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.message_body_text = QtGui.QTextEdit(self.layoutWidget)
        self.message_body_text.setObjectName(_fromUtf8("message_body_text"))
        self.verticalLayout.addWidget(self.message_body_text)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem4 = QtGui.QSpacerItem(400, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.cancel_btn = QtGui.QPushButton(self.layoutWidget)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.horizontalLayout_5.addWidget(self.cancel_btn)
        self.send_btn = QtGui.QPushButton(self.layoutWidget)
        self.send_btn.setObjectName(_fromUtf8("send_btn"))
        self.horizontalLayout_5.addWidget(self.send_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.retranslateUi(SendEmail)
        QtCore.QMetaObject.connectSlotsByName(SendEmail)

    def retranslateUi(self, SendEmail):
        SendEmail.setWindowTitle(_translate("SendEmail", "Form", None))
        self.label.setText(_translate("SendEmail", "To:", None))
        self.label_3.setText(_translate("SendEmail", "Cc:", None))
        self.label_4.setText(_translate("SendEmail", "Bcc:", None))
        self.label_2.setText(_translate("SendEmail", "Subject:", None))
        self.label_5.setText(_translate("SendEmail", "Message:", None))
        self.cancel_btn.setText(_translate("SendEmail", "Cancel", None))
        self.send_btn.setText(_translate("SendEmail", "Send", None))

