"""
The goal of this project is to track who is in space and the ISS as it blips across Earth.

Works Cited: https://projects.raspberrypi.org/en/projects/where-is-the-space-station/2
Map courtesy of NASA
"""

import json
import turtle
import urllib.request

url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

print(result)

print("People in Space: ", result["number"])

people = result["people"]

for p in people:
    print(f'{p["name"]} is in the {p["craft"]}.')

url_2 = "http://api.open-notify.org/iss-now.json"
response_2 = urllib.request.urlopen(url_2)
result_2 = json.loads(response_2.read())

print(result_2)

location = result_2["iss_position"]
lat = float(location["latitude"])
lon = float(location["longitude"])

print("Latitude: ", lat)
print("Longitude: ", lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic("map.gif")

screen.register_shape("iss.gif")
iss = turtle.Turtle()
iss.shape("iss.gif")
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)


