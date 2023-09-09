from enum import unique
from hashlib import blake2s
from sqlite3 import Date
from numpy import unicode_
from sqlalchemy import Column, Boolean, String, create_engine, MetaData, Table, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import socket
import threading
import select
import pickle

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

        self.setWindowTitle("Error!")

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
    BuyFactorDate = Column(String)
    ProductType = Column(String)
    ProductBrand = Column(String)
    ProductModel = Column(String)
    ProductStorageRam = Column(String)
    ProductCountry = Column(String)
    ProductColor = Column(String)
    ProductWarrantyCompany = Column(String)
    ProductWarrantyTime = Column(Integer)
    ProductSerial = Column(String, unique=True)
    ProductBuyPrice = Column(String)
    ProductCode = Column(String)

class LogTable(Base):
    __tablename__ = "Logs"
    id = Column(Integer, primary_key=True, autoincrement=True)
    OrderCode = Column(String)
    OrderDate = Column(String)
    OrdererName = Column(String)
    OrdererNationalCode = Column(String)
    OrderSendType = Column(String)
    OrderRefCode = Column(String)
    ProductSerial = Column(String, unique=True)
    ProductSellPrice = Column(String)
    ProductCode = Column(String)
Base.metadata.create_all(engine)
Session = sessionmaker(bind = engine)
session = Session()