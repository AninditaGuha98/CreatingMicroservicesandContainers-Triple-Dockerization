from flask import Flask, request
from flask import render_template

from app.model import DBConnector
from app.service import MainService

app = Flask(__name__, template_folder='../templates')


@app.route('/', methods=['GET', 'POST'])
def registrationPage():
    # Checking validity of password and confirm password
    if request.method == 'POST':
        if request.form.get('password') != request.form.get('confirmpassword'):
            return render_template('registration.html', status="Passwords do not match")
        else:
            firstname = request.form.get('firstname')
            lastname = request.form.get('lastname')
            email = request.form.get('email')
            password = request.form.get('password')
            DBConnector.SQLenterDetails(firstname, lastname, email, password)
            return render_template('registration.html', status="Registration successful")
    return render_template('registration.html')


@app.route('/login', methods=['GET', 'POST'])
def loginPage():
    # Check login credentials
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # find the username of email id
        flag = DBConnector.CheckLoginCredentials(email, password)
        print(flag)
        if flag != "no":
            list=DBConnector.InsertintoUserState(email)
            return render_template('loginstatus.html', user=flag,list=list)
        else:
            return render_template('login.html', status="Invalid Credentials")
    return render_template('login.html')


@app.route('/loginstatus',methods=['GET','POST'])
def loginstatus():
    if request.method=='POST':
        DBConnector.logoutUser(request.form.get('username'))
        return render_template('loginstatus.html')


if __name__ == '__main__':
    app.run(debug=True)
