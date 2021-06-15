from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1> Home Page</h1>"

@views.route('/about')
def about():
    return "<h1> About Page</h1>"