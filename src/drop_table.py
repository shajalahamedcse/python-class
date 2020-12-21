import mysql.connector 

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',port='3307',
                              database='python_class')

cursor = cnx.cursor()

cursor.execute('DROP TABLE users')

cnx.close()