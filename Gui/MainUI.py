from .include import *
from . import SellProductEnterProductID, ui_Main, NewProductWizard, SellProductForm

class MainUI(QMainWindow, ui_Main.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.AddProductBtn.clicked.connect(self.AddProduct)
        self.SellProductBtn.clicked.connect(self.SellProduct)
        self.show()
    
    def AddProduct(self) -> None:
        self.AddProductWizard = NewProductWizard.NewProductWizard()

    def SellProduct(self) -> None:
        self.SellProductEnterProductID = SellProductEnterProductID.SellProductEnterProductID()
        self.SellProductEnterProductID.closeEvent = self.OpenSellProductForm

    def OpenSellProductForm(self) -> None:
        self.SellProductForm = SellProductForm.SellProductForm()