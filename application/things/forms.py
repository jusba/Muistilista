from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ThingForm(FlaskForm):
    name = StringField("Name" ,[validators.Length(min=2)])
    rank = StringField("Rank")
    class Meta:
        csrf = False

class RankForm(FlaskForm):
    
    rank = StringField("Rank")
    class Meta:
        csrf = False