from flask import jsonify, request

from flask_sqlalchemy import SQLAlchemy

from models.plane import Plane

from utils.connect import Database
import logging as log

db = SQLAlchemy()

def store():
    db = Database.connect()
    cursor = db.cursor()
    req = request.json["response"]
    key = []
    for i in req:
        try:
            if (key==[]) :
                plane = "INSERT INTO `plane` (aircraft_icao, reg_number) VALUES ('{}', '{}')".format(i["aircraft_icao"], i["reg_number"])
                key.append(i["reg_number"])
            else:
                if(i["reg_number"] not in key) :
                    plane+= ", ('{}', '{}')".format(i["aircraft_icao"], i["reg_number"])
                    key.append(i["reg_number"])
          
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

