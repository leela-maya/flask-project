from flask import *
from flask_pymongo import PyMongo

app = Flask(__name__)
mongodb_client = PyMongo(
    app, uri="mongodb+srv://leela:leela@cluster0.c7orl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = mongodb_client.db


@app.route("/login")
def login():
    if request.method == "GET":
        if request.form:
            db.users.find(dict(request.form))
            return redirect(url_for("Success")) 
        else:
            return render_template("signup.html")
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "post":
        if request.form:
            email = request.form['userName']
            password = request.form['password']
            if(len(email)and len(password))>0:
                db.users.insert_one(dict(request.form))
                return render_template('login.html')
            else:
               return "error"
    else:
        return render_template("signup.html")


@app.route("/forgotpassword")
def fpassword():
    return render_template("forgotpassword.html")


@app.route("/")
def landingpage():
    return render_template("landingpage.html")

@app.route("/landing")
def Success():
    return "landing page"

if __name__ == '__main__':
    app.run(debug=True)
