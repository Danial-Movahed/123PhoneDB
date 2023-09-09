from .include import *
from . import ui_NewProductForm

class NewProductForm(ui_NewProductForm.Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        
        self.show()