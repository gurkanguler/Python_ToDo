from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
import main
import error



class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        LoginWindow.setObjectName("LoginWindow")
        LoginWindow.resize(500, 360)
        self.centralwidget = QtWidgets.QWidget(LoginWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.usernameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameEdit.setGeometry(QtCore.QRect(10, 30, 471, 41))
        self.usernameEdit.setObjectName("usernameEdit")
        self.passwordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordEdit.setGeometry(QtCore.QRect(10, 130, 471, 41))
        self.passwordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordEdit.setObjectName("passwordEdit")
        self.LoginBtn = QtWidgets.QPushButton(self.centralwidget)
        self.LoginBtn.setGeometry(QtCore.QRect(10, 200, 461, 51))
        self.LoginBtn.setObjectName("LoginBtn")
        self.RegisterBtn = QtWidgets.QPushButton(self.centralwidget)
        self.RegisterBtn.setGeometry(QtCore.QRect(60, 260, 361, 41))
        self.RegisterBtn.setObjectName("RegisterBtn")
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LoginWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 22))
        self.menubar.setObjectName("menubar")
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LoginWindow)
        self.statusbar.setObjectName("statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(LoginWindow)

        self.LoginBtn.clicked.connect(self.Login)

    def retranslateUi(self, LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
        self.usernameEdit.setPlaceholderText(_translate("LoginWindow", "Username"))
        self.passwordEdit.setPlaceholderText(_translate("LoginWindow", "Password"))
        self.LoginBtn.setText(_translate("LoginWindow", "Login"))
        self.RegisterBtn.setText(_translate("LoginWindow", "Register"))

    def Main_Open(self):
        self.Main_Window = QtWidgets.QMainWindow()
        self.Main_Window_Ui = main.Ui_Main_Window()
        self.Main_Window_Ui.setupUi(self.Main_Window)
        self.username = self.usernameEdit.text()
      
        self.Main_Window.show()

    def Error_Open(self):
        self.Error_Window = QtWidgets.QMainWindow()
        self.Error_Window_Ui = error.Ui_MainWindow()
        self.Error_Window_Ui.setupUi(self.Error_Window)
        self.Error_Window.show()

    def Login(self):
        self.username = self.usernameEdit.text()
        self.password = self.passwordEdit.text()
        self.conn = sqlite3.connect('db.db')
        self.cur = self.conn.cursor()

        self.query = ('SELECT * FROM user WHERE name="%s" and password="%s"' % (self.username,self.password))
       
        self.cur.execute(self.query)
        if self.cur.fetchone() is not None:
            self.Main_Open()
        else:
            self.Error_Open()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QMainWindow()
    ui = Ui_LoginWindow()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())

