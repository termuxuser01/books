import requests
from bs4 import BeautifulSoup

def get_planet_data():
    html = requests.get('http://0.0.0.0/planets.html').text
    soup = BeautifulSoup(html, 'lxml')

    def to_dict(tr):
        tds = tr.findAll('td')
        planet_data = dict()
        planet_data['name'] = tds[1].text.strip()
        planet_data['mass'] = tds[2].text.strip()
        planet_data['radius'] = tds[3].text.strip()
        planet_data['description'] = tds[4].text.strip()
        planet_data['moreinfo'] = tds[5].findAll('a')[0]["href"].strip()
        return planet_data

    planet_tr = soup.html.body.div.table.findAll('tr', {'class': 'planet'})

    planets = [to_dict(tr) for tr in planet_tr]

    return planets

if __name__ == '__main__':
    for data in get_planet_data():
        for k in data.keys():
            print(k, data[k])
