import requests
import json
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query?"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything?"

#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=64STML8PEQ2LX5SO
#https://newsapi.org/v2/everything?q=Tesla inc&searchIn=title&sortBy=popularity&apiKey=e29f948922c4491784f746ab138bbf50

stock_api_key = "64STML8PEQ2LX5SO"
news_api_key = "e29f948922c4491784f746ab138bbf50"
TWILIO_SID = 'AC4fd80c37f52efce85a2a705aeebef8bc'
TWILIO_TOKEN = 'ab2991db95fd389364b83b53d676baf5'

stock_parameters = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "sortBy" : "popularity",
    "apikey" : stock_api_key
}

news_paramters = {
    "q" : COMPANY_NAME,
    "searchIn" : "title",
    "apiKey" : "e29f948922c4491784f746ab138bbf50"

}

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()
daily_data = data["Time Series (Daily)"]
daily_data = [value for (key, value) in daily_data.items()]
yesterday_close = daily_data[0]["4. close"]
day_before_yesterday_close = daily_data[1]["4. close"]
print(yesterday_close, day_before_yesterday_close)

day_diff = (float(yesterday_close) - float(day_before_yesterday_close))
day_diff_change = (abs(day_diff) / float(yesterday_close)) * 100
print(day_diff_change)

up_down = None
if day_diff > 0:
    up_down = "🔼"
elif day_diff < 0:
    up_down = "🔽"

if day_diff_change > 5:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_paramters)
    articles = news_response.json()["articles"]
    #print(articles)
    three_articles = articles[:3]
    #print(three_articles)

    formatted_articles = [f"{STOCK_NAME}: {up_down}{day_diff_change}% \nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]

    client = Client(TWILIO_SID, TWILIO_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
            body= article,
            from_='+19206579927',
            to="+919082618043"
        )
        print(message.status)