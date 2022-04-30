from msilib.schema import Error
from flask import Flask, request, jsonify, json, Response
import pymysql
import logging as log


api = Flask(__name__)


def connect():
    db = pymysql.connect(database='rtap',port=3306, host='rtap.mysql.database.azure.com', user='Flokitoto', password='HgnxrEU7i7ykP4r',ssl_ca="{ca-cert filename}", ssl_disabled=True)
    log.basicConfig(level=log.DEBUG, format='%(asctime)s %(levelname)s:\n%(message)s\n')              
    print("Connexion réussie")
    return db


@api.route('/')
def base():
    return jsonify({"version":"1.0"})

@api.route('/azure/plane', methods=['GET'])
def read():
    db = connect()
    cursor = db.cursor()
    plane = "SELECT * FROM `plane`;"
    log.info('Reading Datas')
    cursor.execute(plane)
    output = cursor.fetchall()
    return jsonify(output)


@api.route('/azure', methods=['POST'])
def write():
    db = connect()
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



if __name__=='__main__':
    api.run(debug=True, port=5000, host='0.0.0.0')