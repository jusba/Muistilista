from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators, TextAreaField, SelectMultipleField
from application.ranks.models import Rank
from application.themes.models import Theme
from flask_login import current_user
from application import db

class NewSelectField(SelectField):
    def pre_validate(self,form):
        pass
class NewSelectMultipleField(SelectMultipleField):
    def pre_validate(self,form):
        pass

class ThingForm(FlaskForm):
    
    
    
    
    

    name = StringField("Muistettava asia" ,[validators.DataRequired(message="Nimi on pakko laittaa"), validators.length(min=1, max=100, message="Nimen pituus 1-100 merkkiä, yritä uudelleen!")])
    description = TextAreaField("Kuvaus", [validators.length(min=1, max=1000, message="Kuvauksen pituus 1-1000 merkkiä, yritä uudelleen!")])
    rank = NewSelectField('Kiireellisyys',[validators.DataRequired(message="Rank on pakko laittaa")], choices= [], coerce= str)
    theme = NewSelectMultipleField("Teema",[validators.DataRequired(message="Teema on pakko laittaa")], choices= [], coerce= str)

    class Meta:
        csrf = False
    

class DescriptionForm(FlaskForm):
    
    description = TextAreaField("Kuvaus", [validators.length(min=1, max=1000, message="Kuvauksen pituus 1-1000 merkkiä, yritä uudelleen!")])
    rank = NewSelectField('Kiireellisyys',[validators.DataRequired(message="Rank on pakko laittaa")], choices= [], coerce= str)
    themes = NewSelectMultipleField('Teemat',[validators.DataRequired(message="Teema on pakko laittaa")], choices= [], coerce= str)
    class Meta:
        csrf = False


    