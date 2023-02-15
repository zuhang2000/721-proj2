from flask import render_template
from app import app
from app import database as db


@app.route("/")
def home():
    return render_template("index.html")