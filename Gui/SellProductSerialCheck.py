from .include import *
from . import ui_SellProductSerialCheck, SellProductForm

class SellProductSerialCheck(ui_SellProductSerialCheck.Ui_MainWindow, QMainWindow):
    def __init__(self, ProductCode) -> None:
        super().__init__()
        self.ProductCode = ProductCode
        self.setupUi(self)
        self.ShowInfo()
        self.SearchSerial()
        self.SearchBtn.clicked.connect(lambda: self.SearchSerial())
        self.NextBtn.clicked.connect(lambda: self.Next())
        self.show()

    def ShowInfo(self):
        prod = session.query(Product).filter(Product.Code == self.ProductCode).first()
        if not prod:
            print("No result found!")
            return
        self.ProductLabel.setText(f"{prod.Type} {prod.Brand} {prod.Model} {prod.StorageRam} {prod.Country} {prod.Color} {prod.WarrantyCompany} {prod.WarrantyTime}")
    
    def SearchSerial(self):
        self.ProductSerialList.clear()
        for x in session.query(Product).filter(((self.ProductSerialEdit.text().strip() == "") or (Product.Serial == self.ProductSerialEdit.text().strip())) and (Product.Code == self.ProductCode)):
            if not x.isAvailable:
                continue
            self.ProductSerialList.addItem(x.Serial)

    def Next(self):
        if len(self.ProductSerialList.selectedItems()) == 0:
            self.errDlg = ErrorDialog("لطفا یک سریال انتخاب کنید!")
            self.errDlg.show()
        self.SellForm = SellProductForm.SellProductForm(self.ProductSerialList.selectedItems()[0].text())
        self.close()