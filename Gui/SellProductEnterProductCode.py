from .include import *
from . import ui_SellProductEnterProductCode

class SellProductEnterProductCode(ui_SellProductEnterProductCode.Ui_Dialog, QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.state = False
        self.NextBtn.clicked.connect(self.StateCheck)
        self.show()

    def StateCheck(self):
        self.state = True
        self.close()