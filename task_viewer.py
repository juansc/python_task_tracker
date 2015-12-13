# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task_viewer.ui'
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

class Ui_taskViewer(object):
    def setupUi(self, taskViewer):
        taskViewer.setObjectName(_fromUtf8("taskViewer"))
        taskViewer.resize(1099, 565)
        taskViewer.setMinimumSize(QtCore.QSize(869, 300))
        taskViewer.setMaximumSize(QtCore.QSize(10000, 10000))
        self.centralwidget = QtGui.QWidget(taskViewer)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.table = QtGui.QTableWidget(self.centralwidget)
        self.table.setGeometry(QtCore.QRect(40, 20, 1031, 481))
        self.table.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.table.setAutoFillBackground(False)
        self.table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
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
        self.table.horizontalHeader().setCascadingSectionResizes(True)
        self.table.horizontalHeader().setDefaultSectionSize(130)
        self.table.horizontalHeader().setHighlightSections(True)
        self.table.horizontalHeader().setMinimumSectionSize(50)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setCascadingSectionResizes(False)
        self.cancel_btn = QtGui.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(960, 520, 113, 32))
        self.cancel_btn.setMouseTracking(False)
        self.cancel_btn.setObjectName(_fromUtf8("cancel_btn"))
        taskViewer.setCentralWidget(self.centralwidget)

        self.retranslateUi(taskViewer)
        QtCore.QMetaObject.connectSlotsByName(taskViewer)

    def retranslateUi(self, taskViewer):
        taskViewer.setWindowTitle(_translate("taskViewer", "Task Viewer", None))
        self.table.setSortingEnabled(True)
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("taskViewer", "Asset Name", None))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("taskViewer", "Assigned To", None))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("taskViewer", "Requester", None))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("taskViewer", "Due Date", None))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("taskViewer", "Status", None))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("taskViewer", "Notes", None))
        self.cancel_btn.setText(_translate("taskViewer", "Close", None))

