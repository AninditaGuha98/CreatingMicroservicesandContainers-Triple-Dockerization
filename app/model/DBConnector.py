import mysql.connector
import datetime



conn = mysql.connector.connect(host='database-2.ccmdqmbvy12j.us-east-1.rds.amazonaws.com'
                                   ,user='admin',
                                   password='serverless',
                                   db='serverless')
cursor = conn.cursor(buffered=True)

def SQLenterDetails(firstname,lastname,email,password):
    insertUser= "INSERT into userData(firstname,lastname,email,password) values(%s,%s,%s,%s)"
    cursor.execute(insertUser,(firstname,lastname,email,password))
    conn.commit()



def CheckLoginCredentials(email,password):
    findUser="Select firstname,lastname,password from userData where email=%s"
    cursor.execute(findUser,(email,))
    results=cursor.fetchone()
    if results[2]==password:
        username=results[0]+' '+results[1]
        return username
    else:
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
    split_data=username.split()
    logoutid="select userId from userData where firstname=%s and lastname=%s"
    cursor.execute(logoutid,(split_data[1],split_data[2]))
    conn.commit()
    userid=cursor.fetchone()
    print(userid)




