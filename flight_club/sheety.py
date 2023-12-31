import requests

SHEETY_API_ENDPOINT = "https://api.sheety.co/0251194048dd5beab7c98ed94381a534/flightDeals/users"

def post_new_row(first_name, last_name, email):

    new_data = {
        "user" : {
            "first" : first_name,
            "last" : last_name, 
            "email" : email
        }
    }

    response = requests.post(url= SHEETY_API_ENDPOINT, json=new_data)
    response.raise_for_status()
    print(response.text)

