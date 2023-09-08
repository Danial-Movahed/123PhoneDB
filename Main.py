from Gui.include import *
from Gui import MainUI

if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName("PhoneDB Management System")
    wnd = MainUI.MainUI()
    app.exec()