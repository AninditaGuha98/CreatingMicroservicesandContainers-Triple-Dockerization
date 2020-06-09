import mysql.connector
import datetime

from app.model import passencryptdecrypt

conn = mysql.connector.connect(host='34.86.198.25'
                                   ,user='root',
                                   password='serverless',
                                   db='serverless')
cursor = conn.cursor(buffered=True)

def SQLenterDetails(firstname,lastname,email,password):
    encryptedpass=passencryptdecrypt.passwordEncrypt(password)
    try:
        insertUser= "INSERT into userData(firstname,lastname,email,password) values(%s,%s,%s,%s)"
        cursor.execute(insertUser,(firstname,lastname,email,encryptedpass))
        conn.commit()
        return True
    except Exception as e:
        print(e)
        return False



def CheckLoginCredentials(email,password):
    try:
        findUser="Select firstname,lastname,password from userData where email=%s"
        cursor.execute(findUser,(email,))
        results=cursor.fetchone()
        decryptpass=passencryptdecrypt.passwordDecrypt(results[2])
        if decryptpass==password:
            username=results[0]+' '+results[1]
        return username
    except:
        return "no"

def InsertintoUserState(email):
    userlist=[]
    status = "online"

    findUser = "Select userId from userData where email=%s"
    cursor.execute(findUser, (email,))
    userid = cursor.fetchone()

    checkonline="select * from userState where userId=%s"   #Check if user is already online
    cursor.execute(checkonline,(userid[0],))
    if cursor.rowcount==0:
        insertOnlineTime="insert into userState (userId,status,onlineTime) values(%s,%s,%s)"
        cursor.execute(insertOnlineTime, (userid[0],status, datetime.datetime.utcnow()))


    # Find list of online users
    findonlineusers="select userData.firstname, userData.lastname from userData natural join userState where userId in(select userId from userState where status=%s and userId!=%s)"
    cursor.execute(findonlineusers,(status,userid[0]))
    users=cursor.fetchall()
    for i in range(len(users)):
        userlist.append(users[i][0]+" "+ users[i][1])
    conn.commit()
    return userlist

def logoutUser(username):
    try:
        status="offline"
        split_data=username.split()
        logoutid="select userId from userData where firstname=%s and lastname=%s"
        cursor.execute(logoutid,(split_data[1],split_data[2]))
        conn.commit()
        userid=cursor.fetchone()
        logQuery="update userState set status=%s, offlineTime=%s where userId=%s"
        cursor.execute(logQuery, (status, datetime.datetime.utcnow(), userid[0]))
        conn.commit()
        return True
    except:
        return False







