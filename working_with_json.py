import json
from storing_data import get_planet_data

planets = get_planet_data()
print(json.dumps(planets, indent=4))

with open('./planets.json', 'w+') as f:
    json.dump(planets, f, indent=4)

# json can also read from json webfiles
import requests

r = requests.get('http://0.0.0.0/planets.json')
print(json.loads(r.text))