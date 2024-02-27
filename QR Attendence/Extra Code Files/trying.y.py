import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar


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
    flag=1
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
            flag=0
            print("done")

            break
        else:
            counter += 1
        gr_No=""
        Qr_gr=""
    if flag==1:
        print(type(Gr_no), "Gr_no")
        print(type(grno), "grn")




while True:
    _, frame = cap.read()

    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        print("Data", obj.data)
        grn = obj.data

        break

        cv2.putText(frame, str(obj.data), (50, 50), font, 2,
                    (255, 0, 0), 3)

    cv2.imshow("Frame", frame)



    key = cv2.waitKey(1)
    if key == 27:
        myFunc()
        break
