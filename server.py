from flask import Flask
from webapp import app
from webapp import db

#init db
db.init_app(app)
with app.app_context():
    db.create_all()

app.run(host="realstateproject.com", port=8500, debug=True)
