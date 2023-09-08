from .include import *
from . import ui_SellProductEnterProductID

class SellProductEnterProductID(QMainWindow, ui_SellProductEnterProductID.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.show()