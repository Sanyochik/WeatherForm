import requests
import json

class weatherAPI():
    def getWeather(city):

        API_key = 'openweathermapkey'

        apiurl = f'http://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&appid={API_key}&units=metric'
        print(apiurl)
        response = requests.get(apiurl,timeout=20)
        data = response.json()
        if (response.status_code == 200):
            weather = f"Текущая температура в городе: {data['main']['temp']}"
        else:
            weather = 'Не удалось найти указанный вами город'
        return weather