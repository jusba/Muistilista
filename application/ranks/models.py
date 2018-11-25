from application import db
from application.models import Base
from sqlalchemy.sql import text

class Rank(Base):
    

    name = db.Column(db.String(144), nullable=False)
    

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'),
                           nullable=False)
    things = db.relationship("Thing", backref='rank', lazy=True)                   


    def __init__(self, name):
        self.name = name

     
# def get_ranks():
#     print("testia")
#     stmt = text("SELECT Rank.name FROM Rank"
#                     " GROUP BY Rank.name")
              
#     res = db.engine.execute(stmt)
    

#     response = []
#     number = 0
#     for row in res:
#         values = (number, row)
#         response.append(values)
#         number = number + 1
#     print("toimiiko?")
#     return response
