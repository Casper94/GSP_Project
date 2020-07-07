# from tkinter import *
# from front import Window2
#
# def displayClients(self):
#     list1 = Listbox(Window2, height=6, width=35)
#     list1.grid(row=2, column=0, rowspan=6, columnspan=2)




# Multi-frame tkinter application v2.3
import tkinter as tk

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is the start page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Open page one",
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="Open page two",
                  command=lambda: master.switch_frame(PageTwo)).pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page one").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="This is page two").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()


    # ---------------- scroll text----------------
    ttk.Label(frm2, text="Account \tTransaction\t Amount \tBalance \t\t").grid(column=0, row=2, padx=4, pady=4,
                                                                               sticky='W')
    scrolW1 = 80;
    scrolH1 = 35
    self.scrolList2 = scrolledtext.ScrolledText(frm2, width=scrolW1, height=scrolH1, wrap=tk.WORD)
    self.scrolList2.grid(column=0, row=3, padx=4, pady=4, sticky='WE', columnspan=3)
    self.do_showLedger(0)


def do_showLedger(self, account):
    self.scrolList2.delete(1.0, tk.END)
    account = int(account)

    listAll = AccountDB.getLedgerAccount(self, account)
    for row in listAll:
        # self.do_formatedList(row)
        self.scrolList2.insert(tk.END, row[0])
        self.scrolList2.insert(tk.END, '\t    ')
        mTransact = str(row[1])
        transactLength = len(mTransact) + (10 - len(mTransact))
        mTransact = mTransact.ljust(transactLength)
        self.scrolList2.insert(tk.END, mTransact)
        self.scrolList2.insert(tk.END, '\t  ')
        mAmount = str(row[2])
        amountLength = len(mAmount) + (8 - len(mAmount))
        mAmount = mAmount.ljust(amountLength)
        self.scrolList2.insert(tk.END, mAmount)
        self.scrolList2.insert(tk.END, '\t')
        mBalance = str(round(row[3], 2))
        balanceLength = len(mBalance) + (8 - len(mBalance))
        mBalance = mBalance.rjust(balanceLength)
        self.scrolList2.insert(tk.END, mBalance)
        self.scrolList2.insert(tk.END, '\n')