start = Entryroll.get()
    mydb = pymysql.connect(host="localhost", user="root", passwd="punit", db="Project")
    mycursor = mydb.cursor()  # Connecting the database
    '''sql = "SELECT Gr_no, name, std, Roll_no, DOB, Address, Bloodgr, MobileNo from Student_details where Gr_no='914'"
    #mycursor.execute(sql)
    var =mycursor.execute(sql)
    var.fetchall()
    print(var.fetchall()'''
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

    for index, dat in enumerate(myresult):
        Label(tab2, text=dat[0]).grid(row=index + 1, column=0)
        Label(tab2, text=dat[1]).grid(row=index + 1, column=1)
        Label(tab2, text=dat[2]).grid(row=index + 1, column=2)
        Label(tab2, text=dat[3]).grid(row=index + 1, column=3)
        Label(tab2, text=dat[4]).grid(row=index + 1, column=4)
        Label(tab2, text=dat[5]).grid(row=index + 1, column=5)
        Label(tab2, text=dat[6]).grid(row=index + 1, column=6)
        Label(tab2, text=dat[7]).grid(row=index + 1, column=7)
        Edit = Button(tab2, text="EDIT", bg='green', fg='white', command=ED)
        Edit.place(x=20, y=60)
    Label1.grid_forget()
