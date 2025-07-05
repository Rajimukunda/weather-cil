import requests

API_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city, api_key):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    return response.json()
