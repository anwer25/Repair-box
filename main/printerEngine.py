from PyQt5.QtCore import QThread, pyqtSignal, QSettings
import threading
from win32com import client
import pythoncom
import time
import os


class printer(QThread):

    def __init__(self, fileName=None):
        super(printer, self).__init__()
        self.fileName = fileName

    def run(self) -> None:
        self.worker()

    def worker(self) -> None:
        pythoncom.CoInitialize()
        word = client.DispatchEx("Word.Application")
        currentPath = os.getcwd() + '\\main\\data\\clientsWordFile\\'
        word.Documents.Open(f'{currentPath}{self.fileName}.docx')
        word.ActiveDocument.PrintOut()
        time.sleep(5)
        word.ActiveDocument.Close()
        self.exit(0)