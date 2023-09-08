from .include import *
from . import ui_NewProductWizard

class NewProductWizard(QMainWindow, ui_NewProductWizard.Ui_MainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.show()