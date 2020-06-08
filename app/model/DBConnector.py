import mysql.connector



conn = mysql.connector.connect(host='database-2.ccmdqmbvy12j.us-east-1.rds.amazonaws.com'
                                   ,user='admin',
                                   password='serverless',
                                   db='login_database')
cursor = conn.cursor()

def SQLenterDetails():
    


