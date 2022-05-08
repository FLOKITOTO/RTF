from flask import jsonify, request

from flask_sqlalchemy import SQLAlchemy

# from models.plane import Plane
# from models.flight import Flight

from utils.connect import Database
import logging as log

db = SQLAlchemy()

def store():
    db = Database.connect()
    cursor = db.cursor()
    req = request.json["response"]
    for i in req:
        try:
            plane = "INSERT INTO `plane` (aircraft_icao, reg_number, lng, lat) VALUES ('{}', '{}', '{}', '{}')".format(i["aircraft_icao"], i["reg_number"],i["lng"],i["lat"])
        except Exception as e:
             print("failed")

    cursor.execute(plane)
    
    db.commit()
    cursor.close()
    return jsonify(req)



def show():
    db = Database.connect()
    cursor = db.cursor()
    plane = "SELECT * FROM `plane`;"
    log.info('Reading Datas')
    cursor.execute(plane)
    output = cursor.fetchall()
    return jsonify(output)

