from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


def create_app():
    app = Flask(__name__) #first thing to do when making flask app, name = mkodule we are running
    app.config['SECRET_KEY'] = "Justin"

    from .views import views #use .views because importing from python package, realtive import
    from .auth import auth

    app.register_blueprint(views, url_prefix="/") #urlprefix = all orutes inside of views, what will they be prefixed by? Do we want prefix to be/home/api? or just /home? We do not want url prefix.
    app.register_blueprint(auth, url_prefix="/")
 
    return app

#route = /home /page /profile they are endpoints we can go to.


    