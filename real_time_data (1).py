from geopy.geocoders import Nominatim
import requests
import json
geolocator = Nominatim(user_agent="forestfireapp")
forest = input("Enter name of Forest: ").strip()
location = geolocator.geocode({forest})
res = requests.get(f'https://api.darksky.net/forecast/1c9424849fc849dc22a73f5c96032111/{location.latitude},{location.longitude}')
json_data = json.loads(res.text)

#---------------Print Real-Time Data--------------#
for key,value in json_data['currently'].items():
    print(key,' -> ',value)
