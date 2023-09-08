from .include import *
from . import SellProductEnterProductCode, ui_Main, NewProductWizard, SellProductForm

class MainUI(ui_Main.Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.AddProductBtn.clicked.connect(self.AddProduct)
        self.SellProductBtn.clicked.connect(self.SellProduct)
        self.show()
    
    def AddProduct(self) -> None:
        self.AddProductWizard = NewProductWizard.NewProductWizard()

    def SellProduct(self) -> None:
        self.SellProductEnterProductCode = SellProductEnterProductCode.SellProductEnterProductCode()
        self.SellProductEnterProductCode.closeEvent = self.OpenSellProductForm

    def OpenSellProductForm(self) -> None:
        self.SellProductForm = SellProductForm.SellProductForm(self.SellProductEnterProductCode.ProductCodeEdit.text())