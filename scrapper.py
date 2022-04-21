import pymysql
import logging as log
import requests
import json
from flask import request


class ScraperSQL:
    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}
        self.urlConnectStr = "http://localhost:5000/get"
        self.req = requests.get('https://airlabs.co/api/v9/flights?api_key=7d20049f-9fa2-41ac-82dd-60023d4b5058&_fields=reg_number,aircraft_icao')

    def response_s(self):
        response = request.post(self.urlConnectStr, self.req)
        print(response.text)



execute = ScraperSQL()
execute.response_s()

        # request.post('http://127.0.0.1:5000/post', json = {"id": 1, "marque" : paires_marque[1].text, "modele" : paires_modele[1].text, "prix" : paires_prix[1].text}) 
        