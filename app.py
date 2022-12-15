from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
from os import path
import sqlite3
from sqlalchemy.ext.automap import automap_base

app = Flask(__name__, static_url_path='/static')
app.config["SECRET_KEY"] = "secret_key"
app.permanent_session_lifetime = timedelta(minutes=2)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# connect to table by auto map
Base = automap_base()
Base.prepare (db.engine, reflect=True)
faculties = Base.classes.faculties
departments = Base.classes.departments
lecturers = Base.classes.lecturers
students = Base.classes.students
subjects = Base.classes.subjects
classes = Base.classes.classes
projects = Base.classes.projects
libraries = Base.classes.libraries
books = Base.classes.books

enroll_in = db.Table('enroll_in', db.metadata, autoload=True, autoload_with=db.engine)
guide = db.Table('guide', db.metadata, autoload=True, autoload_with=db.engine)
participate_in = db.Table('participate_in', db.metadata, autoload=True, autoload_with=db.engine)
can_borrow = db.Table('can_borrow', db.metadata, autoload=True, autoload_with=db.engine)

@app.route("/enroll_in")
def def_enroll_in():
    results = db.session.query(enroll_in).all()
    return render_template("enroll_in.html", results = results)

@app.route("/can_borrow")
def def_can_borrow():
    results = db.session.query(can_borrow).all()
    return render_template("can_borrow.html", results = results)

@app.route("/participate_in")
def def_participate_in():
    results = db.session.query(participate_in).all()
    return render_template("participate_in.html", results = results)

@app.route("/guide")
def def_guide():
    results = db.session.query(guide).all()
    return render_template("guide.html", results = results)

@app.route("/book")
def book():
    results = db.session.query(books).all()
    return render_template("books.html", results = results)

@app.route("/library")
def library():
    results = db.session.query(libraries).all()
    return render_template("libraries.html", results = results)

@app.route("/project")
def project():
    results = db.session.query(projects).all()
    return render_template("projects.html", results = results)

@app.route("/def_class")
def def_class():
    results = db.session.query(classes).all()
    return render_template("classes.html", results = results)

@app.route("/subject")
def subject():
    results = db.session.query(subjects).all()
    return render_template("subjects.html", results = results)

@app.route("/student")
def student():
    results = db.session.query(students).all()
    return render_template("students.html", results = results)

@app.route("/lecturer")
def lecturer():
    results = db.session.query(lecturers).all()
    return render_template("lecturers.html", results = results)

@app.route("/department")
def department():
    results = db.session.query(departments).all()
    return render_template("departments.html", results = results)

@app.route("/faculty")
@app.route("/")
def faculty():
    results = db.session.query(faculties).all()
    # for r in results:
    #     print(r.f_name)
    return render_template("faculties.html", results = results)

if __name__=="__main__":
    app.run(debug=True)
