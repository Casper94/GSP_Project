import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext, messagebox
from tkinter import *


import datetime as dt
import pytz

from Tooltips import createToolTip
from Database import Database
database = Database('GSP_database.db') #creates database file


class insertClientForm():

    def __init__(self, goal, comp):
        '''
        Constructor for Add to Client in it's own pop-up data dialog window
        '''

        # Create instance
        self.goal = goal
        c = comp
        self.frm = tk.Tk()
        # Add a title
        self.frm.title("Add New Client Entry")
        self.addClientForm(c)
        self.frm.mainloop()

    def addClientForm(self, comp):
        '''
        The form for journal access for anew transaction entry
        '''
        # Whole form label frame---------------------------------------
        self.infoFrame = ttk.LabelFrame(self.frm, text=' Input Form ')
        self.infoFrame.grid(column=0, row=0, padx=10, pady=10, sticky='W')

        # Name Entry field -------------------------------------
        self.lbl0 = tk.Label(self.infoFrame, text="First Name:").grid(column=0, row=0)
        self.e0 = tk.Entry(self.infoFrame, width=20)
        self.e0.grid(column=1, row=0, padx=5, pady=4, sticky='W')

        self.lbl0 = tk.Label(self.infoFrame, text="Last Name:").grid(column=0, row=1)
        self.e1 = tk.Entry(self.infoFrame, width=20)
        self.e1.grid(column=1, row=1, padx=5, pady=4, sticky='W')

        # -------------------------------------------------------------
        self.lbl2 = tk.Label(self.infoFrame, text="Email").grid(column=0, row=2)
        self.e2 = tk.Entry(self.infoFrame, width=25)
        self.e2.grid(column=1, row=2, padx=5, pady=4, sticky='W')

        # -------------------------------------------------------------
        self.lbl3 = tk.Label(self.infoFrame, text="Address").grid(column=0, row=3)
        self.e3 = tk.Entry(self.infoFrame, width=25)
        self.e3.grid(column=1, row=3, padx=5, pady=4, sticky='W')
        # -------------------------------------------------------------
        self.lbl4 = tk.Label(self.infoFrame, text="Phone no.").grid(column=0, row=4)
        self.e4 = tk.Entry(self.infoFrame, width=10)
        self.e4.grid(column=1, row=4, padx=5, pady=4, sticky='W')
        # -------------------------------------------------------------
        self.lbl5 = tk.Label(self.infoFrame, text="Mob Num : ").grid(column=0, row=5)
        self.e5 = tk.Entry(self.infoFrame, width=10)
        self.e5.grid(column=1, row=5, padx=5, pady=4, sticky='W')

        # --------------------------------------------------------------
        self.btn1 = ttk.Button(self.infoFrame, text="Add Client", command=lambda c=comp: self.on_click(c)).grid(column=0, row=9, padx=8,
                                                                                          pady=4, sticky='W')
        self.btn2 = ttk.Button(self.infoFrame, text="Cancel", command=lambda: self.on_cancel()).grid(column=1, row=9, padx=8,
                                                                                           pady=4, sticky='W')

    def on_click(self, comp):
        '''
        Save new Client information Entry and update associated Ledger accounts
        '''
        self.fname = self.e0.get()
        self.lname = self.e1.get()
        self.email = self.e2.get()
        self.address = self.e3.get()
        self.phone = self.e4.get()
        self.mobile = self.e5.get()
        ctype = comp
        c_row = (self.fname, self.lname, self.email, self.address, self.phone, self.mobile, ctype)

        if not all(c_row)==True:
            tk.messagebox.showerror(title='Empty Fields Error', message="Please fill all the empty fields")
        else:
            Database.addClient(self, c_row)
            self.frm.destroy()

    def on_cancel(self):
        self.frm.destroy()

