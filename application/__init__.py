# Importing flask
from flask import Flask
app = Flask(__name__)

# Importing sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# Determine things.db database for use, either local or heroku
import os
if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///things.db"    
    app.config["SQLALCHEMY_ECHO"] = True

# Creating db object to control databases
db = SQLAlchemy(app)

# importing views from application
from application import views

# Importing models from things
from application.things import models
# Importing views from things
from application.things import views
# Importing models from auth
from application.auth import models
# Importing views from auth
from application.auth import views
# Importing things for rank
from application.ranks import models
from application.ranks import views
# Importing things for themes
from application.themes import models
from application.themes import views

#Importing things needed for sign in
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Please login to use this functionality."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Creating databases needed if necessary
try: 
    db.create_all()
except:
    pass
