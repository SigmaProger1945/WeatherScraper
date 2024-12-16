import requests
from translate import Translator

key = 'dc16f30bcf50f83d5b2c9ad10fe9c8e0'
class Location:
    name = ''
    latitude = 0
    longtitude = 0
    def __init__(name, lat, lon):
        pass
kyiv = [50.44870892818473, 30.525467078790278]
lviv = [49.8401884639178, 24.03454924068941]
yasenuza = [49.19366395791635, 23.16307749825465]
locations = [kyiv, lviv, yasenuza]
str_locations = ['Києві', 'Львові','Ясениці']
for i in range(len(locations)):
    req = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?lat={locations[i][0]}&lon={locations[i][1]}&appid=dc16f30bcf50f83d5b2c9ad10fe9c8e0')
    if req.status_code != 200:
        print(req.status_code)

    resp = req.json()
    data = resp['list'][0]
    temp = round(data['main']['temp'] - 273.15)
    temp_min = round(data['main']['temp_min'] - 273.15)
    temp_max = round(data['main']['temp_max'] - 273.15)
    feel_temp = round(data['main']['feels_like'] - 273.15)
    # rain = data['weather'][0]['main']
    clouds = data['weather'][0]['description']
    wind = data['wind']['speed']

    translator = Translator(to_lang="ru")
    clouds_ua = translator.translate(clouds)
    print(f"Погода у {str_locations[i]}: Температура: {temp}, Відчувається як: {feel_temp}, Швидкість вітру: {wind}м/с, {clouds_ua}")