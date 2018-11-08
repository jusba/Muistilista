
from application import app, db
from flask import redirect, render_template, request, url_for
from application.things.models import Thing

#Showing list of things
@app.route("/things", methods=["GET"])
def things_index():
    return render_template("things/list.html", things = Thing.query.all())

# Showing the page to make new things
@app.route("/things/new/")
def things_form():
    return render_template("things/new.html")
#Saving new thing with parameters from the new form
@app.route("/things/", methods=["POST"])
def things_create():
    t = Thing(request.form.get("name"))
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("things_index")) 
        
