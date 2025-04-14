weather_database = {
    "new york": {
        "temperature": 15,
        "condition": "Partly Cloudy",
        "humidity": 70
    },
    "london": {
        "temperature": 12,
        "condition": "Rainy",
        "humidity": 85
    },
    "tokyo": {
        "temperature": 22,
        "condition": "Sunny",
        "humidity": 60
    },
    "sydney": {
        "temperature": 25,
        "condition": "Clear",
        "humidity": 50
    },
    "paris": {
        "temperature": 18,
        "condition": "Cloudy",
        "humidity": 75
    }
}

def get_weather_for_city(city):
    city = city.lower()
    return weather_database.get(city)