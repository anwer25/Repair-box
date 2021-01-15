from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from main.loading import loading_MainWindow
from main.dataBase import repairBoxDb
from os import path

counter = 0

class MainWindow(QMainWindow):
    switch_window = pyqtSignal()
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = loading_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
    ##################################################
    # DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadwoFrame.setGraphicsEffect(self.shadow)
        self.timer = QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(100)
        self.show()
        if not path.exists('db'):
            self.data = repairBoxDb()
            self.data.start()



    def progress(self):
        global counter
        self.ui.progressBar.setValue(counter)

        if counter > 100:
            self.timer.stop()
            self.switch_window.emit()
        counter +=1

if __name__ == '__main__':


    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
