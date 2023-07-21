# Weather App

## Description
Weather App is a simple web-based application that allows users to check the current weather for a specific city. The app uses the OpenWeatherMap API to fetch weather data and displays the city name, temperature, and weather description.

## Features
- User-friendly interface with a clean design.
- Real-time weather information for the entered city.
- Temperature displayed in Celsius units.

## Setup
To run the Weather App locally, follow these steps:

1. Clone the repository to your local machine
   
2. Obtain an API key from OpenWeatherMap:

Visit https://openweathermap.org/appid and sign up for a free account.
Once you have an account, go to the API Keys section and copy your API key.

3. Create a config.json file in the project directory and paste your API key:

{
  "api_key": "YOUR_OPENWEATHERMAP_API_KEY"
}

4. Start the Flask app:

python app.py

5. Open your web browser and visit http://localhost:5000 to access the Weather App.

## Usage

- Enter the name of the city you want to check the weather for in the input field.
- Click the "Submit" button to get the current weather information for that city.
- The app will display the city name, temperature, and weather description.




