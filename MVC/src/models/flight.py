#from flask_sqlalchemy import SQLAlchemy
#from models.plane import Plane
#db = SQLAlchemy()

#class Flight(db.Model):

  #  __tablename__ = 'flight'
   
  #  long = db.Column(db.Float)
  #  lat = db.Column(db.Float)
 #   id_plane = db.Column(db.Int)
  #  id = db.Column(db.Int)
    #A REVOIR ICI FOREIGN KEY sur id_plane ET LA GESTION DES BLUEPRINTS
    #https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
    # ForeignKey('parent.id')

  ######  @property
 #####   def serialize(self):
  ####      return {
 #           'long': self.long,
   ###         'lat': self.lat,
   ##     }
