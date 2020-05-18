from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Add_Window(object):
    def setupUi(self, Add_Window):
        Add_Window.setObjectName("Add_Window")
        Add_Window.resize(598, 425)
        self.centralwidget = QtWidgets.QWidget(Add_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.addTxt = QtWidgets.QLineEdit(self.centralwidget)
        self.addTxt.setGeometry(QtCore.QRect(20, 40, 551, 51))
        self.addTxt.setObjectName("addTxt")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(20, 140, 551, 51))
        self.addBtn.setObjectName("addBtn")
        Add_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Add_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 598, 22))
        self.menubar.setObjectName("menubar")
        Add_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Add_Window)
        self.statusbar.setObjectName("statusbar")
        Add_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Add_Window)
        QtCore.QMetaObject.connectSlotsByName(Add_Window)

        self.addBtn.clicked.connect(self.Add)

    def retranslateUi(self, Add_Window):
        _translate = QtCore.QCoreApplication.translate
        Add_Window.setWindowTitle(_translate("Add_Window", "Add"))
        self.addTxt.setPlaceholderText(_translate("Add_Window", "New To Do"))
        self.addBtn.setText(_translate("Add_Window", "Add"))

    def Add(self):
        self.add_txt = self.addTxt.text()
        self.conn = sqlite3.connect('db.db')
        self.cur = self.conn.cursor()
        self.query = ("INSERT INTO user(todo) VALUES('%s')" % self.add_txt)
        self.cur.execute(self.query)
        self.conn.commit()
        if self.cur.rowcount:
            print("Inserted")
        else:
            print("Error")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Add_Window = QtWidgets.QMainWindow()
    ui = Ui_Add_Window()
    ui.setupUi(Add_Window)
    Add_Window.show()
    sys.exit(app.exec_())

