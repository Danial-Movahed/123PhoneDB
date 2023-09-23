from .include import *
from . import ui_SellProductEnterProductCode

class SellProductEnterProductCode(ui_SellProductEnterProductCode.Ui_Dialog, QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.state = False
        self.NextBtn.clicked.connect(self.StateCheck)
        self.CancelBtn.clicked.connect(self.close)
        self.show()

    def StateCheck(self):
        if self.ProductCodeEdit.text().strip() == "":
            self.dlg = ErrorDialog("لطفا کد محصول را وارد کنید!", self)
            self.dlg.show()
            return
        self.state = True
        self.close()