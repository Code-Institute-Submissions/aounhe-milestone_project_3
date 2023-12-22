from flask import render_template
from filmmanager import app, db
from filmmanager.models import film


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/films")
def films():
    return render_template("films.html")


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    return render_template("add_review.html")

@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    return render_template("add_review.html")

