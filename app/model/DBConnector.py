import mysql.connector



conn = mysql.connector.connect(host='database-2.ccmdqmbvy12j.us-east-1.rds.amazonaws.com'
                                   ,user='admin',
                                   password='serverless',
                                   db='serverless')
cursor = conn.cursor()

def SQLenterDetails(firstname,lastname,email,password):
    insertUser= "INSERT into userData(firstname,lastname,email,password) values(%s,%s,%s,%s)"
    cursor.execute(insertUser,(firstname,lastname,email,password))
    conn.commit()

def CheckLoginCredentials(email,password):

    findUser="Select password from userData where email=%s"
    cursor.execute(findUser,(email,))
    results=cursor.fetchone()
    if results[0]==password:
        return True
    else:
        return False


