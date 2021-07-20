from werkzeug.utils import redirect
from application import app, db
from application.models import Pilot, Ship, Pilot_Ship, AddPilotForm, AddShipForm, AddPilot_ShipForm
from flask import render_template

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_pilot', methods=['GET', 'POST'])
def add_pilot():
    form = AddPilotForm()
    if form.validate_on_submit():
        new_pilot = Pilot(name=form.name.data, combat_level=form.combat_level.data)
        db.session.add(new_pilot)
        db.session.commit()
        return render_template('index.html', message="Pilot Added!")
    else:
        return render_template('add_pilot.html', form=form)

@app.route('/pilots')
def pilots():
    pilots = Pilot.query.all()
    return render_template('pilots.html', pilots=pilots)