class showClientData():
    def __init__(self, parent, clientData):
        '''
        Constructor for Show to Client Data in it's own pop-up data dialog window
        '''
        # self.clientData = parent
        self.frm = tk.Tk()
        # self.frm.update()
        self.frm.geometry(f'800x600+250+150')
        self.frm.title(f"{clientData[1]}'s Profile")

        self.showData(clientData)
        self.frm.mainloop()

    def _select_data_row(self, parent):
        global txnData
        print(self)
        print(parent)
        items = self.TxnDataview.item(self.TxnDataview.selection())
        txnData = []
        for i in items['values']:
            txnData.append(i)


    def showData(self, clientData):

        '''
        The window to show overall transaction with a customer
        '''
        # ----Customer Data label frame---------------------------------------
        self.upperframe = ttk.Labelframe(self.frm, width=650, height=300)
        self.upperframe.pack(fill='x')
        # -------------------- Customer Info Display --------------------
        self.infoFrame = ttk.Labelframe(self.upperframe, text=" Customer's Information ", width=550, height=500)
        self.infoFrame.grid(column=0, row=0, padx=4, pady=4)

        ttk.Label(self.infoFrame, text=f"Name \t: \t{clientData[1]}\nEmail \t: \t{clientData[3]}\nPhone \t: \t{clientData[4]}\nMob \t: \t{clientData[5]}").grid(column=0, row=0, padx=4, pady=4, sticky='W')
        ttk.Label(self.infoFrame, text= '\t').grid(column=1, row=0, padx=4, pady=4, sticky='W')
        ttk.Label(self.infoFrame, text=f"Address  \t: {clientData[2]}\nCompany\t: \nCustomer ID \t: {clientData[0]}").grid(column=2, row=0, padx=4, pady=4, sticky='W')

        #----------- Journal Action Buttons  --------------------------------
        actionBtnFrm = ttk.Labelframe(self.upperframe, text=" Perform Actions ")
        actionBtnFrm.grid(column=0, row=1, padx=4, pady=4, sticky='W')
        self.addCredit = ttk.Button(actionBtnFrm, text="Give Credit", command=lambda x='Credit', curID = clientData[0] : addTransaction(self,x, curID)).grid(column=0,row=0,padx=4, pady=4)
        self.addPayment = ttk.Button(actionBtnFrm, text="Accept Payment", command=lambda x='Payment', curID = clientData[0]: addTransaction(self,x, curID)).grid(column=1,row=0,padx=4, pady=4)
        self.getStatement = ttk.Button(actionBtnFrm, text="Refresh List", command = lambda : self._showJournal(clientData[0])).grid(column=3,row=0,padx=4, pady=4)
        self.getStatement = ttk.Button(actionBtnFrm, text="Delete item", command = lambda: Database.deleteTransaction(self, txnData[0])).grid(column=4,row=0,padx=4, pady=4)
        self.getStatement = ttk.Button(actionBtnFrm, text="Get Statement").grid(column=5,row=0,padx=4, pady=4)

        #-------------- Journal Data View Frame ---------------------------
        self.lowerframe = ttk.Labelframe(self.frm, width=200, height=300)
        self.lowerframe.pack(fill='x')
        ttk.Label(self.lowerframe, text="Clients Journal").pack()

        self.TxnDataview = ttk.Treeview(self.lowerframe, columns=(1, 2, 3, 4, 5, 6, 7), show='headings', height="15",
                                       selectmode='browse')
        self.TxnDataview.pack(side='left', fill='both', expand=True)
        self.scrlBar1 = ttk.Scrollbar(self.lowerframe, orient="vertical", command=self.TxnDataview.yview)
        self.TxnDataview.configure(yscrollcommand=self.scrlBar1.set)
        self.scrlBar1.pack(side='right', fill='y')

        self.TxnDataview.column(1, width=1, minwidth=1, anchor=tk.W);    self.TxnDataview.heading(1, text='Txn_ID')
        self.TxnDataview.column(2, width=75, minwidth=20, stretch=tk.NO);   self.TxnDataview.heading(2, text='Date')
        self.TxnDataview.column(3, width=75, minwidth=50, anchor=tk.W);    self.TxnDataview.heading(3, text='Time')
        self.TxnDataview.column(4, width=200, minwidth=50, anchor=tk.W);     self.TxnDataview.heading(4, text='Description')
        self.TxnDataview.column(5, width=100, minwidth=50, anchor=tk.W);    self.TxnDataview.heading(5, text='Credit')
        self.TxnDataview.column(6, width=100, minwidth=50, anchor=tk.W);    self.TxnDataview.heading(6, text='Payment')
        self.TxnDataview.column(7, width=100, minwidth=50, anchor=tk.W);    self.TxnDataview.heading(7, text='Rem. Balance')
        self.TxnDataview.bind('<ButtonRelease-1>', self._select_data_row)
        self._showJournal(clientData[0])


    def _showJournal(self, id):
        for row in self.TxnDataview.get_children():
            self.TxnDataview.delete(row)
        listAll = Database.getTransaction(self, id)
        for row in listAll:
            self.TxnDataview.insert("", 'end', values=(row[0], row[2], row[3], row[1], row[4], row[5], row[6]))


