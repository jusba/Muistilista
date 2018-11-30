from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators
from application.ranks.models import Rank
from flask_login import current_user
from application import db



class ThingForm(FlaskForm):
    
    
    
    response = []
    

    name = StringField("Name" ,[validators.DataRequired(message="Nimi on pakko laittaa"), validators.length(min=1, max=100, message="Nimen pituus 1-100 merkkiä")])
    description = StringField("Description",[validators.DataRequired(message="Kuvaus on pakko laittaa"), validators.length(min=1, max=1000, message="Kuvauksen pituus 1-1000 merkkiä")])
    rank = SelectField('Rank',[validators.DataRequired(message="Rank on pakko laittaa")], choices= [])
    

    class Meta:
        csrf = False
    

class DescriptionForm(FlaskForm):
    
    description = StringField("Description",[validators.Length(max=400)])
    class Meta:
        csrf = False
