import mysql.connector as mysql

mycon = mysql.connect(host="localhost", user="root", password="root",
                      database="Quiz", auth_plugin='mysql_native_password')
if mycon.is_connected():
    print("Database connected successfully")
else:
    print("Error in connecting")

cur = mycon.cursor()

cur.execute("Select * from Ques")
questions = cur.fetchall()

cur.execute("Select * from options")
choices = cur.fetchall()


# To save scores if needed
def save(username, score):
    s = 'insert into quizscores values("' + username + '",' + str(score) + ");"
    cur.execute(s)
    mycon.commit()
    mycon.close()
