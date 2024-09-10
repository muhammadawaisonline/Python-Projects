import requests

# Function to fetch weather data for a city using the OpenWeatherMap API
def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        # If city is not found
        if data.get('cod') != 200:
            print(f"City '{city}' not found.")
            return None

        # Extracting necessary data from the API response
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather
    except requests.exceptions.RequestException as e:
        print("Error connecting to the weather service.")
        print(e)
        return None

# Main function for the weather application
def weather_app():
    api_key = input("Enter your OpenWeatherMap API key: ").strip()

    while True:
        city = input("\nEnter city name (or 'q' to quit): ").strip()
        if city.lower() == 'q':
            print("Goodbye!")
            break

        weather = get_weather(city, api_key)

        if weather:
            print(f"\nWeather in {weather['city']}:")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Description: {weather['description']}")
            print(f"Humidity: {weather['humidity']}%")
            print(f"Wind Speed: {weather['wind_speed']} m/s")

# Run the weather application
weather_app()
