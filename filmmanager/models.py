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

    id_film="1",
    title="The Hunger Games",
    director="Francis Lawrence",
    year="2023-11-17",
    genre="Drama",
    overview="64 years before he becomes the tyrannical president of Panem, Coriolanus Snow sees a chance for a change in fortunes when he mentors Lucy Gray Baird, the female tribute from District 12.",
    image="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/ePquoeNxJ6vg8U7iSjRAZ2KdztX.jpg"
)
Aquaman_and_the_Lost_Kingdom = Film(

    id_film="2",
    title="Aquaman and the Lost Kingdom (2023)",
    director="James Wan",
    year="2023-12-2",
    genre="Action, Adventure, Fantasy",
    overview="Black Manta, still driven by the need to avenge his father death and wielding the power of the mythic Black Trident, will stop at nothing to take Aquaman down once and for all. To defeat him, Aquaman must turn to his imprisoned brother Orm, the former King of Atlantis, to forge an unlikely alliance in order to save the world from irreversible destruction.",
    image="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/8xV47NDrjdZDpkVcCFqkdHa3T0C.jpg"
)
Silent_Night = Film(

    id_film="3",
    title="Silent Night (2023)",
    director="John Woo",
    year="2023-12-24",
    genre="Action, Crime",
    overview="Black Manta, still driven by the need to avenge his father death and wielding the power of the mythic Black Trident, will stop at nothing to take Aquaman down once and for all. To defeat him, Aquaman must turn to his imprisoned brother Orm, the former King of Atlantis, to forge an unlikely alliance in order to save the world from irreversible destruction.",
    image="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/8xV47NDrjdZDpkVcCFqkdHa3T0C.jpg"
)
The_Family_Plan = Film(

    id_film="4",
    title="The Family Plan (2023)",
    director="Simon Cellan Jone",
    year="2023-12-15",
    genre="Action, Comedy",
    overview="Dan Morgan is many things: a devoted husband, a loving father, a celebrated car salesman. He also a former assassin. And when his past catches up to his present, he forced to take his unsuspecting family on a road trip unlike any other.",
    image="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/jLLtx3nTRSLGPAKl4RoIv1FbEBr.jpg"
)
Wonka = Film(

    id_film="5",
    title="Wonka (2023)",
    director="Paul Kin",
    year="2023-12-08",
    genre="Comedy, Family, Fantasy",
    overview="Willy Wonka chock-full of ideas and determined to change the world one delectable bite at a time is proof that the best things in life begin with a dream, and if you re lucky enough to meet Willy Wonka, anything is possible.",
    image="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/qhb1qOilapbapxWQn9jtRCMwXJF.jpg"
)
Chicken_Run_Dawn_of_the_Nugget = Film(

    id_film="6",
    title="Chicken Run: Dawn of the Nugget (2023)",
    director="Sam Fell",
    year="2023-12-08",
    genre="Animation, Adventure",
    overview="A band of fearless chickens flock together to save poultry-kind from an unsettling new threat: a nearby farm thats cooking up something suspicious.",
    image="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/exNtEY8QUuQh9e23wSQjkPxKIU3.jpg"
)
Oppenheimer = Film(

    id_film="7",
    title="Oppenheimer (2023)",
    director="Christopher Nolan",
    year="2023-07-21",
    genre="Drama, History",
    overview="The story of J. Robert Oppenheimer role in the development of the atomic bomb during World War II.",
    image="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg"
)
Freelance = Film(

    id_film="8",
    title="Freelance (2023)",
    director="Pierre Morel",
    year="2024-01-01",
    genre="Action, Comedy",
    overview="An ex-special forces operative takes a job to provide security for a journalist as she interviews a dictator, but a military coup breaks out in the middle of the interview, they are forced to escape into the jungle where they must survive.",
    image="https://www.themoviedb.org/t/p/w600_and_h900_bestv2/7Bd4EUOqQDKZXA6Od5gkfzRNb0.jpg"
)
db.session.add(The_Hunger_Games)
db.session.add(Aquaman_and_the_Lost_Kingdom)
db.session.add(Silent_Night)
db.session.add(The_Family_Plan)
db.session.add(Wonka)
db.session.add(Chicken_Run_Dawn_of_the_Nugget)
db.session.add(Oppenheimer)
db.session.add(Freelance)
db.session.commit()
db.session.close()

