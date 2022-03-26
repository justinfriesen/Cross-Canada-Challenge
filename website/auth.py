from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import current_user, login_user, logout_user, login_required, current_user ##current_user allows us to access any info about user when they are logged in.
from werkzeug.security import generate_password_hash, check_password_hash ##in new_user variable in signup function below. We were trying to store password in plain text. This is no bueno. Need to hash the password. This is what this module is for.
from . import db
from .models import User

##request import is a variable will store all of the context related to a specific request

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password =request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password): #passing it hashed password first and then plain text password. 
                flash("Logged In", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
        
            else:
                flash('Password is incorrect', category='error')
        
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)

@auth.route("/sign-up", methods=['GET', 'POST'])
def sign_up():
    ##to get data in form use the variable below, enter the name of the item we are requesting from signup.html
    if request.method == 'POST': ##must see if user is creating account or is just requesting for HTML using GET. Must check what method we have.
      email =request.form.get("email")
      username =request.form.get("username")
      password1 =request.form.get("password1")
      password2 =request.form.get("password2")

      ##how to look into db to see if user already exists.
      email_exists = User.query.filter_by(email=email).first()#using .first guarantees we will find only instance of user with that email, if they exist.
      username_exists = User.query.filter_by(username=username).first()
      if email_exists: #means we cannot create account because this email exists.
          flash('Email is already in use.', category='error')
      elif username_exists:
          flash('Username has been taken', category='error')
      elif password1 != password2:
          flash("Password's do not match", category='error')
      elif len(username) < 2:
          flash('Username is too short', category='error')
      elif len(password1) < 6:
          flash('Password is too short', category='error')
      elif len(email) < 4:
          flash('Email is invalid', category='error')
          ##if we get none of these error messages, then we can create an account.
      else:
          new_user = User(email=email, username=username, password=generate_password_hash(password1, method='sha256'))##use the class we made (User) to make a new user, duh!!! ID will be auto created and same with time, do not need ot pass it into our class.
          ##at this point, user is still not in db. Below is how to add user to db.
          db.session.add(new_user) ##this preps it to be added to db.
          db.session.commit() ##this actually adds it to db. 
          login_user(new_user, remember=True)
          flash('User Created!')
          return redirect(url_for('views.home'))


    return render_template("signup.html", user=current_user) ##not post method. Just return signup html page.


##just GET request right now in auth. Get request is requesting something from the server. Method not allowed on sign-up because we have not defined that these routes can accpet post requests.
##POST request is the one that is typically used to send data to server from user. Some exceptions, but creating something new typically will send POst request. URL will lisgen for post request and then use it to create it
@auth.route("/logout")
@login_required ##login required decorator. It means that you can only access this function when login_user function has been used. Therefore, need to be loggedin to access logout function or route.
def logout():
    logout_user()
    return redirect(url_for("views.home")) #Saying views.hpme because we are refernecing views.home function. Redirect user to irl for views.home.