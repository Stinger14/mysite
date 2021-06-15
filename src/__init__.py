from flask import Flask
from .views import views
from .auth import auth

def create_app():
    _app = Flask(__name__)
    _app.config['SECRET KEY'] = 'Maxsteel2!'

    _app.register_blueprint(views, url_prefix='/')
    _app.register_blueprint(auth, url_prefix='/')

    return _app

    