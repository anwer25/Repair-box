from PyQt5.QtCore import QThread, pyqtSignal
import sqlite3 as sql
from sqlite3 import Error
from main.template import templateEngine


class saver(QThread):
    refresh = pyqtSignal()
    def __init__(self, id, deviceType, devicebrands, devicemodel, clientName, Date, Governorate, delegation, exit_date='', state='Non fixé', companyName='',
                 CIN_number='', addressEmail='', phoneNumber='', addrese='', price=0, observation='', accessoires='', prepaid=False, db='main/data/userdata.sqlite'):
        super(saver, self).__init__()
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
        self.id = id



    def run(self):

        self.saverwork()



    def dbconnecter(self):

        try:
            self.connect = sql.connect(self.db)
            self.courser = self.connect.cursor()
        except Error:
            pass


    def saverwork(self):
        self.dbconnecter()
        __Qurey = f"""UPDATE ITEMS SET CLIENT_NAME = ?, PHONE_NUMBER= ?, COMPANY_NAME = ?, DEVICE_TYPE= ?,
                DEVICE_BRAND = ?,DEVICE_MODEL= ?, STATE_= ?, PRICE =?, PREPAID = ?,GOUVERNORAT= ?,DELEGATION= ?,
                ADDRESS= ?,CIN_NUMBER = ?, EMAIL_ADDRESS = ?, OBSERVATION = ?,ACCESSOIRES = ?, ENTER_DATE = ?,
                EXIT_DATE = ? where ID = ?"""
        __data = (self.clientName, self.phoneNumber, self.companyName, self.deviceType, self.devicebrands,
                  self.deviceModel, self.state, self.price, self.prepaid, self.governorate, self.delegation,
                  self.addrese, self.CIN_number, self.address_email, self.observation, self.accessoires, self.date,
                  self.exit_date, self.id)
        try:

            self.courser.execute(__Qurey, __data)
            self.connect.commit()
            self.refresh.emit()
            if self.prepaid:
                prepaid = 'Oui'
            else:
                prepaid = 'Non'
            word = templateEngine(clientName=self.clientName, phoneNumber=self.phoneNumber,
                                  companyName=self.companyName,
                                  deviceType=self.deviceType, deviceBrand=self.devicebrands,
                                  deviceModel=self.deviceModel,
                                  ID=self.id, date=self.date, prePaid=prepaid, price=self.price,
                                  accessories=self.accessoires, qrimage=f'main/data/QRCODE/{self.id}.png')
            word.templateWriter()
        except Error as executeProblem:
            print(executeProblem)
        self.connect.close()


