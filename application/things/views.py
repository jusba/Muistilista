
from application import app, db
from flask import redirect, render_template, request, url_for
from application.things.models import Thing, ThingTheme
from application.things.forms import ThingForm
from application.things.forms import DescriptionForm
from flask_login import login_required, current_user
from application.ranks.models import Rank
from application.themes.models import Theme
from sqlalchemy.sql import text
import os.path
from pathlib import Path


#Showing list of things
@app.route("/things", methods=["GET"])
@login_required
def things_index():
    return render_template("things/list.html", things = Thing.query.filter(Thing.account_id == current_user.id).all(), ranks = Rank.query.filter(Rank.account_id == current_user.id).all(), themes = Theme.query.filter(Theme.account_id == current_user.id).all(), thingthemes = ThingTheme.query.filter(ThingTheme.account_id == current_user.id).all(), form = DescriptionForm())

# Showing the page to make new things
@app.route("/things/new/")
@login_required
def things_form():
    formC = ThingForm()
    
    res = Rank.query.filter(Rank.account_id == current_user.id).all()
    

    response = []
    
    for row in res:
        rowName = str(row.name)    
        
        values = (rowName, rowName)
        response.append(values)
    formC.rank.choices = response

    themeRes = Theme.query.filter(Theme.account_id == current_user.id).all()
    themeResponse = []
    for row in themeRes:
        rowName = str(row.name)    
        
        values = (rowName, rowName)
        themeResponse.append(values)
    formC.theme.choices = themeResponse

    return render_template("things/new.html", form = formC)
#Saving new thing with parameters from the new form
@app.route("/things", methods=["POST"])
@login_required
def things_create():
    
    form =  ThingForm(request.form)
    
    
    if not form.validate_on_submit():
        
        return render_template("things/list.html", form = form)
    
    
    
    t = Thing(form.name.data, form.description.data)
    rank = Rank.query.filter_by(name = form.rank.data).first()
    
     
    
    
    t.rank_id = rank.id
    t.account_id = current_user.id
    db.session().add(t)
    for x in form.theme.data:
        theme = Theme.query.filter_by(name = x).first()
        thing = t
        tt = ThingTheme(t.id, theme.id)
        tt.account_id = current_user.id
        db.session().add(tt)
    
    try:
        db.session().commit()
    except Exception as e:
        
        print(str(e))
        
  
    return redirect(url_for("things_index")) 
#Changing thing description
@app.route("/things/<thing_id>/",methods=["POST"])
@login_required
def thing_change_description(thing_id):
    
    form = DescriptionForm()
    
    if not form.validate_on_submit():
        return render_template("things/list.html", form = form)
    t = Thing.query.get(thing_id)
    t.description = form.description.data
    rank = Rank.query.filter_by(name = form.rank.data).first()
    t.rank_id = rank.id
    ThingTheme.query.filter(ThingTheme.thing_id == thing_id).delete()
    
    for x in form.themes.data:
        theme = Theme.query.filter_by(name = x).first()
        
        tt = ThingTheme(t.id, theme.id)
        tt.account_id = current_user.id
        db.session().add(tt)
    
    
    db.session().commit()
    return redirect(url_for("things_index")) 
#Delete thing
@app.route("/things/<thing_id>/",methods=["GET", "POST"])
@login_required
def thing_delete(thing_id):
    Thing.query.filter(Thing.id == thing_id).delete()
    ThingTheme.query.filter(ThingTheme.thing_id == thing_id).delete()
    db.session().commit()
    return redirect(url_for("things_index")) 
#Showing one thing
@app.route("/things/thing/<thing_id>/",methods=["GET"])
@login_required
def thing_show(thing_id):
    formC = DescriptionForm()
    
    res = Rank.query.filter(Rank.account_id == current_user.id).all()
    

    response = []
    
    for row in res:
        rowName = str(row.name)    
        
        values = (rowName, rowName)
        response.append(values)
    formC.rank.choices = response

    
    themes = Theme.query.filter(Theme.account_id == current_user.id).all()
    response2 = []
    
    for row2 in themes:
        
        rowName = str(row2.name)    
        values = (rowName, rowName)
        response2.append(values)



    
    formC.themes.choices = response2

    form = formC
    return render_template("things/thing.html", things = Thing.query.filter(Thing.id == thing_id).all(),ranks = Rank.query.filter(Rank.account_id == current_user.id).all(),themes = Theme.query.filter(Theme.account_id == current_user.id).all(), thingthemes = ThingTheme.query.filter(ThingTheme.account_id == current_user.id).all(), form = form)




    

