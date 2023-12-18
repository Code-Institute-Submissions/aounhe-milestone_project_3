from flask import render_template
from filmmanager import app, db
from filmmanager.models import Film, Review, Users


@app.route("/")
def home():
    return render_template("index.html")