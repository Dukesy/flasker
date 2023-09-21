from flask import Flask, render_template

# Create a Flask instance
app = Flask(__name__)


# -----jinja2 filters-----

# safe
# capitalize
# lower
# upper
# title
# trim
# strimtags


# Create route decorator
@app.route('/')
def index():
    first_name = "Fred"
    stuff = "This is <strong>bold strong type</strong> text"
    favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)


@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name=name)


# Create Custom Error Pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
