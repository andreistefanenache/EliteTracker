from werkzeug.utils import redirect
from application import app, db
from application.models import Pilots, Ships, Pilot_Ship
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')