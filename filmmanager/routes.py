from flask import render_template
from filmmanager import app, db
from filmmanager.models import Film, Review, Users


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/films")
def films():
    
    films = list(Film.query.order_by(Film.id_film, Film.title, Film.director, Film.year,
    Film.genre, Book.overview).all())
    reviews = list(Review.query.order_by(Review.book_id, Review.review_text,
    Review.users_review).all())
    return render_template("films.html", books = books, reviews=reviews)

