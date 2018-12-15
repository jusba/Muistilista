from application import db
from application.models import Base

class Theme(Base):
    

    name = db.Column(db.String(144), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
                       
    thingThemes = db.relationship("ThingTheme", backref='theme', lazy=True)

    def __init__(self, name):
        self.name = name
        


