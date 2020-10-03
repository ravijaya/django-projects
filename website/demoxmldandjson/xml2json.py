import xml.etree.ElementTree as et
from pprint import pprint as pp
from json import dump

etree = et.parse('test.xml')
content = []

for book_tag in etree.getroot():
    temp = {}
    temp['isbn'] = book_tag.get('isbn')
    temp[book_tag[0].tag] = book_tag[0].text
    temp['authors'] = [author.text for author in book_tag[1]]
    content.append(temp)

dump(content, open('test.json', 'w'), indent=2)
