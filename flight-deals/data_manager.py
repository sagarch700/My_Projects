from pprint import pprint
import requests

SHEETY_ENDPOINT = "https://api.sheety.co/0251194048dd5beab7c98ed94381a534/flightDeals/prices"

class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # use sheety get API to get all the data from the google sheet
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        #pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)

