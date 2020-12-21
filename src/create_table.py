

import mysql.connector 

cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',port='3307',
                              database='python_class')

cursor = cnx.cursor()

cursor.execute("CREATE TABLE  users (user_id int NOT NULL AUTO_INCREMENT,email VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL,PRIMARY KEY (user_id),UNIQUE (email))")
cursor.close()