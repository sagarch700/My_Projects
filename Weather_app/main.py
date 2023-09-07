import requests
import datetime
from twilio.rest import Client


present_day = datetime.datetime.now()
PRESENT_DATE = present_day.day
FLAG = False

api_key = input("Enter your Api_key: ")
weather_dict = {}
own_endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
parameters = {
    "lat" : 17.663309,
    "lon" : 83.219050,
    "appid" : api_key,
    "units" : "metric"
}

response = requests.get(url= own_endpoint, params=parameters)
response.raise_for_status()
data = response.json()

for i in data["list"]:
    key = i["dt_txt"]
    value = i["weather"][0]["id"]
    weather_dict[key] = value



for key, value in weather_dict.items():
    if value >= 500 and value <= 600:
            time = int(key.split(" ")[1].split(":")[0])
            date = int(key.split(" ")[0].split("-")[2])
            print(time, date)
            if time >= 9 and time <= 20 and date == PRESENT_DATE:
                 FLAG = True

account_sid = 'AC4fd80c37f52efce85a2a705aeebef8bc'
auth_token = input("Enter the auth_token: ")
reciever_number = input("Enter the number of reciever in the format +(code)(number) for e.g: +912222222222: ")
client = Client(account_sid, auth_token)

if FLAG:
    message = client.messages.create(
        body="it is going to rain today, carry umbrella with you",
        from_='+19206579927',
        to=reciever_number
        )

    print(message.status)
                 


