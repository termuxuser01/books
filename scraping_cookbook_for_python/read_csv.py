import csv
import requests

planets_data = requests.get('http://0.0.0.0/planets.csv').text
planets = planets_data.split()

reader = csv.reader(planets, delimiter=',', quotechar='"')

lines = [line for line in reader][:-1]

for line in lines: print(line)