from PyQt5.QtCore import QThread, pyqtSignal, QSettings
import sqlite3 as sql
from sqlite3 import Error
import pandas as pd
import os


class export(QThread):

    def __init__(self):
        super(export, self).__init__()
        self.___settings = QSettings('alpha', 'Repair_box')
        self.connect = None

    def run(self) -> None:
        self.export()

    def connectToDb(self):
        database_ = self.___settings.value('DATA_BASE_FILE', 'main/data/userdata.sqlite', type=str)
        try:
            self.connect = sql.connect(database_)
        except Error as er:
            print(f'line 20 export engine {er}')

    def export(self):
        self.connectToDb()

        fileName = self.___settings.value('CSV_SAVE_LOCATION', 'EXPORT/articles', type=str)
        db_ = pd.read_sql_query("SELECT * FROM ITEMS", self.connect)
        db_.to_csv(f'{fileName}.csv', index=False)
        read_file = pd.read_csv(f'{fileName}.csv')
        read_file.to_excel(f'{fileName}.xlsx', index=None, header=True)
        os.remove(f'{fileName}.csv')
        self.connect.close()
        self.exit(0)
