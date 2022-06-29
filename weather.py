from urllib import response
import requests

API_KEY = "f1ec9bfd1dc24b5bf78ca296d7733b2d"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_ulr = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_ulr)

if response.status_code == 200:
    data = response.json()
    print(data)
    weather = data['weather'][0]['description']
    print("Weather is:", weather)
    temperature = round(data["main"]["temp"] - 273.15)
    print("Temperature is:",temperature, "celsius")
else:
    print("An error occurred.")
    