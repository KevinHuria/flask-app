from app import app

from flask import render_template

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/jinja")
def jinja():

    my_name= 'Kevin'
    return render_template("public/jinja.html",my_name=my_name)


@app.route("/about")
def about():
    return "<h1>About!</h1>"
