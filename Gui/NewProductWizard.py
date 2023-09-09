from .include import *
from . import ui_NewProductWizard, NewProductForm

class InsertQueryCareTaker():
    def __init__(self, insertQuery) -> None:
        self._mementos = []
        self._current = insertQuery
    
    def save(self):
        self._mementos.append(self._current.save())
    
    def undo(self):
        if not len(self._mementos):
            print("cannot undo")
            return
        self._current.restore(self._mementos.pop())
    
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
        self.Type = None
        self.Brand = None
        self.Model = None
        self.StorageRam = None
        self.Country = None
        self.Color = None
        self.WarrantyCompany = None
    
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
        self.InsertQuery = InsertQuery()
        self.QueryCareTaker = InsertQueryCareTaker(self.InsertQuery)
        self.currentListWidget = None
        self.setupUi(self)
        # Next and back buttons
        self.NextBtn.setVisible(False)
        self.BackBtn.setVisible(False)
        self.ConnectBtns()
        self.show()
    
    def ConnectBtns(self):
        self.NextBtn.clicked.connect(lambda: self.NextPage())
        self.BackBtn.clicked.connect(lambda: self.LastPage())
        # Page type
        self.PhoneBtn.clicked.connect(lambda: self.SelectType("Phone"))
        self.TabletBtn.clicked.connect(lambda: self.SelectType("Tablet"))
        self.WatchBtn.clicked.connect(lambda: self.SelectType("Watch"))
        self.HandsfreeBtn.clicked.connect(lambda: self.SelectType("Handsfree"))
        self.OtherBtn.clicked.connect(lambda: self.SelectType("Other"))
        # New btns
        self.NewBrandBtn.clicked.connect(lambda: self.OpenForm())
        self.NewModelBtn.clicked.connect(lambda: self.OpenForm())
        self.NewStorageRamBtn.clicked.connect(lambda: self.OpenForm())
        self.NewCountryBtn.clicked.connect(lambda: self.OpenForm())
        self.NewColorBtn.clicked.connect(lambda: self.OpenForm())
        self.NewWarrantyCompanyBtn.clicked.connect(lambda: self.OpenForm())

    def LastPage(self):
        self.QueryCareTaker.undo()
        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1)
        if self.stackedWidget.currentIndex() == 0:
            self.NextBtn.setVisible(False)
            self.BackBtn.setVisible(False)

    def NextPage(self):
        if self.stackedWidget.currentIndex() != 0:
            if len(self.currentListWidget.selectedItems()) < 1:
                print("Please select an item")
                return
        column = None
        if self.stackedWidget.currentIndex() + 1 == 1:
            # Brand
            column = Product.Brand.distinct()
            self.currentListWidget = self.BrandList
        elif self.stackedWidget.currentIndex() + 1 == 2:
            # Model
            column = Product.Model.distinct()
            self.QueryCareTaker.SetBrand(self.currentListWidget.currentItem().text().strip())
            self.currentListWidget = self.ModelList
        elif self.stackedWidget.currentIndex() + 1 == 3:
            # Storage Ram
            column = Product.StorageRam.distinct()
            self.QueryCareTaker.SetModel(self.currentListWidget.currentItem().text().strip())
            self.currentListWidget = self.StorageRamList
        elif self.stackedWidget.currentIndex() + 1 == 4:
            # Country
            column = Product.Country.distinct()
            self.QueryCareTaker.SetStorageRam(self.currentListWidget.currentItem().text().strip())
            self.currentListWidget = self.CountryList
        elif self.stackedWidget.currentIndex() + 1 == 5:
            # Color
            column = Product.Color.distinct()
            self.QueryCareTaker.SetCountry(self.currentListWidget.currentItem().text().strip())
            self.currentListWidget = self.ColorList
        elif self.stackedWidget.currentIndex() + 1 == 6:
            # Warranty
            column = Product.WarrantyCompany.distinct()
            self.QueryCareTaker.SetColor(self.currentListWidget.currentItem().text().strip())
            self.currentListWidget = self.WarrantyList
        else:
            self.QueryCareTaker.SetWarrantyCompany(self.currentListWidget.currentItem().text().strip())
            self.OpenForm()

        self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)
        self.currentListWidget.clear()
        for x in session.query(column).filter(
            ((self.InsertQuery.Type == None) or (Product.Type == self.InsertQuery.Type)),
            ((self.InsertQuery.Brand == None) or (Product.Brand == self.InsertQuery.Brand)),
            ((self.InsertQuery.Model == None) or (Product.Model == self.InsertQuery.Model)),
            ((self.InsertQuery.StorageRam == None) or (Product.StorageRam == self.InsertQuery.StorageRam)),
            ((self.InsertQuery.Country == None) or (Product.Country == self.InsertQuery.Country)),
            ((self.InsertQuery.Color == None) or (Product.Color == self.InsertQuery.Color)),
            ((self.InsertQuery.WarrantyCompany == None) or (Product.WarrantyCompany == self.InsertQuery.WarrantyCompany))
        ):
                self.currentListWidget.addItem(x[0])
        
    def OpenForm(self):
        self.wnd = NewProductForm.NewProductForm(self.InsertQuery)
        self.close()

    def SelectType(self, type):
        self.QueryCareTaker.SetType(type)
        self.NextBtn.setVisible(True)
        self.BackBtn.setVisible(True)
        self.NextPage()