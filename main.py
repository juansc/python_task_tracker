from PyQt4 import QtGui  # Import the PyQt4 module we'll need
import sys  # We need sys so that we can pass argv to QApplication
import design  # This file holds our MainWindow and all design related things
import csv
# it also keeps events etc that we defined in Qt Designer
import os  # For listing directory methods

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class taskNotification(QtGui.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Explaining super is out of the scope of this article
        # So please google it if you're not familar with it
        # Simple reason why we use it here is that it allows us to
        # access variables, methods etc in the design.py file
        self.file_name = None
        self.string_to_match = None
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
        # It sets up layout and widgets that are defined
        self.setup_table()

    def setup_table(self):
        tasks = []
        with open('tool_files.csv', 'rb') as csvfile:
            file_reader = csv.reader(csvfile, delimiter=',')
            for row in file_reader:
                tasks.append(row)

        number_of_tasks = len(tasks) - 1
        self.table.setRowCount(number_of_tasks)
        for row in range(1, number_of_tasks + 1):
            for col in range(0, number_of_tasks):
                item = QtGui.QTableWidgetItem()
                self.table.setItem(row - 1, col, item)
                item.setText(_translate("MainWindow", tasks[row][col], None))



def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = taskNotification()  # We set the form to be our stringFinder (design)
    form.show()  # Show the form
    app.exec_()  # and execute the app


if __name__ == '__main__':  # if we're running file directly and not importing it
    main()  # run the main function