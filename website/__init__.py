from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) #first thing to do when making flask app, name = mkodule we are running
    app.config['SECRET_KEY'] = "Justin"

    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views #use .views because importing from python package, realtive import
    from .auth import auth

    app.register_blueprint(views, url_prefix="/") #urlprefix = all orutes inside of views, what will they be prefixed by? Do we want prefix to be/home/api? or just /home? We do not want url prefix.
    app.register_blueprint(auth, url_prefix="/")
    
    from .models import User ##must import User from .models. If we do not import user, when we create db it will nto create user table. Must import all models we want to be created before we created db so the db creates the models.

    
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.login" #If someone tries to access a page without being loggedin, they should be redirected to login page.
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    return app

#route = /home /page /profile they are endpoints we can go to.

#must actually create db, this function will create it.
def create_database(app):
    if not path.exists("website/" + DB_NAME): #path.exists seeing if path exists. If it does not exist, we will create it. Do DB_createll> pass app to it and it will make the db file for us. Then we print db. Not what you do in production code.
        db.create_all(app=app)
        print("Created database!")

    return app

#route = /home /page /profile they are endpoints we can go to.


    