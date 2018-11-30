from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Username",[validators.DataRequired(message="Käyttäjätunnus on pakko laittaa"), validators.length(min=3, max=20, message="Käyttäjätunnuksen pituus 3-20 merkkiä")])
    password = PasswordField("Password",[validators.DataRequired(message="Salasana on pakko laittaa"), validators.length(min=3, max=100, message="Salasanan pituus 3-100 merkkiä")])
  
    class Meta:
        csrf = False
