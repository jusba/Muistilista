from application import db
from application.models import Base
from sqlalchemy.sql import text
import os.path
from pathlib import Path

class Rank(Base):
    

    name = db.Column(db.String(144), nullable=False)
    

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    things = db.relationship("Thing", backref='rank', lazy=True)                   


    def __init__(self, name):
        self.name = name

  

