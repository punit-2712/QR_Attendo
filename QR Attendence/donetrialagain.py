from PIL import Image, ImageDraw, ImageFont
from PIL import Image
image = Image.new('RGB', (1000, 900), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=18)
font1 = ImageFont.truetype('arial.ttf', size=15)
import qrcode
import cv2
from tkinter import *
from tkinter import PhotoImage
from tkinter import ttk
from tkinter import messagebox
from pynput.keyboard import Key, Controller
keyboard = Controller()
import pandas as pd
import pymysql
import os
import sqlalchemy as ac
from pynput.keyboard import Key, Controller
keyboard = Controller()

def modify():
    start = Entryroll_start.get()
    mydb = pymysql.connect(host="localhost", user="root", passwd="punit", db="Project")
    mycursor = mydb.cursor()  # Connecting the database
    sql1 = "SELECT * FROM Student_details WHERE Gr_no=%s"
    val2 = (start)
    mycursor.execute(sql1, val2)
    myresult = mycursor.fetchall()
    Label1 = Label(tab2, text="Gr Number", width=10)
    Label1.grid(row=0, column=0)
    Label2 = Label(tab2, text="FULL NAME", width=10)
    Label2.grid(row=0, column=1)
    Label3 = Label(tab2, text="STD", width=10)
    Label3.grid(row=0, column=2)
    Label4 = Label(tab2, text="ROLL NO.", width=10)
    Label4.grid(row=0, column=3)
    Label5 = Label(tab2, text="DOB", width=10)
    Label5.grid(row=0, column=4)
    Label6 = Label(tab2, text="Address", width=30)
    Label6.grid(row=0, column=5)
    Label7 = Label(tab2, text="Blood gr.", width=10)
    Label7.grid(row=0, column=6)
    Label8 = Label(tab2, text="Mobile No.", width=10)
    Label8.grid(row=0, column=7)
    for index, myresult in enumerate(myresult):
        Label(tab2, text=myresult[0]).grid(row=index + 1, column=0)
        Label(tab2, text=myresult[1]).grid(row=index + 1, column=1)
        Label(tab2, text=myresult[2]).grid(row=index + 1, column=2)
        Label(tab2, text=myresult[3]).grid(row=index + 1, column=3)
        Label(tab2, text=myresult[4]).grid(row=index + 1, column=4)
        Label(tab2, text=myresult[5]).grid(row=index + 1, column=5)
        Label(tab2, text=myresult[6]).grid(row=index + 1, column=6)
        Label(tab2, text=myresult[7]).grid(row=index + 1, column=7)
        Edit = Button(tab2, text="EDIT", bg='green', fg='white', command=ED)
        Edit.place(x=20, y=60)
()

def ED():
    gr = Label(tab2, text="Gr Number:", font=('Arial', 12, 'bold'), fg='black')
    gr.place(x=150, y=190)
    global Entry10,Entry11, Entry12, Entry13, Entry14, Entry15, Entry16, Entry17
    Entry10 = Entry(tab2, fg='blue', bd=3, width=40)
    Entry10.place(x=270, y=190)

    b = Label(tab2, text="Name:", font=('Arial', 12, 'bold'), fg='black')
    b.place(x=150, y=220)
    Entry11 = Entry(tab2, fg='blue', bd=3, width=40)
    Entry11.place(x=270, y=220)

    c = Label(tab2, text="Std:", font=('Arial', 12, 'bold'), fg='black')
    c.place(x=150, y=250)
    Entry12 = Entry(tab2, fg='blue', bd=3, width=40)
    Entry12.place(x=270, y=250)

    d = Label(tab2, text="Roll Number:", font=('Arial', 12, 'bold'), fg='black')
    d.place(x=150, y=280)
    Entry13 = Entry(tab2, fg='blue', bd=3, width=40)
    Entry13.place(x=270, y=280)

    e = Label(tab2, text="DOB:", font=('Arial', 12, 'bold'), fg='black')
    e.place(x=150, y=310)
    Entry14 = Entry(tab2, fg='blue', bd=3, width=40)
    Entry14.place(x=270, y=310)

    f = Label(tab2, text="Blood Group:", font=('Arial', 12, 'bold'), fg='black')
    f.place(x=150, y=340)
    Entry15 = Entry(tab2, fg='blue', bd=3, width=40)
    Entry15.place(x=270, y=340)

    PI = Label(tab2, text="Address:", font=('Arial', 12, 'bold'), fg='black')
    PI.place(x=150, y=370)
    Entry17 = Entry(tab2, fg='blue', bd=3, width=40)
    Entry17.place(x=270, y=370)

    h = Label(tab2, text="Mobile No:", font=('Arial', 12, 'bold'), fg='black')
    h.place(x=150, y=400)
    Entry16 = Entry(tab2, fg='blue', bd=3, width=40)
    Entry16.place(x=270, y=400)

    upd = Button(tab2, text="Update", bg='green', fg='white', command=Upt)
    upd.place(x=350, y=440)
