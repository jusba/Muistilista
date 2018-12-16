from application import app, db
from flask import redirect, render_template, request, url_for
from application.themes.forms import ThemeForm, ThemeEditForm
from flask_login import login_required, current_user
from application.themes.models import Theme
from application.things.models import Thing, ThingTheme

#Showing list of themes
@app.route("/themes", methods=["GET"])
@login_required
def themes_index():
    return render_template("themes/list.html", themes = Theme.query.filter(Theme.account_id == current_user.id).all())
# Showing the page to make new themes
@app.route("/themes/new/")
@login_required
def themes_form():
    return render_template("themes/new.html", form = ThemeForm())
#Saving new theme with parameters from the new form
@app.route("/themes", methods=["POST"])
@login_required
def themes_create():
    form =  ThemeForm(request.form)
    if not form.validate():
        return render_template("themes/new.html", form = form)

    t = Theme(form.name.data)
    t.account_id = current_user.id
    db.session().add(t)
    db.session().commit()
  
    return redirect(url_for("themes_index"))     

#Edit theme
@app.route("/themes/<theme_id>/",methods=["POST"])
@login_required
def theme_edit(theme_id):
    
    form = ThemeEditForm()
    if not form.validate_on_submit():
        return render_template("themes/list.html", form = form)
    
    t = Theme.query.get(theme_id)
    t.name = form.name.data
    things_data = form.things.data
    things = []
    for row in things_data:
        
        thing = Thing.query.filter_by(name = row).first()
        things.append(thing)

    tt = ThingTheme.query.filter(ThingTheme.theme_id == t.id).all()
    for row in things:
        for row2 in tt:
            if row.id == row2.thing_id and row2.theme_id == t.id:
                
                ThingTheme.query.filter(ThingTheme.thing_id == row.id).delete()    

    
    db.session().commit()
    return redirect(url_for("themes_index")) 
#Showing one theme
@app.route("/themes/theme/<theme_id>/",methods=["GET"])
@login_required
def theme_show(theme_id):
    form = ThemeEditForm()
    
    thingthemes = ThingTheme.query.filter(ThingTheme.theme_id == theme_id).all() 
    things = Thing.query.filter(Thing.account_id == current_user.id).all()
    response = []
    for row in thingthemes:
        for row2 in things:
            if row.thing_id == row2.id:
                rowName = str(row2.name)    
                values = (rowName, rowName)
                response.append(values)



    
    form.things.choices = response
    
    return render_template("themes/theme.html", themes = Theme.query.filter(Theme.id == theme_id).all(), form = form, thingthemes = ThingTheme.query.filter(ThingTheme.account_id == current_user.id).all(), things = Thing.query.filter(Thing.account_id == current_user.id).all())

#Delete theme
@app.route("/themes/<theme_id>/",methods=["GET", "POST"])
@login_required
def theme_delete(theme_id):
    Theme.query.filter(Theme.id == theme_id).delete()
    db.session().commit()
    return redirect(url_for("themes_index")) 