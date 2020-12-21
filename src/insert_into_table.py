

import mysql.connector 

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',port='3307',
                              database='python_class')

cursor = cnx.cursor()
sql = "INSERT INTO users(email,password) VALUES (%s,%s)"
val = ("shaj@gmail.com","hello")
cursor.execute(sql,val)
cnx.commit()
# cnx.rollback()
cursor.close()