class addTransaction():


    here = pytz.timezone('Asia/kathmandu')
    currentDT = dt.datetime.now(here)
    def __init__(self, goal, txnType, ID):
        '''
        The form for a new transaction entry
        '''

        # Create instance
        self.goal = goal
        self.txnType = txnType
        self.clientID = ID
        self.frm = tk.Tk()
        # Add a title
        if txnType =='Credit':
            self.frm.title("Give Credit ")
        else:
            self.frm.title("Accept Payment ")

        self.add_ActionForm(txnType, self.clientID)
        self.frm.mainloop()

    def add_ActionForm(self, txnType, clientID):
        '''
        The form for journal access for a new transaction entry
        '''
        print("transaction type ", txnType)
        print("Client ID ", clientID)

        # Whole form label frame---------------------------------------
        if txnType == 'Credit':
            self.infoFrame = ttk.LabelFrame(self.frm, text=' Give Credit  ')
        else:
            self.infoFrame = ttk.LabelFrame(self.frm, text=' Accept Payment ')
        self.infoFrame.grid(column=0, row=0, padx=10, pady=10, sticky='W')

        # --------- Entry field -------------------------------------
        self.lbl0 = tk.Label(self.infoFrame, text="Description").grid(column=0, row=0)
        self.e0 = tk.Entry(self.infoFrame, width=20)
        self.e0.grid(column=1, row=0, padx=5, pady=4, sticky='W')
        # -------------------------------------------------------------
        self.lbl1 = tk.Label(self.infoFrame, text="Date").grid(column=0, row=1)
        self.e1 = tk.Entry(self.infoFrame,width=10)
        self.e1.grid(column=1, row=1, padx=5, pady=4, sticky='W')
        rnow = str(self.currentDT.year)+'-'+str(self.currentDT.month)+'-'+str(self.currentDT.day)
        self.e1.insert(0, rnow)
            # Associated tool tip
        dateEnter = 'Date  transaction entered, yyyy-mm-dd, defaults to today, '
        createToolTip(self.e1, dateEnter)
        # -------------------------------------------------------------
        self.lbl2 = tk.Label(self.infoFrame, text="Time").grid(column=0, row=2)
        self.e2 = tk.Entry(self.infoFrame,width=9)
        self.e2.grid(column=1, row=2, padx=5, pady=4, sticky='W')
        rtime = str(self.currentDT.hour)+':'+str(self.currentDT.minute)+':'+str(self.currentDT.second)
        self.e2.insert(0, rtime)
            # Associated tool tip
        timeEnter = 'Time transaction is entered. [hh:mm:ss] optional, defaults to Now'
        createToolTip(self.e2, timeEnter)
        # -------------------------------------------------------------
        if txnType=='Credit':
            self.lbl3 = tk.Label(self.infoFrame, text="Credit Amount.").grid(column=0, row=4)
        else:
            self.lbl3 = tk.Label(self.infoFrame, text="Payment Amount.").grid(column=0, row=4)
        self.e3 = tk.Entry(self.infoFrame, width=15)
        self.e3.grid(column=1, row=4, padx=5, pady=4, sticky='W')
        # --------------------------------------------------------------
        self.btn1 = ttk.Button(self.infoFrame, text=f'Add {txnType}', command=lambda t=txnType, id=clientID: self.on_commit(t, id)).grid(column=0, row=9, padx=8,
                                                                                          pady=4, sticky='W')
        self.btn2 = ttk.Button(self.infoFrame, text="Cancel", command=lambda: insertClientForm.on_cancel(self)).grid(column=1, row=9, padx=8,
                                                                                           pady=4, sticky='W')

    def on_commit(self, txntype, id):
        try:
            self.description = self.e0.get()
            self.date = self.e1.get()
            self.time = self.e2.get()
            if txntype == 'Credit':
                self.creditAmt =int(self.e3.get())
                self.paymentAmt = 0
            else:
                self.creditAmt = 0
                self.paymentAmt = int(self.e3.get())

            listAll = Database.getTransaction(self, id)
            print(listAll)
            if not listAll == True:
                self.prevBalance = 0
            else:
                self.prevBalance = listAll[-1][-2]
            self.curBalance = self.prevBalance + self.paymentAmt - self.creditAmt

            ldg_data = (self.description, self.date, self.time, self.creditAmt, self.paymentAmt, self.curBalance, id )
            print(ldg_data)
            Database.addTransaction(self, ldg_data)
            self.frm.destroy()


        except ValueError:
            tk.messagebox.showerror(title='Data Type Error', message=f"Please fill Number in {txntype} fields")

    def getStatementForm(self):
        pass