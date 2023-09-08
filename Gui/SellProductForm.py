from .include import *
from . import ui_SellProductForm

class SellProductForm(QMainWindow, ui_SellProductForm.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.show()