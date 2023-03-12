# This coding will cover concept of List Widget
# Add, Edit, Delete, up, down, sort

from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.Qt import Qt

import sys
from os import path

form_class, _ = loadUiType(path.join(path.dirname("__file__"), "List1.ui"))

class Main(QMainWindow, form_class):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)


        self.loadItems()
        self.Button_Handler()
        #self.List_Hnadler()


    def loadItems(self):
        # following line will add values to list widget when program execure
        category = ['T-Shirt','Shirt','Jackets', 'Trousers', 'Jeans']
        #for catgr in category :
        self.list1.addItems(category)

        # following line will highlight value in the list when program execute
        self.list1.setCurrentRow(1)

    def Button_Handler(self):
        self.btnAdd.clicked.connect(self.add_item)
        self.btnEdit.clicked.connect(self.edit_item)
        self.btnDelete.clicked.connect(self.delete_item)
        self.btnUP.clicked.connect(self.moveUP)
        self.btnDown.clicked.connect(self.moveDown)
        self.btnSort.clicked.connect(self.sortItem)


    def add_item(self):
        currentRow = self.list1.currentRow()
        newItem, ok = QInputDialog.getText(self,"New Item", "Enter New Item Name")
        print(newItem)
        if ok and newItem is not None :
            self.list1.insertItem(currentRow+1,newItem)

    def edit_item(self):
        curIndex = self.list1.currentRow()
        item = self.list1.item(curIndex)
        if item is not None :
            new_name, ok = QInputDialog.getText(self,"Edit Item","Item Name", QLineEdit.Normal, item.text())
            if new_name and ok is not None :
                item.setText(new_name)

    def delete_item(self):
        currentRow = self.list1.currentRow()
        item = self.list1.item(currentRow)

        if item is None :
            return

        response = QMessageBox.question(self,"Remove Item","Do You Want to Remove Item - " + item.text() + " ??",
                                        QMessageBox.Yes | QMessageBox.No)

        if response == QMessageBox.Yes :
            item = self.list1.takeItem(currentRow)
            del item

    def moveUP(self):
        curRow = self.list1.currentRow()

        if curRow >= 1 :
            curItem = self.list1.takeItem(curRow)
            self.list1.insertItem(curRow-1,curItem)
            self.list1.setCurrentItem(curItem)


    def moveDown(self):
        curRow = self.list1.currentRow()
        count_item = self.list1.count()
        print(count_item)
        if curRow < count_item - 1 :
            curItem = self.list1.takeItem(curRow)
            self.list1.insertItem(curRow+1,curItem)
            self.list1.setCurrentItem(curItem)

    def sortItem(self):
        self.list1.sortItems()





def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


main()