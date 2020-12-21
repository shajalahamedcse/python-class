import mysql.connector 
from flask import Flask,request
cnx = mysql.connector.connect(user='root', password='root',
                              host='127.0.0.1',port='3307',
                              database='python_class')

cursor = cnx.cursor()

app = Flask(__name__)

@app.route('/api/v1/register',methods=['POST'])
def register():
    data = request.get_json()
    print(data)
    
    sql = "INSERT INTO users(email,password) VALUES (%s,%s)"
    li = [val for key,val in data.items()]
    val = tuple(li)
    try:
        cursor.execute(sql,val)
        cnx.commit()
        return {"msg": "User registered"},200
    except:
        return {"msg": "there is a duplicate"},409

@app.route('/api/v1/alive',methods=['GET'])
def alive():
    return {"msg": "ok"},200


if __name__ == "__main__":
    app.run(host="0.0.0.0",port="8080")
    