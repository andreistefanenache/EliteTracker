from flask_testing import TestCase
from flask import url_for

from application import app, db
from application.models import Pilot, Ship, PilotShip

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            WTF_CSRF_ENABLED=False
        )

        return app

    def setUp(self):
        db.create_all()

        db.session.add(Pilot(name="Dave", combat_level="competent"))
        db.session.add(Pilot(name="John", combat_level="harmless"))

        db.session.add(Ship(make="Fer De Lance", model="Anaconda"))
        db.session.add(Ship(make="Lakon Spaceways", model="Keelback"))

        db.session.add(PilotShip(ship_name="WaveRider", ship_id=1, pilot_id=1, armament_rating=5, skin="good"))
        db.session.add(PilotShip(ship_name="StarRider", ship_id=2, pilot_id=2, armament_rating=5, skin="bad"))

        db.session.commit()

    def tearDown(self):
        db.drop_all()


class TestRead(TestBase):
    def test_home(self):
        response = self.client.get(url_for('home'))

        assert "Welcome Commander" in response.data.decode()

    def test_pilots(self):
        response = self.client.get(url_for('pilots'))

        assert "Dave" in response.data.decode()
        assert "John" in response.data.decode()

    def test_ships(self):
        response = self.client.get(url_for('ships'))

        assert "Anaconda" in response.data.decode()
        assert "Keelback" in response.data.decode()

    def test_pilot_ship(self):
        response = self.client.get(url_for('ship_by_pilot', id=1))

        assert "WaveRider" in response.data.decode()

class TestCreate(TestBase):
    def test_add_pilot_non(self):
        response = self.client.get(url_for('add_pilot'))

        assert "- Add Pilot" in response.data.decode()

    def test_add_pilot(self):
        response = self.client.post(
            url_for('add_pilot'),
            data={"name": "Wayne", "combat_level": "elite"},
            follow_redirects=True
        )

        assert "Pilot Added!" in response.data.decode()

    def test_add_ship_non(self):
        response = self.client.get(url_for('add_ship'))

        assert "- Add Ship" in response.data.decode()

    def test_add_ship(self):
        response = self.client.post(
            url_for('add_ship'),
            data={"make": "Something", "model": "Wicked"},
            follow_redirects=True
        )

        assert "Ship Added!" in response.data.decode()

    def test_add_pilot_ship_non(self):
        response = self.client.get(url_for('add_pilot_ship'))

        assert "- Add Pilots Ship" in response.data.decode()

    def test_add_pilot_ship(self):
        response = self.client.post(
            url_for('add_pilot_ship'),
            data={"ship_name": "Enterprise", "ship_id": 2, "pilot_id": 2, "armament_rating": 10, "skin": "good"},
            follow_redirects=True
        )

        assert "Pilots Ship Added!" in response.data.decode()

class TestUpdate(TestBase):
    def test_update_pilot(self):
        response = self.client.get(url_for('update_pilot', name1="John"))

        assert "- update Pilot" in response.data.decode()

    def test_update_pilot2(self):
        response = self.client.post(
            url_for('update_pilot2', old="John"),
            data={"name": "James", "combat_rating": "harmless"},
            follow_redirects=True
        )

        assert "James" in response.data.decode()

    def test_update_ship(self):
        response = self.client.get(url_for('update_ship', make="Lakon Spaceways", model="Keelback"))

        assert "- Update Ship" in response.data.decode()

    def test_update_ship2(self):
        response = self.client.post(
            url_for('update_ship2', make="Lakon Spaceways", model="Keelback"),
            data={"make": "Testy", "model": "Testier"},
            follow_redirects=True
        )

        assert "Testy" in response.data.decode()

class TestDelete(TestBase):
    def test_delete_pilot(self):
        response = self.client.get(url_for('delete_pilot', name="Dave"))
        response2 = self.client.get(url_for('delete_pilot', name="Stacey"), follow_redirects=True)

        assert "Dave" not in response.data.decode()
        assert "John" in response2.data.decode()

    def test_delete_ship(self):
        response = self.client.get(url_for('delete_ship', make="Fer De Lance", model="Anaconda"))
        response2 = self.client.get(url_for('delete_ship', make="Stacey's", model="Mom"), follow_redirects=True)

        assert "Fer De Lance" not in response.data.decode()
        assert "Lakon Spaceways" in response2.data.decode()