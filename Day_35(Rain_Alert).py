import requests

"""Sending message to oneself requires twilio api for that we would have 
to register and install the twilio package, and that i am not doing!"""

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "69f04e4613056b159c2761a9d9e664d2"

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params = weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["List"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["List"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella.") 