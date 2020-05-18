import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Delete_Window(object):
    def Show_Data(self):
        self.conn = sqlite3.connect("db.db")
        self.query =('SELECT * FROM user')
        self.result = self.conn.execute(self.query)
        self.tableWidget.setRowCount(0)
        for self.row_num,self.row_data in enumerate(self.result):
            self.tableWidget.insertRow(self.row_num)
            for self.col_num,self.data in enumerate(self.row_data):
                self.tableWidget.setItem(self.row_num,self.col_num,QtWidgets.QTableWidgetItem(str(self.data)))

    def setupUi(self, Delete_Window):
        Delete_Window.setObjectName("Delete_Window")
        Delete_Window.resize(685, 478)
        self.centralwidget = QtWidgets.QWidget(Delete_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 661, 181))
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.numberEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.numberEdit.setGeometry(QtCore.QRect(20, 240, 651, 41))
        self.numberEdit.setObjectName("numberEdit")
        self.deleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteBtn.setGeometry(QtCore.QRect(20, 320, 651, 51))
        self.deleteBtn.setObjectName("deleteBtn")
        Delete_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Delete_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 685, 22))
        self.menubar.setObjectName("menubar")
        Delete_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Delete_Window)
        self.statusbar.setObjectName("statusbar")
        Delete_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Delete_Window)
        QtCore.QMetaObject.connectSlotsByName(Delete_Window)

        self.Show_Data()

        self.deleteBtn.clicked.connect(self.Delete)

    def retranslateUi(self, Delete_Window):
        _translate = QtCore.QCoreApplication.translate
        Delete_Window.setWindowTitle(_translate("Delete_Window", "Delete"))
        self.numberEdit.setPlaceholderText(_translate("Delete_Window", "Enter to Number"))
        self.deleteBtn.setText(_translate("Delete_Window", "Delete"))

    def Delete(self):
        self.number = int(self.numberEdit.text())
        self.conn = sqlite3.connect("db.db")
        self.cur = self.conn.cursor()
        self.query = ('DELETE FROM user WHERE id = "%s"'%self.number)
        self.cur.execute(self.query)
        self.conn.commit()
        if self.cur.rowcount:
            print("Deleted")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Delete_Window = QtWidgets.QMainWindow()
    ui = Ui_Delete_Window()
    ui.setupUi(Delete_Window)
    Delete_Window.show()
    sys.exit(app.exec_())

