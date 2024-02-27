import qrcode
from tkinter import *
from tkinter import messagebox





def QRCode():
    website = webEntry.get()
    filename = website + '.jpg'
    img = qrcode.make(website)
    img.save(filename)
    root.photo = PhotoImage(file=filename)
    QR.config(image=root.photo, fg='green', compound=TOP, width=300, height=300)
    messagebox.showinfo('Saved', 'QR code saved as " ' + website + ' " successfully!\n\tin current location')


()
# ===============  GUI Design ================================
root = Tk()
root.title('QR Code Generator')
root.config(bg='plum1')
root.geometry('520x550')
root.resizable(0, 0)
try:
    root.wm_iconbitmap('cid.ico')
except:
    pass

website = Label(tab2, text="Enter Website/Mobile Name:", font=('impact', 10))
website.place(x=10, y=72)
webEntry = Entry(tab2, fg='blue', bd=3, width=40)
webEntry.place(x=170, y=70)
getQRCode = Button(tab2, text='get QR Code', bg='green', fg='white', activebackground='blue',
                   width=30, activeforeground='yellow', command=QRCode)
getQRCode.place(x=180, y=100)
'''
showImage= Button(root,text='Show QR Code in Photos App',fg='green',activebackground='blue',
                  width=30,command=showQR)
showImage.place(x=180,y=140)
'''

QR = Label(root, image='', bg='plum1')
QR.place(x=100, y=170)

copyri8 = Label(root, text='App Developed By: CID An Education Hub [2019]',
                bg='plum1', fg='red3', font=('arial', 10, 'bold'))
copyri8.pack(side=BOTTOM)
root.mainloop()
