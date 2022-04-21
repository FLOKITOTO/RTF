import requests
import json



class ScraperSQL:
    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}
        self.urlConnectStr = "http://localhost:5000/azure"
        self.req = requests.get('https://airlabs.co/api/v9/flights?api_key=7d20049f-9fa2-41ac-82dd-60023d4b5058&_fields=reg_number,aircraft_icao')

    def response_s(self):
        response = requests.post(self.urlConnectStr, json = json.loads(self.req.content))
        


execute = ScraperSQL()
execute.response_s()

        