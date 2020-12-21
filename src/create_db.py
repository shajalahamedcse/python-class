import mysql.connector 

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',port='3307',
                              database='evaly')

cursor = cnx.cursor()

cursor.execute('CREATE DATABASE python_class')

cnx.close()