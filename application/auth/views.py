from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user
from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm


@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "No such username or password")


    login_user(user)
    return redirect(url_for("index"))  


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index")) 

@app.route("/auth/new")
def account_form():
    return render_template("auth/new.html", form = LoginForm())

@app.route("/auth", methods=["POST"])  
def account_create():
    form = LoginForm(request.form)
    if not form.validate():
        return render_template("auth/new.html", form = form)
    a = User(form.username.data, form.username.data, form.password.data)
    db.session().add(a)
    db.session().commit()
    return render_template("index.html")