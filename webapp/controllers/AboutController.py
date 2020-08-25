"""MODULES FLASK"""
from webapp import app
from flask import render_template, redirect, url_for, request, session, flash

@app.before_request
def before_request():  
    pass

#route home
@app.route('/about', methods = ['GET'])
def about():
    title = 'Urban Ithaca'
    heading_text = 'About Us'
    return render_template('public_about/index.html.j2', title = title, heading_text = heading_text)
