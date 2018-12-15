from application import db
from application.models import Base

class Thing(Base):
    

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(400), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    rank_id = db.Column(db.Integer, db.ForeignKey('rank.id'),
                           nullable=False)                       
    thingThemes = db.relationship("ThingTheme", backref='rank', lazy=True)  



    def __init__(self, name, description):
        self.name = name
        self.description = description

class ThingTheme(Base):
    id = db.Column(db.Integer, primary_key=True)
    thing_id = db.Column(db.Integer, db.ForeignKey('thing.id'),
                           nullable=False)
    theme_id = db.Column(db.Integer, db.ForeignKey('theme.id'),
                           nullable=False)