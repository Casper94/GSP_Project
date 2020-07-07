import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import *

from Functions import insertClientForm, showClientData
from Database import Database


def get_selected_row(event):
    try:
        global selected_tuple
        print('argument in get selected row function', event)
        items = event.Clientview.selection()
        print('rows selected - ', items)
        clientData = []
        for i in items:
            clientData.append(event.Clientview.item(i)['values'])

        # for item in items:
        #     item_text = event.tree.item(item,"text")
        #     print(item_text)

        # selected_tuple = event.Clientview.get(index)
        # print(selected_tuple)

    except IndexError:
        pass


class mainApp(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self._center_window()
        self.switch_frame(AfterLoginPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def _center_window(self):
        self.update()
        width = 800 # self.winfo_width()
        height = 600 # self.winfo_height()

        x_offset = (self.winfo_screenwidth() - width) // 2
        y_offset = (self.winfo_screenheight()- height) // 2
        self.geometry(
            f'{width}x{height}+{x_offset}+{y_offset}'
        )

    def get_selected_row(event):
        try:
            global selected_tuple
            items = event.Clientview.selection()
            print('rows selected - ', items)
            # for item in items:
            #     item_text = event.tree.item(item,"text")
            #     print(item_text)

            # selected_tuple = event.Clientview.get(index)
            # print(selected_tuple)

        except IndexError:
            pass

    def createWidgets(self, c_type):
        # Tab Controls created here --------------------------------------
        self.tabControl = ttk.Notebook(self)  # Create Tab Controls

        self.tab1 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab1, text=' Clients List ')

        self.tab2 = ttk.Frame(self.tabControl)
        self.tabControl.add(self.tab2, text=' Reminder ')

        self.tabControl.pack()  # Pack to make visible

        #CLient's List TAB
        frm1 = ttk.Labelframe(self.tab1, width=650, height=300)
        frm1.pack(fill='x')
        ttk.Label(frm1).grid(column=0, row=0, padx=4, pady=4, sticky='W')
        #------------- Buttons Frame----------------------
        frm1a = ttk.Labelframe(frm1,text="Perform Actions", width=550, height=500)
        frm1a.grid(column=0, row=1, padx=4, pady=4)

        self.newClient = ttk.Button(frm1a, text="Add New Client", command=lambda c=c_type: insertClientForm(self, c)).grid(column=1,row=1,padx=4, pady=4)
        self.deleteClient = ttk.Button(frm1a, text="Delete Existing Client" ).grid(column=2,row=1,padx=4, pady=4)
        self.refreshList = ttk.Button(frm1a, text="Refresh List"  ).grid(column=3,row=1,padx=4, pady=4)
        self.clientAccount = ttk.Button(frm1a, text="View Selected Account", command=lambda : showClientData(self)).grid(column=4,row=1,padx=4, pady=4)

        # #----------------Tree View Frame-------------------
        treeViewFrame = ttk.Labelframe(self.tab1, width=200, height=400)
        treeViewFrame.pack(fill='x')
        ttk.Label(treeViewFrame,text="List of Clients").pack()
        self.Clientview = ttk.Treeview(treeViewFrame, columns=(1,2,3,4,5,6,7), show='headings', height="15",selectmode='browse')
        self.Clientview.pack(side='left',fill='both', expand=True)
        self.scrlBar1 = ttk.Scrollbar(treeViewFrame, orient="vertical", command=self.Clientview.yview)
        self.Clientview.configure(yscrollcommand=self.scrlBar1.set)
        self.scrlBar1.pack(side='right', fill='y')

        self.Clientview.column(1,width=30,minwidth=20,stretch=tk.NO, anchor=tk.W);self.Clientview.heading(1, text='S/n')
        self.Clientview.column(2,width=150,minwidth=50, anchor=tk.W);self.Clientview.heading(2, text='Name')
        self.Clientview.column(3,width=75,minwidth=50, anchor=tk.W);self.Clientview.heading(3, text='Address')
        self.Clientview.column(4,width=150,minwidth=50, anchor=tk.W);self.Clientview.heading(4, text='Email')
        self.Clientview.column(5,width=100,minwidth=50, anchor=tk.W);self.Clientview.heading(5, text='Phone')
        self.Clientview.column(6,width=100,minwidth=50, anchor=tk.W);self.Clientview.heading(6, text='Mob')
        self.Clientview.column(7,width=100,minwidth=50, anchor=tk.W);self.Clientview.heading(7, text='Balance')
        listAll = Database.showClientList(self, c_type)
        s_n = 1
        for row in listAll:
            if row[-1] == c_type:
                self.Clientview.insert("", 'end', values=(s_n, f"{row[1]} {row[2]}", row[4], row[3], row[5], row[6]))
            s_n += 1
        self.Clientview.bind('<<TreeviewSelect>>', get_selected_row)

    #------------End of Client List TAB -------------------------------


        #---------------------Remainder tab------------------
        remainderTab = ttk.Labelframe(self.tab2, text="Reminder List", width=650, height=600)
        remainderTab.pack(fill='x')

        lbfr1 = ttk.Label(remainderTab)
        lbfr1.grid(column=0,row=1,padx=4,pady=4,sticky='W')
        self.refreshList = ttk.Button(lbfr1, text="Refresh List").grid(column=1,row=1,padx=4, pady=4)
        self.removeFrmList = ttk.Button(lbfr1, text="Remove from List").grid(column=3,row=1,padx=4, pady=4)

        # #----------------Tree View Frame-------------------
        treeViewFrame = ttk.Labelframe(self.tab2, width=200, height=400)
        treeViewFrame.pack(fill='x')
        ttk.Label(treeViewFrame, text="List of Clients").pack()
        self.nameList2 = ttk.Treeview(treeViewFrame, columns=(1, 2, 3, 4, 5, 6), show='headings', height="15")
        self.nameList2.pack(side='left', fill='both', expand=True)
        self.scrlBar2 = ttk.Scrollbar(treeViewFrame, orient="vertical", command=self.nameList2.yview)
        self.nameList2.configure(yscrollcommand=self.scrlBar2.set)
        self.scrlBar2.pack(side='right', fill='y')

        self.nameList2.column(1, width=150, minwidth=20, stretch=tk.NO, anchor=tk.W);    self.nameList2.heading(1, text='Name')
        self.nameList2.column(2, width=75, minwidth=50, anchor=tk.W);  self.nameList2.heading(2, text='Address')
        self.nameList2.column(3, width=100, minwidth=50, anchor=tk.W);  self.nameList2.heading(3, text='Mob')
        self.nameList2.column(4, width=100, minwidth=50, anchor=tk.W);  self.nameList2.heading(4, text='Date of Last Credit')
        self.nameList2.column(5, width=100, minwidth=50, anchor=tk.W);  self.nameList2.heading(5, text='Days since last Txn')
        self.nameList2.column(6, width=100, minwidth=50, anchor=tk.W);  self.nameList2.heading(6, text='Net Balance')




class AfterLoginPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master.title("GSP Management Logs")
        tk.Label(self, text="Select Company ",font=('arial', 24, 'bold')).pack(side="top", fill="x", pady=15)
        tk.Button(self, text="Trading Profile",
                  command=lambda: master.switch_frame(TradingPage)).pack(pady=10)
        tk.Button(self, text="Manufacturing Profile",
                  command=lambda: master.switch_frame(ManuPage)).pack(pady=10)

class TradingPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        c = 'Trading'
        tk.Label(self, text="Trading Company Profile", font=('arial', 24, 'bold')).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Change Company Type",
                  command=lambda: master.switch_frame(AfterLoginPage)).pack()
        tk.Label(self).pack(side="top", fill="x", pady=10)
        mainApp.createWidgets(self, c)


class ManuPage(tk.Frame):
    def __init__(self, master):
        c = 'Manufacture'
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Manufacture Company Profile",font=('arial', 24, 'bold')).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Change Company Type",
                  command=lambda: master.switch_frame(AfterLoginPage)).pack()

        mainApp.createWidgets(self,c)



if __name__ == "__main__":
    app = mainApp()
    app.mainloop()