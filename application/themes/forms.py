from flask_wtf import FlaskForm
from wtforms import StringField, validators, SelectMultipleField

class NewSelectMultipleField(SelectMultipleField):
    def pre_validate(self,form):
        pass

class ThemeForm(FlaskForm):
    name = StringField("Nimi" ,[validators.DataRequired(message="Teema on pakko laittaa"), validators.length(min=1, max=100, message="Teeman pituus 1-100 merkkiä")])
    
    class Meta:
        csrf = False

class ThemeEditForm(FlaskForm):
    name = StringField("Nimi" ,[validators.DataRequired(message="Teema on pakko laittaa"), validators.length(min=1, max=100, message="Teeman pituus 1-100 merkkiä")])
    things = NewSelectMultipleField("Muistettavat asiat", choices=[], coerce= str)