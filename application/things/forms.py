from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators
from application.ranks.models import Rank, get_ranks
from flask_login import current_user
from application import db



class ThingForm(FlaskForm):
    
    
    
    response = []
    

    name = StringField("Name" ,[validators.Length(min=2)])
    description = StringField("Description",[validators.Length(max=400)])
    rank = SelectField('Rank', choices= [])
    

    class Meta:
        csrf = False
    

class DescriptionForm(FlaskForm):
    
    description = StringField("Description",[validators.Length(max=400)])
    class Meta:
        csrf = False
