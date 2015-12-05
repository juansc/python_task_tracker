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
        MainWindow.resize(869, 364)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.table = QtGui.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(40, 70, 781, 192))
        self.table.setRowCount(1)
        self.table.setColumnCount(6)
        self.table.setObjectName(_fromUtf8("table"))
        item = QtGui.QTableWidgetItem()
        self.table.setVerticalHeaderItem(0, item)
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
        item = QtGui.QTableWidgetItem()
        self.table.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        self.table.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.table.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        self.table.setItem(0, 3, item)
        item = QtGui.QTableWidgetItem()
        self.table.setItem(0, 4, item)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setCascadingSectionResizes(False)
        self.table.horizontalHeader().setDefaultSectionSize(130)
        self.table.horizontalHeader().setMinimumSectionSize(50)
        self.table.verticalHeader().setVisible(False)
        self.add_row_btn = QtGui.QPushButton(self.centralwidget)
        self.add_row_btn.setGeometry(QtCore.QRect(240, 310, 113, 32))
        self.add_row_btn.setObjectName(_fromUtf8("add_row_btn"))
        self.delete_row_tb = QtGui.QPushButton(self.centralwidget)
        self.delete_row_tb.setGeometry(QtCore.QRect(400, 310, 113, 32))
        self.delete_row_tb.setObjectName(_fromUtf8("delete_row_tb"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.table.setSortingEnabled(True)
        item = self.table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Juan", None))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Asset Name", None))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Assigned To", None))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Owner", None))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Status", None))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Due Date", None))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Notes", None))
        __sortingEnabled = self.table.isSortingEnabled()
        self.table.setSortingEnabled(False)
        item = self.table.item(0, 0)
        item.setText(_translate("MainWindow", "Juan", None))
        item = self.table.item(0, 1)
        item.setText(_translate("MainWindow", "Liz", None))
        item = self.table.item(0, 2)
        item.setText(_translate("MainWindow", "Stuff", None))
        item = self.table.item(0, 4)
        item.setText(_translate("MainWindow", "Nice", None))
        self.table.setSortingEnabled(__sortingEnabled)
        self.add_row_btn.setText(_translate("MainWindow", "Add Row", None))
        self.delete_row_tb.setText(_translate("MainWindow", "Delete Row", None))

