import os



from cs50 import SQL,get_string
from flask import Flask, flash, redirect, render_template, request, session,jsonify
from flask_session import Session
from tempfile import mkdtemp
import datetime
import sys
from werkzeug.security import check_password_hash, generate_password_hash

#from helpers import apology, login_required, lookup, usd
#api_key=pk_6f837f4b4b234228ab76f65bfac9d740
# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///Diary.db")


@app.route("/")
def index():
    """Show homepage"""

    return render_template("homepage.html")


@app.route("/Introduction", methods=["GET", "POST"])
def Introduction():
    """Show homepage"""

    return render_template("Introduction.html")

@app.route("/WhatamIdoing", methods=["GET", "POST"])
def WhatamIdoing():
    

    return render_template("whatamidoing.html")


@app.route("/Hobby", methods=["GET", "POST"])
def Hobby():
    

    return render_template("Hobby.html")


@app.route("/Diary", methods=["GET", "POST"])
def Diary():

    diary_db=db.execute("SELECT ID, Content, DateTime FROM Diary")

    return render_template("Diary.html",database=diary_db)

@app.route("/Writenew", methods=["GET", "POST"])
def Writenew():

    if request.method == "GET":
       
        return render_template("Writenew.html")

    else:

        Writenew=request.form.get("Writenew")


        date=datetime.datetime.now()
        #INSERT INTO table_name (column1, column2 , column3,..) VALUES (value1,value2,value3,...)
        db.execute("INSERT INTO Diary (Content,DateTime) VALUES(?,?)",Writenew,date)


        return redirect("/Diary")
