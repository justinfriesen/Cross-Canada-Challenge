from re import A
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
    teams = Team.query.all()
    locations = [
      ["Victoria", 48.428406, -123.365387, 7247],
      ["Vancouver", 49.282945, -123.121194, 7106],
      ["Kamloops", 50.674561, -120.327341, 6753],
      ["Calgary", 51.044724, -114.071831, 6138],
      ["Medicine Hat", 50.034502, -110.703889, 5845],
      ["Regina", 50.445299, -104.618991, 5367],
      ["Winnipeg", 49.895073, -97.138443, 4794],
      ["Thunder Bay", 47.570335, -52.697437, 4117],
      ["Matheson", 48.533765, -80.463990, 3304],
      ["Montreal", 45.499871, -73.568940, 2537],
      ["Riviere-du-Loup", 47.836216, -69.537106, 2110],
      ["Moncton", 46.086575, -64.780316, 1557],
      ["North Sydney", 46.206392, -60.252124 ,1082],
      ["Channel-Port aux Basques", 47.579503, -59.141799, 904],
      ['Sheppardville', 49.451462, -56.432671, 550],
      ['St Johns', 47.561068, -52.712285, 0]]

    return render_template("home.html", user=current_user, team=team, teams=teams, locations=locations)

@views.route("/maps/<team_id>", methods=['POST'])
@login_required
def map_info(team_id):
    team = Team.query.filter_by(id=current_user.team_name).first()
    teams = team.query.all()
    team_names = list(map(lambda x: x.name, teams))

    print(team_names)

    activity = Activity.query.filter_by(team_name=team.id).all()

    activity_amount = sum(list(map(lambda x: x.amount, activity)))
    print(activity_amount)
    print(activity)

    locations = [
      ["Victoria", 48.428406, -123.365387, 7247],
      ["Vancouver", 49.282945, -123.121194, 7106],
      ["Kamloops", 50.674561, -120.327341, 6753],
      ["Calgary", 51.044724, -114.071831, 6138],
      ["Medicine Hat", 50.034502, -110.703889, 5845],
      ["Regina", 50.445299, -104.618991, 5367],
      ["Winnipeg", 49.895073, -97.138443, 4794],
      ["Thunder Bay", 47.570335, -52.697437, 4117],
      ["Matheson", 48.533765, -80.463990, 3304],
      ["Montreal", 45.499871, -73.568940, 2537],
      ["Riviere-du-Loup", 47.836216, -69.537106, 2110],
      ["Moncton", 46.086575, -64.780316, 1557],
      ["North Sydney", 46.206392, -60.252124 ,1082],
      ["Channel-Port aux Basques", 47.579503, -59.141799, 904],
      ['Sheppardville', 49.451462, -56.432671, 550],
      ['St Johns', 47.561068, -52.712285, 0]]



    return jsonify({"amount": activity_amount, "locations":locations})


@views.route("/team-standings")
@login_required
def team_standings():
    team = Team.query.filter_by(id= current_user.team_name).first() ##to be able to access My_Team from nav bar.
    teams = Team.query.all()
    
    activity = Activity.query.all()
    
    return render_template("team_standings.html", user=current_user, teams=teams, team=team, activity=activity)

@views.route("/team/<id>")
@login_required
def my_team(id):
    team = Team.query.filter_by(id=id).first()
    

    team_members = team.users
    print (team_members)
    

    
    return render_template("my_team.html", user=current_user, team=team, team_members=team_members)

@views.route("/submit-activity/", methods=['GET'])
@login_required
def submit_activity():
    ##will need to make this with team captains, but people without team captain status will only see own activity.
    user = User.query.filter_by(id = current_user.id).first()
    team = Team.query.filter_by(id=current_user.team_name).first()
    activity = Activity.query.filter_by(user_id = current_user.id).all()
    members = team.users

     ##have to think about case of no prior activities logged for team. Must check if list is empty first.

    if len(activity) == 0:
        last_activity = activity
    
    if len(activity) > 0:
        last_activity = activity [-1]
    
    return render_template("submit_activity.html", user=current_user, team=team, activity=activity, last_activity=last_activity, members=members)

@views.route("/submit/<member_id>", methods=['POST'])
@login_required
def submit_activity_team_captain(member_id):
    ##will need to make this with team captains, but people without team captain status will only see own activity.
    team = Team.query.filter_by(id=current_user.team_name).first()
    members = team.users

    

    days_to_weeks_in_may = 31/7
    hours_per_week = 3
    activity_hours_per_month = days_to_weeks_in_may*hours_per_week
    cross_canada_distance = 7560
    point_amount_per_individual = cross_canada_distance/activity_hours_per_month

    point_amount_for_team = round(point_amount_per_individual/len(team.users), 2)


    if request.method =='POST': ##have to have setting for team captain submitting activities. Makes form all weird.
        activity = int(request.form.get('activity'))
        new_activity = Activity(amount=activity*point_amount_for_team, team_name=team.id, user_id=member_id)
        db.session.add(new_activity)
        db.session.commit()
        return redirect(url_for("views.submit_activity"))
    
    
