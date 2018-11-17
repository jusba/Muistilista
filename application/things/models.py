from application import db

class Thing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    rank = db.Column(db.String(144), nullable=False)

    def __init__(self, name, rank):
        self.name = name
        self.rank = rank

