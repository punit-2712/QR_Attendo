'''import qrcode
img = qrcode.make(input('PLEASE ENTER GR NO. '))
img.save("2045.png")#To save QR after generation

img.show('saved.png') #To show QR after generation'''

from tkinter import *
import tkinter as tk
from tkinter import ttk
import qrcode
def Generate():
    img = qrcode.make(input('PLEASE ENTER GR NO. '))
    img.save("save.png")  # To save QR after generation


root=Tk()
root.title("Attendence System")
root.resizable(width=FALSE, height=FALSE)
root.geometry('800x500')
tk.Label(root, text="Gr Number").grid(row=0)
e1 = tk.Entry(root)
e1.grid(row=0, column=1)
tk.Button(root,
          text='Done',
          command=Generate).grid(row=3,
                                    column=0,
                                    sticky=tk.W,
                                    pady=4)
root.mainloop()

