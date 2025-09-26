import os
import requests
from flask import Flask, render_template, request, abort
from dotenv import load_dotenv
# Triggering a new deployment

# This line loads the API key from your .env file for local testing
load_dotenv()

app = Flask(__name__)

def get_weather_data(city):
    # This gets the API key from the environment (works both locally and in Azure)
    API_KEY = os.getenv('WEATHER_API_KEY')
    
    # If the key isn't set, the app will show an error
    if not API_KEY:
        abort(500, description="Weather API Key is not configured.")

    # This is the URL for the OpenWeatherMap API
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={API_KEY}'
    
    # This sends the request to the API
    response = requests.get(url)
    
    # If the city is not found, the API returns a 404 error
    if response.status_code == 404:
        return None
        
    # This will raise an error for other issues (like an invalid API key)
    response.raise_for_status()
    
    # This returns the weather data as a JSON object
    return response.json()

@app.route('/')
def index():
    # This function renders the main page with the search form
    return render_template('index.html')

@app.route('/weather', methods=['POST'])
def get_weather():
    # This gets the city name the user typed into the form
    city = request.form['city']
    
    # Basic check to ensure the user typed something
    if not city:
        return render_template('index.html', error="City name cannot be empty.")

    # Call the function to get the weather data
    weather_data = get_weather_data(city)

    # If the city wasn't found, show an error on the home page
    if not weather_data:
        return render_template('index.html', error=f"Could not find weather for '{city}'. Please try again.")

    # If data is found, show the results on the weather.html page
    return render_template(
        'weather.html',
        title=weather_data["name"],
        temp=f"{weather_data['main']['temp']:.1f}",
        description=weather_data["weather"][0]["description"].title(),
        humidity=weather_data["main"]["humidity"],
        wind_speed=f"{weather_data['wind']['speed']:.1f}"
    )

if __name__ == '__main__':
    app.run(debug=True)