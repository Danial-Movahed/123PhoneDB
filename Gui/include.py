from enum import unique
from hashlib import blake2s
from sqlite3 import Date
from sqlalchemy import Column, Boolean, String, create_engine, MetaData, Table, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from persiantools.jdatetime import JalaliDate

class CDialog(QDialog):
    def __init__(self, label, Title, parent=None):
        super().__init__(parent)

        self.setWindowTitle(Title)
        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout = QVBoxLayout()
        message = QLabel(label)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

class ErrorDialog(QDialog):
    def __init__(self, label, parent=None):
        super().__init__(parent)

        self.setWindowTitle("خطا!")

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(lambda: self.close())
        self.layout = QVBoxLayout()
        message = QLabel(label)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


engine = create_engine('sqlite:///Database.db', echo = False)
Base = declarative_base()
class Product(Base):
    __tablename__ = "Products"
    id = Column(Integer, primary_key=True, autoincrement=True)
    BuyFactorCode = Column(String)
    BuyFactorDate = Column(Date)
    Type = Column(String)
    Brand = Column(String)
    Model = Column(String)
    StorageRam = Column(String)
    Country = Column(String)
    Color = Column(String)
    WarrantyCompany = Column(String)
    WarrantyTime = Column(Integer)
    Serial = Column(String, unique=True)
    BuyPrice = Column(String)
    Code = Column(String)
    isAvailable = Column(Boolean)

class Log(Base):
    __tablename__ = "Logs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    OrderCode = Column(String)
    OrderDate = Column(String)
    OrdererName = Column(String)
    OrdererNationalCode = Column(String)
    OrderSendType = Column(String)
    OrderRefCode = Column(String)
    Serial = Column(String, unique=True)
    SellPrice = Column(String)
    ProductCode = Column(String)
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()