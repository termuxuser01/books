import requests
from bs4 import BeautifulSoup

planet_url = 'http://0.0.0.0:8000/planets.html'
r = requests.get(planet_url)
html = r.text
a = '#' * 60
soup = BeautifulSoup(html, 'lxml')

# find first table element in document
table = soup.find('table')
print(str(table)[:100])

# find all tr in table element
tr = [str(tr)[:45] for tr in table.findAll('tr')]
print(a)
print(tr)

# get only tr with id planet3
planet3 = table.find("tr", {'id':'planet3'})
print(a)
print(str(planet3)[:45])

#get planet with name Venux
venus = table.find('tr', {'name':'Venus'})
print(str(venus)[:45])

print(a)
# get name and mass into a dictionary
planets = dict()
planet_row = table.findAll('tr', {'class':'planet'})
for p in planet_row:
    print('parsing:')
    print(p.findAll('td')[1].text.strip())
    planets[p.findAll('td')[1].text.strip()] = p.findAll('td')[2].text.strip()
print(planets)