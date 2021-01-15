from main.register import Ui_registerUi
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread
import sqlite3
from passlib.context import CryptContext


class key:
    pwd_context = CryptContext(
        schemes=["pbkdf2_sha256"],
        default="pbkdf2_sha256",
        pbkdf2_sha256__default_rounds=30000)

    def __init__(self):
        pass


class Crypt(QThread):
    def __init__(self, username, password):
        super(Crypt, self).__init__()
        self.username = username
        self.password = password

    def run(self):
        self.connection = sqlite3.connect('db/programme_data.db')
        self.connection.execute("INSERT INTO USERS VALUES(?,?,?)",
                                (0, self.encrypt_username(), self.encrypt_password()))
        self.connection.commit()
        self.connection.close()

    def encrypt_password(self):
        return key.pwd_context.encrypt(self.password)

    def encrypt_username(self):
        return key.pwd_context.encrypt(self.username)


class MainRegister(QMainWindow, Ui_registerUi):
    switch_window = pyqtSignal()

    def __init__(self, parent=None):
        super(MainRegister, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.password_problem = QMessageBox()
        self.ok = QMessageBox()
        self.Ui()
        self.Buttons()
        self.save = None
        self.main_programme = None
        self.show()

    def Ui(self):
        self.password_problem.setWindowTitle('Erreur de mot de passe')
        self.password_problem.setText('Le mot de passe ne ressemble pas à une réinitialisation')
        self.password_problem.setInformativeText('la longueur du mot de passe doit être supérieure à quatre')
        self.password_problem.setIcon(QMessageBox.Warning)
        self.password_problem.setStandardButtons(QMessageBox.Ok)
        self.ok.setWindowTitle('Inscription')
        self.ok.setText('Inscription terminée correctement')
        self.ok.setIcon(QMessageBox.Information)
        self.ok.setStandardButtons(QMessageBox.Ok)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_2.setEchoMode(QtWidgets.QLineEdit.Password)

    def Buttons(self):
        self.save.clicked.connect(self.createAccount)

    def createAccount(self):
        if self.password_2.text() == self.password.text() and len(self.password.text()) >= 4:
            self.save = Crypt(self.username.text(), self.password.text())
            self.save.start()
            self.save.finished.connect(self.login)
        else:
            self.password_problem.exec_()
            self.password.clear()
            self.password_2.clear()

    def login(self):
        self.switch_window.emit()


if __name__ == '__main__':
    pass
