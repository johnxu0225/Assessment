import requests

# Constants for API access
API_KEY = "e8be4611b82248800a55bcb8e501fd2e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    """Fetches weather data for a given city from OpenWeatherMap API."""
    params = {

         #Query parameters sent with the GET request
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'
    }
    
    response = requests.get(BASE_URL, params=params)

    data = response.json()
    
    if response.status_code == 200:
        return {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]}
    else:
        return None
    

