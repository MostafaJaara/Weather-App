import os
import requests
import json
from flask import Flask, render_template, request


app = Flask(__name__)

API_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

config_file_path = os.path.join(os.path.dirname(__file__), 'config.json')
with open(config_file_path, 'r') as config_file:
    config = json.load(config_file)
API_KEY = config["api_key"]

def get_coordinates(city):
    geocoding_api_base_url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {"q": city, "limit": 1, "appid": API_KEY}

    response = requests.get(geocoding_api_base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data and len(data) > 0:
            return data[0]["lat"], data[0]["lon"]
    return None, None

def get_weather_data(city):
    lat, lon = get_coordinates(city)
    if lat is None or lon is None:
        return None

    params = {"lat": lat, "lon": lon, "appid": API_KEY, "units": "metric"}
    weather_api_response = requests.get(API_BASE_URL, params=params)

    if weather_api_response.status_code == 200:
        return weather_api_response.json()
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    city = request.form.get("city")
    weather_data = None

    if city:
        weather_data = get_weather_data(city)

    return render_template("index.html", weather_data=weather_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
