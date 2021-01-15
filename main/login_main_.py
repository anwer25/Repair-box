from main.login import Ui_MainLoagin
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QLineEdit
from PyQt5.QtCore import QThread, pyqtSignal
import sqlite3 as sql
from main.register_ import key

class Dcrypt(QThread):
    state = pyqtSignal(bool)

    def __init__(self, username, password, dbusername, dbpassword):
        super(Dcrypt, self).__init__()
        self.username = username
        self.password = password
        self.dbusername = dbusername
        self.dbpassword = dbpassword

    def run(self):
        if self.Dencrypt_password() and self.Dencrypt_username():
            self.state.emit(True)
        else:
            self.state.emit(False)

    def Dencrypt_password(self):
        return key.pwd_context.verify(self.password, self.dbpassword)

    def Dencrypt_username(self):
        return key.pwd_context.verify(self.username, self.dbusername)


class MainLogin(QMainWindow, Ui_MainLoagin):
    switch_window = pyqtSignal()
    def __init__(self, parent=None):
        super(MainLogin, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.worker = None
        self.connect = sql.connect('db/programme_data.db')
        self.error = QMessageBox()
        self.Ui()
        self.Buttons()
        self.show()

    def Ui(self):
        self.error.setWindowTitle("Problème de mot de passe")
        self.error.setText("Mot de passe ou nom d'utilisateur erroné")
        self.error.setIcon(QMessageBox.Warning)
        self.error.setStandardButtons(QMessageBox.Ok)
        self.password.setEchoMode(QLineEdit.Password)


    def Buttons(self):
        self.login_Button.clicked.connect(self.login)

    def login(self):
        self.data = self.connect.cursor()
        self.dbusername = None
        self.dbpassword = None

        for user_name in self.data.execute("SELECT USERNAME FROM USERS"):
            # return from from data is tupl this why i convert it to string

            self.dbusername = str(user_name)[2:-3]
        for password in self.data.execute("SELECT PASSWORD FROM USERS"):
            #print("password from lop: ",password)
            self.dbpassword = str(password)[2:-3]
        #print("dbusername: ", self.dbusername,"\ndbpassword: ",self.dbpassword, "\nusername",self.username.text(),"\npassword", self.password.text())

        self.worker = Dcrypt(self.username.text(), self.password.text(), self.dbusername, self.dbpassword)
        self.worker.start()
        self.worker.state.connect(self.signal)

    def signal(self, state):
        if state:
            self.switch_window.emit()
        else:
            self.error.exec_()
            self.username.clear()
            self.password.clear()

if __name__ == '__main__':
    """
    # For debug
    import sys
    app = QApplication(sys.argv)
    windo = MainLogin()
    sys.exit(app.exec_())
    """