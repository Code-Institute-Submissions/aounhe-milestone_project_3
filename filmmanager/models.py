from filmmanager import db


class Review(db.Model):

    # schema for Reviews model
    id = db.Column(db.Integer, primary_key=True)  # the id is an integer
    film_id = db.Column(db.String, db.ForeignKey(
        "film.id_film", ondelete="CASCADE"))  # connected to the film ISBN
    review_text = db.Column(db.Text)  # review information
    users_review = db.Column(db.String, db.ForeignKey(
        "users.id_email", ondelete="CASCADE"))  # user who posts the review


def __repr__(self):
    # to represent ISBN in the form of a string
    return "#{0} - ISBN: {1} | Users: {4}".format(
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
    # film id is the unique ISBN
    id_film = db.Column(db.String, unique=True, primary_key=True)
    title = db.Column(db.String, unique=True,
                      nullable=False)  # film title unique
    director = db.Column(db.String, nullable=False)  # film director
    year = db.Column(db.Date, nullable=False)  # film year
    genre = db.Column(db.String, nullable=False)  # film genre
    # reviews related to each film
    film_reviews = db.relationship(
        "Review", backref="film", cascade="all, delete", lazy=True)
    image = db.Column(db.String)  # image source from each film (link)
    description = db.Column(db.String)  # film description


def __repr__(self):
    # __rep__ to represent itself in the form of a string
    return "# ID: {0} - Title: {1} - director: {2} | ISBN: {5}".format(
        self.id_film, self.title, self.director, self.isbn
    )
