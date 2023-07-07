from app.models import User, Post

from app import app
from flask import render_template, url_for, flash, redirect
from app.forms import RegistrationForm, LoginForm

posts = [
    {
        "author": "Pablo Martín Páez Gavira",
        "title": "Futbol Club Barcelona",
        "content": "Creative Playmaker",
        "date_posted": "July 1, 2021"
    },
    {
        "author": "Bastian Schweinsteiger",
        "title": "Fußball-Club Bayern München",
        "content": "Box-to-Box Player",
        "date_posted": "July 1, 1998"
    },
    {
        "author": "David Beckham OBE",
        "title": "Manchester United Football Club",
        "content": "Cross Specialist",
        "date_posted": "January 23, 1993"
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title='Register', form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "draxler@cmarkt.com" and form.password.data == "abcd":
            flash(f"You have been logged in, Julian!", "success")
            return redirect(url_for("home"))
        else:
            flash(f"Login unsuccessful. Please check username & password", "danger")

    return render_template("login.html", title='Login', form=form)

