from flask import Flask, render_template, request
from dotenv import load_dotenv
import os
import requests


load_dotenv()

app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def weather():

    url = 'http://api.weatherapi.com/v1/current.json?key={}&q={}&aqi=no'
    API_KEY = os.getenv('WEATHER_API_KEY')


    city = 'Kolkata'
    if request.method == 'POST':
        city = request.form.get('city')

    r = requests.get(url.format(API_KEY,city)).json()

    if 'error' in r:
        return render_template('index.html', error = r['error']['message'])
    
    city_weather = {
        'city' : city,
        'temperature' : r['current']['temp_c'],
        'description' : r['current']['condition']['text'],
        'icon' : r['current']['condition']['icon']
    }

    return render_template('index.html', city_weather = city_weather)

if __name__ == '__main__' : app.run(debug = True)