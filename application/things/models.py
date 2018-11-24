from application import db
from application.models import Base

class Thing(Base):
    

    name = db.Column(db.String(144), nullable=False)
    rank = db.Column(db.String(144), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)


    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

