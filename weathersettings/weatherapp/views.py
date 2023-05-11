import datetime

from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    api_key = '<YOUR API KEY>'

    if request.method == 'POST':
        city = request.POST['city']
        current_weather_url = ('https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city, api_key))
        response = requests.get(current_weather_url).json()

        # forecast_url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly&appid={}'.format(lat, lon, api_key)
        if response['cod'] == '404':
            pass
        else:
            weather_forecast = 'http://api.openweathermap.org/data/2.5/forecast?q={}&appid={}'.format(city, api_key)
            weather_forecast = requests.get(weather_forecast).json()
        # print(weather_forecast)

        n = response['cod']

        print(n)
        if n == '404':
            weather_data = {
                'city': city,
                'status': 'NOT AVAILABLE',
                'description': 'NOT AVAILABLE',
                'icon': 'NOT AVAILABLE',
                'temp': 'NOT AVAILABLE',

            }
            daily_forecast = []


        else:
            weather_data = {
                'city': city,
                'status': response['weather'][0]['main'],
                'description': response['weather'][0]['description'],
                'icon': response['weather'][0]['icon'],
                'temp': round(response['main']['temp'] - 273.5, 2),
            }

            daily_forecast =[]
            x = 0
            while x != 18 and n != '404':

                print(datetime.datetime.fromtimestamp(weather_forecast['list'][x]['dt']).strftime('%A'))
                print((weather_forecast['list'][x]['main']['temp'] - 273.5))
                print((weather_forecast['list'][x]['dt_txt']))
                print(weather_forecast['list'][x]['weather'][0]['icon'])
                x = x + 1

                daily_forecast.append({
                    'day': datetime.datetime.fromtimestamp(weather_forecast['list'][x]['dt']).strftime('%A'),
                    'temp1': round(weather_forecast['list'][x]['main']['temp'] - 273.5, 2),
                    'time': weather_forecast['list'][x]['dt_txt'],
                    'icon': weather_forecast['list'][x]['weather'][0]['icon']

                })

        # print(weather_forecast)

        return render(request, 'index.html', {'weather_data': weather_data, 'daily_data': daily_forecast}, )
    return render(request, 'index.html')
