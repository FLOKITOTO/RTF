from flask import jsonify, request

from flask_sqlalchemy import SQLAlchemy
from utils.connect import Database
import logging as log

db = SQLAlchemy()

def store():
    db = Database.connect()
    cursor = db.cursor()
    req = request.json["response"]
    for i in req:
        try:
            plane = "INSERT INTO `plane` (aircraft_icao, reg_number) VALUES ('{}', '{}')".format(i["aircraft_icao"], i["reg_number"])
            cursor.execute(plane)
            flight = "INSERT INTO `flight` (lng, lat, id_plane) VALUES ({},{},{})".format(i["lng"],i["lat"], cursor.lastrowid)
            cursor.execute(flight)

        except Exception as e:
             print(e)
        

    cursor.close()
    db.commit()
    return jsonify(req)

def show():
    db = Database.connect()
    cursor = db.cursor()
    plane = "SELECT * FROM `plane`;"
    log.info('Reading Datas')
    cursor.execute(plane)
    output = cursor.fetchall()
    print(plane)
    return jsonify(output)

def update():
    db = Database.connect()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `plane`;")
    planes = cursor.fetchall()
    req = request.json["response"]
    for i in req:
        try:
            for plane in planes:
                if(i["reg_number"] == plane[2]): 
                    update = "UPDATE `flight` SET lat = {}, lng = {} WHERE `id_plane` = {}".format(i["lat"], i["lng"],plane[0])
                    cursor.execute(update)
        except Exception as e:
            print(e)
 
    cursor.close()
    db.commit()
    return jsonify(req)
