from sqlite3.dbapi2 import Cursor, Connection
from typing import List, Any
from PyQt5.QtCore import QSettings, QThread, pyqtSignal
from firebase_admin import db, exceptions, firestore, storage, initialize_app
import firebase_admin
from time import sleep
import sqlite3 as sql
from sqlite3 import Error
from firebase_admin.credentials import Certificate

___settings = QSettings('alpha', 'Repair_box')
dataBaseUrl = ___settings.value('REAL_TIME_URL_DATA', '', type=str)
confFile = ___settings.value('CLOUD_CONF_FILE', '', type=str)
try:
    if ___settings.value('REAL_TIME_ENABLE', False, type=bool):
        firebase_admin.initialize_app(Certificate(confFile), {'databaseURL': dataBaseUrl})
except FileNotFoundError as e:
    print(f'line 15: {e}')


class connect_ToDb:
    def __init__(self):
        pass

    @staticmethod
    def dict_factory(cursor, row) -> dict:
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]

        return d

    def connectToDb(self):
        try:
            ___connect = sql.connect('main/data/userdata.sqlite')
            ___connect.row_factory = self.dict_factory

            return ___connect
        except Error as sqlproblem:
            print(sqlproblem, 'sync line 31')


class realTimeSync(QThread):
    cursor_: Cursor
    ___connect: Connection
    ___data: List[Any]

    def __init__(self):
        super(realTimeSync, self).__init__()
        self.___settings = QSettings('alpha', 'Repair_box')

    def run(self):
        self.rSyncer()

    def dataReader(self) -> any:

        db_ = connect_ToDb()
        connect = db_.connectToDb()
        cursor = connect.cursor()
        cursor.execute('SELECT * FROM ITEMS')
        data = cursor.fetchall()
        items = {}
        for row in data:
            row['QR_IMAGE'] = row['QR_IMAGE'].decode('ISO-8859-1')
            items.setdefault(row['ID'], row)
        connect.close()
        return items

    def rSyncer(self):

        sleeper = self.___settings.value('REAL_TIMER_UPDATER_T', 5, type=int) * 60
        # confFile = self.___settings.value('CLOUD_CONF_FILE', '', type=str)
        # dataBaseUrl = self.___settings.value('REAL_TIME_URL_DATA', '', type=str)
        reference = self.___settings.value('REAL_TIME_REFERENCE', '/', type=str)
        breaker = self.___settings.value('REAL_TIME_ENABLE', False, type=bool)
        while breaker:
            ref = db.reference(reference)
            """
            cread = credentials.Certificate('')
            firebase_admin.initialize_app(cread, {
                'databaseURL': ''
            })
            
            ref = db.reference('/')
            """
            data = self.dataReader()
            ref.set({
                'items': data
            })
            sleep(sleeper)


class cloudStore(QThread):
    def __init__(self):
        super(cloudStore, self).__init__()
        self.___settings = QSettings('alpha', 'Repair_box')

    def run(self) -> None:
        self.fireSync()

    def fireSync(self) -> None:
        breaker = self.___settings.value('CLOUD_ENABLE', False, type=bool)
        configFile = self.___settings.value('CLOUD_CONF_FILE', '', type=str)
        sleep_ = self.___settings.value('CLOUD_SYNC_TIME', 5, type=int) * 60
        # cred = Certificate(configFile)
        # firebase_admin.initialize_app(cred)
        try:
            firestoreDb = firestore.client()
        except ValueError as e:
            print(f'sync line 108: {e}')
        while breaker:
            db_ = connect_ToDb()
            connect = db_.connectToDb()
            cursor = connect.cursor()
            cursor.execute('SELECT * FROM ITEMS')
            data = cursor.fetchall()
            for row in data:

                doc_ref = firestoreDb.collection(u'items').document(f"{row['ID']}")
                doc_ref.set(
                    row
                )
            connect.close()
            sleep(sleep_)