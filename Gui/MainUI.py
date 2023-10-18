from .include import *
from . import EnterProductCode, ui_Main, NewProductWizard, SellProductSerialCheck, LogsFilter

class MainUI(ui_Main.Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.AddProductBtn.clicked.connect(self.AddProduct)
        self.SellProductBtn.clicked.connect(self.SellProduct)
        self.LogsBtn.clicked.connect(self.OpenLogsFilter)
        self.show()
    
    def OpenLogsFilter(self) -> None:
        self.LogsFilterWnd = LogsFilter.LogsFilter()

    def AddProduct(self) -> None:
        self.AddProductEnterProductCode = EnterProductCode.EnterProductCode(True)
        self.AddProductEnterProductCode.closeEvent = self.OpenAddProductWizard

    def OpenAddProductWizard(self, event) -> None:
        if self.AddProductEnterProductCode.state:
            self.AddProductWizard = NewProductWizard.NewProductWizard(self.AddProductEnterProductCode.ProductCodeEdit.text().strip())

    def SellProduct(self) -> None:
        self.SellProductEnterProductCode = EnterProductCode.EnterProductCode(False)
        self.SellProductEnterProductCode.closeEvent = self.OpenSellProductForm

    def OpenSellProductForm(self, event) -> None:
        if self.SellProductEnterProductCode.state:
            self.SellProductSerialCheck = SellProductSerialCheck.SellProductSerialCheck(self.SellProductEnterProductCode.ProductCodeEdit.text().strip())