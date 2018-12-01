
from application import app, db
from flask import redirect, render_template, request, url_for
from application.things.models import Thing
from application.things.forms import ThingForm
from application.things.forms import DescriptionForm
from flask_login import login_required, current_user
from application.ranks.models import Rank
from sqlalchemy.sql import text
import os.path
from pathlib import Path


#Showing list of things
@app.route("/things", methods=["GET"])
@login_required
def things_index():
    return render_template("things/list.html", things = Thing.query.filter(Thing.account_id == current_user.id).all(), ranks = Rank.query.filter(Rank.account_id == current_user.id).all(),form = DescriptionForm())

# Showing the page to make new things
@app.route("/things/new/")
@login_required
def things_form():
    formC = ThingForm()
    
    res = Rank.query.all()
    

    response = []
    
    for row in res:
        rowName = str(row.name)    
        
        values = (rowName, rowName)
        response.append(values)
    formC.rank.choices = response
    return render_template("things/new.html", form = formC)
#Saving new thing with parameters from the new form
@app.route("/things", methods=["POST"])
@login_required
def things_create():
    
    form =  ThingForm(request.form)
    ### Estää uusien thingien luonnin jostain syystä
    #if form.is_submitted():
    #    if not form.validate():
    #        return render_template("things/new.html", form = form)
    
   
    
    
    t = Thing(form.name.data, form.description.data)
    rank = Rank.query.filter_by(name = form.rank.data).first()
    
     
    
    
    t.rank_id = rank.id
    t.account_id = current_user.id
    db.session().add(t)
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
    #Estää muokkauksen jostain syystä
    #if not form.validate():
        #return render_template("things/list.html", form = form)
    t = Thing.query.get(thing_id)
    t.description = form.description.data
    rank = Rank.query.filter_by(name = form.rank.data).first()
    t.rank_id = rank.id
    
    db.session().commit()
    return redirect(url_for("things_index")) 
#Delete thing
@app.route("/things/<thing_id>/",methods=["GET", "POST"])
@login_required
def thing_delete(thing_id):
    Thing.query.filter(Thing.id == thing_id).delete()
    db.session().commit()
    return redirect(url_for("things_index")) 
#Showing one thing
@app.route("/things/thing/<thing_id>/",methods=["GET"])
@login_required
def thing_show(thing_id):
    formC = DescriptionForm()
    
    res = Rank.query.all()
    

    response = []
    
    for row in res:
        rowName = str(row.name)    
        
        values = (rowName, rowName)
        response.append(values)
    formC.rank.choices = response

    form = formC
    return render_template("things/thing.html", things = Thing.query.filter(Thing.id == thing_id).all(),ranks = Rank.query.filter(Rank.account_id == current_user.id).all(), form = form)




    

