import requests
from scrapy.selector import Selector

a = '#' * 50

# retreive most recent questions from slackoverflow
r = requests.get('http://stackoverflow.com/questions')

# now create a selector
selector = Selector(r)

summaries = selector.xpath('//div[@class="summary"]/h3')
print(summaries[0:5])
for s in summaries[0:5]:
    print(s)

question_title = [x.extract() for x in summaries.xpath('a[@class="question-hyperlink"]/text()')[0:10]]

print(a)
for q in question_title:
    print(q)