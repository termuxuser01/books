import csv
from storing_data import get_planet_data

planets = get_planet_data()

with open('./planets.csv', 'w+', newline='') as c:
    write = csv.writer(c)
    write.writerow(['Name', 'Mass', 'Radius', 'Description', 'MoreInfo'])
    for planet in planets:
        write.writerow([planet['name'], planet['mass'],planet['radius'], planet['description'], planet['moreinfo']])
