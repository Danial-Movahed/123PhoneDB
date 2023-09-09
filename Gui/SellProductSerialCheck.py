from .include import *
from . import ui_SellProductSerialCheck

class SellProductSerialCheck(ui_SellProductSerialCheck.Ui_MainWindow, QMainWindow):
    def __init__(self, ProductCode) -> None:
        super().__init__()
        self.ProductCode = ProductCode
        self.setupUi(self)
        print(ProductCode)
        self.show()