# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainLoagin(object):
    def setupUi(self, MainLoagin):
        MainLoagin.setObjectName("MainLoagin")
        MainLoagin.resize(383, 438)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainIcon/icons/movil_05.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainLoagin.setWindowIcon(icon)
        MainLoagin.setStyleSheet("/*-----QWidget-----*/\n"
"QWidget\n"
"{\n"
"    background-color: #0f0f0f;\n"
"    color: #fff;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLabel-----*/\n"
"QLabel\n"
"{\n"
"    background-color: transparent;\n"
"    color: #fff;\n"
"    font-weight: bold;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QPushButton-----*/\n"
"QPushButton\n"
"{\n"
"    background-color: #d10000;\n"
"    color: #fff;\n"
"    font-weight: bold;\n"
"    border: 1px solid #d10000;  \n"
"    border-radius: 2px;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"    background-color: #ad0000;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"QPushButton::pressed\n"
"{\n"
"    background-color: #e00000;\n"
"    color: #fff;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QToolButton-----*/\n"
"QToolButton\n"
"{\n"
"    background-color: transparent;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-color: #000000;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::hover\n"
"{\n"
"    background-color: #d10000;\n"
"    color: #000000;\n"
"    border-radius: 15px;\n"
"    border-color: #d10000;\n"
"\n"
"}\n"
"\n"
"\n"
"QToolButton::pressed\n"
"{\n"
"    background-color: #d10000;\n"
"    color: #000000;\n"
"    border-style: solid;\n"
"    border-width: 0px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QLineEdit-----*/\n"
"QLineEdit{\n"
"    background-color: #4d4d4d;\n"
"    color: #fff;\n"
"    font-weight: bold;\n"
"    border-style: solid;\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"\n"
"}\n"
"\n"
"\n"
"/*-----QCheckBox-----*/\n"
"QCheckBox\n"
"{\n"
"    background-color: transparent;\n"
"    color: #b9b9bb;\n"
"    font-weight: bold;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #00111d;\n"
"    border: 1px solid #d10000;\n"
"    width: 12px;\n"
"    height: 12px;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(\"./ressources/check.png\"); /*To replace*/\n"
"    background-color: #d10000;\n"
"    border: 1px solid #d10000;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:unchecked:hover\n"
"{\n"
"    border: 1px solid #ff0000;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::disabled\n"
"{\n"
"    color: #656565;\n"
"\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator:disabled\n"
"{\n"
"    background-color: #656565;\n"
"    color: #656565;\n"
"    border: 1px solid #656565;\n"
"\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainLoagin)
        self.centralwidget.setObjectName("centralwidget")
        self.text = QtWidgets.QLabel(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(30, 30, 331, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text.sizePolicy().hasHeightForWidth())
        self.text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.text.setFont(font)
        self.text.setTextFormat(QtCore.Qt.AutoText)
        self.text.setObjectName("text")
        self.img = QtWidgets.QLabel(self.centralwidget)
        self.img.setGeometry(QtCore.QRect(-10, 70, 391, 181))
        self.img.setMinimumSize(QtCore.QSize(391, 181))
        self.img.setMaximumSize(QtCore.QSize(391, 181))
        self.img.setStyleSheet("image: url(:/newPrefix/icons/33513.jpg);")
        self.img.setText("")
        self.img.setObjectName("img")
        self.username = QtWidgets.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(130, 290, 241, 25))
        self.username.setAcceptDrops(False)
        self.username.setObjectName("username")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(10, 290, 141, 21))
        self.username_label.setObjectName("username_label")
        self.password = QtWidgets.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(130, 350, 241, 25))
        self.password.setObjectName("password")
        self.password_label = QtWidgets.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(10, 350, 101, 21))
        self.password_label.setObjectName("password_label")
        self.login_Button = QtWidgets.QPushButton(self.centralwidget)
        self.login_Button.setGeometry(QtCore.QRect(140, 400, 89, 25))
        self.login_Button.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.login_Button.setObjectName("login_Button")
        MainLoagin.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainLoagin)
        QtCore.QMetaObject.connectSlotsByName(MainLoagin)

    def retranslateUi(self, MainLoagin):
        _translate = QtCore.QCoreApplication.translate
        MainLoagin.setWindowTitle(_translate("MainLoagin", "Boîte de réparation"))
        self.text.setText(_translate("MainLoagin", "Compte Boîte de réparation"))
        self.username_label.setText(_translate("MainLoagin", "Nom d\'utilisateur :"))
        self.password_label.setText(_translate("MainLoagin", "Mot de passe :"))
        self.login_Button.setText(_translate("MainLoagin", "soumettre"))
from qrc_sources import source


if __name__ == "__main__":
    """
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainLoagin = QtWidgets.QMainWindow()
    ui = Ui_MainLoagin()
    ui.setupUi(MainLoagin)
    MainLoagin.show()
    sys.exit(app.exec_())
    """
