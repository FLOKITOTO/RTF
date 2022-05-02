import os

SECRET_KEY = os.urandom(32)


basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

BDD_USER = 'Flokitoto'
BDD_PASS = 'HgnxrEU7i7ykP4r'
BDD_NAME = 'rtap'
BDD_PORT = 3306
BDD_HOST = 'rtap.mysql.database.azure.com'
# BDD_SSL = True

SQLALCHEMY_TRACK_MODIFICATIONS = False