()

def Upt():
    gro = Entry10.get()
    name1 = Entry11.get()  # Getting entries data from GUI
    std1 = Entry12.get()
    roll = Entry13.get()
    dob = Entry14.get()
    bloodgr = Entry15.get()
    add = Entry17.get()
    mobile = Entry16.get()
    start1 = Entryroll_start.get()

    mydb = pymysql.connect(host="localhost", user="root", passwd="punit", db="Project")
    mycursor = mydb.cursor()  # Connecting the database
    sql2 = "UPDATE Student_details SET Gr_no=%s , name=%s , std=%s , Roll_no=%s , DOB=%s , Address=%s , Bloodgr=%s, MobileNo=%s WHERE Gr_no=%s"
    val3 = (gro, name1, std1, roll, dob, add , bloodgr, mobile, start1)
    mycursor.execute(sql2, val3)
    mydb.commit()

    U=ac.create_engine('mysql+pymysql://root:punit@127.0.0.1:3306/project')
    full_deatils = pd.read_sql_table('student_details', U)
    full_deatils.to_excel("Students Details.xlsx", index=FALSE)
    student=pd.read_sql_table('student_details', U, columns=['Gr_no','name'])
    student.to_excel("attendance2.xlsx", index=FALSE)

    Entry10.delete(0, "end")
    Entry11.delete(0, "end")  # Reseting the entry after clicking button
    Entry12.delete(0, "end")
    Entry13.delete(0, "end")
    Entry14.delete(0, "end")
    Entry15.delete(0, "end")
    Entry16.delete(0, "end")
    Entry17.delete(0, "end")
()

def new():
    gro = Entry3.get()
    name = Entry4.get()  # Getting entries data from GUI
    std = Entry5.get()
    roll = Entry6.get()
    dob = Entry7.get()
    bloodgr = Entry8.get()
    add = Entry9.get()
    mobile = Entry10.get()
    mydb = pymysql.connect(host="localhost", user="root", passwd="punit", db="Project")
    mycursor = mydb.cursor()                                                                  # Connecting the database
    sql = "INSERT INTO Student_details (Gr_no, name, std, Roll_no, DOB, Address, Bloodgr, MobileNo) " \
          "VALUES (%s, %s,%s, %s, %s, %s,%s, %s )"
    val = (gro, name, std, roll, dob, add, bloodgr, mobile)
    mycursor.execute(sql, val)
    QR_code = Entry3.get()  # getting data from GUI
    filename = QR_code + '.jpg'
    img = qrcode.make(QR_code)  # .make makes Qr code
    img.save(filename)  # saving the Qr code
    root.photo = PhotoImage(file=filename)  # getting Qrcode Image
    QR.config(image=root.photo, width=300, height=300)
    messagebox.showinfo('Saved', 'QR code saved as " ' + QR_code + ' " successfully!\n\tin current location \n\t And all detials are added to database')
    mydb.commit()
    from PIL import Image, ImageDraw
    im = Image.open("ID.JPG")

    d = ImageDraw.Draw(im)
    location = (320, 125)
    text_color = (255, 255, 255)
    d.text(location, name, font=font, fill=text_color)

    location = (405, 173)
    text_color = (0, 0, 0)
    d.text(location, QR_code, font=font, fill=text_color)

    location = (270, 220)
    text_color = (0, 0, 0)
    d.text(location, "STD: " + std, font=font1, fill=text_color)

    location = (270, 250)
    text_color = (0, 0, 0)
    d.text(location, "DOB: " + dob, font=font1, fill=text_color)

    location = (270, 280)
    text_color = (0, 0, 0)
    d.text(location, "MOBILE: " + mobile, font=font1, fill=text_color)

    location = (270, 310)
    text_color = (0, 0, 0)
    d.text(location, "ADDRESS: " + "\n" + add, font=font1, fill=text_color)
    path = 'C:/Users/VK/PycharmProjects/QR Attendence/ID CARDS/'
    im.save('hello.png')
    til = Image.open(r"hello.png")
    im1 = Image.open(filename)  # 25x25
    images = im1.resize((160, 160))
    til.paste(images, (60, 180))
    til.save(name + ".png")


    Entry3.delete(0, "end")
    Entry4.delete(0, "end")  # Reseting the entry after clicking button
    Entry5.delete(0, "end")
    Entry6.delete(0, "end")
    Entry7.delete(0, "end")
    Entry8.delete(0, "end")
    Entry9.delete(0, "end")
    Entry10.delete(0, "end")

    U=ac.create_engine('mysql+pymysql://root:punit@127.0.0.1:3306/project') # sqlalchemy because sql_table only run with this connecttable
    full_deatils = pd.read_sql_table('student_details', U)
    full_deatils.to_excel("Students Details.xlsx", index=FALSE)
    student=pd.read_sql_table('student_details', U, columns=['Gr_no','name'])
    student.to_excel("attendance2.xlsx", index=FALSE)


