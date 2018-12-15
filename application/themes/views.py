from application import app, db
from flask import redirect, render_template, request, url_for
from application.themes.forms import ThemeForm
from flask_login import login_required, current_user
from application.themes.models import Theme

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
#Delete theme
@app.route("/themes/<theme_id>/",methods=["GET", "POST"])
@login_required
def theme_delete(theme_id):
    Theme.query.filter(Theme.id == theme_id).delete()
    db.session().commit()
    return redirect(url_for("themes_index")) 

