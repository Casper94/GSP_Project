import tkinter as tk
from tkinter import ttk

from Functions import insertClientForm, showClientData
from Database import Database




class Basic(object):
    def __init__(self, parent, controller):
        pass

    def _get_selected_row(self, parent):
        global clientData
        items = self.Clientview.item(self.Clientview.selection())
        clientData=[]
        for i in items['values']:
            clientData.append(i)

    def createWidgets(self,parent, c_type):
    # --------------Tab Controls created here --------------------------------------
            self.tabControl = ttk.Notebook(parent)  # Create Tab Controls

            self.tab1 = ttk.Frame(self.tabControl)
            self.tabControl.add(self.tab1, text=' Clients List ')

            self.tab2 = ttk.Frame(self.tabControl)
            self.tabControl.add(self.tab2, text=' Reminder ')

            self.tabControl.pack()  # Pack to make visible

            # CLient's List TAB
            frm1 = ttk.Labelframe(self.tab1, width=650, height=300)
            frm1.pack(fill='x')
            ttk.Label(frm1).grid(column=0, row=0, padx=4, pady=4, sticky='W')
            # ------------- Buttons Frame----------------------
            frm1a = ttk.Labelframe(frm1, text="Perform Actions", width=550, height=500)
            frm1a.grid(column=0, row=1, padx=4, pady=4)
            self.newClient = ttk.Button(frm1a, text="Add New Client",
                                        command= lambda: insertClientForm(self, c_type)).grid(column=1, row=1, padx=4, pady=4)
            self.deleteClient = ttk.Button(frm1a, text="Delete Existing Client").grid(column=2, row=1, padx=4, pady=4)
            self.refreshList = ttk.Button(frm1a, text="Refresh List", command=lambda: self.displayList(c_type)).grid(column=3, row=1, padx=4, pady=4)
            self.clientAccount = ttk.Button(frm1a, text="View Selected Account",
                                            command=lambda: showClientData(self, clientData)).grid(column=4, row=1, padx=4, pady=4)

            # #----------------Tree View Frame-------------------
            treeViewFrame = ttk.Labelframe(self.tab1, width=200, height=400)
            treeViewFrame.pack(fill='x')
            ttk.Label(treeViewFrame, text="List of Clients").pack()
            self.Clientview = ttk.Treeview(treeViewFrame, columns=(1, 2, 3, 4, 5, 6, 7), show='headings', height="15",
                                           selectmode='browse')
            self.Clientview.pack(side='left', fill='both', expand=True)
            self.Clientview.bind("<ButtonRelease-1>", self._get_selected_row)

            self.scrlBar1 = ttk.Scrollbar(treeViewFrame, orient="vertical", command=self.Clientview.yview)
            self.Clientview.configure(yscrollcommand= self.scrlBar1.set)
            self.scrlBar1.pack(side='right', fill='y')

            self.Clientview.column(1, width=40, minwidth=20, stretch=tk.NO, anchor=tk.W);
            self.Clientview.heading(1, text='C_ID')
            self.Clientview.column(2, width=150, minwidth=50, anchor=tk.W);
            self.Clientview.heading(2, text='Name')
            self.Clientview.column(3, width=75, minwidth=50, anchor=tk.W);
            self.Clientview.heading(3, text='Address')
            self.Clientview.column(4, width=150, minwidth=50, anchor=tk.W);
            self.Clientview.heading(4, text='Email')
            self.Clientview.column(5, width=100, minwidth=50, anchor=tk.W);
            self.Clientview.heading(5, text='Phone')
            self.Clientview.column(6, width=100, minwidth=50, anchor=tk.W);
            self.Clientview.heading(6, text='Mob')
            self.Clientview.column(7, width=100, minwidth=50, anchor=tk.W);
            self.Clientview.heading(7, text='Balance')

            # ---------- Fill Treeview -------------------------------
            self.displayList(c_type)

            # ---------------------Remainder tab----------------------------------------------------------------------
            remainderTab = ttk.Labelframe(self.tab2, text="Reminder List", width=650, height=600)
            remainderTab.pack(fill='x')

            lbfr1 = ttk.Label(remainderTab)
            lbfr1.grid(column=0, row=1, padx=4, pady=4, sticky='W')
            self.refreshList = ttk.Button(lbfr1, text="Refresh List").grid(column=1, row=1, padx=4, pady=4)
            self.removeFrmList = ttk.Button(lbfr1, text="Remove from List").grid(column=3, row=1, padx=4, pady=4)

            # #----------------Tree View Frame-------------------
            treeViewFrame = ttk.Labelframe(self.tab2, width=200, height=400)
            treeViewFrame.pack(fill='x')
            ttk.Label(treeViewFrame, text="List of Clients").pack()
            self.nameList2 = ttk.Treeview(treeViewFrame, columns=(1, 2, 3, 4, 5, 6), show='headings', height="15")
            self.nameList2.pack(side='left', fill='both', expand=True)
            self.scrlBar2 = ttk.Scrollbar(treeViewFrame, orient="vertical", command=self.nameList2.yview)
            self.nameList2.configure(yscrollcommand=self.scrlBar2.set)
            self.scrlBar2.pack(side='right', fill='y')

            self.nameList2.column(1, width=150, minwidth=20, stretch=tk.NO, anchor=tk.W);
            self.nameList2.heading(1, text='Name')
            self.nameList2.column(2, width=75, minwidth=50, anchor=tk.W);
            self.nameList2.heading(2, text='Address')
            self.nameList2.column(3, width=100, minwidth=50, anchor=tk.W);
            self.nameList2.heading(3, text='Mob')
            self.nameList2.column(4, width=100, minwidth=50, anchor=tk.W);
            self.nameList2.heading(4, text='Date of Last Credit')
            self.nameList2.column(5, width=100, minwidth=50, anchor=tk.W);
            self.nameList2.heading(5, text='Days since last Txn')
            self.nameList2.column(6, width=100, minwidth=50, anchor=tk.W);
            self.nameList2.heading(6, text='Net Balance')

    def displayList(self, c_type):
        for row in self.Clientview.get_children():
            self.Clientview.delete(row)
        listAll = Database.showClientList(self, c_type)
        for row in listAll:
            if row[-1] == c_type:
                self.Clientview.insert("", 'end',values=(row[0], f"{row[1]} {row[2]}", row[4], row[3], row[5], row[6]))




