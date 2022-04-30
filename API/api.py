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

@api.route('/azure', methods=['GET'])
def read():
    db = connect()
    log.info('Reading Datas')
    plane = "SELECT * FROM `plane`;"
    cursor = db.cursor()
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
 





































# @api.route('/post', methods=['POST'])
# def post_one():
#     db = connect()
#     model = request.json['aircraft_icao']
#     numAvion = request.json['reg_number']
    
#     req = requests.get('https://airlabs.co/api/v9/flights?api_key=7d20049f-9fa2-41ac-82dd-60023d4b5058&_fields=reg_number,aircraft_icao')

#     avion = "INSERT INTO `avion` (model, numAvion) VALUES ('" +model+"','"+numAvion+"');"
#     cursor = db.cursor()
#     cursor.execute(avion)
#     return jsonify({"aircraft_icao" : model, "reg_number" : numAvion})
    


# @app.route('/all', methods=['GET'])
# def get_all():
#     sql_0 = "SELECT * FROM `chaussure`;"
#     db = connection()
#     cursor = db.cursor()
#     cursor.execute(sql_0)
#     result = cursor.fetchall()
#     return jsonify(result)


# @ap.route('/post', methods=['POST'])
# def post_one():
#     db = connect()
#     id = request.json['id']
#     marque = request.json['marque']
#     modele = request.json['modele']
#     prix = request.json['prix']
#     sql_2 = "INSERT INTO `chaussure` (marque, modele, prix) VALUES ('" +marque+"','"+modele+"'," + str(prix) + ");"
#     cursor = db.cursor()
#     cursor.execute(sql_2)
#     return jsonify({"id" : id, "marque" : marque, "modele" : modele, "prix" : prix})


# def connection():
#     db = pymysql.connect(database='rtap', host='rtap.mysql.database.azure.com', user='Flokitoto', password='HgnxrEU7i7ykP4r')
#     log.basicConfig(level=log.DEBUG, format='%(asctime)s %(levelname)s:\n%(message)s\n')                             

#     print("Connexion réussie")
#     return db






# https://airlabs.co/api/v9/flights?_view=array&_fields=model&api_key=7d20049f-9fa2-41ac-82dd-60023d4b5058

# @app.route('/<id>', methods=['GET'])
# def get_one(id):
#     sql_1 = "SELECT * FROM `chaussure` WHERE id = " + id + ";"
#     db = connection()
#     cursor = db.cursor()
#     cursor.execute(sql_1)
#     result = cursor.fetchone()
#     return jsonify(result)

# @app.route('/delete/<id>', methods=['DELETE'])
# def delete_one(id):
#     sql_delete = "DELETE FROM `chaussure` WHERE id = " + id + ";"
#     db = connection()
#     cursor = db.cursor()
#     cursor.execute(sql_delete)
#     return jsonify({"deleted_succes" : id})
