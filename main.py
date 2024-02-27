from config import MY_LAT, MY_LONG
import requests

API_KEY = '21928f0cb32cdb4b2cec76361bd87a6c'

owm_endpoint = 'https://api.openweathermap.org/data/2.5/forecast'
parameters = {
    'lat': MY_LAT,
    'lon': MY_LONG,
    'appid': API_KEY,
    'cnt': 6
}

response = requests.get(owm_endpoint, params=parameters)
response.raise_for_status()
data = response.json()

will_rain = sum([i['weather'][0]['id'] < 700 for i in data['list']]) > 0

if will_rain:
    print('Bring your rain pants!')