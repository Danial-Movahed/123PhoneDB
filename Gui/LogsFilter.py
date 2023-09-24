from .include import *
from . import ui_LogsFilter

class LogsFilter(ui_LogsFilter.Ui_MainWindow, QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.SetupEditValidator()
        self.SetupComboBox()
        self.SearchBtn.clicked.connect(self.Search)
        self.show()

    def SetupEditValidator(self) -> None:
        onlyInt = QIntValidator()
        onlyInt.setRange(0, 2147483647)
        self.BuyPriceFrom.setValidator(onlyInt)
        self.BuyPriceTo.setValidator(onlyInt)
        self.SellPriceFrom.setValidator(onlyInt)
        self.SellPriceTo.setValidator(onlyInt)

    def SetupComboBox(self) -> None:
        self.ProductType.addItem("None")
        self.ProductType.setCurrentIndex(0)
        for x in session.query(Product.Type).distinct():
            self.ProductType.addItem(x.Type)
        
        self.ProductModel.addItem("None")
        self.ProductModel.setCurrentIndex(0)
        for x in session.query(Product.Model).distinct():
            self.ProductModel.addItem(x.Model)
        
        self.ProductBrand.addItem("None")
        self.ProductBrand.setCurrentIndex(0)
        for x in session.query(Product.Brand).distinct():
            self.ProductBrand.addItem(x.Brand)
        
        self.WarrantyCompany.addItem("None")
        self.WarrantyCompany.setCurrentIndex(0)
        for x in session.query(Product.WarrantyCompany).distinct():
            self.WarrantyCompany.addItem(x.WarrantyCompany)
            
        self.StorageRam.addItem("None")
        self.StorageRam.setCurrentIndex(0)
        for x in session.query(Product.StorageRam).distinct():
            self.StorageRam.addItem(x.StorageRam)
            
        self.OrderSendType.addItem("None")
        self.OrderSendType.setCurrentIndex(0)
        for x in session.query(Log.OrderSendType).distinct():
            self.OrderSendType.addItem(x.OrderSendType)
        
        self.Color.addItem("None")
        self.Color.setCurrentIndex(0)
        for x in session.query(Product.Color).distinct():
            self.Color.addItem(x.Color)
        
        self.Country.addItem("None")
        self.Country.setCurrentIndex(0)
        for x in session.query(Product.Country).distinct():
            self.Country.addItem(x.Country)

    def GetCheckBoxValue(self, checkbox: QCheckBox) -> bool:
        if checkbox.checkState() == Qt.PartiallyChecked:
            return False
        return True

    def Search(self) -> None:
        self.ShowTable.setRowCount(0)
        treeItemList = []
        try:
            for x in session.query(Product).outerjoin(Log, Product.Serial == Log.Serial).filter(
                (
                    (self.BuyDateFromDay.value() == 0 or self.BuyDateFromMonth.value() == 0 or self.BuyDateFromYear.value() == 0) or
                    (self.BuyDateToDay.value() == 0 or self.BuyDateToMonth.value() == 0 or self.BuyDateToYear.value() == 0) or
                    (
                        Product.BuyFactorDate.between(
                            JalaliDate(
                                self.BuyDateFromYear.value(),
                                self.BuyDateFromMonth.value(),
                                self.BuyDateFromDay.value()
                            ).to_gregorian(),
                            JalaliDate(
                                self.BuyDateToYear.value(),
                                self.BuyDateToMonth.value(),
                                self.BuyDateToDay.value()
                            ).to_gregorian()
                        )
                    )
                ),
                (
                    (self.BuyPriceFrom.text().strip() == "" or self.BuyPriceTo.text().strip() == "") or
                    (
                        Product.BuyPrice.between(
                            int(self.BuyPriceFrom.text().strip()),
                            int(self.BuyPriceTo.text().strip())
                        )
                    )
                ),
                (
                    (self.IsAvailable.checkState() == Qt.Unchecked) or
                    (Product.isAvailable == self.GetCheckBoxValue(self.IsAvailable))
                ),
                (
                    (self.SellDateFromDay.value() == 0 or self.SellDateFromMonth.value() == 0 or self.SellDateFromYear.value() == 0) or
                    (self.SellDateToDay.value() == 0 or self.SellDateToMonth.value() == 0 or self.SellDateToYear.value() == 0) or
                    (
                        Product.log.OrderDate.between(
                            JalaliDate(
                                self.SellDateFromYear.value(),
                                self.SellDateFromMonth.value(),
                                self.SellDateFromDay.value()
                            ).to_gregorian(),
                            JalaliDate(
                                self.SellDateToYear.value(),
                                self.SellDateToMonth.value(),
                                self.SellDateToDay.value()
                            ).to_gregorian()
                        )
                    )
                ),
                (
                    (self.SellPriceFrom.text().strip() == "" or self.SellPriceTo.text().strip() == "") or
                    (
                        Product.log.SellPrice.between(
                            int(self.SellPriceFrom.text().strip()),
                            int(self.SellPriceTo.text().strip())
                        )
                    )
                ),
                (
                    (self.ProductCode.text().strip() == "") or
                    (Product.Code == self.ProductCode.text().strip())
                ),
                (
                    (self.ProductType.currentText() == "None") or
                    (Product.Type == self.ProductType.currentText())
                ),
                (
                    (self.ProductModel.currentText() == "None") or
                    (Product.Model == self.ProductModel.currentText())
                ),
                (
                    (self.ProductBrand.currentText() == "None") or
                    (Product.Brand == self.ProductBrand.currentText())
                ),
                (
                    (self.WarrantyCompany.currentText() == "None") or
                    (Product.WarrantyCompany == self.WarrantyCompany.currentText())
                ),
                (
                    (self.WarrantyTime.value() == 0) or
                    (Product.WarrantyTime == self.WarrantyTime.value())
                ),
                (
                    (self.OrdererNationalCode.text().strip() == "") or
                    (Product.log.OrdererNationalCode == self.OrdererNationalCode.text().strip())
                ),
                (
                    (self.OrdererName.text().strip() == "") or
                    (Product.log.OrdererName == self.OrdererName.text().strip())
                ),
                (
                    (self.StorageRam.currentText() == "None") or
                    (Product.StorageRam == self.StorageRam.currentText())
                ),
                (
                    (self.OrderSendType.currentText() == "None") or
                    (Product.log.OrderSendType == self.OrderSendType.currentText())
                ),
                (
                    (self.Color.currentText() == "None") or
                    (Product.Color == self.Color.currentText())
                ),
                (
                    (self.Country.currentText() == "None") or
                    (Product.Country == self.Country.currentText())
                )
            ):
                rowPosition = self.ShowTable.rowCount()
                self.ShowTable.insertRow(rowPosition)
                self.ShowTable.setItem(rowPosition, 0, QTableWidgetItem(x.BuyFactorCode))
                jDate = JalaliDate(x.BuyFactorDate)
                self.ShowTable.setItem(rowPosition, 1, QTableWidgetItem(f"{jDate.year}/{jDate.month}/{jDate.day}"))
                self.ShowTable.setItem(rowPosition, 2, QTableWidgetItem(x.Type))
                self.ShowTable.setItem(rowPosition, 3, QTableWidgetItem(x.Brand))
                self.ShowTable.setItem(rowPosition, 4, QTableWidgetItem(x.Model))
                self.ShowTable.setItem(rowPosition, 5, QTableWidgetItem(x.StorageRam))
                self.ShowTable.setItem(rowPosition, 6, QTableWidgetItem(x.Country))
                self.ShowTable.setItem(rowPosition, 7, QTableWidgetItem(x.Color))
                self.ShowTable.setItem(rowPosition, 8, QTableWidgetItem(x.WarrantyCompany))
                self.ShowTable.setItem(rowPosition, 9, QTableWidgetItem(str(x.WarrantyTime)))
                self.ShowTable.setItem(rowPosition, 10, QTableWidgetItem(x.Serial))
                self.ShowTable.setItem(rowPosition, 11, QTableWidgetItem(str(x.BuyPrice)))
                self.ShowTable.setItem(rowPosition, 12, QTableWidgetItem(x.Code))

                tmp = QTableWidgetItem()
                tmp.setFlags(Qt.ItemIsEnabled)
                tmp.setText("موجود؟")
                if x.isAvailable:
                    tmp.setCheckState(Qt.Checked)
                else:
                    tmp.setCheckState(Qt.Unchecked)
                self.ShowTable.setItem(rowPosition, 13, tmp)
                currentLog = None
                if x.log == None:
                    continue
                if type(x.log) == InstrumentedList:
                    if len(x.log) == 0:
                        continue
                    currentLog = x.log[0]
                else:
                    currentLog = x.log
                self.ShowTable.setItem(rowPosition, 14, QTableWidgetItem(currentLog.OrderCode))
                jDate = JalaliDate(currentLog.OrderDate)
                self.ShowTable.setItem(rowPosition, 15, QTableWidgetItem(f"{jDate.year}/{jDate.month}/{jDate.day}"))
                self.ShowTable.setItem(rowPosition, 16, QTableWidgetItem(currentLog.OrdererName))
                self.ShowTable.setItem(rowPosition, 17, QTableWidgetItem(currentLog.OrdererNationalCode))
                self.ShowTable.setItem(rowPosition, 18, QTableWidgetItem(currentLog.OrderSendType))
                self.ShowTable.setItem(rowPosition, 19, QTableWidgetItem(currentLog.OrderRefCode))
                self.ShowTable.setItem(rowPosition, 20, QTableWidgetItem(str(currentLog.SellPrice)))
                
        except ValueError:
            errDlg = ErrorDialog("لطفا تاریخ را درست وارد کنید!")
            errDlg.show()