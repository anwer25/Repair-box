from docxtpl import DocxTemplate, InlineImage
from docx.shared import Inches


doc = DocxTemplate('templete/Fillable cash receipt template.docx')
myimage = InlineImage(doc, 'data/QRCODE/1158855_Imprimant_Epson.png', width=Inches(1.38),
                      height=Inches(1.23))
context = {
    'QR': myimage,
    'ID': 8845879854654

}
doc.render(context)
doc.save('test.docx')