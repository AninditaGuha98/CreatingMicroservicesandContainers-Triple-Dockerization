from flask import Flask, request
from flask import render_template

from app.service import MainService

app = Flask(__name__, template_folder='../templates')



@app.route('/', methods=['GET','POST'])
def registrationPage():

    # Checking validity of password and confirm password
    if request.method== 'POST':
        if request.form.get('password')!=request.form.get('confirmpassword'):
                return render_template('registration.html', status="Passwords do not match")
        else:
            firstname= request.form.get('firstname')
            lastname = request.form.get('lastname')
            email = request.form.get('email')
            password= request.form.get('password')
            MainService.sendRegistrationDetails(firstname,lastname,email,password)
            return render_template('registration.html', status="Registration done")
    return render_template('registration.html')


if __name__ == '__main__':
    app.run(debug=True)
