import requests
from lxml import html

planet_url = 'http://0.0.0.0:8000/planets.html'
html1 = requests.get(planet_url).text

# load html into a lxml etree
tree = html.fromstring(html1)

# use xpath to find all tr in table
for t in [tr for tr in tree.xpath('/html/body/div/table/tr')]:
    print(t)
    
# if there were other div elements und body the query table/tr would be done on those divs aswell

# convert element objects to string
from lxml import etree

for t in [etree.tostring(tr)[:45].strip() for tr in tree.xpath('/html/body/div/table/tr')]:
    print(t)

a = "#" * 60
print(a)
# find only tr with class=planet
for t in [etree.tostring(tr)[:45] for tr in tree.xpath("/html/body/div/table/tr[@class='planet']")]:
    print(t)

# only search in the first div element
# indexing in xpath starts at 1
print(a)
for t in [etree.tostring(tr)[:45] for tr in tree.xpath("/html/body/div[1]/table/tr")]:
    print(t)

# the second div has id footer, we can also use this to select it
print(a)
for t in [etree.tostring(tr)[:45] for tr in tree.xpath("/html/body/div[@id='footer']/table/tr")]:
    print(t)

# get all planets but exclude earth
print(a)
for t in [etree.tostring(tr)[:45] for tr in tree.xpath("/html/body/div[1]/table/tr[@name!='Earth']")]:
    print(t)

# use position() to skip first row
print(a)
for t in [etree.tostring(tr)[:45] for tr in tree.xpath("/html/body/div/table/tr[position() > 1]")]:
    print(t)

print(a)
for t in [etree.tostring(tr)[:45] for tr in tree.xpath("/html/body/div/table/tr[position() > 2]")]:
    print(t)

# navigate to parent
print(a)
for t in [etree.tostring(tr)[:45] for tr in tree.xpath("/html/body/div/table/tr/parent::*")]:
    print(t)

# the same but return only table parent element
print(a)
for t in [etree.tostring(tr)[:45] for tr in tree.xpath("/html/body/div/table/tr/parent::table")]:
    print(t)

print(a)
# getting a specific parent
for t in [etree.tostring(tr)[:45] for tr in tree.xpath("/html/body/div/table/tr/parent::table[@id='footerTable']")]:
    print(t)

print(a)
# get mass of earth
earth_mass = tree.xpath("/html/body/div/table/tr[@name='Earth']/td[3]/text()")[0].strip()
print(earth_mass)