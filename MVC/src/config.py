import os

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Connect to the database

BDD_USER = 'Flokitoto'
BDD_PASS = 'HgnxrEU7i7ykP4r'
BDD_NAME = 'rtap'
BDD_PORT = 3306
BDD_HOST = 'rtap.mysql.database.azure.com'
# BDD_SSL = True

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False