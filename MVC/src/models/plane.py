from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plane(db.Model):

    __tablename__ = 'plane'
   
    reg_number = db.Column(db.String(120))
    aircraft_icao = db.Column(db.String(120))
    id = db.Column(db.Int, primary_key=True) #CHECK opé ici

    @property
    def serialize(self):
        return {
            'reg_number': self.reg_number,
            'aircraft_icao': self.aircraft_icao,
            'id': self.id,
        }
