from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from os import path
import sqlite3

app = Flask(__name__, static_url_path='/static')
app.config["SECRET_KEY"] = "secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lecturer.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
app.permanent_session_lifetime = timedelta(minutes=2)

db = SQLAlchemy(app)

class Lecturer(db.Model):
    l_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    phonenum = db.Column(db.String(50))
    
    def __init__(self, name, phonenum):
        pass

@app.route("/logged_in")
def logged_in():
    flash("add successfull")
    return redirect(url_for("home"))

@app.route("/faculty")
def faculty():
    return render_template("faculty.html")

@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("home.html")

if __name__=="__main__":
    
    if not path.exists("lecturer"):
        db.create_all(app=app)
        print("database created!")
    else:
        print("database is already created!")
    app.run(debug=True)
