from application import app, db
from flask import redirect, render_template, request, url_for
from application.ranks.forms import RankForm
from flask_login import login_required, current_user
from application.ranks.models import Rank

#Showing list of ranks
@app.route("/ranks", methods=["GET"])
@login_required
def ranks_index():
    return render_template("ranks/list.html", ranks = Rank.query.filter(Rank.account_id == current_user.id).all())
# Showing the page to make new ranks
@app.route("/ranks/new/")
@login_required
def ranks_form():
    return render_template("ranks/new.html", form = RankForm())
#Saving new rank with parameters from the new form
@app.route("/ranks", methods=["POST"])
@login_required
def ranks_create():
    form =  RankForm(request.form)
    if not form.validate():
        return render_template("ranks/new.html", form = form)

    r = Rank(form.name.data)
    r.account_id = current_user.id
    db.session().add(r)
    db.session().commit()
  
    return redirect(url_for("ranks_index"))     
#Delete rank
@app.route("/ranks/<rank_id>/",methods=["GET", "POST"])
@login_required
def rank_delete(rank_id):
    Rank.query.filter(Rank.id == rank_id).delete()
    db.session().commit()
    return redirect(url_for("ranks_index")) 