from filmmanager import db


class film(db.Model):

    # schema for films model
    title= db.Column(db.String, unique=True, primary_key=True)
                       # film title unique
    director = db.Column(db.String, nullable=False)  # film director
    year = db.Column(db.Date, nullable=False)  # film year
    genre = db.Column(db.String, nullable=False)  # film genre
    overview = db.Column(db.String)  # film description


def __repr__(self):
    # __rep__ to represent itself in the form of a string
  return self.title
