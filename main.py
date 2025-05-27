import requests
import os

def get_weather(city):
    api_key = os.getenv("Weather_api")  # Uses environment variable
    if not api_key:
        raise Exception("API key not found in environment variables.")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f"Weather in {city}: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}°C")
    else:
        print(f"Error: {data.get('message', 'Failed to fetch weather')}")

if __name__ == "__main__":
    get_weather("Toronto")
