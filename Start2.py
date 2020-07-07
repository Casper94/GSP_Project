import tkinter as tk
from tkinter import ttk

from CommonWidgets import Basic
from Functions import insertClientForm, showClientData
from Database import Database



class gspApp(tk.Tk):
    def __init__(self, *args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "GSP Management Logs")
        tk.Tk.geometry(self, "800x600+200+100")
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)

        container.rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for f in (StartPage, TradingPage, ManuPage):
            frame = f(container, self)
            self.frames[f] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        frame.grid(row=0, column=0, sticky='nsew')
        self.show_frame(StartPage)


    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Select Company ", font=('arial', 24, 'bold')).pack(side="top", fill="x", padx=10, pady=10)
        ttk.Button(self, text="Trading Profile",
                  command=lambda: controller.show_frame(TradingPage)).pack(pady=10)
        ttk.Button(self, text="Manufacturing Profile",
                  command=lambda: controller.show_frame(ManuPage)).pack(pady=10)


class TradingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        c = 'Trading'
        obj = Basic(parent, controller)
        ttk.Label(self, text="Trading Company Profile", font=('arial', 24, 'bold')).pack(side="top", fill="x", pady=10)

        ttk.Button(self, text="Change Company Type",
                  command=lambda: controller.show_frame(StartPage)).pack()
        obj.createWidgets(self, c)


class ManuPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        c = 'Manufacture'
        obj2 = Basic(parent, controller)
        ttk.Label(self, text="Manufacture Company Profile", font=('arial', 24, 'bold')).pack(side="top", fill="x", pady=10 )

        ttk.Button(self, text="Change Company Type",
                    command=lambda: controller.show_frame(StartPage)).pack()
        obj2.createWidgets(self, c)




if __name__ == "__main__":
    app = gspApp()
    app.mainloop()
