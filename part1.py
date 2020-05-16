import requests
from bs4 import BeautifulSoup

a = '#' * 80

planet_url = "http://0.0.0.0/planets.html"
html = requests.get(planet_url)
soup = BeautifulSoup(html.text, "lxml")

#print the html as string
print(str(soup)[:100])

print(a)
#navigate to the div element
print(str(soup.html.body.div.table)[:100])

# retreive the first <tr> element
print(a)
print(str(soup.html.body.div.table.tr))

# Each node has both children and descendants. 
# Descendants are all the nodes underneath a given node 
# (event at further levels than the immediate children), while children are those that are a first level descendant. 
# The following retrieves the children of the table, which is actually a list_iterator object:
print(a)
print(soup.html.body.div.table.children)

#we can create a list of all the children
print(a)
children = [str(c)[:45] for c in soup.html.body.div.table.children]
print(children)

for c in children:
    print('child:')
    print(c)

# We can also get parent elements
print(a)
print(str(soup.html.body.div.table.tr.parent)[:200])
