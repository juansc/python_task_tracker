from PyQt4 import QtCore, QtGui  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication
import task_viewer, email_window  # This file holds our MainWindow and all design related things
import csv
from operator import itemgetter
# it also keeps events etc that we defined in Qt Designer
import os  # For listing directory methods

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class taskNotification(QtGui.QMainWindow, task_viewer.Ui_taskViewer):
    def __init__(self):
        self.data = []
        self.modified_rows = []
        self.csv_file = 'tool_files.csv'
        self.target_file = 'test.csv'

        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically

        self.setup_table()
        self.setup_connections()
        self.table.cellChanged.connect(self.data_has_been_changed)
        self.newWindow = None

    def setup_connections(self):
        self.table.cellChanged.connect(self.data_has_been_changed)
        self.cancel_btn.clicked.connect(self.close)
        self.save_btn.clicked.connect(self.save_changes)

    def close_app(self):
        self.close()


    def data_has_been_changed(self):
        modified_row = self.table.currentRow()
        row_contents = []

        for col in range(0, self.table.columnCount()):
            text = str(self.table.item(modified_row, col).text())
            row_contents.append(text)

        is_row_changed = sum(i != j for i, j in zip(row_contents, self.data[modified_row])) > 0
        self.modified_rows[modified_row] = is_row_changed

    def read_csv_file(self):
        tasks = []
        with open(self.csv_file, 'rb') as csvfile:
            file_reader = csv.reader(csvfile, delimiter=',')
            for row in file_reader:
                tasks.append(row)
        return tasks

    def setup_table(self):
        tasks = self.read_csv_file()

        self.data = tasks[1:]

        number_of_columns = len(tasks[0])
        number_of_tasks = len(tasks) - 1
        self.modified_rows = [False] * number_of_tasks
        self.table.setRowCount(number_of_tasks)

        for row in range(1, number_of_tasks + 1):
            for col in range(0, number_of_columns):
                item = QtGui.QTableWidgetItem()
                self.table.setItem(row - 1, col, item)
                item.setText(_translate("MainWindow", tasks[row][col], None))

        disabled_columns = [0, 1, 4, 5]

        for row in range(0, number_of_tasks):
            for col in disabled_columns:
                item = self.table.item(row, col)
                item.setFlags(QtCore.Qt.ItemIsEnabled)

    def save_changes(self):
        self.write_to_csv_file()
        self.send_email()

    def write_to_csv_file(self):
        data = self.get_data_from_table()
        headers = ['Asset Name','Owner','Status','Notes','Due Date','Requester']
        data.insert(0, headers)
        with open(self.target_file, 'wb') as f:
            writer = csv.writer(f)
            writer.writerows(data)



    def get_data_from_table(self):
        data = []
        row_data = []
        num_of_rows = self.table.rowCount()
        num_of_cols = self.table.columnCount()

        for row in range(0, num_of_rows):
            row_data = []
            for col in range(0, num_of_cols):
                row_data.append(str(self.table.item(row, col).text()))
            data.append(row_data)

        return data


    def send_email(self):
        self.newWindow = emailWindow()
        self.newWindow.show()

class emailWindow(QtGui.QMainWindow, email_window.Ui_sendEmail):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.setup_connections()

    def setup_connections(self):
        self.send_btn.clicked.connect(self.send_email)
        self.dont_send_btn.clicked.connect(self.close)

    def send_email(self):
        print "We sent the following email."

def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = taskNotification()  # We set the form to be our mainWindow (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function