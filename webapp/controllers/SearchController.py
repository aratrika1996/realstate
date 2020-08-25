"""MODULES FLASK"""
from webapp import app
from flask import render_template, redirect, url_for, request, session, flash

@app.before_request
def before_request():  
    pass

#route home
@app.route('/search', methods = ['GET'])
def search():
    title = 'Urban Ithaca'
    heading_text = 'Urban Ithaca'
    return render_template('public_search/index.html.j2', title = title, heading_text = heading_text)