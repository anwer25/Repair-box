from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QFileDialog, QTableWidget, QMessageBox
# from PyQt5.QtCore import QSettings
from PyQt5.QtGui import QCloseEvent
from main.mainui import Ui_MainWindow
from main.data import *
import sqlite3 as sql
from sqlite3 import Error as sqlError
from main.cameramain import app
from main.modifierMain import modifier_
from main.settings_ import settingsMain
from main.sync import realTimeSync, cloudStore, Certificate, firestore, initialize_app
from main.printerEngine import printer

# from main.template import templateEngine
___settings = QSettings('alpha', 'Repair_box')
dataBaseUrl = ___settings.value('REAL_TIME_URL_DATA', '', type=str)
confFile = ___settings.value('CLOUD_CONF_FILE', '', type=str)
try:
    initialize_app(Certificate(confFile), {'databaseURL': dataBaseUrl})
except ValueError as e:
    print(f'line 20 main: {e}')


class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        QMainWindow.__init__(self)
        self.___settings = QSettings('alpha', 'Repair_box')
        self.sync_EngineRealTime = realTimeSync()
        self.sync_EngineCloud = cloudStore()
        self.sync_EngineCloud.start()
        self.sync_EngineRealTime.start()
        self.setupUi(self)
        self.UI()
        self.Buttons()
        ####################################################
        self.__Gouvernorat_read = Gouvernorat_reading()
        self.__Gouvernorat_read.start()
        self.__Gouvernorat_read.data.connect(self.add)
        ##########################################################
        self.devicetype = deviceTypeReading()
        self.devicetype.start()
        self.devicetype.data__.connect(self.addDeviceType)
        ##########################################################
        self.show()
        ###########################################################

    def UI(self):
        self.items_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.pushButton.setEnabled(True)
        self.searsh_button.setEnabled(True)
        self.display_refresh()
        self.items_table.setSelectionBehavior(QTableWidget.SelectRows)

    def Buttons(self):
        #############################################################
        # get current selected item on governorate combobox
        self.governorate.activated.connect(self.readDelegationValues)
        #############################################################
        # get cuurent selected  delegation
        self.delegation.activated.connect(self.curentdelegation)
        #############################################################
        # get current selected item on device type
        self.deviceType.activated.connect(self.readDeviceTypeValues)
        #############################################################
        # get current selected brands name
        self.deviceBrands.activated.connect(self.readbrandvalues)
        #############################################################
        # get current selcted model name
        self.deviceModel.activated.connect(self.getmodelname)
        ############################################################
        # save button
        self.pushButton.clicked.connect(self.save)
        #############################################################
        # refresh button
        self.refresh.clicked.connect(self.display_refresh)
        #############################################################
        # open qr_file
        self.open_QRimage.clicked.connect(self.qr_code_decoder)
        #############################################################
        # open camera button
        self.openCamera.clicked.connect(self._openCamera)
        # searsh button
        self.searsh_button.clicked.connect(self.searsh_Qurey)
        ############################################################
        self.items_table.itemClicked.connect(self.button_enabled)
        ###########################################################
        self.edit_button.clicked.connect(self.edit)
        ###########################################################
        # remove button
        self.delet_button.clicked.connect(self.remove)
        ###########################################################
        # change state
        self.state_button.clicked.connect(self.change_state)
        ###########################################################
        # open setting
        self.actionParameter.triggered.connect(self.opensettings)
        ###########################################################
        # print Button
        self.printer_Button.clicked.connect(self.printItem)
        ###########################################################
        # sync Button
        self.synchroniser_Button.clicked.connect(self.sync)

    ##############################################################################################
    # add values to Gouvernorat combobox
    def add(self, data):
        self.governorate.addItem(data)

    ###############################################################################################
    # add values to delegation combobox
    def readDelegationValues(self):

        self.aria_selected = "'" + self.governorate.currentText() + "'"
        self.delegation.clear()
        self.__delegationread = delegation_reading(self.aria_selected)
        self.__delegationread.start()
        self.__delegationread.data_.connect(self.add_values_to_delegation)

    ###############################################################################################
    def add_values_to_delegation(self, data):
        self.delegation.addItem(data)

    ################################################################################################
    # get curent selected delegation
    def curentdelegation(self):

        self.delegation_ = self.delegation.currentText()

    ################################################################################################
    # add values device Type combobox

    def addDeviceType(self, data):
        self.deviceType.addItem(data)

    ################################################################################################
    # add values to deviceBrands combobox
    def readDeviceTypeValues(self):

        self.device_Type = "'" + self.deviceType.currentText() + "'"
        self.deviceBrands.clear()
        self.brands = deviceBrands(self.device_Type)
        self.brands.start()
        self.brands.data.connect(self.addBrands)

    def addBrands(self, brands):
        self.deviceBrands.addItem(brands)

    def readbrandvalues(self):

        self.devicebrandName = "'" + self.deviceBrands.currentText() + "'"
        self.deviceModel.clear()
        self.models = deviceModel(self.devicebrandName)
        self.models.start()
        self.models.data.connect(self.addModel)

    def addModel(self, model):
        self.deviceModel.addItem(model)

    def getmodelname(self):

        self.modelname = self.deviceModel.currentText()

    ################################################################################
    # save
    def save(self):
        self.username = self.userNameAndLastName_2.text()
        self.date = self.dateTimeEdit.dateTime()
        self.strdate = self.date.toString(self.dateTimeEdit.displayFormat())
        if self.prepaid.isChecked():
            self.ppaid = 'Oui'
        else:
            self.ppaid = 'Non'
        try:
            self.save_engine = save_data(deviceType=self.device_Type[1:-1], devicebrands=self.devicebrandName[1:-1],
                                         devicemodel=self.modelname, clientName=self.username, Date=self.strdate,
                                         Governorate=self.aria_selected[1:-1],
                                         delegation=self.delegation_, companyName=self.companyName_2.text(),
                                         CIN_number=self.idNumber_2.text(), addressEmail=self.emailAddress_2.text(),
                                         phoneNumber=self.phoneNumber_2.text(), addrese=self.homeAddress_2.text(),
                                         price=self.price.text(), observation=self.textEdit.toPlainText(),
                                         accessoires=self.textEdit_2.toPlainText(), prepaid=self.ppaid)
            self.save_engine.start()
        except AttributeError:
            print("Error: main_ file line 161")
        self.save_engine.refresh.connect(self.display_refresh)
        if self.___settings.value('CLOUD_ENABLE', False, type=bool) and not self.sync_EngineCloud.isRunning():
            self.sync_EngineCloud.start()
        if self.___settings.value('REAL_TIME_ENABLE', False, type=bool) and not self.sync_EngineRealTime.isRunning():
            self.sync_EngineRealTime.start()

    def connectTodb(self):
        try:
            self.connect = sql.connect('main/data/userdata.sqlite')
            self.cursor_ = self.connect.cursor()
        except sqlError as sql_connectProblem:
            print(sql_connectProblem)

    def display_refresh(self):
        self.connectTodb()
        self.Qurey = 'SELECT * FROM ITEMS'
        self.data_ = self.cursor_.execute(self.Qurey)
        self.items_table.setRowCount(0)
        for row_number, row_data in enumerate(self.data_):
            self.items_table.insertRow(row_number)
            for col_number, data in enumerate(row_data):
                self.items_table.setItem(row_number, col_number, QTableWidgetItem(str(data)))
        self.connect.close()

    def qr_code_decoder(self):
        self.file = QFileDialog.getOpenFileName(self, caption='Ouvrir Image QR',
                                                filter='Fichier Image (*.jpg *.gif *.png)')
        self.decoder = qr(str(self.file)[2:-39])
        self.decoder.start()
        self.decoder.data__.connect(self.searsh_engine)

    def searsh_Qurey(self):

        if self.client_searsh_line.text() != "":
            self.Qurey_searsh = f'SELECT * FROM ITEMS WHERE CLIENT_NAME=\'{self.client_searsh_line.text()}\''

        elif self.society_search_line.text() != "":
            self.Qurey_searsh = f'SELECT * FROM ITEMS WHERE COMPANY_NAME=\'{self.society_search_line.text()}\''

        elif self.searsh_ID.text() != "":
            self.Qurey_searsh = f'SELECT * FROM ITEMS WHERE ID=\'{self.searsh_ID.text()}\''

        self.searsh_engine(self.Qurey_searsh)

    def _openCamera(self):

        self.camera = app()
        self.camera.show()
        self.camera.data.connect(self.searsh_engine)

    def searsh_engine(self, Qurey):
        self.connectTodb()
        self.items_table.setRowCount(0)
        try:
            self.cursor_.execute(Qurey)
            rows = self.cursor_.fetchall()
            for row_number, row_data in enumerate(rows):
                self.items_table.insertRow(row_number)
                for col_number, data in enumerate(row_data):
                    self.items_table.setItem(row_number, col_number, QTableWidgetItem(str(data)))
        except Error as searshproblem:
            # add alert
            print(searshproblem)
        self.client_searsh_line.clear()
        self.society_search_line.clear()
        self.searsh_ID.clear()

    def button_enabled(self, state):
        self.edit_button.setEnabled(True)
        self.delet_button.setEnabled(True)
        self.state_button.setEnabled(True)
        self.printer_Button.setEnabled(True)

    def getSelectedItem(self):
        try:
            # Get the first QTableWidgetItem from the selected row or catch the
            # exception if no row is selected.
            IDvalue: QTableWidgetItem = self.items_table.selectedItems()[6]
            return IDvalue.text()
        except (IndexError):
            # make Qmessage Here
            print(IndexError)

    def edit(self):

        ID = self.getSelectedItem()
        self.modfier_Windows = modifier_(ID)
        self.modfier_Windows.complete.connect(self.display_refresh)

    def remove(self):

        try:
            ID = self.getSelectedItem()
            self.connectTodb()
            Qurey = f'DELETE FROM ITEMS WHERE ID=\'{ID}\''
            try:
                self.cursor_.execute(Qurey)
                self.connect.commit()
                self.connect.close()
                if self.___settings.value('CLOUD_ENABLE', False, type=bool):
                    firestoreDb = firestore.client()
                    firestoreDb.collection(u'items').document(ID).delete()
            except Error as removeError:
                print(removeError)
        except IndexError:
            print('no item selected')

        self.display_refresh()

    def change_state(self):
        ID = self.getSelectedItem()
        self.connectTodb()
        try:
            IDvalue: QTableWidgetItem = self.items_table.selectedItems()[7]

            if IDvalue.text() == 'fixée':
                state = 'Pas fixée'
            else:
                state = 'fixée'

            Qurey = f'UPDATE ITEMS SET STATE_=\'{state}\' where ID=\'{ID}\''

            self.cursor_.execute(Qurey)
            self.connect.commit()
            self.connect.close()
        except IndexError:
            print('no item selected')
        self.display_refresh()

    def opensettings(self):
        self.settings = settingsMain()
        self.settings.show()

    def printItem(self):
        ID = self.getSelectedItem()
        print_ = printer(ID)
        print_.start()

    def sync(self):
        if self.sync_EngineCloud.isRunning():
            self.sync_EngineCloud.exit(0)
        if self.sync_EngineRealTime.isRunning():
            self.sync_EngineRealTime.exit(0)
        if self.___settings.value('CLOUD_ENABLE', False, type=bool):
            self.sync_EngineCloud.start()
        if self.___settings.value('REAL_TIME_ENABLE', False, type=bool):
            self.sync_EngineRealTime.start()

    def closeEvent(self, a: QCloseEvent) -> None:
        self.sync_EngineRealTime.exit(0)
        self.sync_EngineCloud.exit(0)


if __name__ == '__main__':
    # for test
    """
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = Main()
    sys.exit((app.exec_()))
    """
