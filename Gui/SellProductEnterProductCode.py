from .include import *
from . import ui_SellProductEnterProductCode

class SellProductEnterProductCode(ui_SellProductEnterProductCode.Ui_Dialog, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.show()