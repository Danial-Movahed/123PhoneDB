# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Resources/NewProductWizard.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(30, 30, 30, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("B Titr")
        font.setPointSize(30)
        self.label_12.setFont(font)
        self.label_12.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_12.setStyleSheet("padding: 20px;\n"
"background-color: rgb(17, 167, 0);\n"
"border-radius: 20px;")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.TypePage = QtWidgets.QWidget()
        self.TypePage.setObjectName("TypePage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.TypePage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.PhoneBtn = QtWidgets.QPushButton(self.TypePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PhoneBtn.sizePolicy().hasHeightForWidth())
        self.PhoneBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(20)
        self.PhoneBtn.setFont(font)
        self.PhoneBtn.setObjectName("PhoneBtn")
        self.verticalLayout_2.addWidget(self.PhoneBtn)
        self.TabletBtn = QtWidgets.QPushButton(self.TypePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TabletBtn.sizePolicy().hasHeightForWidth())
        self.TabletBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(20)
        self.TabletBtn.setFont(font)
        self.TabletBtn.setObjectName("TabletBtn")
        self.verticalLayout_2.addWidget(self.TabletBtn)
        self.WatchBtn = QtWidgets.QPushButton(self.TypePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WatchBtn.sizePolicy().hasHeightForWidth())
        self.WatchBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(20)
        self.WatchBtn.setFont(font)
        self.WatchBtn.setObjectName("WatchBtn")
        self.verticalLayout_2.addWidget(self.WatchBtn)
        self.HandsfreeBtn = QtWidgets.QPushButton(self.TypePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HandsfreeBtn.sizePolicy().hasHeightForWidth())
        self.HandsfreeBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(20)
        self.HandsfreeBtn.setFont(font)
        self.HandsfreeBtn.setObjectName("HandsfreeBtn")
        self.verticalLayout_2.addWidget(self.HandsfreeBtn)
        self.OtherBtn = QtWidgets.QPushButton(self.TypePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OtherBtn.sizePolicy().hasHeightForWidth())
        self.OtherBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("B Mitra")
        font.setPointSize(20)
        self.OtherBtn.setFont(font)
        self.OtherBtn.setObjectName("OtherBtn")
        self.verticalLayout_2.addWidget(self.OtherBtn)
        self.stackedWidget.addWidget(self.TypePage)
        self.BrandPage = QtWidgets.QWidget()
        self.BrandPage.setObjectName("BrandPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.BrandPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.NewBrandBtn = QtWidgets.QPushButton(self.BrandPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewBrandBtn.sizePolicy().hasHeightForWidth())
        self.NewBrandBtn.setSizePolicy(sizePolicy)
        self.NewBrandBtn.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.NewBrandBtn.setFont(font)
        self.NewBrandBtn.setObjectName("NewBrandBtn")
        self.horizontalLayout_5.addWidget(self.NewBrandBtn)
        self.label = QtWidgets.QLabel(self.BrandPage)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.BrandList = QtWidgets.QListWidget(self.BrandPage)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.BrandList.setFont(font)
        self.BrandList.setObjectName("BrandList")
        self.verticalLayout_3.addWidget(self.BrandList)
        self.stackedWidget.addWidget(self.BrandPage)
        self.ModelPage = QtWidgets.QWidget()
        self.ModelPage.setObjectName("ModelPage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.ModelPage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.NewModelBtn = QtWidgets.QPushButton(self.ModelPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewModelBtn.sizePolicy().hasHeightForWidth())
        self.NewModelBtn.setSizePolicy(sizePolicy)
        self.NewModelBtn.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.NewModelBtn.setFont(font)
        self.NewModelBtn.setObjectName("NewModelBtn")
        self.horizontalLayout_6.addWidget(self.NewModelBtn)
        self.label_2 = QtWidgets.QLabel(self.ModelPage)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.ModelList = QtWidgets.QListWidget(self.ModelPage)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.ModelList.setFont(font)
        self.ModelList.setObjectName("ModelList")
        self.verticalLayout_4.addWidget(self.ModelList)
        self.stackedWidget.addWidget(self.ModelPage)
        self.StorageRamPage = QtWidgets.QWidget()
        self.StorageRamPage.setObjectName("StorageRamPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.StorageRamPage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.NewStorageRamBtn = QtWidgets.QPushButton(self.StorageRamPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewStorageRamBtn.sizePolicy().hasHeightForWidth())
        self.NewStorageRamBtn.setSizePolicy(sizePolicy)
        self.NewStorageRamBtn.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.NewStorageRamBtn.setFont(font)
        self.NewStorageRamBtn.setObjectName("NewStorageRamBtn")
        self.horizontalLayout_7.addWidget(self.NewStorageRamBtn)
        self.label_3 = QtWidgets.QLabel(self.StorageRamPage)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.StorageRamList = QtWidgets.QListWidget(self.StorageRamPage)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.StorageRamList.setFont(font)
        self.StorageRamList.setObjectName("StorageRamList")
        self.verticalLayout_5.addWidget(self.StorageRamList)
        self.stackedWidget.addWidget(self.StorageRamPage)
        self.CountryPage = QtWidgets.QWidget()
        self.CountryPage.setObjectName("CountryPage")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.CountryPage)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.NewCountryBtn = QtWidgets.QPushButton(self.CountryPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewCountryBtn.sizePolicy().hasHeightForWidth())
        self.NewCountryBtn.setSizePolicy(sizePolicy)
        self.NewCountryBtn.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.NewCountryBtn.setFont(font)
        self.NewCountryBtn.setObjectName("NewCountryBtn")
        self.horizontalLayout_8.addWidget(self.NewCountryBtn)
        self.label_4 = QtWidgets.QLabel(self.CountryPage)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        self.CountryList = QtWidgets.QListWidget(self.CountryPage)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.CountryList.setFont(font)
        self.CountryList.setObjectName("CountryList")
        self.verticalLayout_6.addWidget(self.CountryList)
        self.stackedWidget.addWidget(self.CountryPage)
        self.ColorPage = QtWidgets.QWidget()
        self.ColorPage.setObjectName("ColorPage")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.ColorPage)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.NewColorBtn = QtWidgets.QPushButton(self.ColorPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewColorBtn.sizePolicy().hasHeightForWidth())
        self.NewColorBtn.setSizePolicy(sizePolicy)
        self.NewColorBtn.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.NewColorBtn.setFont(font)
        self.NewColorBtn.setObjectName("NewColorBtn")
        self.horizontalLayout_9.addWidget(self.NewColorBtn)
        self.label_5 = QtWidgets.QLabel(self.ColorPage)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.verticalLayout_7.addLayout(self.horizontalLayout_9)
        self.ColorList = QtWidgets.QListWidget(self.ColorPage)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.ColorList.setFont(font)
        self.ColorList.setObjectName("ColorList")
        self.verticalLayout_7.addWidget(self.ColorList)
        self.stackedWidget.addWidget(self.ColorPage)
        self.WarrantyPage = QtWidgets.QWidget()
        self.WarrantyPage.setObjectName("WarrantyPage")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.WarrantyPage)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.NewWarrantyCompanyBtn = QtWidgets.QPushButton(self.WarrantyPage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewWarrantyCompanyBtn.sizePolicy().hasHeightForWidth())
        self.NewWarrantyCompanyBtn.setSizePolicy(sizePolicy)
        self.NewWarrantyCompanyBtn.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.NewWarrantyCompanyBtn.setFont(font)
        self.NewWarrantyCompanyBtn.setObjectName("NewWarrantyCompanyBtn")
        self.horizontalLayout_10.addWidget(self.NewWarrantyCompanyBtn)
        self.label_6 = QtWidgets.QLabel(self.WarrantyPage)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_10.addWidget(self.label_6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_10)
        self.WarrantyList = QtWidgets.QListWidget(self.WarrantyPage)
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.WarrantyList.setFont(font)
        self.WarrantyList.setObjectName("WarrantyList")
        self.verticalLayout_8.addWidget(self.WarrantyList)
        self.stackedWidget.addWidget(self.WarrantyPage)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(23)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.BackBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BackBtn.sizePolicy().hasHeightForWidth())
        self.BackBtn.setSizePolicy(sizePolicy)
        self.BackBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.BackBtn.setFont(font)
        self.BackBtn.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(175, 0, 0);")
        self.BackBtn.setObjectName("BackBtn")
        self.horizontalLayout_4.addWidget(self.BackBtn)
        self.NextBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NextBtn.sizePolicy().hasHeightForWidth())
        self.NextBtn.setSizePolicy(sizePolicy)
        self.NextBtn.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("B Nazanin")
        font.setPointSize(20)
        self.NextBtn.setFont(font)
        self.NextBtn.setStyleSheet("border-radius: 10px;\n"
"background-color: rgb(0, 117, 14);")
        self.NextBtn.setObjectName("NextBtn")
        self.horizontalLayout_4.addWidget(self.NextBtn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "جادوگر ورود محصول"))
        self.label_12.setText(_translate("MainWindow", "فرم ورود محصولات به انبار"))
        self.PhoneBtn.setText(_translate("MainWindow", "گوشی موبایل"))
        self.TabletBtn.setText(_translate("MainWindow", "تبلت و کتابخوان"))
        self.WatchBtn.setText(_translate("MainWindow", "ساعت هوشمند"))
        self.HandsfreeBtn.setText(_translate("MainWindow", "هدفون و هندزفری"))
        self.OtherBtn.setText(_translate("MainWindow", "لوازم جانبی دیگر"))
        self.NewBrandBtn.setText(_translate("MainWindow", "جدید"))
        self.label.setText(_translate("MainWindow", "برند"))
        self.NewModelBtn.setText(_translate("MainWindow", "جدید"))
        self.label_2.setText(_translate("MainWindow", "مدل"))
        self.NewStorageRamBtn.setText(_translate("MainWindow", "جدید"))
        self.label_3.setText(_translate("MainWindow", "حافظه / رم"))
        self.NewCountryBtn.setText(_translate("MainWindow", "جدید"))
        self.label_4.setText(_translate("MainWindow", "کشور سازنده"))
        self.NewColorBtn.setText(_translate("MainWindow", "جدید"))
        self.label_5.setText(_translate("MainWindow", "رنگ"))
        self.NewWarrantyCompanyBtn.setText(_translate("MainWindow", "جدید"))
        self.label_6.setText(_translate("MainWindow", "شرکت گارانتی‌کننده"))
        self.BackBtn.setText(_translate("MainWindow", "قبلی"))
        self.NextBtn.setText(_translate("MainWindow", "بعدی"))
