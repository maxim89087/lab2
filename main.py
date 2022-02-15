import requests
city = "Moscow,RU"
appid = "241a53fd4a30449e2f512d23dd470a4b"
res = requests.get("http://api.openweathermap.org/data/2.5/weather",
params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Город:", city)
print("Погодные условия:", data['weather'][0]['description'])
print("Температура:", data['main']['temp'])
print("Минимальная температура:", data['main']['temp_min'])
print("Максимальная температура", data['main']['temp_max'])
print("Скорость ветра", data['wind']['speed'])
print("Видимость", data['visibility'])
print("____________________________")
res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
    print("Дата", i['dt_txt'], " \r\nТемпература ",i['main']['temp'],'°C'
          "\r\nПогодные условия", i['weather'][0]['description'],
            "\r\nСкорость ветра", i['wind']['speed'], 'м/c', "\r\nВидимость", i['visibility'], "метров")
print("____________________________")
