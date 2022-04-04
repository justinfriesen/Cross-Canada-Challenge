from flask import Blueprint, render_template, request, flash, redirect, url_for, jsonify
from flask_login import login_required, current_user ##need these because can only access home page when loggedin.
from .models import Team, User, Activity
from . import db


views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
@login_required
def home():
    team = Team.query.filter_by(id= current_user.team_name).first()
    return render_template("home.html", user=current_user, team=team)

@views.route("/team-standings")
@login_required
def team_standings():
    teams = Team.query.all()
    team = Team.query.filter_by(id= current_user.team_name).first()
    return render_template("team_standings.html", user=current_user, teams=teams, team=team)

@views.route("/team/<id>")
@login_required
def my_team(id):
    team = Team.query.filter_by(id=id).first()
    

    team_members = team.users
    

    
    return render_template("my_team.html", user=current_user, team=team, team_members=team_members)

@views.route("/submit-activity/", methods=['GET', 'POST'])
@login_required
def submit_activity():
    ##will need to make this with team captains, but people without team captain status will only see own activity.
    user = User.query.filter_by(id = current_user.id).first()
    team = Team.query.filter_by(id=current_user.team_name).first()
    activity = Activity.query.filter_by(user_id = current_user.id).all()
    last_activity = activity[-1]

    if request.method =='POST':
        activity = int(request.form.get('activity'))
        new_activity = Activity(amount=activity, team_name=team.id, user_id=user.id)
        db.session.add(new_activity)
        db.session.commit()
        return redirect(url_for("views.submit_activity"))
    
    return render_template("submit_activity.html", user=current_user, team=team, activity=activity, last_activity=last_activity)
