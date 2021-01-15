# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modifier.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_modifier(object):
    def setupUi(self, modifier):
        modifier.setObjectName("modifier")
        modifier.resize(915, 576)
        modifier.setMinimumSize(QtCore.QSize(915, 576))
        modifier.setMaximumSize(QtCore.QSize(915, 576))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        modifier.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/mainIcon/icons/movil_05.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        modifier.setWindowIcon(icon)
        modifier.setLocale(QtCore.QLocale(QtCore.QLocale.French, QtCore.QLocale.Tunisia))
        self.gridLayout = QtWidgets.QGridLayout(modifier)
        self.gridLayout.setContentsMargins(-1, 11, 9, -1)
        self.gridLayout.setHorizontalSpacing(19)
        self.gridLayout.setObjectName("gridLayout")
        self.ID = QtWidgets.QLineEdit(modifier)
        self.ID.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ID.setFont(font)
        self.ID.setObjectName("ID")
        self.gridLayout.addWidget(self.ID, 0, 0, 1, 2)
        self.clientNameLabel = QtWidgets.QLabel(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.clientNameLabel.setFont(font)
        self.clientNameLabel.setObjectName("clientNameLabel")
        self.gridLayout.addWidget(self.clientNameLabel, 1, 0, 1, 1)
        self.clientName = QtWidgets.QLineEdit(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.clientName.setFont(font)
        self.clientName.setObjectName("clientName")
        self.gridLayout.addWidget(self.clientName, 1, 1, 1, 1)
        self.deviceTypeLabel = QtWidgets.QLabel(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.deviceTypeLabel.setFont(font)
        self.deviceTypeLabel.setObjectName("deviceTypeLabel")
        self.gridLayout.addWidget(self.deviceTypeLabel, 1, 2, 1, 1)
        self.deviceType = QtWidgets.QLineEdit(modifier)
        self.deviceType.setObjectName("deviceType")
        self.gridLayout.addWidget(self.deviceType, 1, 3, 1, 2)
        self.CIN_LABEL = QtWidgets.QLabel(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.CIN_LABEL.setFont(font)
        self.CIN_LABEL.setObjectName("CIN_LABEL")
        self.gridLayout.addWidget(self.CIN_LABEL, 2, 0, 1, 1)
        self.CIN = QtWidgets.QLineEdit(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.CIN.setFont(font)
        self.CIN.setObjectName("CIN")
        self.gridLayout.addWidget(self.CIN, 2, 1, 1, 1)
        self.deviceBrandNameLabel = QtWidgets.QLabel(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.deviceBrandNameLabel.setFont(font)
        self.deviceBrandNameLabel.setObjectName("deviceBrandNameLabel")
        self.gridLayout.addWidget(self.deviceBrandNameLabel, 2, 2, 1, 1)
        self.deviceBrandName = QtWidgets.QLineEdit(modifier)
        self.deviceBrandName.setObjectName("deviceBrandName")
        self.gridLayout.addWidget(self.deviceBrandName, 2, 3, 1, 2)
        self.companyNameLabel = QtWidgets.QLabel(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.companyNameLabel.setFont(font)
        self.companyNameLabel.setObjectName("companyNameLabel")
        self.gridLayout.addWidget(self.companyNameLabel, 3, 0, 1, 1)
        self.companyName = QtWidgets.QLineEdit(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.companyName.setFont(font)
        self.companyName.setObjectName("companyName")
        self.gridLayout.addWidget(self.companyName, 3, 1, 1, 1)
        self.modelNameLabel = QtWidgets.QLabel(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.modelNameLabel.setFont(font)
        self.modelNameLabel.setObjectName("modelNameLabel")
        self.gridLayout.addWidget(self.modelNameLabel, 3, 2, 1, 1)
        self.deviceModel = QtWidgets.QLineEdit(modifier)
        self.deviceModel.setObjectName("deviceModel")
        self.gridLayout.addWidget(self.deviceModel, 3, 3, 1, 2)
        self.phoneNumberLabel = QtWidgets.QLabel(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.phoneNumberLabel.setFont(font)
        self.phoneNumberLabel.setObjectName("phoneNumberLabel")
        self.gridLayout.addWidget(self.phoneNumberLabel, 4, 0, 1, 1)
        self.phoneNmber = QtWidgets.QLineEdit(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.phoneNmber.setFont(font)
        self.phoneNmber.setObjectName("phoneNmber")
        self.gridLayout.addWidget(self.phoneNmber, 4, 1, 1, 1)
        self.gouvernoratLabel = QtWidgets.QLabel(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.gouvernoratLabel.setFont(font)
        self.gouvernoratLabel.setObjectName("gouvernoratLabel")
        self.gridLayout.addWidget(self.gouvernoratLabel, 4, 2, 1, 1)
        self.gouvernorat = QtWidgets.QLineEdit(modifier)
        self.gouvernorat.setObjectName("gouvernorat")
        self.gridLayout.addWidget(self.gouvernorat, 4, 3, 1, 2)
        self.emailAddresLabel = QtWidgets.QLabel(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.emailAddresLabel.setFont(font)
        self.emailAddresLabel.setObjectName("emailAddresLabel")
        self.gridLayout.addWidget(self.emailAddresLabel, 5, 0, 1, 1)
        self.emailAddress = QtWidgets.QLineEdit(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.emailAddress.setFont(font)
        self.emailAddress.setObjectName("emailAddress")
        self.gridLayout.addWidget(self.emailAddress, 5, 1, 1, 1)
        self.delegationLabel = QtWidgets.QLabel(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.delegationLabel.setFont(font)
        self.delegationLabel.setObjectName("delegationLabel")
        self.gridLayout.addWidget(self.delegationLabel, 5, 2, 1, 1)
        self.delegation = QtWidgets.QLineEdit(modifier)
        self.delegation.setObjectName("delegation")
        self.gridLayout.addWidget(self.delegation, 5, 3, 1, 2)
        self.addressLabel = QtWidgets.QLabel(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.addressLabel.setFont(font)
        self.addressLabel.setObjectName("addressLabel")
        self.gridLayout.addWidget(self.addressLabel, 6, 0, 1, 1)
        self.address = QtWidgets.QLineEdit(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.address.setFont(font)
        self.address.setObjectName("address")
        self.gridLayout.addWidget(self.address, 6, 1, 1, 1)
        self.label = QtWidgets.QLabel(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 6, 2, 1, 1)
        self.exit_date = QtWidgets.QDateTimeEdit(modifier)
        self.exit_date.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.exit_date.setFont(font)
        self.exit_date.setObjectName("exit_date")
        self.gridLayout.addWidget(self.exit_date, 6, 3, 1, 2)
        self.priceLabel = QtWidgets.QLabel(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.priceLabel.setFont(font)
        self.priceLabel.setObjectName("priceLabel")
        self.gridLayout.addWidget(self.priceLabel, 7, 0, 1, 1)
        self.price = QtWidgets.QLineEdit(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.price.setFont(font)
        self.price.setObjectName("price")
        self.gridLayout.addWidget(self.price, 7, 1, 1, 1)
        self.exit_checkbox = QtWidgets.QCheckBox(modifier)
        self.exit_checkbox.setObjectName("exit_checkbox")
        self.gridLayout.addWidget(self.exit_checkbox, 7, 3, 1, 1)
        self.fixed_checkbox = QtWidgets.QCheckBox(modifier)
        self.fixed_checkbox.setObjectName("fixed_checkbox")
        self.gridLayout.addWidget(self.fixed_checkbox, 7, 4, 1, 1)
        self.dateLabel = QtWidgets.QLabel(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.dateLabel.setFont(font)
        self.dateLabel.setObjectName("dateLabel")
        self.gridLayout.addWidget(self.dateLabel, 8, 0, 1, 1)
        self.date = QtWidgets.QDateTimeEdit(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.date.setFont(font)
        self.date.setObjectName("date")
        self.gridLayout.addWidget(self.date, 8, 1, 1, 1)
        self.prePaid = QtWidgets.QCheckBox(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.prePaid.setFont(font)
        self.prePaid.setObjectName("prePaid")
        self.gridLayout.addWidget(self.prePaid, 8, 4, 1, 1)
        self.observationLabel = QtWidgets.QLabel(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.observationLabel.setFont(font)
        self.observationLabel.setObjectName("observationLabel")
        self.gridLayout.addWidget(self.observationLabel, 9, 0, 1, 1)
        self.accessoiresLabel = QtWidgets.QLabel(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.accessoiresLabel.setFont(font)
        self.accessoiresLabel.setObjectName("accessoiresLabel")
        self.gridLayout.addWidget(self.accessoiresLabel, 9, 2, 1, 1)
        self.observationText = QtWidgets.QTextEdit(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.observationText.setFont(font)
        self.observationText.setObjectName("observationText")
        self.gridLayout.addWidget(self.observationText, 10, 0, 1, 2)
        self.accessoiresText = QtWidgets.QTextEdit(modifier)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.accessoiresText.setFont(font)
        self.accessoiresText.setObjectName("accessoiresText")
        self.gridLayout.addWidget(self.accessoiresText, 10, 2, 1, 3)
        self.label_2 = QtWidgets.QLabel(modifier)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 11, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(modifier)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 11, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(modifier)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 11, 2, 1, 1)
        self.save_button = QtWidgets.QPushButton(modifier)
        self.save_button.setIconSize(QtCore.QSize(16, 16))
        self.save_button.setObjectName("save_button")
        self.gridLayout.addWidget(self.save_button, 11, 3, 1, 1)
        self.cancel_Button = QtWidgets.QPushButton(modifier)
        self.cancel_Button.setObjectName("cancel_Button")
        self.gridLayout.addWidget(self.cancel_Button, 11, 4, 1, 1)

        self.retranslateUi(modifier)
        QtCore.QMetaObject.connectSlotsByName(modifier)

    def retranslateUi(self, modifier):
        _translate = QtCore.QCoreApplication.translate
        modifier.setWindowTitle(_translate("modifier", "Modifier"))
        self.clientNameLabel.setText(_translate("modifier", "Nom et prénom du client : "))
        self.deviceTypeLabel.setText(_translate("modifier", "Type de l\'appareil :"))
        self.CIN_LABEL.setText(_translate("modifier", "Numéro de CIN :"))
        self.deviceBrandNameLabel.setText(_translate("modifier", "Marques de l\'appareil :"))
        self.companyNameLabel.setText(_translate("modifier", "Nom de la société :"))
        self.modelNameLabel.setText(_translate("modifier", "Model de l\'appareil :"))
        self.phoneNumberLabel.setText(_translate("modifier", "Numéro de téléphone :"))
        self.gouvernoratLabel.setText(_translate("modifier", "Gouvernorat :"))
        self.emailAddresLabel.setText(_translate("modifier", "Address Email :"))
        self.delegationLabel.setText(_translate("modifier", "Délégation :"))
        self.addressLabel.setText(_translate("modifier", "Adresse :"))
        self.label.setText(_translate("modifier", "Date de sortie :"))
        self.exit_date.setDisplayFormat(_translate("modifier", "d/M/yyyy h:mm"))
        self.priceLabel.setText(_translate("modifier", "Prix:"))
        self.exit_checkbox.setText(_translate("modifier", "Sorte"))
        self.fixed_checkbox.setText(_translate("modifier", "Fixée"))
        self.dateLabel.setText(_translate("modifier", "Date:"))
        self.date.setDisplayFormat(_translate("modifier", "d/M/yyyy h:mm"))
        self.prePaid.setText(_translate("modifier", "Prépayé"))
        self.observationLabel.setText(_translate("modifier", "Observation :"))
        self.accessoiresLabel.setText(_translate("modifier", "Accessoires Reçus"))
        self.save_button.setText(_translate("modifier", "Enregistrer"))
        self.save_button.setShortcut(_translate("modifier", "Return"))
        self.cancel_Button.setText(_translate("modifier", "Annuler"))
from qrc_sources import source