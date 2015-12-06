# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(869, 300)
        MainWindow.setMinimumSize(QtCore.QSize(869, 300))
        MainWindow.setMaximumSize(QtCore.QSize(869, 300))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.table = QtGui.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(40, 30, 781, 192))
        self.table.setRowCount(0)
        self.table.setColumnCount(6)
        self.table.setObjectName(_fromUtf8("table"))
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setDefaultSectionSize(130)
        self.table.horizontalHeader().setMinimumSectionSize(50)
        self.table.verticalHeader().setVisible(False)
        self.cancel_btn = QtGui.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(30, 240, 113, 32))
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        self.save_btn = QtGui.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(140, 240, 113, 32))
        self.save_btn.setObjectName(_fromUtf8("save_btn"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.table.setSortingEnabled(True)
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Asset Name", None))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Owner", None))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Status", None))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Notes", None))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Due Date", None))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Requester", None))
        self.cancel_btn.setText(_translate("MainWindow", "Cancel", None))
        self.save_btn.setText(_translate("MainWindow", "Save", None))

