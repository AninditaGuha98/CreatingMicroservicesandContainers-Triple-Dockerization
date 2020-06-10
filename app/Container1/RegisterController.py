from flask import Flask, request
from flask import render_template
import DBConnector

app = Flask(__name__)



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
            flag= DBConnector.SQLenterDetails(firstname, lastname, email, password)
            if flag:
                return render_template('registration.html', status="Registration successful")
            else:
                return render_template('registration.html',status="User already registered.")
    return render_template('registration.html')





if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0",port=5000)
