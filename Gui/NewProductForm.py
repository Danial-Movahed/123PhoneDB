from .include import *
from . import ui_NewProductForm
import datetime

class NewProductForm(ui_NewProductForm.Ui_MainWindow, QMainWindow):
    def __init__(self, insertQuery) -> None:
        super().__init__()
        self.setupUi(self)
        self.InsertQuery = insertQuery
        self.SetValues()
        self.CancelBtn.clicked.connect(lambda: self.close())
        self.ContinueBtn.clicked.connect(lambda: self.Save())
        self.show()

    def SetValues(self):
        self.ProductTypeEdit.setText(self.InsertQuery.Type)
        self.ProductBrandEdit.setText(self.InsertQuery.Brand)
        self.ProductModelEdit.setText(self.InsertQuery.Model)
        self.ProductStorageRamEdit.setText(self.InsertQuery.StorageRam)
        self.ProductCountryEdit.setText(self.InsertQuery.Country)
        self.ProductColorEdit.setText(self.InsertQuery.Color)
        self.ProductWarrantyCompanyEdit.setText(self.InsertQuery.WarrantyCompany)
        self.SetProductCode()
        self.SetTodayDate()

    def SetTodayDate(self):
        today = JalaliDate.today()
        self.BuyFactorDateYearSpin.setValue(today.year)
        self.BuyFactorDateMonthSpin.setValue(today.month)
        self.BuyFactorDateDaySpin.setValue(today.day)

    def Check(self):
        if (
            self.BuyFactorCodeEdit.text().strip() != ""          and
            self.BuyFactorDateYearSpin.text().strip() != ""      and
            self.ProductTypeEdit.text().strip() != ""            and
            self.ProductBrandEdit.text().strip() != ""           and
            self.ProductModelEdit.text().strip() != ""           and
            self.ProductStorageRamEdit.text().strip() != ""      and
            self.ProductCountryEdit.text().strip() != ""         and
            self.ProductColorEdit.text().strip() != ""           and
            self.ProductWarrantyCompanyEdit.text().strip() != "" and
            self.ProductWarrantyTimeSpin.text().strip() != ""    and
            self.ProductSerialEdit.text().strip() != ""          and
            self.ProductBuyPriceEdit.text().strip() != ""        and
            self.ProductCodeEdit.text().strip() != ""
            ):
            return True
        return False
    
    def Save(self):
        if not self.Check():
            self.dlg = ErrorDialog("لطفا همه بخش‌ها را پر کنید!", self)
            self.dlg.show()
            return
        session.add(Product(
            BuyFactorCode = self.BuyFactorCodeEdit.text().strip(),
            BuyFactorDate = self.BuyFactorDateYearSpin.text().strip()+"/"+self.BuyFactorDateMonthSpin.text().strip()+"/"+self.BuyFactorDateDaySpin.text().strip(),
            Type = self.ProductTypeEdit.text().strip(),
            Brand = self.ProductBrandEdit.text().strip(),
            Model = self.ProductModelEdit.text().strip(),
            StorageRam = self.ProductStorageRamEdit.text().strip(),
            Country = self.ProductCountryEdit.text().strip(),
            Color = self.ProductColorEdit.text().strip(),
            WarrantyCompany = self.ProductWarrantyCompanyEdit.text().strip(),
            WarrantyTime = self.ProductWarrantyTimeSpin.text().strip(),
            Serial = self.ProductSerialEdit.text().strip(),
            BuyPrice = self.ProductBuyPriceEdit.text().strip(),
            Code = self.ProductCodeEdit.text().strip()
        ))
        session.commit()
        self.close()

    def SetProductCode(self):
        for x in session.query(Product.Code.distinct()).filter(
            (Product.Type == self.InsertQuery.Type),
            (Product.Brand == self.InsertQuery.Brand),
            (Product.Model == self.InsertQuery.Model),
            (Product.StorageRam == self.InsertQuery.StorageRam),
            (Product.Country == self.InsertQuery.Country),
            (Product.Color == self.InsertQuery.Color),
            (Product.WarrantyCompany == self.InsertQuery.WarrantyCompany)
        ):
            self.ProductCodeEdit.setText(x[0])