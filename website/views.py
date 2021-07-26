from flask import Blueprint, render_template, session, url_for, session, redirect

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('index.html')

@views.route('/login')
def login():
    return render_template('login.html')

@views.route('/logout')
def logout():
    return redirect(url_for("views.login"))

@views.route('/sign-up')
def signup():
    return render_template('signup.html')
