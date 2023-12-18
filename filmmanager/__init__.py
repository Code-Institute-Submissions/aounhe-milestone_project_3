import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
if os.path.exists("env.py"):
    # in order to use the env.py file I need to import it
    import env  # noqa "No Quality Assurance"


# I have created an instance of the imported Flask() class, it would be stored
# in a variable called app which takes the default name Flask__name__module.
app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

db = SQLAlchemy(app)
    
from filmmanager import routes # noqa 


