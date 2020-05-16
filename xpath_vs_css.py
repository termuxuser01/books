import requests
from lxml import html

html_planets = requests.get('http://0.0.0.0/planets.html').text
tree = html.fromstring(html_planets)

# select all tr elments with class planets and return tuple with their names
tr = [(v, v.xpath('@name')) for v in tree.cssselect('tr.planet')]

for p in tr:
    print(p)

# finding data for earth
tr = tree.cssselect("tr#planet3")
print(tr[0], tr[0].xpath("./td[2]/text()")[0].strip())

# Use an attribute with a specific value
tr = tree.cssselect("tr[name='Pluto']")
print(tr[0], tr[0].xpath("./td[2]/text()")[0].strip())