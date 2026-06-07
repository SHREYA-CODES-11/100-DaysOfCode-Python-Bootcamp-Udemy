# Day 33
# API Endpoints & API Paramters - ISS Overhead Notifier
"""An Application Programming Interface (API) is a set of commands,
functions, protocols, and objects that programmers can use to
create software or interact with an external system."""

# import requests
"""If there is a spell error in the url that means the thus given url doesn't even exist,
so it will return 404 response code."""
# response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# # print(response)
# # print(response.status_code)

# # if response.status_code != 200:
# #     # print("Error!")
# #     raise Exception("Bad response from ISS API")

# # if response.status_code == 404:
# #     raise Exception("That resource does not exist.")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorised to access this data.")

# response.raise_for_status()

# data = response.json()
# # data = response.json()["iss_position"]["longitude"]
# print(data)

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)
# print(iss_position)

import requests
from datetime import datetime

MY_LAT = 51.507351
MY_LONG = -0.127758

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0, # off or false
}

response = requests.get("https://api.sunrise-sunset.org/json", params = parameters)
response.raise_for_status()
data = response.json()
# print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

# print(sunrise)
print(sunrise.split("T"))
print(sunrise.split("T")[1].split(":")[0])
# print(sunset)

time_now = datetime.now()
# print(time_now)
print(time_now.hour)