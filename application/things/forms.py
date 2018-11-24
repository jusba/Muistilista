from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ThingForm(FlaskForm):
    name = StringField("Name" ,[validators.Length(min=2)])
    description = StringField("Description",[validators.Length(max=400)])
    class Meta:
        csrf = False

class DescriptionForm(FlaskForm):
    
    description = StringField("Description",[validators.Length(max=400)])
    class Meta:
        csrf = False
