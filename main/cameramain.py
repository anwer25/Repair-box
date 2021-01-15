from main.Camera import Ui_camera
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
from main.search_engine import readQRCode_Camera

class app(QWidget,Ui_camera):

    data=pyqtSignal(str)
    def __init__(self):
        super(app, self).__init__()
        self.setupUi(self)
        self.display_width = 640
        self.display_height = 480
        self.Ui()
        self.button()

    def button(self):
        self.ok_button.clicked.connect(self.ok)

    def Ui(self):
        self.cameraEngine = readQRCode_Camera()
        self.cameraEngine.change_pixmap_signal.connect(self.update_image)
        self.cameraEngine.data.connect(self.id_signal)
        self.cameraEngine.start()

    def closeEvent(self, event):
        self.cameraEngine.stop()
        event.accept()
    def ok(self):
        self.cameraEngine.stop()
        self.close()

    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):

        qt_img = self.convert_cv_qt(cv_img)
        self.image_label.setPixmap(qt_img)

    def convert_cv_qt(self, cv_img):

        # rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch, = cv_img.shape
        bytes_per_line = ch*w
        convert_to_Qt_format = QImage(cv_img.data, w, h, bytes_per_line, QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    def id_signal(self, ID):
        self.data.emit(ID)

