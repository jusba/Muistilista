
from application import app, db
from flask import redirect, render_template, request, url_for
from application.things.models import Thing
from application.things.forms import ThingForm
from application.things.forms import RankForm
from flask_login import login_required, current_user


#Showing list of things
@app.route("/things", methods=["GET"])
def things_index():
    return render_template("things/list.html", things = Thing.query.all(),form = RankForm())

# Showing the page to make new things
@app.route("/things/new/")
@login_required
def things_form():
    return render_template("things/new.html", form = ThingForm())
#Saving new thing with parameters from the new form
@app.route("/things", methods=["POST"])
@login_required
def things_create():
    form =  ThingForm(request.form)
    if not form.validate():
        return render_template("things/new.html", form = form)

    t = Thing(form.name.data, form.rank.data)
    t.account_id = current_user.id
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("things_index")) 
#Changing thing rank
@app.route("/things/<thing_id>/",methods=["POST"])
@login_required
def thing_change_rank(thing_id):
    form = RankForm()
    t = Thing.query.get(thing_id)
    t.rank = form.rank.data
    t.account_id = current_user.id
    db.session().commit()
    return redirect(url_for("things_index")) 
    

