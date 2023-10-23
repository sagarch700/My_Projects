import requests
import datetime
import json

GENDER = "Male"
WEIGHT_KG = 96
HEIGHT_CM = 187
AGE = 29

API_ID = "55e01a2a"
API_key = "539dee6af8c89176e51cdd74c06abad4"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/0251194048dd5beab7c98ed94381a534/myWorkouts/workouts"

exercise_input = input("Tell me which exercise you did today: ")

headers = {
    "x-app-id" : API_ID,
    "x-app-key" : API_key
}

parameters = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
# print(result)

today_date = datetime.datetime.now()
today_date = today_date.strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)

