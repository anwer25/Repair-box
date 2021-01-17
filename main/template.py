from docxtpl import DocxTemplate, InlineImage
from docx.shared import Cm, Inches, Mm, Emu
from PyQt5.QtCore import pyqtSignal, QSettings


class templateEngine:

    def __init__(self, clientName: str, phoneNumber: str, companyName: str, deviceType: str, deviceBrand: str,
                 deviceModel: str, ID: str,date: str, prePaid: str, price: any, accessories: str, qrimage: str):
        super(templateEngine, self).__init__()
        self.___settings = QSettings('alpha', 'Repair_box')
        self.clientName = clientName
        self.phoneNumber = phoneNumber
        self.companyName = companyName
        self.deviceType = deviceType
        self.deviceBrand = deviceBrand
        self.deviceModel = deviceModel
        self.id = ID
        self.date = date
        self.prePaid = prePaid
        self.price = price
        self.accessories = accessories
        self.qrImage = qrimage
    """
    def run(self) -> None:
        self.templateWriter()
    """
    def templateWriter(self) -> None:
        docx = self.___settings.value('DOC_TEMPLATE', 'templete/temp0.docx', type=str)
        qrImageWidth = self.___settings.value('QR_IMAGE_WIDTH', 1.38)
        qrImageHeight = self.___settings.value('QR_IMAGE_HEIGHT', 1.23)
        logoImageWidth = self.___settings.value('LOGO_WIDTH', 1.38)
        logoImageHeight = self.___settings.value('LOGO_HEIGHT', 1.23)
        measuringUnitLogoImage = self.___settings.value('LOGO_IMAGE_MEASURING_UNIT', 'Inches', type=str)
        measuringUnitQrImage = self.___settings.value('QR_IMAGE_MEASURING_UNIT', 'Inches', type=str)
        logoCodePlace = self.___settings.value('LOGO_KEY', 'LOGO', type=str)
        logoImage = self.___settings.value('LOGO_IMAGE', '', type=str)
        qrCodePlace = self.___settings.value('QR_KEY', 'QR', type=str)
        companyAddressCodePlace = self.___settings.value('COMPANY_ADDRESS_KEY', 'companyAddress', type=str)
        companyAddress = self.___settings.value('COMPANY_ADDRESS', 'test', type=str)
        companyPhonePlace = self.___settings.value('COMPANY_PHONE_KEY', 'companyPhone', type=str)
        companyPhone = self.___settings.value('COMPANY_PHONE', '54876555', type=str)
        companyFaxPlace = self.___settings.value('COMPANY_FAX_KEY', 'companyFax', type=str)
        companyFax = self.___settings.value('COMPANY_FAX', '54578754', type=str)
        companyEmailPlace = self.___settings.value('COMPANY_EMAIL_KEY', 'companyEmail', type=str)
        companyEmail = self.___settings.value('COMPANY_EMAIL', 'aaaaa@test.com', type=str)
        companyWebSitePlace = self.___settings.value('COMPANY_WEB_SITE_KEY', 'companySite', type=str)
        companyWebSite = self.___settings.value('COMPANY_SITE', 'www.test.com', type=str)
        companyNamePlace = self.___settings.value('COMPANY_NAME_KEY', 'Company', type=str)
        companyName = self.___settings.value('COMPANY_NAME__KEY', 'TEST', type=str)
        idPlace = self.___settings.value('ID_KEY', 'ID', type=str)
        datePlace = self.___settings.value('DATE_KEY', 'Date', type=str)
        clientNamePlace = self.___settings.value('CLIENT_NAME_KEY', 'clientName', type=str)
        clientNumberPlace = self.___settings.value('CLIENT_NUMBER_KEY', 'clientNumber', type=str)
        deviceTypePlace = self.___settings.value('DEVICE_TYPE_KEY', 'deviceType', type=str)
        deviceBrandPlace = self.___settings.value('DEVICE_BRAND_KEY', 'deviceBrand', type=str)
        deviceModelPlace = self.___settings.value('DEVICE_MODEL_KEY', 'deviceModel', type=str)
        pricePlace = self.___settings.value('PRICE_KEY', 'price', type=str)
        prePaid = self.___settings.value('PRE_PAID_KEY', 'prePaid', type=str)
        Accessories = self.___settings.value('ACCESSORIES_KEY', 'Accessories', type=str)
        clientCompany = self.___settings.value('CLIENT_COMPANY_PLACE', 'clientcompany', type=str)
        savePlace = self.___settings.value('SAVE_WORD_FILE_PLACE', 'main\\data\\clientsWordFile\\', type=str)

        doc = DocxTemplate(docx)
        try:
            if measuringUnitQrImage == 'Inches':
                qrImageUnit = Inches
            elif measuringUnitQrImage == 'Cm':
                qrImageUnit = Cm
            elif measuringUnitQrImage == 'Mm':
                qrImageUnit = Mm
            else:
                qrImageUnit = Emu
        except NameError:
            qrImageUnit = Inches

        try:
            if measuringUnitLogoImage == 'Inches':
                logoUnit = Inches
            elif measuringUnitLogoImage == 'Cm':
                logoUnit = Cm
            elif measuringUnitLogoImage == 'Mm':
                logoUnit = Mm
            else:
                logoUnit = Emu
        except NameError:
            logoUnit = Inches

        qrImage = InlineImage(doc, self.qrImage, width=qrImageUnit(qrImageWidth),
                              height=qrImageUnit(qrImageHeight))
        if logoImage != '':
            logo = InlineImage(doc, logoImage, width=logoUnit(logoImageWidth), height=logoUnit(logoImageHeight))
        else:
            logo = 'logo'
        context = {
            qrCodePlace: qrImage,
            logoCodePlace: logo,
            companyNamePlace: companyName,
            companyAddressCodePlace: companyAddress,
            companyPhonePlace: companyPhone,
            companyFaxPlace: companyFax,
            companyEmailPlace: companyEmail,
            companyWebSitePlace: companyWebSite,
            idPlace: self.id,
            datePlace: self.date,
            clientNamePlace: self.clientName,
            clientNumberPlace: self.phoneNumber,
            deviceTypePlace: self.deviceType,
            deviceBrandPlace: self.deviceBrand,
            deviceModelPlace: self.deviceModel,
            pricePlace: self.price,
            prePaid: self.prePaid,
            Accessories: self.accessories,
            clientCompany: self.companyName
        }
        doc.render(context)
        doc.save(f'{savePlace}{self.id}.docx')
