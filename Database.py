import sqlite3
import os
import tkinter as tk
from tkinter import messagebox as mBox


class Database:

    def __init__(self, db):
        # ------------------------------------------
        # Database Functions
        # ------------------------------------------
        # If Not Existing, Create batabase, data tables and system ledger accounts
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS ClientsInfo ("
                         "Client_ID INTEGER  PRIMARY KEY AUTOINCREMENT, "
                         "FirstName STRING(50) NOT NULL,"
                         "LastName STRING(50) NOT NULL,"
                         "Email VARCHAR (50) NOT NULL, "
                         "Address VARCHAR (50) NOT NULL,"
                         "Phone INT(7) NOT NULL,  "
                         "Mobile INT(10) NOT NULL, "
                         "Company STRING(25) NOT NULL)")

        self.cur.execute("CREATE TABLE IF NOT EXISTS ClientsJournal("
                         "Txn_ID INTEGER PRIMARY KEY NOT NULL,"
                         "Description STRING(50) NOT NULL,"
                         "Date DATETIME NOT NULL,"
                         "Time DATETIME NOT NULL,"
                         "CreditAmount FLOAT (10) NOT NULL,"
                         "DebitAmount FLOAT (10) NOT NULL,"
                         "Balance_Amount DECIMAL NOT NULL,"
                         "Client_ID INTEGER, FOREIGN KEY(Client_ID) REFERENCES ClientsInfo(Client_ID))")
        self.conn.commit()
        self.conn.close()

    def addClient(self, c_row):
        '''
        Insert an entry into Journal
        '''
        self.conn = sqlite3.connect('GSP_database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("INSERT INTO ClientsInfo VALUES  (NULL,?,?,?,?,?,?,? )", c_row)
        self.conn.commit()
        self.conn.close()

    def deleteClient(self, c_row):
        '''
        Insert an entry into Journal
        '''
        self.conn = sqlite3.connect('GSP_database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("DELETE FROM ClientsInfo WHERE FirstName='%s'", c_row)
        self.conn.commit()
        self.conn.close()

    def showClientList(self, c_type):
        '''
        Return all Namelist of Clients
        '''
        namelist = list()
        self.conn = sqlite3.connect('GSP_database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM ClientsInfo ORDER BY Client_ID")
        for row in self.cur:
            namelist.append(row)
        self.conn.close()
        return namelist

    def addTransaction(self, data):
        self.conn = sqlite3.connect('GSP_database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("INSERT INTO ClientsJournal VALUES  (NULL,?,?,?,?,?,?,?)", data)
        self.conn.commit()
        self.conn.close()

    def deleteTransaction(self, id):
        self.conn = sqlite3.connect('GSP_database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("DELETE FROM ClientsJournal WHERE Txn_ID=?", (id,))
        self.conn.commit()
        self.conn.close()

    def getTransaction(self, id):
        '''
        Return Ledger of Clients
        '''
        txnList = list()
        self.conn = sqlite3.connect('GSP_database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM ClientsJournal WHERE Client_ID=? ORDER BY Date", (id,))
        for row in self.cur:
            txnList.append(row)
        self.conn.close()
        return txnList


