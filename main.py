import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("api_key", 'r').read()
CITY = "Odessa"

if __name__ == '__main__':
    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
    response = requests.get(url).json()
    for s in response:
        print(s)
