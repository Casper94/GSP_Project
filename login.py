import tkinter as tk
from tkinter import *
import tkinter.messagebox
# from back import Database5
from tkinter import ttk
import random, time, datetime
import subprocess
from starter import mainApp
from Start2 import gspApp



class loginWindow:
    def loginSystem(self):
        self.master.destroy()
        self.app = gspApp()

        # u = (self.Username.get())
        # p = (self.Password.get())
        #
        # if (u==str('admin') and p==str('admin')):
        #     self.app = mainApp()
        #     self.master.destroy()
        #
        #
        #
        # else:
        #     x = tkinter.messagebox.askyesno("Login Systems", "Invalid login details. Do you want to continue? ")
        #     if x <= 0:
        #         self.master.destroy()
        #     self.Username.set("")
        #     self.Password.set("")
        #     self.txtUsername.focus()

    def reset(self):
        self.Username.set("")
        self.Password.set("")
        self.txtUsername.focus()

    def iExit(self):
        self.iExit = tkinter.messagebox.askyesno("Login Systems", "confirm if you want to exit")
        if self.iExit > 0:
            self.master.destroy()
        else:
            pass

    def __init__(self, master):
        self.master = master
        self.master.title("GSP Account Management System ver: Alfa1.0")
        self.master.geometry('1000x600+0+0')
        # self.master.config(bg="#4D4D4D")
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = ttk.Label(self.frame, text = ' Login ',
                              font=('arial', 24, 'bold'))
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=40)

    # ================================= Frames ============================================
        self.LoginFrame = ttk.Frame(self.frame, width=800, height=600, relief='solid')
        self.LoginFrame.grid(row=1, column=0)

    # ================================    Label and Entry    ===============================

        self.FieldFrame = ttk.Frame(self.LoginFrame, width=500, height=400)
        self.FieldFrame.grid(row=0, column=0, pady=10, padx=10 )

        self.lblUsername = Label(self.FieldFrame, text='Username', font=('arial', 16, 'bold'), bd=22)
        self.lblUsername.grid(row=0, column=0)
        self.txtUsername = Entry(self.FieldFrame, font=('arial', 16, 'bold'),textvariable=self.Username)
        self.txtUsername.grid(row=0, column=1, padx=10)

        self.lblPassword = Label(self.FieldFrame, text='Password', font=('arial', 16, 'bold'), bd=22)
        self.lblPassword.grid(row=1, column=0)
        self.txtPassword = Entry(self.FieldFrame, font=('arial', 16, 'bold'), show="*", textvariable=self.Password)
        self.txtPassword.grid(row=1, column=1, columnspan=2, pady=30)

    # =====================================    Buttons    ====================================
        self.buttonframe = ttk.Frame(self.LoginFrame, width=500, height=50)
        self.buttonframe.grid(row=2, column=0, pady=10, padx=10)
        
        self.btnLogin = Button(self.buttonframe, text = 'Login', width=10, font=('arial', 16, 'bold'),
                               command=self.loginSystem)
        self.btnLogin.grid(row=0, column=0, pady=10, padx=10)

        self.btnReset = Button(self.buttonframe, text = 'Clear', width=10, font=('arial', 16, 'bold'),
                               command=self.reset)
        self.btnReset.grid(row=0, column=1, pady=10, padx=10)

        self.btnExit = Button(self.buttonframe, text = 'Exit', width=10, font=('arial', 16, 'bold'),
                              command=self.iExit)
        self.btnExit.grid(row=0, column=2, pady=10, padx=10)

    # def new_window(self):
    #     self.newWindow = Toplevel(self.master)
    #     self.app = Window2

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


root = tk.Tk()
app = loginWindow(root)
root.mainloop()
