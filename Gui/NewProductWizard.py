from numpy import False_
from .include import *
from . import ui_NewProductWizard

class InsertQueryCareTaker():
    def __init__(self) -> None:
        self._mementos = []
        self._current = InsertQuery()
    
    def save(self):
        self._mementos.append(self._current.save())
        print("saved")
        print(self._mementos[-1].Type)
    
    def undo(self):
        if not len(self._mementos):
            print("cannot undo")
            return
        self._current.restore(self._mementos.pop())
        print("restored")
        print(self._current.Type)
    
    def SetType(self, type):
        self.save()
        self._current.Type = type
    
    def SetBrand(self, brand):
        self.save()
        self._current.Brand = brand
    
    def SetModel(self, model):
        self.save()
        self._current.Model = model
    
    def SetStorageRam(self, storageRam):
        self.save()
        self._current.StorageRam = storageRam
    
    def SetCountry(self, country):
        self.save()
        self._current.Country = country
    
    def SetColor(self, color):
        self.save()
        self._current.Color = color
    
    def SetWarrantyCompany(self, warrantyCompany):
        self.save()
        self._current.WarrantyCompany = warrantyCompany
    
class InsertQueryMemento():
    def __init__(self, state):
        self.Type = state.Type
        self.Brand = state.Brand
        self.Model = state.Model
        self.StorageRam = state.StorageRam
        self.Country = state.Country
        self.Color = state.Color
        self.WarrantyCompany = state.WarrantyCompany

class InsertQuery():
    def __init__(self):
        self.Type = ""
        self.Brand = ""
        self.Model = ""
        self.StorageRam = ""
        self.Country = ""
        self.Color = ""
        self.WarrantyCompany = ""
    
    def save(self):
        return InsertQueryMemento(self)
    
    def restore(self, insertMem):
        self.Type = insertMem.Type
        self.Brand = insertMem.Brand
        self.Model = insertMem.Model
        self.StorageRam = insertMem.StorageRam
        self.Country = insertMem.Country
        self.Color = insertMem.Color
        self.WarrantyCompany = insertMem.WarrantyCompany

class NewProductWizard(ui_NewProductWizard.Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.QueryCareTaker = InsertQueryCareTaker()
        self.setupUi(self)
        self.horizontalLayout_4.setEnabled(False)
        self.BeforeBtn.clicked.connect(lambda: self.QueryCareTaker.undo())
        self.PhoneBtn.clicked.connect(lambda: self.SelectType("phone"))
        self.TabletBtn.clicked.connect(lambda: self.SelectType("tablet"))
        self.WatchBtn.clicked.connect(lambda: self.SelectType("watch"))
        self.HandsfreeBtn.clicked.connect(lambda: self.SelectType("handsfree"))
        self.OtherBtn.clicked.connect(lambda: self.SelectType("other"))

        self.show()

    def SelectType(self, type):
        self.QueryCareTaker.SetType(type)
    