from filmmanager import db


class Film(db.Model):

    # schema for films model
    film_id= db.Column(db.String, unique=True, primary_key=True)
                       # film title unique
    director = db.Column(db.String, nullable=False)  # film director
    year = db.Column(db.Date, nullable=False)  # film year
    genre = db.Column(db.String, nullable=False)  # film genre
    overview = db.Column(db.String)  # film description


def __repr__(self):
    # __rep__ to represent itself in the form of a string
  return  
      self.film_id


class Review(db.Model):
    # schema for Reviews model
    id = db.Column(db.Integer, primary_key=True) 
    film_id = db.Column(db.String, db.ForeignKey("film.id_film", ondelete="CASCADE")) 
    review_text = db.Column(db.Text) # review information
    users_review = db.Column(db.String, db.ForeignKey("users.id_email", ondelete="CASCADE")) # user who posts the review
    
    def __repr__(self):
        # to represent ISBN in the form of a string
        return 
            self.id , self.film_id, self.users_review
        


class Users(db.Model):
    # schema for Users model
    id_email = db.Column(db.String, unique=True, primary_key=True) # the id is a string which is the users' email
    password = db.Column(db.String, nullable=False) # the password which it has been hashed in routes
    fname = db.Column(db.String, nullable=False) # user first name
    lname = db.Column(db.String, nullable=False) # user last name
    reviews = db.relationship("Review", backref="users", cascade="all,delete", lazy=True) # review published
    
    
    def __repr__(self):
        # to represent the user details in the form of a string
        return "# Email: {0} - Name: {2} - Last Name: {3}".format(
            self.id_email, self.fname, self.lname
        )

