"""MODULES FLASK"""
from webapp import app
from flask import render_template, redirect, url_for, request, session, flash
import webapp.forms.LoginForm as form

"""DATABASES"""
from webapp.models.UserModel import UserModel as User

@app.errorhandler(404)
def error_404(e):
    return "Not found 404"

@app.errorhandler(500)
def error_500(e):
    return "Error 500, contact the administrator!"
@app.before_request
def before_request():  
    pass

#route index
@app.route('/', methods = ['GET','POST'])
def home():
    
    title = 'Dashboard'
    
    #get all
    users = User.query.all()

    return render_template('dash.html.j2', users = users)
