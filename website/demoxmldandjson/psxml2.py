import xml.etree.ElementTree as et

etree = et.parse('test.xml')

for book_tag in etree.getroot():
    print(book_tag.get('isbn'))
    print(book_tag[0].tag, ':', book_tag[0].text)

    for author in book_tag[1]:
        print(author.tag, ':', author.text)

    print()

