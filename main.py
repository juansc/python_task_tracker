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

class ComboBoxNoWheel(QtGui.QComboBox):
    def wheelEvent (self, event):
        event.ignore()



class taskNotification(QtGui.QMainWindow, task_viewer.Ui_taskViewer):
    def __init__(self):
        self.data = []
        self.csv_file = 'tool_files.csv'
        self.email_window = None

        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically

        self.setup_table()
        self.setup_connections()


    def setup_connections(self):
        self.cancel_btn.clicked.connect(self.close)
        self.table.cellChanged.connect(self.update_table_and_notify)

    def update_table_and_notify(self):
        self.send_notification()
        self.update_data()
        self.write_to_csv_file()

    def update_data(self):
        status_col = 4
        row = self.table.currentRow()
        original_row = self.table.item(row, 0).original_row
        num_of_rows = self.table.columnCount()
        for col in range(0, num_of_rows):
            if col == status_col:
                self.data[original_row][col] = str(self.table.cellWidget(row, col).currentText())
            else:
                self.data[original_row][col] = str(self.table.item(row, col).text())

    def send_notification(self):
        status_col, notes_col = 4, 5

        row = self.table.currentRow()
        original_row = self.table.item(row, 0).original_row
        num_of_rows = self.table.columnCount()

        current_row_data = []

        for col in range(0, num_of_rows):
            if col == status_col:
                current_row_data.append(str(self.table.cellWidget(row, col).currentText()))
            else:
                current_row_data.append(str(self.table.item(row, col).text()))

        prev_status = self.data[original_row][status_col]
        new_status = current_row_data[status_col]
        prev_notes = self.data[original_row][notes_col]
        new_notes = current_row_data[notes_col]

        message = ""

        if prev_status != new_status:
            message += "Status changed from '%s' to '%s'\n" % (prev_status, new_status)
        if prev_notes != new_notes:
            message += "Notes changed from '%s' to '%s'\n" % (prev_notes, new_notes)


        recipient = str(self.table.item(row, 2).text())
        subject = "Task for Asset \'%s\' Changed" % str(self.table.item(row, 0).text())
        email_string = (  "=====================\n"
                    "From: mail.service@company.com\n"
                    "To: %s@company.com\n"
                    "Subject: %s\n"
                    "Message:\n"
                    "%s"
                    "=====================\n" % (recipient, subject, message))
        print email_string

    def closeEvent(self, event):
        sys.exit(0)

    def setup_table(self):
        task_statuses = ['In Progress', 'Completed', 'On Hold', 'Cancelled']
        drop_down_col = 4
        disabled_columns = [0, 1, 2, 3]

        tasks = self.read_csv_file()
        self.data = tasks[1:]

        self.write_to_table(tasks)
        self.disable_columns(disabled_columns)
        self.add_drop_down_cells_for_col(drop_down_col, task_statuses)

    def disable_columns(self, disabled_columns):
        for row in range(0, self.table.rowCount()):
            for col in disabled_columns:
                item = self.table.item(row, col)
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

    def write_to_table(self, tasks):
        number_of_columns = len(tasks[0])
        number_of_tasks = len(tasks) - 1
        self.table.setRowCount(number_of_tasks)

        for row in range(1, number_of_tasks + 1):
            for col in range(0, number_of_columns):
                item = QtGui.QTableWidgetItem()
                item.original_row = row - 1
                self.table.setItem(row - 1, col, item)
                item.setText(_translate("MainWindow", tasks[row][col], None))

    def add_drop_down_cells_for_col(self, column, values):
        number_of_tasks = self.table.rowCount()
        for row in range(0, number_of_tasks):
            combo = ComboBoxNoWheel()
            for value in values:
                combo.addItem(value)

            currentVal = str(self.table.item(row, column).text())
            if currentVal in values:
                combo.setCurrentIndex(combo.findText(currentVal))

            combo.container = self.table.item(row, column)
            combo.currentIndexChanged.connect(self.set_current_table_cell)
            self.table.setCellWidget(row, column,combo)

    def set_current_table_cell(self):
        current_row = self.sender().container.row()
        self.table.setCurrentCell(current_row, 0)
        self.update_table_and_notify()

    def save_changes(self):
        self.write_to_csv_file()
        self.send_email()

    def read_csv_file(self):
        tasks = []
        with open(self.csv_file, 'rbU') as csvfile:
            file_reader = csv.reader(csvfile, delimiter=',')
            for row in file_reader:
                tasks.append(row)
        return tasks


    def write_to_csv_file(self):
        data = list(self.data)
        headers = ['Asset Name', 'Assigned To', 'Requester', 'Due Date', 'Status', 'Notes']
        data.insert(0, headers)
        with open(self.csv_file, 'wb') as f:
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
        self.email_window = emailWindow(self)
        self.email_window.exec_()


def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = taskNotification()  # We set the form to be our mainWindow (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function