from PyQt5.QtCore import QThread, pyqtSignal, QSettings
import sqlite3 as sqlite
from sqlite3 import Error
import uuid
import qrcode
from pyzbar.pyzbar import decode
import cv2
from main.template import templateEngine


class Gouvernorat_reading(QThread):
    data = pyqtSignal(str)

    def __init__(self):
        super(Gouvernorat_reading, self).__init__()

    def run(self):
        self.add_values_to_governorate()

    def add_values_to_governorate(self):
        self.connect_ = sqlite.connect('main/COUNT/COUNTIS.sqlite')
        self.corser_ = self.connect_.cursor()
        for aria in self.corser_.execute("SELECT name FROM sqlite_master WHERE TYPE='table';"):
            self.data.emit(str(aria)[2:-3])


class delegation_reading(QThread):
    data_ = pyqtSignal(str)

    def __init__(self, Gouvernorat='ARIANA'):
        super(delegation_reading, self).__init__()
        self.Gouvernorat = Gouvernorat

    def run(self):
        self.add_values_to_delegation_()

    def add_values_to_delegation_(self):
        self.connect_ = sqlite.connect('main/COUNT/COUNTIS.sqlite')
        self.corser_ = self.connect_.cursor()
        for delegation in self.corser_.execute(f"SELECT DELEGATION_NAME  FROM {self.Gouvernorat}"):
            self.data_.emit(str(delegation)[2:-3])


class deviceTypeReading(QThread):
    data__ = pyqtSignal(str)

    def __init__(self):
        super(deviceTypeReading, self).__init__()

    def run(self):
        self.readValues()

    def readValues(self):
        self.connect = sqlite.connect('db/programme_data.db')
        self.courser = self.connect.cursor()
        for device_type in self.courser.execute('SELECT TYPE_NAME FROM DEVICE_TYPE'):
            self.data__.emit(str(device_type)[2:-3])


class deviceBrands(QThread):
    data = pyqtSignal(str)

    def __init__(self, type):
        super(deviceBrands, self).__init__()
        self.type = type

    def run(self):
        self.read_Brands()

    def read_Brands(self):
        self.connect = sqlite.connect('db/programme_data.db')
        self.courser = self.connect.cursor()
        for brand in self.courser.execute(f"SELECT BRANDS_NAME FROM {self.type}"):
            self.data.emit(str(brand)[2:-5])


class deviceModel(QThread):
    data = pyqtSignal(str)

    def __init__(self, brand):
        super(deviceModel, self).__init__()
        self.brand = brand

    def run(self):
        self.read_models()

    def read_models(self):
        self.connect = sqlite.connect('db/programme_data.db')
        self.courser = self.connect.cursor()
        for model in self.courser.execute(f'SELECT MODEL_NAME FROM {self.brand}'):
            self.data.emit(str(model)[2:-5])


class save_data(QThread):
    problem = pyqtSignal(str)
    refresh = pyqtSignal()

    def __init__(self, deviceType, devicebrands, devicemodel, clientName, Date, Governorate, delegation, exit_date='',
                 state='Pas fixé', companyName='',
                 CIN_number='', addressEmail='', phoneNumber='', addrese='', price=0, observation='', accessoires='',
                 prepaid='Non', db='main/data/userdata.sqlite'):

        super(save_data, self).__init__()
        # self.___settings = QSettings('alpha', 'Repair_box')
        self.deviceType = deviceType
        self.devicebrands = devicebrands
        self.deviceModel = devicemodel
        self.clientName = clientName
        self.companyName = companyName
        self.CIN_number = CIN_number
        self.address_email = addressEmail
        self.phoneNumber = phoneNumber
        self.addrese = addrese
        self.date = Date
        self.state = state
        self.exit_date = exit_date
        self.governorate = Governorate
        self.delegation = delegation
        self.price = price
        self.observation = observation
        self.accessoires = accessoires
        self.prepaid = prepaid
        self.qr = None
        self.db = db

    def run(self):
        self.save_work()

    def crateQrcode(self):
        self.id = uuid.uuid4()
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        self.qr.add_data(self.id)
        self.qr.make(fit=True)
        self.qr_image = self.qr.make_image(fill_color="black", back_color="white")
        self.qr_image.save(f'main/data/QRCODE/{str(self.id)[6:-2]}.png')
        return self.id

    def connect(self):
        try:
            self.connecting = sqlite.connect(self.db)
        except Error as sqlproblem:
            print(sqlproblem)
            # self.problem.emit(sqlproblem)

    @staticmethod
    def convertToBinaryData(file):

        with open(file, 'rb') as file:
            bindata = file.read()
        return bindata

    def __str__(self):
        pass

    def save_work(self):
        self.crateQrcode()
        self.connect()
        self.cursour = self.connecting.cursor()
        self.binImage = self.convertToBinaryData(f'main/data/QRCODE/{str(self.id)[6:-2]}.png')
        self.col = (
        'CLIENT_NAME', 'PHONE_NUMBER', 'COMPANY_NAME', 'DEVICE_TYPE', 'DEVICE_BRAND', 'DEVICE_MODEL', 'ID', 'STATE',
        'PRICE', 'PREPAID',
        'GOUVERNORAT', 'DELEGATION', 'ADDRESS', 'CIN_NUMBER', 'EMAIL_ADDRESS', 'OBSERVATION', 'ACCESSOIRES',
        'ENTER_DATE', 'SORTED_DATE', 'QR_IMAGE')

        ################################################################################################################
        # add values to items

        __data_place = """INSERT INTO ITEMS VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ? ,? ,?)"""
        __data = (
        self.clientName, self.phoneNumber, self.companyName, self.deviceType, self.devicebrands, self.deviceModel,
        str(self.id)[6:-2], self.state,
        int(self.price), self.prepaid, self.governorate, self.delegation, self.addrese, self.CIN_number,
        self.address_email, self.observation, self.accessoires, self.date, self.exit_date, self.binImage)
        self.cursour.execute(__data_place, __data)

        ################################################################################################################
        # insert values to users table
        self.password = str(self.id)[6:-2]

        try:
            self.cursour.execute(f'INSERT INTO USERS VALUES (?,?)', (self.clientName, self.password[:10]))
        except Error as userError:
            print(userError)
        self.connecting.commit()
        self.connecting.close()
        id_ = str(self.id)[6:-2]
        # self.templateWriter()
        word = templateEngine(clientName=self.clientName, phoneNumber=self.phoneNumber, companyName=self.companyName,
                              deviceType=self.deviceType, deviceBrand=self.devicebrands, deviceModel=self.deviceModel,
                              ID=id_, date=self.date, prePaid=self.prepaid, price=self.price,
                              accessories=self.accessoires, qrimage=f'main/data/QRCODE/{id_}.png')
        word.templateWriter()
        self.refresh.emit()


# read qr image
class qr(QThread):
    data__ = pyqtSignal(str)

    def __init__(self, file):
        super(qr, self).__init__()
        self.file = file

    def run(self):
        self.decoder()

    def decoder(self):
        self.decoder_ = decode(cv2.imread(self.file))
        self.id_ = str(self.decoder_[0])[21:-160]
        self.Q = f"SELECT * FROM ITEMS WHERE ID='{self.id_}'"
        self.data__.emit(self.Q)
