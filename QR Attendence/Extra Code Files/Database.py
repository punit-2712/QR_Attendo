import pymysql

conn= pymysql.connect(host="localhost",  user="root", passwd="punit" ,db="Project")

mycursor=conn.cursor()


"""mycursor.execute("CREATE TABLE Student_Details (Sr_no int, Gr_no int ,name VARCHAR(255), Std int, Roll_no int)")

sql = "INSERT INTO Student_Details (Sr_no, Gr_no, name) VALUES (%s, %s)"
val = ("5","John", "Highway 21")"""
mycursor.execute("DELETE FROM student_details WHERE Gr_no")


conn.commit()