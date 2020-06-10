from flask import Flask, request
from flask import render_template
import DBConnector

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def loginPage():
    # Check login credentials
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # find the username of email id
        flag = DBConnector.CheckLoginCredentials(email, password)
        if flag != "no":
            list= DBConnector.InsertintoUserState(email)
            return render_template('loginstatus.html', user=flag,list=list)
        else:
            return render_template('login.html', status="Invalid Credentials")
    return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5001)
