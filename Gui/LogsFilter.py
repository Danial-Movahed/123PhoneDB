from .include import *
from . import ui_LogsFilter



class LogsFilter(ui_LogsFilter.Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.show()
