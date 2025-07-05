import os
from weather.fetch import get_weather
from weather.utils import format_weather

def main():
    city = input("Enter city name: ")
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        print("❌ Please set your OPENWEATHER_API_KEY environment variable.")
        return
    try:
        weather_data = get_weather(city, api_key)
        print(format_weather(weather_data))
    except Exception as e:
        print("Error fetching weather:", e)

if __name__ == "__main__":
    main()
