from application import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, IntegerField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError
from wtforms_sqlalchemy.fields import QuerySelectField

class Pilot(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    combat_level = db.Column(db.String(15))
    pilotship = db.relationship('PilotShip', backref='pilot')

    def __repr__(self):
        return 'Choose {}'.format(self.name)

class Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(30))
    model = db.Column(db.String(30))
    pilotship = db.relationship('PilotShip', backref='ship')

    def __repr__(self):
        return 'Choose {}: {}'.format(self.make, self.model)

class PilotShip(db.Model):
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

def ship_query():
    return Ship.query

def pilot_query():
    return Pilot.query

class AddPilotShipForm(FlaskForm):
    ship_name = StringField('Ships Name')
    ship_id = QuerySelectField('Make/Model', query_factory=ship_query, allow_blank=True)
    pilot_id = QuerySelectField('The Pilot', query_factory=pilot_query, allow_blank=True)
    armament_rating = IntegerField('How Dangerous?')
    skin = SelectField('Looks', choices=[('good', 'Good'), ('bad', 'Bad'), ('meh', 'Meh')])
    submit = SubmitField('Add it!')
    