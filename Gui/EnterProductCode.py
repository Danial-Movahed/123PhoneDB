from .include import *
from . import ui_EnterProductCode

class EnterProductCode(ui_EnterProductCode.Ui_Dialog, QDialog):
    def __init__(self, allowEmpty) -> None:
        super().__init__()
        self.setupUi(self)
        self.AllowEmpty = allowEmpty
        self.state = False
        self.NextBtn.clicked.connect(self.StateCheck)
        self.CancelBtn.clicked.connect(self.close)
        self.installEventFilter(self)
        self.show()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            if event.key() in (Qt.Key_Return, Qt.Key_Enter,):
                self.StateCheck()
                return True
        return super().eventFilter(obj, event)


    def StateCheck(self):
        if self.AllowEmpty:
            self.state = True
            self.close()
            return
        if self.ProductCodeEdit.text().strip() == "":
            self.dlg = ErrorDialog("لطفا کد محصول را وارد کنید!", self)
            self.dlg.show()
            return
        self.state = True
        self.close()