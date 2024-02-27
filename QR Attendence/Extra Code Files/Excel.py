import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import datetime
from xlwt import Workbook

def attendence ():
    import Excel

()

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN

show=0
def myFunc():
    import pymysql

    conn = pymysql.connect(host="localhost", user="root", passwd="punit", db="Project")


    mycursor = conn.cursor()
    mycursor.execute("select Gr_no from Student_details")

    myresults= mycursor.fetchall()

    counter = 0
    grno = str(grn)
    gr_No=""
    Qr_gr=""

    for Gr_no in myresults:
        Gr_no = str(Gr_no)
        for i in Gr_no:
            if(i not in ['(',',',')']):
                gr_No+=i
        for j in grno:
            if (j not in ['b', "'", "'"]):

                Qr_gr+=j

        if str(gr_No) == str(Qr_gr):
            print("done")
            return Qr_gr

        else:
            counter += 1

while True:
    _,   frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        print("Data", obj.data)
        grn = obj.data

        break

        #cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                   # (255, 0, 0), 3)

    cv2.imshow("Frame", frame)




    key = cv2.waitKey(1)
    if key == 27:
        myFunc()
        break
def make(name):
    Qr_gr=myFunc()
    subject = "Sheet1"
    names = set(name)
    print(names)
    xls = ExcelFile('Student_details.xlsx')
    df = read_excel(xls, "Sheet1")

    today = dt.datetime.now()
    today = today.strftime('%d/%m/%y')

    student_status = ['AB' for i in range(len(df))]
    # print(df["name"])
    df[today] = student_status  # Marking NIL initially to all student

    excelbook = load_workbook('Student_details.xlsx')
    sheet = excelbook.get_sheet_by_name("Sheet1")
    max_col_no = sheet.max_column
    max_col_letter = get_column_letter(sheet.max_column + 1)
    row_1 = []

    for i in range(max_col_no):
        row_1.append(sheet.cell(row=1, column=i + 1).value)


    # mark attendance
    excelbook.save('attendance1.xlsx')
make(name=[Qr_gr])