# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class loading_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 359)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainIcon/icons/movil_05.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dropShadwoFrame = QtWidgets.QFrame(self.centralwidget)
        self.dropShadwoFrame.setStyleSheet("QFrame {\n"
"        \n"
"    background-color:rgb(56,58,89);\n"
"    color:rgb(220,220,220);\n"
"    border-radius: 10px;\n"
"\n"
"    \n"
"}")
        self.dropShadwoFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.dropShadwoFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dropShadwoFrame.setObjectName("dropShadwoFrame")
        self.title_label = QtWidgets.QLabel(self.dropShadwoFrame)
        self.title_label.setGeometry(QtCore.QRect(6, 60, 611, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: rgb(153, 29, 255);")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.progressBar = QtWidgets.QProgressBar(self.dropShadwoFrame)
        self.progressBar.setGeometry(QtCore.QRect(10, 220, 601, 23))
        self.progressBar.setStyleSheet("QProgressBar {\n"
"    \n"
"    background-color:rgb(98,114,164);\n"
"    color:rgb(200,200,200);\n"
"    border-style: none;\n"
"    border-radius:10px;\n"
"    text-align:center;\n"
"    \n"
"\n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius:10px;    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.54, x2:1, y2:0.534, stop:0 rgba(153, 29, 255, 255), stop:1 rgba(85, 0, 255, 255));\n"
"}")
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.loading_label = QtWidgets.QLabel(self.dropShadwoFrame)
        self.loading_label.setGeometry(QtCore.QRect(0, 260, 621, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.loading_label.setFont(font)
        self.loading_label.setStyleSheet("color: rgb(120, 120, 120);")
        self.loading_label.setAlignment(QtCore.Qt.AlignCenter)
        self.loading_label.setObjectName("loading_label")
        self.Credite = QtWidgets.QLabel(self.dropShadwoFrame)
        self.Credite.setGeometry(QtCore.QRect(10, 320, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.Credite.setFont(font)
        self.Credite.setStyleSheet("color: rgb(120, 120, 120);")
        self.Credite.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Credite.setObjectName("Credite")
        self.version = QtWidgets.QLabel(self.dropShadwoFrame)
        self.version.setGeometry(QtCore.QRect(520, 320, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.version.setFont(font)
        self.version.setStyleSheet("color: rgb(120, 120, 120);")
        self.version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.version.setObjectName("version")
        self.verticalLayout.addWidget(self.dropShadwoFrame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Boîte de réparation"))
        self.title_label.setText(_translate("MainWindow", "<html><head/><body><p>BOITE DE REPARATION</p></body></html>"))
        self.loading_label.setText(_translate("MainWindow", "<html><head/><body><pre style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Courier New\'; font-size:12pt;\">Chargement...</span></pre></body></html>"))
        self.Credite.setText(_translate("MainWindow", "<strong>Crédité</strong>:Anwer.Dv\n"
""))
        self.version.setText(_translate("MainWindow", "<strong>Version</strong>:0.1b"))
from qrc_sources import source

if __name__ == "__main__":
    pass
