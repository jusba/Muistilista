from flask_wtf import FlaskForm
from wtforms import StringField

class ThingForm(FlaskForm):
    name = StringField("Name")
    rank = StringField("Rank")
    class Meta:
        csrf = False
