import requests
from datetime import datetime

USERNAME = "xcrs"
TOKEN = "Xcrstheman@legend"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_parms = {
    "token" : TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes",
}

# # response = requests.post(url=pixela_endpoint, json=user_parms)
# # print(response.text)

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"

graph_config = {
    "id" : GRAPH_ID,
    "name" : "Walking graph",
    "unit" : "Km",
    "type" : "float",
    "color" : "shibafu"  
}

headers = {
    "X-USER-TOKEN" : TOKEN
}

# reposne = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(reposne.text)
today = datetime.now()
# today = datetime(year=2023, month=9, day=16)
# print(today.strftime("%Y%m%d"))
pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

pixel_config = {
    "date" : today.strftime("%Y%m%d"),
    "quantity" : input("How many kilometers did you walk today? "),
    #"optionalData" : {"Steps" : "4,111", "Activity cal" : "494"}
    }

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

delete_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/20230916"

response = requests.delete(url=delete_endpoint, headers=headers)

