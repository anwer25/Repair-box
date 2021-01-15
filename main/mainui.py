# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainui.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 705)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainIcon/icons/movil_05.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tabWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tabWidget.setWhatsThis("")
        self.tabWidget.setAccessibleDescription("")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.additem = QtWidgets.QWidget()
        self.additem.setObjectName("additem")
        self.gridLayout = QtWidgets.QGridLayout(self.additem)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.paid = QtWidgets.QGroupBox(self.additem)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.paid.setFont(font)
        self.paid.setObjectName("paid")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.paid)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.dateText = QtWidgets.QLabel(self.paid)
        self.dateText.setObjectName("dateText")
        self.gridLayout_9.addWidget(self.dateText, 0, 0, 1, 1)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.paid)
        self.dateTimeEdit.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.Tunisia))
        self.dateTimeEdit.setProperty("showGroupSeparator", False)
        self.dateTimeEdit.setMinimumDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateTimeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.gridLayout_9.addWidget(self.dateTimeEdit, 0, 1, 1, 1)
        self.governorateText = QtWidgets.QLabel(self.paid)
        self.governorateText.setObjectName("governorateText")
        self.gridLayout_9.addWidget(self.governorateText, 2, 0, 1, 1)
        self.governorate = QtWidgets.QComboBox(self.paid)
        self.governorate.setObjectName("governorate")
        self.gridLayout_9.addWidget(self.governorate, 2, 1, 1, 1)
        self.delegationText = QtWidgets.QLabel(self.paid)
        self.delegationText.setObjectName("delegationText")
        self.gridLayout_9.addWidget(self.delegationText, 3, 0, 1, 1)
        self.delegation = QtWidgets.QComboBox(self.paid)
        self.delegation.setObjectName("delegation")
        self.gridLayout_9.addWidget(self.delegation, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.paid)
        self.label_13.setObjectName("label_13")
        self.gridLayout_9.addWidget(self.label_13, 4, 0, 1, 1)
        self.price = QtWidgets.QLineEdit(self.paid)
        self.price.setAcceptDrops(False)
        self.price.setInputMethodHints(QtCore.Qt.ImhNone)
        self.price.setMaxLength(100)
        self.price.setObjectName("price")
        self.gridLayout_9.addWidget(self.price, 4, 1, 1, 1)
        self.prepaid = QtWidgets.QCheckBox(self.paid)
        self.prepaid.setObjectName("prepaid")
        self.gridLayout_9.addWidget(self.prepaid, 4, 2, 1, 1)
        self.gridLayout_5.addWidget(self.paid, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_5, 0, 1, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox_4 = QtWidgets.QGroupBox(self.additem)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_14 = QtWidgets.QLabel(self.groupBox_4)
        self.label_14.setObjectName("label_14")
        self.gridLayout_10.addWidget(self.label_14, 0, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_4)
        self.label_15.setObjectName("label_15")
        self.gridLayout_10.addWidget(self.label_15, 0, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_10.addWidget(self.textEdit, 1, 0, 1, 1)
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox_4)
        self.textEdit_2.setObjectName("textEdit_2")
        self.gridLayout_10.addWidget(self.textEdit_2, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/save/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_10.addWidget(self.pushButton, 2, 1, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox_4, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_6, 1, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.customerOrCompanyInformation = QtWidgets.QGroupBox(self.additem)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.customerOrCompanyInformation.setFont(font)
        self.customerOrCompanyInformation.setObjectName("customerOrCompanyInformation")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.customerOrCompanyInformation)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.companyNameText_2 = QtWidgets.QLabel(self.customerOrCompanyInformation)
        self.companyNameText_2.setObjectName("companyNameText_2")
        self.gridLayout_8.addWidget(self.companyNameText_2, 0, 0, 1, 1)
        self.companyName_2 = QtWidgets.QLineEdit(self.customerOrCompanyInformation)
        self.companyName_2.setObjectName("companyName_2")
        self.gridLayout_8.addWidget(self.companyName_2, 0, 1, 1, 1)
        self.userNameText_2 = QtWidgets.QLabel(self.customerOrCompanyInformation)
        self.userNameText_2.setObjectName("userNameText_2")
        self.gridLayout_8.addWidget(self.userNameText_2, 1, 0, 1, 1)
        self.userNameAndLastName_2 = QtWidgets.QLineEdit(self.customerOrCompanyInformation)
        self.userNameAndLastName_2.setObjectName("userNameAndLastName_2")
        self.gridLayout_8.addWidget(self.userNameAndLastName_2, 1, 1, 1, 1)
        self.idNumberText_2 = QtWidgets.QLabel(self.customerOrCompanyInformation)
        self.idNumberText_2.setObjectName("idNumberText_2")
        self.gridLayout_8.addWidget(self.idNumberText_2, 2, 0, 1, 1)
        self.idNumber_2 = QtWidgets.QLineEdit(self.customerOrCompanyInformation)
        self.idNumber_2.setObjectName("idNumber_2")
        self.gridLayout_8.addWidget(self.idNumber_2, 2, 1, 1, 1)
        self.addressEmailText_2 = QtWidgets.QLabel(self.customerOrCompanyInformation)
        self.addressEmailText_2.setObjectName("addressEmailText_2")
        self.gridLayout_8.addWidget(self.addressEmailText_2, 3, 0, 1, 1)
        self.emailAddress_2 = QtWidgets.QLineEdit(self.customerOrCompanyInformation)
        self.emailAddress_2.setObjectName("emailAddress_2")
        self.gridLayout_8.addWidget(self.emailAddress_2, 3, 1, 1, 1)
        self.phoneNumberText_2 = QtWidgets.QLabel(self.customerOrCompanyInformation)
        self.phoneNumberText_2.setObjectName("phoneNumberText_2")
        self.gridLayout_8.addWidget(self.phoneNumberText_2, 4, 0, 1, 1)
        self.phoneNumber_2 = QtWidgets.QLineEdit(self.customerOrCompanyInformation)
        self.phoneNumber_2.setObjectName("phoneNumber_2")
        self.gridLayout_8.addWidget(self.phoneNumber_2, 4, 1, 1, 1)
        self.homeAddressText_2 = QtWidgets.QLabel(self.customerOrCompanyInformation)
        self.homeAddressText_2.setObjectName("homeAddressText_2")
        self.gridLayout_8.addWidget(self.homeAddressText_2, 5, 0, 1, 1)
        self.homeAddress_2 = QtWidgets.QLineEdit(self.customerOrCompanyInformation)
        self.homeAddress_2.setObjectName("homeAddress_2")
        self.gridLayout_8.addWidget(self.homeAddress_2, 5, 1, 1, 1)
        self.gridLayout_2.addWidget(self.customerOrCompanyInformation, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.deviceinformation = QtWidgets.QGroupBox(self.additem)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.deviceinformation.setFont(font)
        self.deviceinformation.setObjectName("deviceinformation")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.deviceinformation)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.deviceModel = QtWidgets.QComboBox(self.deviceinformation)
        self.deviceModel.setObjectName("deviceModel")
        self.gridLayout_7.addWidget(self.deviceModel, 3, 2, 1, 1)
        self.deviceBrands = QtWidgets.QComboBox(self.deviceinformation)
        self.deviceBrands.setObjectName("deviceBrands")
        self.gridLayout_7.addWidget(self.deviceBrands, 2, 2, 1, 1)
        self.deviceModelText = QtWidgets.QLabel(self.deviceinformation)
        self.deviceModelText.setObjectName("deviceModelText")
        self.gridLayout_7.addWidget(self.deviceModelText, 3, 0, 1, 1)
        self.deviceBrandsText = QtWidgets.QLabel(self.deviceinformation)
        self.deviceBrandsText.setObjectName("deviceBrandsText")
        self.gridLayout_7.addWidget(self.deviceBrandsText, 2, 0, 1, 1)
        self.deviceType = QtWidgets.QComboBox(self.deviceinformation)
        self.deviceType.setObjectName("deviceType")
        self.gridLayout_7.addWidget(self.deviceType, 0, 2, 1, 1)
        self.deviceTypeText = QtWidgets.QLabel(self.deviceinformation)
        self.deviceTypeText.setObjectName("deviceTypeText")
        self.gridLayout_7.addWidget(self.deviceTypeText, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.deviceinformation, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/additem/icons/blog.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.additem, icon2, "")
        self.search = QtWidgets.QWidget()
        self.search.setObjectName("search")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.search)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.printer_Button = QtWidgets.QPushButton(self.search)
        self.printer_Button.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/printer/icons/printer.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.printer_Button.setIcon(icon3)
        self.printer_Button.setObjectName("printer_Button")
        self.gridLayout_3.addWidget(self.printer_Button, 0, 10, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.search)
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_3.addWidget(self.line_9, 0, 11, 1, 1)
        self.refresh = QtWidgets.QPushButton(self.search)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/refresh/icons/loading.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refresh.setIcon(icon4)
        self.refresh.setObjectName("refresh")
        self.gridLayout_3.addWidget(self.refresh, 0, 8, 1, 1)
        self.line_11 = QtWidgets.QFrame(self.search)
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_3.addWidget(self.line_11, 0, 7, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.search)
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_3.addWidget(self.line_10, 0, 9, 1, 1)
        self.edit_button = QtWidgets.QPushButton(self.search)
        self.edit_button.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Modifier/icons/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.edit_button.setIcon(icon5)
        self.edit_button.setObjectName("edit_button")
        self.gridLayout_3.addWidget(self.edit_button, 0, 0, 1, 1)
        self.line_15 = QtWidgets.QFrame(self.search)
        self.line_15.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_15.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_15.setObjectName("line_15")
        self.gridLayout_3.addWidget(self.line_15, 0, 1, 1, 1)
        self.delet_button = QtWidgets.QPushButton(self.search)
        self.delet_button.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/delet/icons/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delet_button.setIcon(icon6)
        self.delet_button.setObjectName("delet_button")
        self.gridLayout_3.addWidget(self.delet_button, 0, 2, 1, 1)
        self.state_button = QtWidgets.QPushButton(self.search)
        self.state_button.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/state/icons/yes-or-no.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.state_button.setIcon(icon7)
        self.state_button.setObjectName("state_button")
        self.gridLayout_3.addWidget(self.state_button, 0, 4, 1, 1)
        self.synchroniser_Button = QtWidgets.QPushButton(self.search)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/sync/icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.synchroniser_Button.setIcon(icon8)
        self.synchroniser_Button.setObjectName("synchroniser_Button")
        self.gridLayout_3.addWidget(self.synchroniser_Button, 0, 6, 1, 1)
        self.line_13 = QtWidgets.QFrame(self.search)
        self.line_13.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.gridLayout_3.addWidget(self.line_13, 0, 3, 1, 1)
        self.line_12 = QtWidgets.QFrame(self.search)
        self.line_12.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout_3.addWidget(self.line_12, 0, 5, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.search)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.searsh_ID = QtWidgets.QLineEdit(self.groupBox)
        self.searsh_ID.setObjectName("searsh_ID")
        self.gridLayout_12.addWidget(self.searsh_ID, 2, 2, 1, 2)
        self.ID_label = QtWidgets.QLabel(self.groupBox)
        self.ID_label.setObjectName("ID_label")
        self.gridLayout_12.addWidget(self.ID_label, 2, 0, 1, 1)
        self.client_searsh_line = QtWidgets.QLineEdit(self.groupBox)
        self.client_searsh_line.setObjectName("client_searsh_line")
        self.gridLayout_12.addWidget(self.client_searsh_line, 0, 3, 1, 1)
        self.client_name_label = QtWidgets.QLabel(self.groupBox)
        self.client_name_label.setObjectName("client_name_label")
        self.gridLayout_12.addWidget(self.client_name_label, 0, 0, 1, 2)
        self.society_name_label = QtWidgets.QLabel(self.groupBox)
        self.society_name_label.setObjectName("society_name_label")
        self.gridLayout_12.addWidget(self.society_name_label, 1, 0, 1, 3)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_12.addWidget(self.label_9, 4, 0, 1, 2)
        self.society_search_line = QtWidgets.QLineEdit(self.groupBox)
        self.society_search_line.setObjectName("society_search_line")
        self.gridLayout_12.addWidget(self.society_search_line, 1, 3, 1, 1)
        self.open_QRimage = QtWidgets.QPushButton(self.groupBox)
        self.open_QRimage.setObjectName("open_QRimage")
        self.gridLayout_12.addWidget(self.open_QRimage, 3, 2, 1, 2)
        self.searsh_button = QtWidgets.QPushButton(self.groupBox)
        self.searsh_button.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/research_button/icons/research.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searsh_button.setIcon(icon9)
        self.searsh_button.setObjectName("searsh_button")
        self.gridLayout_12.addWidget(self.searsh_button, 6, 3, 1, 1)
        self.Qr_Image_label = QtWidgets.QLabel(self.groupBox)
        self.Qr_Image_label.setObjectName("Qr_Image_label")
        self.gridLayout_12.addWidget(self.Qr_Image_label, 3, 0, 1, 2)
        self.using_phonelabel = QtWidgets.QLabel(self.groupBox)
        self.using_phonelabel.setObjectName("using_phonelabel")
        self.gridLayout_12.addWidget(self.using_phonelabel, 5, 0, 1, 4)
        self.openCamera = QtWidgets.QPushButton(self.groupBox)
        self.openCamera.setObjectName("openCamera")
        self.gridLayout_12.addWidget(self.openCamera, 4, 2, 1, 2)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 2)
        self.items_table = QtWidgets.QTableWidget(self.search)
        self.items_table.setObjectName("items_table")
        self.items_table.setColumnCount(19)
        self.items_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.items_table.setHorizontalHeaderItem(18, item)
        self.gridLayout_3.addWidget(self.items_table, 1, 2, 1, 10)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/Recherche_tab_icon/icons/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabWidget.addTab(self.search, icon10, "")
        self.gridLayout_11.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1366, 21))
        self.menubar.setObjectName("menubar")
        self.menufichier = QtWidgets.QMenu(self.menubar)
        self.menufichier.setObjectName("menufichier")
        self.menuEditer = QtWidgets.QMenu(self.menubar)
        self.menuEditer.setObjectName("menuEditer")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionParameter = QtWidgets.QAction(MainWindow)
        self.actionParameter.setObjectName("actionParameter")
        self.menuEditer.addAction(self.actionParameter)
        self.menubar.addAction(self.menufichier.menuAction())
        self.menubar.addAction(self.menuEditer.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Boîte de réparation"))
        self.paid.setTitle(_translate("MainWindow", "Payé :"))
        self.dateText.setText(_translate("MainWindow", "Date :"))
        self.dateTimeEdit.setDisplayFormat(_translate("MainWindow", "d/M/yyyy h:mm"))
        self.governorateText.setText(_translate("MainWindow", "Gouvernorat :"))
        self.delegationText.setText(_translate("MainWindow", "Délégation :"))
        self.label_13.setText(_translate("MainWindow", "Prix : "))
        self.prepaid.setText(_translate("MainWindow", "Prépayé"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Note technique :"))
        self.label_14.setText(_translate("MainWindow", "Observation :"))
        self.label_15.setText(_translate("MainWindow", "Accessoires Reçus"))
        self.pushButton.setText(_translate("MainWindow", "Enregistrer"))
        self.customerOrCompanyInformation.setTitle(_translate("MainWindow", "Informations client ou entreprise :"))
        self.companyNameText_2.setText(_translate("MainWindow", "Nom de la société :"))
        self.userNameText_2.setText(_translate("MainWindow", "Nom et prénom du client : "))
        self.idNumberText_2.setText(_translate("MainWindow", "Numéro de CIN :"))
        self.addressEmailText_2.setText(_translate("MainWindow", "Address Email :"))
        self.phoneNumberText_2.setText(_translate("MainWindow", "Numéro de téléphone :"))
        self.homeAddressText_2.setText(_translate("MainWindow", "Adresse :"))
        self.deviceinformation.setTitle(_translate("MainWindow", "Informations sur l\'appareil :"))
        self.deviceModelText.setText(_translate("MainWindow", "Model de l\'appareil :"))
        self.deviceBrandsText.setText(_translate("MainWindow", "Marques de l\'appareil :"))
        self.deviceTypeText.setText(_translate("MainWindow", "Type de l\'appareil :"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.additem), _translate("MainWindow", "Ajouter des articles"))
        self.printer_Button.setText(_translate("MainWindow", "Imprimer"))
        self.refresh.setText(_translate("MainWindow", "Rafraîchir"))
        self.refresh.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.edit_button.setText(_translate("MainWindow", "Modifier"))
        self.edit_button.setShortcut(_translate("MainWindow", "Ctrl+M"))
        self.delet_button.setText(_translate("MainWindow", "Supprimer"))
        self.delet_button.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.state_button.setText(_translate("MainWindow", "Changer D\'état"))
        self.state_button.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.synchroniser_Button.setText(_translate("MainWindow", "Synchroniser"))
        self.groupBox.setTitle(_translate("MainWindow", "Recherché par"))
        self.ID_label.setText(_translate("MainWindow", "Ref:"))
        self.client_name_label.setText(_translate("MainWindow", "Nom du client :"))
        self.society_name_label.setText(_translate("MainWindow", "Nom de la société : "))
        self.label_9.setText(_translate("MainWindow", "Lecteur QR"))
        self.open_QRimage.setText(_translate("MainWindow", "Emplacement du fichier"))
        self.searsh_button.setText(_translate("MainWindow", "Chercher"))
        self.Qr_Image_label.setText(_translate("MainWindow", "QR Image :"))
        self.using_phonelabel.setText(_translate("MainWindow", "Ou vous pouvez scanner le QR avec phone"))
        self.openCamera.setText(_translate("MainWindow", "Camera"))
        item = self.items_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.items_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nom du client"))
        item = self.items_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Numéro de téléphone"))
        item = self.items_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nom de la société"))
        item = self.items_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Type de l\'appareil"))
        item = self.items_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Marques de l\'appareil"))
        item = self.items_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Model de l\'appareil"))
        item = self.items_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Ref"))
        item = self.items_table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Etat"))
        item = self.items_table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Prix"))
        item = self.items_table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Prépayé"))
        item = self.items_table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Gouvernorat"))
        item = self.items_table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Delegation"))
        item = self.items_table.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Address"))
        item = self.items_table.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "CIN"))
        item = self.items_table.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "E-mail"))
        item = self.items_table.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Observation"))
        item = self.items_table.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Accessoires"))
        item = self.items_table.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "Date de d\'entrée"))
        item = self.items_table.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "Date de sortie"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.search), _translate("MainWindow", "Recherche d\'articles"))
        self.menufichier.setTitle(_translate("MainWindow", "fichier"))
        self.menuEditer.setTitle(_translate("MainWindow", "Editer"))
        self.actionParameter.setText(_translate("MainWindow", "Parameter"))
from qrc_sources import source