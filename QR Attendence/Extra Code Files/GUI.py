import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super(App, self).__init__()

        self.title("Tkinter Tab Widgets")
        self.minsize(600, 400)
        self.wm_iconbitmap("icon.ico")

        tabControl = ttk.Notebook(self)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text="Tab 1")

        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text="Tab 2")

        tabControl.pack(expan=1, fill="both")


app = App()
app.mainloop()