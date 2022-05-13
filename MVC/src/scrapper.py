import requests
import json

class ScraperSQL:
    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}
        self.urlConnectStr = "http://localhost:5000/plane/update"
        self.req = requests.get('https://airlabs.co/api/v9/flights?api_key=7d20049f-9fa2-41ac-82dd-60023d4b5058&_fields=reg_number,aircraft_icao,lng,lat')

    def response_s(self):
        response = requests.put(self.urlConnectStr, json = json.loads(self.req.content))
        print(response)

    

while True:
    execute = ScraperSQL()
    execute.response_s()
    time.sleep(20)
    print("20 seconds okay that refresh")

        
