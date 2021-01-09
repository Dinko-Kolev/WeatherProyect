import datetime

import requests

from weather_app.models import City


def search_city_weather():
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=35b8b27127678a121511c2bd0af1f0a3'
    # city = 'Madrid'
    cities_database = City.objects.all()
    all_cities = []
    for city in cities_database:
        city_id = city.id
        city_weather = requests.get(
            url.format(city)).json()  # request the API data and convert the JSON to Python data types

        time = datetime.datetime.now()

        city = {
            'name': city,
            'temperature': round(float(city_weather['main']['temp'], )),
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon'],
            'time': f'{time.hour}:{time.minute}',
            'id': city_id,
        }
        all_cities.append(city)
    return all_cities
