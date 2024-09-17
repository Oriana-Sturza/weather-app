
---

### **3. Weather App**

```python
import requests

# API configuration
API_KEY = "your_openweathermap_api_key"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city):
    """
    Fetches weather data for a given city using the OpenWeatherMap API.
    Args:
        city (str): The name of the city to get weather for.
    """
    try:
        url = BASE_URL + "appid=" + API_KEY + "&q=" + city
        response = requests.get(url)
        data = response.json()

        if data["cod"] != "404":
            weather_info = data["main"]
            temperature = weather_info["temp"]
            pressure = weather_info["pressure"]
            humidity = weather_info["humidity"]
            weather_desc = data["weather"][0]["description"]

            # Display the weather details
            print(f"\nTemperature: {temperature} K")
            print(f"Atmospheric Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
            print(f"Description: {weather_desc.capitalize()}")
        else:
            print("City not found.")
    except Exception as e:
        print(f"Error occurred: {e}")

def main():
    """
    Main function to handle user input and display weather information.
    """
    while True:
        city = input("Enter city name (or type 'quit' to exit): ").strip()
        if city.lower() == "quit":
            break
        get_weather(city)

if __name__ == "__main__":
    main()
