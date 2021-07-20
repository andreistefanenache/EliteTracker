from werkzeug.utils import redirect
from application import app, db
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')