from .include import *
from . import ui_SellProductForm

class SellProductForm(ui_SellProductForm.Ui_MainWindow, QMainWindow):
    def __init__(self, ProductSerial) -> None:
        super().__init__()
        self.setupUi(self)
        self.Product = self.GetProductBySerial(ProductSerial)
        if not self.Product:
            print("No result found!")
        self.SetValues()
        self.CancelBtn.clicked.connect(lambda: self.close())
        self.ContinueBtn.clicked.connect(lambda: self.Save())
        self.show()
    
    def GetProductBySerial(self, ProductSerial):
        return session.query(Product).filter(Product.Serial == ProductSerial).first()

    def SetValues(self):
        self.SetTodayDate()
        self.ProductTypeEdit.setText(self.Product.Type)
        self.ProductTypeEdit.setReadOnly(True)
        self.ProductBrandEdit.setText(self.Product.Brand)
        self.ProductBrandEdit.setReadOnly(True)
        self.ProductModelEdit.setText(self.Product.Model)
        self.ProductModelEdit.setReadOnly(True)
        self.ProductStorageRamEdit.setText(self.Product.StorageRam)
        self.ProductStorageRamEdit.setReadOnly(True)
        self.ProductCountryEdit.setText(self.Product.Country)
        self.ProductCountryEdit.setReadOnly(True)
        self.ProductColorEdit.setText(self.Product.Color)
        self.ProductColorEdit.setReadOnly(True)
        self.ProductWarrantyCompanyEdit.setText(self.Product.WarrantyCompany)
        self.ProductWarrantyCompanyEdit.setReadOnly(True)
        self.ProductWarrantyTimeSpin.setValue(self.Product.WarrantyTime)
        self.ProductWarrantyTimeSpin.setReadOnly(True)
        self.ProductSerialEdit.setText(self.Product.Serial)
        self.ProductSerialEdit.setReadOnly(True)
        self.ProductCodeEdit.setText(self.Product.Code)
        self.ProductCodeEdit.setReadOnly(True)

    def SetTodayDate(self):
        today = JalaliDate.today()
        self.OrderDateYearSpin.setValue(today.year)
        self.OrderDateMonthSpin.setValue(today.month)
        self.OrderDateDaySpin.setValue(today.day)

    def Check(self):
        if (
            self.OrderCodeEdit.text().strip()  != "" and
            self.OrderDateYearSpin.text().strip()  != "" and
            self.OrderDateMonthSpin.text().strip()  != "" and
            self.OrderDateDaySpin.text().strip()  != "" and
            self.OrdererNameEdit.text().strip()  != "" and
            self.OrdererNationalCodeEdit.text().strip()  != "" and
            self.OrderSendTypeEdit.text().strip()  != "" and
            self.OrderRefCodeEdit.text().strip()  != "" and
            self.ProductSerialEdit.text().strip()  != "" and
            self.ProductSellPriceEdit.text().strip()  != "" and
            self.ProductCodeEdit.text().strip()  != ""
            ):
            return True
        return False

    def Save(self):
        if not self.Check():
            self.dlg = ErrorDialog("لطفا همه بخش‌ها را پر کنید!", self)
            self.dlg.show()
            return
        session.add(Log(
            OrderCode = self.OrderCodeEdit.text().strip(),
            OrderDate = self.OrderDateYearSpin.text().strip()+"/"+self.OrderDateMonthSpin.text().strip()+"/"+self.OrderDateDaySpin.text().strip(),
            OrdererName = self.OrdererNameEdit.text().strip(),
            OrdererNationalCode = self.OrdererNationalCodeEdit.text().strip(),
            OrderSendType = self.OrderSendTypeEdit.text().strip(),
            OrderRefCode = self.OrderRefCodeEdit.text().strip(),
            ProductSerial = self.ProductSerialEdit.text().strip(),
            ProductSellPrice = self.ProductSellPriceEdit.text().strip(),
            ProductCode = self.ProductCodeEdit.text().strip()
        ))
        self.Product.isSold = True
        session.commit()
        self.close()