from app.model import DBConnector

author="Anindita"

def sendRegistrationDetails(firstname,lastname,email,password):
    DBConnector.SQLenterDetails(firstname,lastname,email,password)


def CheckLoginCredentials(email,password):
    DBConnector.CheckLoginCredentials(email,password)
