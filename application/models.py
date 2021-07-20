from application import db

class Pilots(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    combat_level = db.Column(db.Integer())
    ship_id = db.Column(db.Integer())

class Ships(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(30))
    model = db.Column(db.String(30))

class Pilot_Ship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ship_name = db.Column(db.String(50))
    ship_id = db.Column(db.Integer())
    pilot_id = db.Column(db.Integer())
    armament_rating = db.Column(db.Integer())
    skin = db.Column(db.String(30))