from __future__ import print_function
from PyQt5.QtCore import QThread, pyqtSignal
import pyzbar.pyzbar as pyzbar
import numpy as np
import cv2
import time


class readQRCode_Camera(QThread):
    data = pyqtSignal(str)
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super(readQRCode_Camera, self).__init__()
        self.id_ = None
        self._run_falg = True

    def run(self):
        self.camera()

    def camera(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640)
        self.cap.set(4, 480)
        self.font = cv2.FONT_HERSHEY_SIMPLEX

        while self._run_falg:
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            # Our operations on the frame come here
            try:
                im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            except:
                break

            decodedObjects = pyzbar.decode(im)
            for decodedObject in decodedObjects:
                points = decodedObject.polygon
                # If the points do not form a quad, find convex hull
                if len(points) > 4:
                    hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                    hull = list(map(tuple, np.squeeze(hull)))
                else:
                    hull = points
                # Number of points in the convex hull
                n = len(hull)
                # Draw the convext hull
                for j in range(0, n):
                    cv2.line(im, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)
                x = decodedObject.rect.left
                y = decodedObject.rect.top
                barCode = str(decodedObject.data)[8:-3]
                cv2.putText(im, barCode, (x, y), self.font, 1, (0, 255, 255), 2, cv2.LINE_AA)
            if ret:
                self.change_pixmap_signal.emit(im)
            self.id_ = str(decodedObjects)
            # Display the resulting frame
            if len(self.id_) > 10:
                self.Q = f"SELECT * FROM ITEMS WHERE ID='{self.id_[22:50]}'"
                self.data.emit(self.Q)

            # When everything done, release the capture

    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.cap.release()
        self.exit()
