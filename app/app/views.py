from app import app

from flask import render_template, request, redirect


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
    if request.method == "POST":
        req = request.form
        username = req["username"]
        email=req.get("email")
        password=request.form["password"]

        print(username, email, password)

        return redirect(request.url)
    return render_template("public/sign_up.html")
