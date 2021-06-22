from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('login')
def login():
    return "<p>Login</h1>"

@auth.route('logout')
def logout():
    return "<p>Logout</h1>"


@auth.route('sign-up')
def sigh_up():
    return "<p>Sigh Uup</h1>"
