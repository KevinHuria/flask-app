from tkinter.tix import Form
from app import app
from flask import render_template, url_for, redirect, flash, request
from app.forms import SignUpform, LogInform
from app.models import User, db
from app import app, db, pwd
from flask_login import login_user, current_user, logout_user, login_required

app.config['SECRET_KEY'] = '19a27057ac27ad42c9f047c62aeb6f15'


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route('/about')
def about():
    return "<h1>About!</h1>"


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if current_user.is_authenticated:
        flash("You are already logged in.", "warning")
        return redirect(url_for('index'))
    form = SignUpform(request.form)
    if request.method == "POST" and form.validate():
        hashed = pwd.generate_password_hash(form.password.data).decode('utf-8')
        element = User(uname=form.username.data,
                       email=form.email.data, password=hashed)
        db.session.add(element)
        db.session.commit()
        flash("Account created for %s!" % (form.username.data), "success")
        # Displays flash message upon form validation
        return redirect(url_for('index'))
    return render_template("public/sign_up.html", form=form)


@app.route('/logIn', methods=['GET', 'POST'])
def LogIn():
    if current_user.is_authenticated:
        flash("You are already logged in.", "warning")
        return redirect(url_for('index'))
        form = LogInForm(request.form)
        if request.method == "POST" and form.validate():
              user = User.query.filter_by(uname=form.username.data).first()
        if user and pwd.check_password_hash(user.password, form.password.data):
                    login_user(user)
                    flash("Welcome, %s!" % (form.username.data), "success")
                    return redirect(url_for('index'))
        else:
            flash("LogIn Unsuccessful", 'danger')
    return redirect(url_for('LogIn'))
    return render_template("public/login.html", form=form)


@app.route("/logout")
def logoutpage():
    logout_user()
    flash("Successfuly logged out.", "success")
    return redirect(url_for('index'))


@ app.route("/profile/<username>")
def profile(username):
    return render_template("public/profile.html")
