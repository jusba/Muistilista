# Importing flask
from flask import Flask
app = Flask(__name__)

# Importing sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# Determine thins.db database for use
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///things.db"
# Have sqlalchemy print all sql queries
app.config["SQLALCHEMY_ECHO"] = True

# Creating db object to control databases
db = SQLAlchemy(app)

# importing views from application
from application import views

# Importing models from things
from application.things import models
# Importing views from things
from application.things import views

# Creating databases needed
db.create_all()
