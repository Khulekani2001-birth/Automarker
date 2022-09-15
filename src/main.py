from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from wtforms import HiddenField, SubmitField, StringField
from flask_wtf import FlaskForm
from flask_migrate import Migrate
app = Flask(__name__)
app.config['SECRET_KEY'] = '12345'


@app.route("/")
def main():
    return render_template("main.html", title="Home")

class StudentForm(FlaskForm):
    id = HiddenField()
    name = StringField("Name")
    submit = SubmitField("Save")


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////tmp/students.db"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Student(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    
    def __repr__(self):
        return self.name

@app.route("/student", methods=["GET", "POST"])
def createStudent():
    #return render_template("students.html", title="Student")
    #'''
    form = StudentForm(request.form)
    students = Student.query.all()
    if form.validate_on_submit():
        student = Student(name=form.name.data)
        db.session.add(student)
        db.session.commit()
        db.session.refresh(student)
        db.session.commit()
        flash("Student added successfully.")
        return redirect(url_for("createStudent"))
    return render_template("students.html", title="Student",form=form,students=students)
    #'''