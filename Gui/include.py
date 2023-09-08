from enum import unique
from hashlib import blake2s
from sqlite3 import Date
from numpy import unicode_
from sqlalchemy import Column, Boolean, String, create_engine, MetaData, Table, Integer, Date
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
meta = MetaData()
ProductsTable = Table(
    'Products', meta, 
    Column('BuyFactorCode', String), 
    Column('BuyFactorDate', Date),
    Column('ProductType', String),
    Column('ProductBrand', String),
    Column('ProductModel', String),
    Column('ProductStorageRam', String),
    Column('ProductCountry', String),
    Column('ProductColor', String),
    Column('ProductWarrantyCompany', String),
    Column('ProductWarrantyTime', Integer),
    Column('ProductSerial', String, unique=True),
    Column('ProductBuyPrice', String),
    Column('ProductCode', String)
)
LogTable = Table(
    'Logs', meta, 
    Column("OrderCode", String),
    Column("OrderDate", Date),
    Column("OrdererName", String),
    Column("OrdererNationalCode", String),
    Column("OrderSendType", String),
    Column("OrderRefCode", String),
    Column('ProductSerial', String, unique=True),
    Column("ProductSellPrice", String),
    Column("ProductCode", String)
)
meta.create_all(engine)
DBConnection = engine.connect()