()


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


def check():
    import trial

()


# GUI CODING
root = Tk()
root.title("Attendance System")
root.resizable(width=FALSE, height=FALSE)
root.geometry('1300x1200')

tab_parent = ttk.Notebook(root)
tab1 = Frame(tab_parent)
tab2 = Frame(tab_parent)
tab3 = Frame(tab_parent)
tab_parent.add(tab1, text='Home')
tab_parent.add(tab2, text='Modification')
tab_parent.add(tab3, text='New Entry')
tab_parent.pack(expand=1, fill='both')

title = Label(tab1, text="AIRPORT SCHOOL \n AHMEDABAD", font=('Old English Text MT', 36), fg='Brown')
title.place(x=350, y=50)
system = Label(tab1, text="QR Code Attendance system", font=('Arial', 11, 'bold', 'underline'), fg='black')
system.place(x=1000, y=600)
punch = Button(tab1, text="Punch Your ID-Card", bg='green',  font=('Arial', 11),fg='white', width=30, height=10, command=check)
punch.place(x=450, y=300)
title1 = Label(tab3, text="Please fill all the details for new entry.", font=('Arial', 20), fg='Brown')
title1.place(x=350, y=20)
QR_code = Label(tab2, text="Gr Number:", font=('Arial', 12, 'bold'))
QR_code.place(x=75, y=67)

a = Label(tab3, text="Gr Number:", font=('Arial', 12, 'bold'), fg='black')
a.place(x=120, y=66)
Entry3 = Entry(tab3, fg='blue', bd=3, width=40)
Entry3.place(x=250, y=70)

b = Label(tab3, text="Name:", font=('Arial', 12, 'bold'), fg='black')
b.place(x=120, y=100)
Entry4 = Entry(tab3, fg='blue', bd=3, width=40)
Entry4.place(x=250, y=100)

c = Label(tab3, text="Std:", font=('Arial', 12, 'bold'), fg='black')
c.place(x=120, y=130)
Entry5 = Entry(tab3, fg='blue', bd=3, width=40)
Entry5.place(x=250, y=130)

d = Label(tab3, text="Roll Number:", font=('Arial', 12, 'bold'), fg='black')
d.place(x=120, y=160)
Entry6 = Entry(tab3, fg='blue', bd=3, width=40)
Entry6.place(x=250, y=160)

e = Label(tab3, text="DOB:", font=('Arial', 12, 'bold'), fg='black')
e.place(x=120, y=190)
Entry7 = Entry(tab3, fg='blue', bd=3, width=40)
Entry7.place(x=250, y=190)

f = Label(tab3, text="Blood Group:", font=('Arial', 12, 'bold'), fg='black')
f.place(x=120, y=220)
Entry8 = Entry(tab3, fg='blue', bd=3, width=40)
Entry8.place(x=250, y=220)

g = Label(tab3, text="Address:", font=('Arial', 12, 'bold'), fg='black')
g.place(x=120, y=250)
Entry9 = Entry(tab3, fg='blue', bd=3, width=40)
Entry9.place(x=250, y=250)

h = Label(tab3, text="Mobile Number:", font=('Arial', 12, 'bold'), fg='black')
h.place(x=120, y=280)
Entry10 = Entry(tab3, fg='blue', bd=3, width=40)
Entry10.place(x=250, y=280)

QR = Label(tab3, image='')
QR.place(x=100, y=350)
lab = Label(tab1, image='')
lab.place(x=-60, y=-80)
root.photo2 = PhotoImage(file='logo.png')
lab.config(image=root.photo2, width=400, height=400)

btn = Button(tab3, text="Submit", bg='green', fg='white', command=new)
btn.place(x=330, y=310)
donegr = Label(tab2, text="Gr Number:", font=('Arial', 12, 'bold'), fg='black')
a.place(x=120, y=66)

Entryroll_start = Entry(tab2, fg='blue', bd=3, width=40)
Entryroll_start.place(x=250, y=70)
btn5 = Button(tab2, text="Submit", bg='green', fg='white', command=modify)
btn5.place(x=330, y=100)

root.mainloop()



