from .include import *
from . import ui_NewProductForm
from persiantools.jdatetime import JalaliDate
import datetime

class NewProductForm(ui_NewProductForm.Ui_MainWindow, QMainWindow):
    def __init__(self, insertQuery: "InsertQuery") -> None:
        super().__init__()
        self.setupUi(self)
        self.InsertQuery = insertQuery
        self.ProductTypeEdit.setText(insertQuery.Type)
        self.ProductBrandEdit.setText(insertQuery.Brand)
        self.ProductModelEdit.setText(insertQuery.Model)
        self.ProductStorageRamEdit.setText(insertQuery.StorageRam)
        self.ProductCountryEdit.setText(insertQuery.Country)
        self.ProductColorEdit.setText(insertQuery.Color)
        self.ProductWarrantyCompanyEdit.setText(insertQuery.WarrantyCompany)
        self.SetProductCode()
        self.CancelBtn.clicked.connect(lambda: self.close())
        self.ContinueBtn.clicked.connect(lambda: self.Save())
        today = JalaliDate.today()
        self.BuyFactorDateYearSpin.setValue(today.year)
        self.BuyFactorDateMonthSpin.setValue(today.month)
        self.BuyFactorDateDaySpin.setValue(today.day)
        self.show()

    def Check(self):
        if self.BuyFactorCodeEdit.text() != "" and self.BuyFactorDateYearSpin.text() != "" and self.ProductTypeEdit.text() != "" and self.ProductBrandEdit.text() != "" and self.ProductModelEdit.text() != "" and self.ProductStorageRamEdit.text() != "" and self.ProductCountryEdit.text() != "" and self.ProductColorEdit.text() != "" and self.ProductWarrantyCompanyEdit.text() != "" and self.ProductWarrantyTimeSpin.text() != "" and self.ProductSerialEdit.text() != "" and self.ProductBuyPriceEdit.text() != "" and self.ProductCodeEdit.text() != "":
            return True
        return False
    
    def Save(self):
        if not self.Check():
            self.dlg = ErrorDialog("لطفا همه بخش‌ها را پر کنید!", self)
            self.dlg.show()
            return
        session.add(Product(
            BuyFactorCode = self.BuyFactorCodeEdit.text(),
            BuyFactorDate = self.BuyFactorDateYearSpin.text()+"/"+self.BuyFactorDateMonthSpin.text()+"/"+self.BuyFactorDateDaySpin.text(),
            ProductType = self.ProductTypeEdit.text(),
            ProductBrand = self.ProductBrandEdit.text(),
            ProductModel = self.ProductModelEdit.text(),
            ProductStorageRam = self.ProductStorageRamEdit.text(),
            ProductCountry = self.ProductCountryEdit.text(),
            ProductColor = self.ProductColorEdit.text(),
            ProductWarrantyCompany = self.ProductWarrantyCompanyEdit.text(),
            ProductWarrantyTime = self.ProductWarrantyTimeSpin.text(),
            ProductSerial = self.ProductSerialEdit.text(),
            ProductBuyPrice = self.ProductBuyPriceEdit.text(),
            ProductCode = self.ProductCodeEdit.text()
        ))
        session.commit()
        self.close()

    def SetProductCode(self):
        for x in session.query(Product.ProductCode.distinct()).filter(
            (Product.ProductType == self.InsertQuery.Type),
            (Product.ProductBrand == self.InsertQuery.Brand),
            (Product.ProductModel == self.InsertQuery.Model),
            (Product.ProductStorageRam == self.InsertQuery.StorageRam),
            (Product.ProductCountry == self.InsertQuery.Country),
            (Product.ProductColor == self.InsertQuery.Color),
            (Product.ProductWarrantyCompany == self.InsertQuery.WarrantyCompany)
        ):
            self.ProductCodeEdit.setText(x[0])