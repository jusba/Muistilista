from flask_wtf import FlaskForm
from wtforms import StringField, validators

class RankForm(FlaskForm):
    name = StringField("Nimi" ,[validators.DataRequired(message="Rank on pakko laittaa"), validators.length(min=1, max=100, message="Rankin pituus 1-100 merkkiä")])
    
    class Meta:
        csrf = False
