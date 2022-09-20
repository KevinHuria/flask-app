from app import app
from flask import render_template,url_for, request, redirect
from .forms import SignUpform,LogInform

app.config['SECRET KEY'] = 'c8bb8624813e116b58652015766ac934'
@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/jinja")
def jinja():

    my_name = 'Kevin'
    return render_template("public/jinja.html", my_name=my_name)


@app.route("/about")
def about():
    return "<h1>About!</h1>"


@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    form =SignUpform()
    return render_template("public/sign_up.html",form=form)

@app.route('/logIn')
def LogIn():
    form=LogInform()
    return render_template('public/login.html', form=form)

@app.route("/profile/<username>")
def profile(username):
    return render_template("public/profile.html")