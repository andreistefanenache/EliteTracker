from application import app, db
from application.models import Pilot, Ship, Pilot_Ship, AddPilotForm, AddShipForm, AddPilot_ShipForm
from flask import render_template, redirect, url_for, request

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

@app.route('/add_ship', methods=['GET', 'POST'])
def add_ship():
    form = AddShipForm()
    if form.validate_on_submit():
        new_ship = Ship(make=form.make.data, model=form.model.data)
        db.session.add(new_ship)
        db.session.commit()
        return render_template('index.html', message="Ship Added!")
    else:
        return render_template('add_ship.html', form=form)

@app.route('/ships')
def ships():
    ships = Ship.query.all()
    return render_template('ships.html', ships=ships)

@app.route('/update_pilot/<name1>', methods=['GET', 'POST'])
def update_pilot(name1):
    form = AddPilotForm()
    pilot = Pilot(name=name1)
    if pilot:
        return render_template('update_pilot.html', pilot=pilot, form=form)
    else:
        return redirect('/pilots')

@app.route('/update_pilot2/<old>', methods=['POST'])
def update_pilot2(old):
    updated_pilot = Pilot(name=old)
    print(old)
    print(request)
    print(request.args)
    if request.args.get('name'):
        updated_pilot.name = request.args.get('name')
        updated_pilot.combat_level = request.args.get('combat_level')
        db.session.commit()
        return redirect('/pilots')
    else:
        return redirect('/')