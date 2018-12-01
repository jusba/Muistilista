from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators, TextAreaField
from application.ranks.models import Rank
from flask_login import current_user
from application import db



class ThingForm(FlaskForm):
    
    
    
    response = []
    

    name = StringField("Muistettava asia" ,[validators.DataRequired(message="Nimi on pakko laittaa"), validators.length(min=1, max=100, message="Nimen pituus 1-100 merkkiä")])
    description = TextAreaField("Kuvaus", [validators.length(min=1, max=1000, message="Kuvauksen pituus 1-1000 merkkiä")])
    rank = SelectField('Kiireellisyys',[validators.DataRequired(message="Rank on pakko laittaa")], choices= [], coerce= str)
    

    class Meta:
        csrf = False
    

class DescriptionForm(FlaskForm):
    
    description = TextAreaField("Kuvaus", [validators.length(min=1, max=1000, message="Kuvauksen pituus 1-1000 merkkiä")])
    rank = SelectField('Kiireellisyys',[validators.DataRequired(message="Rank on pakko laittaa")], choices= [], coerce= str)
    class Meta:
        csrf = False
