from application import db
from application.models import Base

class Thing(Base):
    

    name = db.Column(db.String(144), nullable=False)
    description = db.Column(db.String(400), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    rank_id = db.Column(db.Integer, db.ForeignKey('rank.id'),
                           nullable=False)                       


    def __init__(self, name, description):
        self.name = name
        self.description = description

