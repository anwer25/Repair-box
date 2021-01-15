from main.modifier import Ui_modifier
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QDateTime, Qt, pyqtSignal
from main.modifier_T import *


class modifier_(QWidget, Ui_modifier):
    complete = pyqtSignal()

    def __init__(self, data):
        super(modifier_, self).__init__()
        self.data = data
        self.__exit_date = ''
        self.setupUi(self)
        self.Ui()
        self.Buttons()

    def Ui(self):
        self.show()
        self.ID.setText(self.data)
        ############################################################
        # get values from user db
        self.getValues()

    def Buttons(self):
        self.cancel_Button.clicked.connect(self.exit)
        self.save_button.clicked.connect(self.save)
        self.exit_checkbox.stateChanged.connect(self.exit_date_display)

    ##############################################################################################

    def dbConnect(self):

        try:
            self.connect = sql.connect('main/data/userdata.sqlite')
            self.cursor_ = self.connect.cursor()
        except Error:
            print(Error)

    def getValues(self):
        self.dbConnect()
        self.Qurey_searsh = f'SELECT * FROM ITEMS WHERE ID=\'{self.data}\''
        data_ = []
        try:
            self.cursor_.execute(self.Qurey_searsh)
            rows = self.cursor_.fetchall()
            for row_number, row_data in enumerate(rows):
                for col_number, data in enumerate(row_data):
                    data_.append(str(data))

        except Error as searshproblem:
            # add alert
            print(searshproblem)
        self.connect.close()

        self.clientName.setText(data_[0])
        self.phoneNmber.setText(data_[1])
        self.companyName.setText(data_[2])
        self.deviceType.setText(data_[3])
        self.deviceBrandName.setText(data_[4])
        self.deviceModel.setText(data_[5])
        self.price.setText(data_[8])
        self.gouvernorat.setText(data_[10])
        self.delegation.setText(data_[11])
        self.address.setText(data_[12])
        self.CIN.setText(data_[13])
        self.emailAddress.setText(data_[14])
        self.observationText.setText(data_[15])
        self.accessoiresText.setText(data_[16])
        now = QDateTime.fromString(data_[17], 'd/M/yyyy h:mm')
        self.date.setDateTime(now)
        if data_[7] != 'Non fixé':
            self.fixed_checkbox.setChecked(True)
        if data_[9] != 'Non':
            self.prePaid.setChecked(True)
        if data_[18] != "":
            exit_ = QDateTime.fromString(data_[18], 'd/M/yyyy h:mm')
            self.exit_date.setEnabled(True)
            self.exit_checkbox.setChecked(True)
            self.exit_date.setDateTime(exit_)

    def exit(self):
        self.close()

    def closeEvent(self, event):
        pass

    def exit_date_display(self, state):

        if Qt.Checked == state:
            self.exit_date.setEnabled(True)
            exit_date = self.exit_date.dateTime()
            self.__exit_date = exit_date.toString(self.exit_date.displayFormat())
        else:
            self.exit_date.setEnabled(False)

    def save(self):
        # work here
        if self.fixed_checkbox.isChecked():
            self.state = 'fixée'
        else:
            self.state = 'pas fixée'

        if self.prePaid.isChecked():
            self.prepaid = 'Oui'
        else:
            self.prepaid = 'Non'
        date = self.date.dateTime()
        __date = date.toString(self.date.displayFormat())
        worker = saver(id=self.data, deviceType=self.deviceType.text(), devicemodel=self.deviceModel.text(),
                       devicebrands=self.deviceBrandName.text(), accessoires=self.accessoiresText.toPlainText(),
                       clientName=self.clientName.text(), Date=__date, Governorate=self.gouvernorat.text(),
                       delegation=self.delegation.text(), exit_date=self.__exit_date, state=self.state,
                       companyName=self.companyName.text(), CIN_number=self.CIN.text(),
                       addressEmail=self.emailAddress.text(), phoneNumber=self.phoneNmber.text(),
                       addrese=self.address.text(), price=self.price.text(),
                       observation=self.observationText.toPlainText(), prepaid=self.prepaid)

        worker.start()
        worker.refresh.connect(self.refresh)

    def refresh(self):
        self.complete.emit()
        self.close()
