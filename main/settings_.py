from main.settings import Ui_settings
from PyQt5.QtWidgets import QFileDialog, QWidget
from PyQt5.QtCore import Qt, QSettings


class settingsMain(QWidget, Ui_settings):
    ___cloud_file: str
    ___config_file: str
    ___settings = QSettings('alpha', 'Repair_box')

    def __init__(self):
        super(settingsMain, self).__init__()
        self.setupUi(self)
        self.Ui()
        self.Buttons()

    def Ui(self):
        self.show()
        updater_firebase = self.___settings.value('REAL_TIME_ENABLE', False, type=bool)
        updater_cloud = self.___settings.value('CLOUD_ENABLE', False, type=bool)
        realTimeConf = self.___settings.value('REAL_TIME_CONF_FILE', '', type=str)
        realTimeDataBaseUrl = self.___settings.value('REAL_TIME_URL_DATA', '', type=str)
        realTimeReference = self.___settings.value('REAL_TIME_REFERENCE', '', type=str)
        realTimeUpdateTime = self.___settings.value('REAL_TIMER_UPDATER_T', 1, type=int)
        cloudFile = self.___settings.value('CLOUD_CONF_FILE', '', type=str)
        cloudUpdateTime = self.___settings.value('CLOUD_SYNC_TIME', 1, type=int)
        self.filedisplayplacecloud.setText(cloudFile)
        self.updatetimercloud.setCurrentText(str(cloudUpdateTime))
        self.urldatabaseplace.setText(realTimeDataBaseUrl)
        self.refrence.setText(realTimeReference)
        self.filedisplayplacerealtime.setText(realTimeConf)
        self.updatetimer.setCurrentText(str(realTimeUpdateTime))
        self.realtimeractivator.setChecked(updater_firebase)
        self.cloudActivator.setChecked(updater_cloud)
        self.dataBaseLocaition.setText(self.___settings.value('DATA_BASE_FILE', defaultValue='main/data/userdata.sqlite'
                                                              , type=str))
        self.dataBaseTabelName.setText(self.___settings.value('TABEL_NAME', defaultValue='ITEMS', type=str))
        self.___settings.sync()

        if self.realtimeractivator.isChecked():
            self.openfile_realtimeconf.setEnabled(True)
            self.filelocationlabel.setEnabled(True)
            self.urllabe.setEnabled(True)
            self.refrencelabel.setEnabled(True)
            self.updatetimerlabel.setEnabled(True)
            self.urldatabaseplace.setEnabled(True)
            self.refrence.setEnabled(True)
            self.updatetimer.setEnabled(True)
            self.openconffilelocation_cloud_firestore.setEnabled(True)
            self.updatetime_cloud.setEnabled(True)
            self.filedisplayplacerealtime.setEnabled(True)
        else:
            self.openfile_realtimeconf.setEnabled(False)
            self.urldatabaseplace.setEnabled(False)
            self.refrence.setEnabled(False)
            self.updatetimer.setEnabled(False)
            self.openconffilelocation_cloud_firestore.setEnabled(False)
            self.updatetime_cloud.setEnabled(False)
            self.filelocationlabel.setEnabled(False)
            self.urllabe.setEnabled(False)
            self.refrencelabel.setEnabled(False)
            self.updatetimerlabel.setEnabled(False)
            self.filedisplayplacerealtime.setEnabled(False)

        if self.cloudActivator.isChecked():
            self.openconffilelocation_cloud_firestore.setEnabled(True)
            self.conffilelab.setEnabled(True)
            self.updatetime_cloud.setEnabled(True)
            self.updatetimercloud.setEnabled(True)
            self.filedisplayplacecloud.setEnabled(True)
        else:
            self.openconffilelocation_cloud_firestore.setEnabled(False)
            self.conffilelab.setEnabled(False)
            self.updatetime_cloud.setEnabled(False)
            self.updatetimercloud.setEnabled(False)
            self.filedisplayplacecloud.setEnabled(False)



    def Buttons(self):
        self.openfile_realtimeconf.clicked.connect(self.open_realtime_conf)
        self.openconffilelocation_cloud_firestore.clicked.connect(self.cloud_firebase_conf)
        self.savebutton.clicked.connect(self.saver)
        self.cancelbutton.clicked.connect(self.exit)
        self.realtimeractivator.stateChanged.connect(self.realtime)
        self.cloudActivator.stateChanged.connect(self.cloudUi)
        self.openDataBase.clicked.connect(self.dataBaseFile)
        self.cancelbutton.clicked.connect(self.exit)
        self.openLogo.clicked.connect(self.openLogoEngine)
        self.openSavePlace.clicked.connect(self.openSavePlaceEngine)

    def realtime(self, state):
        self.___settings.setValue('REAL_TIME_ENABLE', self.realtimeractivator.isChecked())
        if Qt.Checked == state:
            self.openfile_realtimeconf.setEnabled(True)
            self.filelocationlabel.setEnabled(True)
            self.urllabe.setEnabled(True)
            self.refrencelabel.setEnabled(True)
            self.updatetimerlabel.setEnabled(True)
            self.urldatabaseplace.setEnabled(True)
            self.refrence.setEnabled(True)
            self.updatetimer.setEnabled(True)
            self.filedisplayplacerealtime.setEnabled(True)
        else:
            self.openfile_realtimeconf.setEnabled(False)
            self.urldatabaseplace.setEnabled(False)
            self.refrence.setEnabled(False)
            self.updatetimer.setEnabled(False)
            self.filelocationlabel.setEnabled(False)
            self.urllabe.setEnabled(False)
            self.refrencelabel.setEnabled(False)
            self.updatetimerlabel.setEnabled(False)
            self.filedisplayplacerealtime.setEnabled(False)

    def cloudUi(self, state):
        self.___settings.setValue('CLOUD_ENABLE', self.cloudActivator.isChecked())
        if Qt.Checked == state:
            self.openconffilelocation_cloud_firestore.setEnabled(True)
            self.conffilelab.setEnabled(True)
            self.updatetime_cloud.setEnabled(True)
            self.updatetimercloud.setEnabled(True)
            self.filedisplayplacecloud.setEnabled(True)
        else:
            self.openconffilelocation_cloud_firestore.setEnabled(False)
            self.conffilelab.setEnabled(False)
            self.updatetime_cloud.setEnabled(False)
            self.updatetimercloud.setEnabled(False)
            self.filedisplayplacecloud.setEnabled(False)

    def open_realtime_conf(self) -> None:
        """

        :rtype: None
        """
        confFile = QFileDialog.getOpenFileName(caption='Ouvrir le fichier de configuration',
                                               filter='fichier Json (*.json)')
        ___config_file = str(confFile)[2:-27]
        self.filedisplayplacerealtime.setText(___config_file)

    def cloud_firebase_conf(self) -> None:
        """

        :rtype: None
        """
        confFile = QFileDialog.getOpenFileName(caption='Ouvrir le fichier de configuration',
                                               filter='fichier Json (*.json)')

        ___cloud_file = str(confFile)[2:-27]
        self.filedisplayplacecloud.setText(___cloud_file)

    def dataBaseFile(self) -> None:
        """

        :rtype: None
        """
        dataBaseFile = QFileDialog.getOpenFileName(caption='Ouvrir le baseDone',
                                                   filter='basedone sqlite (*.db) (*.sqlite)')
        ___dataBaseFile = str(dataBaseFile)[2:-39]
        self.dataBaseLocaition.setText(___dataBaseFile)

    def openLogoEngine(self) -> None:
        """
        :rtype: None
        """

        logoFile = QFileDialog.getOpenFileName(caption='Ouvrir logo', filter='Image (*.jpg) (*.jpeg) (*.png)')
        ___logoFile = str(logoFile)[2:-36]
        self.logoPlace.setText(___logoFile)

    def openSavePlaceEngine(self) -> None:
        """
        :rtype: None

        """
        savePlace = QFileDialog.getExistingDirectory(caption='L\'emplacement du Fichier')
        self.savePlace.setText(str(savePlace))

    def openTemplate(self) -> None:
        """
        :rtype: None
        :return: None
        """
        template = QFileDialog.getOpenFileName(caption='L\'emplacement du modele')
        self.templatePlace.setText(str(template))

    def saver(self):
        if self.realtimeractivator.isChecked() and self.filedisplayplacerealtime.text() != '' and self.urldatabaseplace.text() != '' \
                and self.refrence.text() != '':
            self.___settings.setValue('REAL_TIME_CONF_FILE', self.filedisplayplacerealtime.text())
            self.___settings.setValue('REAL_TIME_URL_DATA', self.urldatabaseplace.text())
            self.___settings.setValue('REAL_TIME_REFERENCE', self.refrence.text())
            self.___settings.setValue('REAL_TIMER_UPDATER_T', self.updatetimer.currentText())

        if self.cloudActivator.isChecked() and self.filedisplayplacecloud.text() != '':
            self.___settings.setValue('CLOUD_CONF_FILE', self.filedisplayplacecloud.text())
            self.___settings.setValue('CLOUD_SYNC_TIME', self.updatetimercloud.currentText())
        self.___settings.setValue('DATA_BASE_FILE', self.dataBaseLocaition.text())
        self.___settings.setValue('TABEL_NAME', self.dataBaseTabelName.text())
        self.___setting.setValue('LOGO_IMAGE', self.logoPlace.text())
        self.___settings.setValue('SAVE_WORD_FILE_PLACE', self.savePlace.text())
        self.___settings.setValue('COMPANY_NAME', self.siteWeb.text())
        self.___settings.setValue('COMPANY_NAME__KEY', self.companyName.text())
        self.___settings.setValue('COMPANY_ADDRESS', self.companyAdresse.text())
        self.___settings.setValue('COMPANY_PHONE', self.phoneNumber.text())
        self.___settings.setValue('COMPANY_FAX', self.companyFax.text())
        self.___settings.setValue('COMPANY_EMAIL', self.companyEmail.text())
        self.___settings.setValue('LOGO_WIDTH', self.logoWidth.value())
        self.___settings.setValue('LOGO_HEIGHT', self.logoHeight.value())
        self.___settings.setValue('SAVE_WORD_FILE_PLACE', self.savePlace.text())
        # second tab company
        self.___settings.setValue('DOC_TEMPLATE', self.templatePlace.text())
        self.___settings.setValue('LOGO_KEY', self.logoCode.text())
        self.___settings.setValue('COMPANY_ADDRESS_KEY', self.companyAdresseCode.text())
        self.___settings.setValue('COMPANY_PHONE_KEY', self.companyPhoneNumberCode.text())
        self.___settings.setValue('COMPANY_FAX_KEY', self.companyFaxCode.text())
        self.___settings.setValue('COMPANY_EMAIL_KEY', self.companyEmailCode.text())
        self.___settings.setValue('COMPANY_WEB_SITE_KEY', self.companyWebSiteCode.text())
        self.___settings.setValue('COMPANY_NAME_KEY', self.companyNameCode.text())
        # client data
        self.___settings.setValue('ID_KEY', self.deviceREF.text())
        self.___settings.setValue('DATE_KEY', self.dateCode.text())
        self.___settings.setValue('CLIENT_NAME_KEY', self.clientNameCode.text())
        self.___settings.setValue('CLIENT_NUMBER_KEY', self.clientPhoneNumberCode.text())
        self.___settings.setValue('DEVICE_TYPE_KEY', self.deviceTypeCode.text())
        self.___settings.setValue('DEVICE_BRAND_KEY', self.deviceBrandCode.text())
        self.___settings.setValue('DEVICE_MODEL_KEY', self.deviceModelCode.text())
        self.___settings.setValue('PRICE_KEY', self.priceCode.text())
        self.___settings.setValue('PRE_PAID_KEY', self.prePaidCode.text())
        self.___settings.setValue('ACCESSORIES_KEY', self.accessoriseCode.text())
        self.___settings.setValue('CLIENT_COMPANY_PLACE', self.clientNameCode.text())
        self.___settings.setValue('QR_KEY', self.QRCode.text())
        self.___settings.sync()
        self.close()

    def exit(self):
        self.close()
