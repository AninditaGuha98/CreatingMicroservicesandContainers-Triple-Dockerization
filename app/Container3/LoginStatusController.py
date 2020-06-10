from flask import Flask, request
from flask import render_template
from app.Container1 import DBConnector

app = Flask(__name__)

@app.route('/loginstatus',methods=['GET','POST'])
def loginstatus():
    if request.method=='POST':
        flag= DBConnector.logoutUser(request.form.get('username'))
        if flag:
            return render_template('loginstatus.html',status="You have successfully logged out.")
        else:
            return render_template('loginstatus.html', status="Could not log out.")
    return render_template('loginstatus.html')




if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5003)
