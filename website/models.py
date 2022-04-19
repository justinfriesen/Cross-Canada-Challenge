from email.policy import default
from time import timezone
from . import db ##dot is current package we are in. From Init.py file import db here.
from flask_login import UserMixin
from sqlalchemy.sql import func


##db.Model is a base class whichh is a database model. A model is a table. 
##Model of atable. Table has row + columns. New row = new user. 
##Every column is info related to each user. Define all columns that will be in user table.

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    users = db.relationship('User', backref='team', passive_deletes=True)
    activities = db.relationship('Activity', backref='team', passive_deletes=True)

    def __repr__(self):
        return f"team('{self.id}'), '{self.name}', '{self.users}' "


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) #first variable in db.Column, stating what data is stored in column, then state what type of key it is. Every db table you will need one column which is primary key. It is unique, what we will use to look up rows or users.
    email = db.Column(db.String(150), unique=True) #no users can have duplicate emails.
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    team_captain = db.Column(db.Boolean)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    team_name = db.Column(db.Integer, db.ForeignKey('team.id', ondelete="CASCADE"), nullable=False)
    activities = db.relationship('Activity', backref='user', passive_deletes=True)

    def __repr__(self):
        return f"user('{self.team_name}'), '{self.email}', '{self.password}' "

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    team_name = db.Column(db.Integer, db.ForeignKey('team.id', ondelete="CASCADE"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"), nullable=False)

