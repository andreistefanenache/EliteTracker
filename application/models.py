from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class Pilot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    combat_level = db.Column(db.String(15))
    pilot_ship = db.relationship('Pilot_ship', backref='pilot')

class Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(30))
    model = db.Column(db.String(30))
    pilot_ship = db.relationship('Pilot_ship', backref='ship')

class Pilot_Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ship_name = db.Column(db.String(50))
    ship_id = db.Column('ship_id', db.Integer, db.ForeignKey('ship.id'))
    pilot_id = db.Column('pilot_id', db.Integer, db.ForeignKey('pilot.id'))
    armament_rating = db.Column(db.Integer)
    skin = db.Column(db.String(30))

class AddPilotForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    combat_level = SelectField('Combat Level', choices=[('harmless', 'Harmless'), ('mostly_harmless', 'Mostly Harmless'), ('novice', 'Novice'), ('competent', 'Competent'), ('expert', 'Expert'), ('master', 'Master'), ('dangerous', 'Dangerous'), ('deadly', 'Deadly'), ('elite', 'Elite')])
    submit = SubmitField('Add Them!')

class AddShipForm(FlaskForm):
    make = StringField('Make')
    model = StringField('Model')
    submit = SubmitField('Add It!')

class AddPilot_ShipForm(FlaskForm):
    ship_name = StringField('Ships Name')
    ship_id = SelectField('Their Ship')
    pilot_id = SelectField('The Pilot')
    armament_rating = IntegerField('How Dangerous?')
    skin = SelectField('Looks')
    