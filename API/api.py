from msilib.schema import Error
from flask import Flask, request, jsonify, json, Response
import psycopg2
import logging as log

    # db = pymysql.connect(database='rtap',port=3306, host='rtap.mysql.database.azure.com', user='Flokitoto', password='HgnxrEU7i7ykP4r',ssl_ca="{ca-cert filename}", ssl_disabled=True)
    # log.basicConfig(level=log.DEBUG, format='%(asctime)s %(levelname)s:\n%(message)s\n')
    # print("Connexion réussie")
    # return db
    
api = Flask(__name__)


def connect():
    db = psycopg2.connect(
    host="localhost",
    database="mabase",
    user="postgres",
    password="postgres"
    )
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
    sql = "INSERT INTO plane (reg_number) VALUES ('{}')".format('L410')
    # val = ('L410')
    cursor.execute(sql)
    db.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")
 
    log.info('Post Datas')

    print(sql)
    print(cursor.rowcount, "record inserted.")
    return jsonify(val)

if __name__=='__main__':
    api.run(debug=True, port=5000, host='0.0.0.0')


    # req = request.json["response"]
    # cursor.executemany("INSERT INTO `plane` (aircraft_icao, reg_number) VALUES (%s, %s);", req)
    # print(req)
    # key = []
    # for i in req:
    #     try:
    #         if (key==[]) :
    #             plane = "INSERT INTO `plane` (reg_number) VALUES ('{}')".format(i["reg_number"])
    #             key.append(i["reg_number"])
            # else:
            #     if(i["reg_number"] not in key) : #si la key na pas encore été utilisé, on peut ecrire la requette, sinon on ne fait rien
            #         plane+= ", ('{}', '{}')".format(i["reg_number"])
            #         key.append(i["reg_number"])
        # except Exception as e:
        #      print("failed")
    # print(plane)
    # cursor.execute(plane)
    # return jsonify(req)