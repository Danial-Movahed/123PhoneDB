from .include import *
from . import ui_NewProductForm

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
        self.show()

    def SetProductCode(self):
        for x in session.query(ProductsTable.ProductCode.distinct()).filter(
            (ProductsTable.ProductType == self.InsertQuery.Type),
            (ProductsTable.ProductBrand == self.InsertQuery.Brand),
            (ProductsTable.ProductModel == self.InsertQuery.Model),
            (ProductsTable.ProductStorageRam == self.InsertQuery.StorageRam),
            (ProductsTable.ProductCountry == self.InsertQuery.Country),
            (ProductsTable.ProductColor == self.InsertQuery.Color),
            (ProductsTable.ProductWarrantyCompany == self.InsertQuery.WarrantyCompany)
        ):
            self.ProductCodeEdit.setText(x[0])