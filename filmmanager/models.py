from filmmanager import db, app


class Review(db.Model):
    # schema for Reviews model
    id = db.Column(db.Integer, primary_key=True)
    film_id = db.Column(db.String, db.ForeignKey(
        "film.id_film", ondelete="CASCADE"))
    review_text = db.Column(db.Text)  # review information
    users_review = db.Column(db.String, db.ForeignKey(
        "users.id_email", ondelete="CASCADE"))  # user who posts the review

    def __repr__(self):
        # to represent id in the form of a string
        return "#{0} - id: {1} | Users: {4}".format(
            self.id, self.film_id, self.users_review
        )


class Users(db.Model):
    # schema for Users model
    # the id is a string which is the users' email
    id_email = db.Column(db.String, unique=True, primary_key=True)
    # the password which it has been hashed in routes
    password = db.Column(db.String, nullable=False)
    fname = db.Column(db.String, nullable=False)  # user first name
    lname = db.Column(db.String, nullable=False)  # user last name
    reviews = db.relationship(
        "Review", backref="users", cascade="all,delete", lazy=True)  # review published

    def __repr__(self):
        # to represent the user details in the form of a string
        return "# Email: {0} - Name: {2} - Last Name: {3}".format(
            self.id_email, self.fname, self.lname
        )


class Film(db.Model):

    # schema for films model
    id_film = db.Column(db.String, unique=True, primary_key=True)
    # film title unique
    title = db.Column(db.String(50), unique=True, nullable=False)
    director = db.Column(db.String, nullable=False)  # film director
    year = db.Column(db.Date, nullable=False)  # film year
    genre = db.Column(db.String, nullable=False)  # film genre
    overview = db.Column(db.String, nullable=False)  # film description
    film_reviews = db.relationship(
        "Review", backref="film", cascade="all, delete", lazy=True)
    image = db.Column(db.String)


def __repr__(self):
    # __rep__ to represent itself in the form of a string
    return "#{0} - title: {1} | image: {2}".format
    (self.id_film, title, director, year, genre, overview, film_reviews)

#tried to enter data manully 
The_Hunger_Games = Film(

    id_film="86918",
    title="The Hunger Games",
    director="Francis Lawrence",
    year="2023-11-17",
    genre="Drama",
    overview="64 years before he becomes the tyrannical president of Panem, Coriolanus Snow sees a chance for a change in fortunes when he mentors Lucy Gray Baird, the female tribute from District 12.",
    image="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/ePquoeNxJ6vg8U7iSjRAZ2KdztX.jpg"
)

#db.session.add(The_Hunger_Games)
#db.session.commit()
