from .include import *
from . import ui_SellProductForm

class SellProductForm(QMainWindow, ui_SellProductForm.Ui_MainWindow):
    def __init__(self, ProductCode) -> None:
        super().__init__()
        self.setupUi(self)
        print(ProductCode)
        self.show()