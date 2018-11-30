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

  
def get_ranks():
    
    stmt = text("SELECT Rank.name FROM Rank"
                    " GROUP BY Rank.name")

    
    data_folder = Path("application/")

    file_to_open = data_folder / "things.db"
    if os.path.isfile(file_to_open):
        res = db.engine.execute(stmt)
    

        response = []
    
        for row in res:
            
        
            values = (row[0], row[0])
            response.append(values)
        
    
            return response
