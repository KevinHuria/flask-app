from app import app
from flask import render_template, url_for, redirect
from forms import SignUpform, LogInform

app.config['SECRET_KEY'] = '19a27057ac27ad42c9f047c62aeb6f15'


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/jinja")
def jinja():

    my_name = 'Kevin'
    return render_template("public/jinja.html", my_name=my_name)


@app.route('/about')
def about():
    return "<h1>About!</h1>"


@app.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    form = SignUpform()
    return render_template("public/sign_up.html", form=form)


@app.route('/logIn')
def LogIn():
    form = LogInform()
    return render_template('public/login.html', form=form)


@app.route("/profile/<username>")
def profile(username):
    return render_template("public/profile.html")
