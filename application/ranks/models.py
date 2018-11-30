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

  
def get_ranks():
    
    stmt = text("SELECT Rank.name FROM Rank"
                    " GROUP BY Rank.name")
              
    res = db.engine.execute(stmt)
    

    response = []
    
    for row in res:
        print("jeesus" , type(row[0]))
        print("keesus", row[0])
        
        values = (row[0], row[0])
        response.append(values)
        
    print("toimiiko?")
    return response
