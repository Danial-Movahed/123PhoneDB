from .include import *
from . import ui_SellProductSerialCheck

class SellProductSerialCheck(QMainWindow, ui_SellProductSerialCheck.Ui_MainWindow):
    def __init__(self, ProductCode) -> None:
        super().__init__()
        self.ProductCode = ProductCode
        self.setupUi(self)
        print(ProductCode)
        self.show()