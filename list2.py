# Second Example for List Widget
# Try to get Checkable list items

from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.Qt import Qt

import sys
from os import path

form_class, _ = loadUiType(path.join(path.dirname("__file__"), "List2.ui"))
to_do_list = ['Dialysis Process',  'Lecture with Jinay', 'Guide to Hetu fpr Board Exam']

class Main(QMainWindow, form_class):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.updateTaskList()
        self.btnAdd.clicked.connect(self.add_task)
        self.btnSort.clicked.connect(self.sortList)
        self.btnEdit.clicked.connect(self.edit_item)


    def updateTaskList(self):
        for task in to_do_list:
            item = QListWidgetItem(task)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget.addItem(item)

    def add_task(self):
        newTask, ok = QInputDialog.getText(self, "New Task", "Enter New Task")
        print(newTask)

        if ok and newTask is not None:
            self.listWidget.clear()
            to_do_list.append(newTask)
            self.updateTaskList()


    def sortList(self):
        self.listWidget.sortItems()


    def edit_item(self):
        curIndex = self.listWidget.currentRow()
        item = self.listWidget.item(curIndex)
        if item is not None :
            new_name, ok = QInputDialog.getText(self,"Edit task","Task Details", QLineEdit.Normal, item.text())
            if new_name and ok is not None :
                item.setText(new_name)


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


main()