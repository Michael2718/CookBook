import requests
import datetime as dt

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open("api_key", 'r').read()
CITY = "Odessa"

if __name__ == '__main__':
    # CITY = input("Input City: ")

    url = BASE_URL + "appid=" + API_KEY + "&units=metric" + "&q=" + CITY
    response = requests.get(url).json()

    country = response['sys']['country']
    description = response['weather'][0]['description']
    temp = response['main']['temp']
    temp_feels_like = response['main']['feels_like']
    pressure = response['main']['pressure']
    humidity = response['main']['humidity']
    wind_speed = response['wind']['speed']

    current_time = dt.datetime.utcfromtimestamp(response['dt'] + response['timezone'])
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

    # Test printing
    print(f"Weather currently (at {current_time}) in {CITY} {country}: {description}")
    print(f"Temperature: {temp}°C feels like {temp_feels_like}°C")
    print(f"Pressure: {pressure} 1*10² Pa")
    print(f"Humidity: {humidity}%")
    print(f"Wind speed: {wind_speed} meter/sec")
    print(f"Sun rises at {sunrise_time}")
    print(f"Sun sets at {sunset_time}")
