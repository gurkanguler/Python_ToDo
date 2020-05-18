import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import add
import delete

class Ui_Main_Window(object):

    def Show_Data(self):
        self.conn = sqlite3.connect("db.db")
        self.query =('SELECT * FROM user')
        self.result = self.conn.execute(self.query)
        self.listWidget.setRowCount(0)
        for self.row_num,self.row_data in enumerate(self.result):
            self.listWidget.insertRow(self.row_num)
            for self.col_num,self.data in enumerate(self.row_data):
                self.listWidget.setItem(self.row_num,self.col_num,QtWidgets.QTableWidgetItem(str(self.data)))

  
    def setupUi(self, Main_Window):
        Main_Window.setObjectName("Main_Window")
        Main_Window.resize(723, 623)
        self.centralwidget = QtWidgets.QWidget(Main_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(20, 30, 191, 41))
        self.addBtn.setObjectName("addBtn")
        self.deleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteBtn.setGeometry(QtCore.QRect(270, 30, 191, 41))
        self.deleteBtn.setObjectName("deleteBtn")
        self.updateBtn = QtWidgets.QPushButton(self.centralwidget)
        self.updateBtn.setGeometry(QtCore.QRect(490, 30, 191, 41))
        self.updateBtn.setObjectName("updateBtn")
        self.showBtn = QtWidgets.QPushButton(self.centralwidget)
        self.showBtn.setGeometry(QtCore.QRect(20, 490, 661, 41))
        self.showBtn.setObjectName("showBtn")
        self.listWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 80, 661, 381))
        self.listWidget.setRowCount(20)
        self.listWidget.setColumnCount(4)
        self.listWidget.setObjectName("listWidget")
        Main_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Main_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 723, 22))
        self.menubar.setObjectName("menubar")
        Main_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Main_Window)
        self.statusbar.setObjectName("statusbar")
        Main_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Main_Window)
        QtCore.QMetaObject.connectSlotsByName(Main_Window)
        self.showBtn.clicked.connect(self.Show_Data)

        self.addBtn.clicked.connect(self.Add)
        self.deleteBtn.clicked.connect(self.Delete)

    def retranslateUi(self, Main_Window):
        _translate = QtCore.QCoreApplication.translate
        Main_Window.setWindowTitle(_translate("Main_Window", "TO DO"))
        self.addBtn.setText(_translate("Main_Window", "Add"))
        self.deleteBtn.setText(_translate("Main_Window", "Delete"))
        self.updateBtn.setText(_translate("Main_Window", "Update"))
        self.showBtn.setText(_translate("Main_Window", "Show"))

    def Add(self):
        self.Add_Window = QtWidgets.QMainWindow()
        self.Add_Window_Ui = add.Ui_Add_Window()
        self.Add_Window_Ui.setupUi(self.Add_Window)
        self.Add_Window.show() 

    def Delete(self):
        self.Delete_Window = QtWidgets.QMainWindow()
        self.Delete_Window_Ui = delete.Ui_Delete_Window()
        self.Delete_Window_Ui.setupUi(self.Delete_Window)
        self.Delete_Window.show() 

   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Main_Window = QtWidgets.QMainWindow()
    ui = Ui_Main_Window()
    ui.setupUi(Main_Window)
    Main_Window.show()
    sys.exit(app.exec_())

