import xml.etree.ElementTree as et

etree = et.parse('test.xml')
print(etree.getroot())
print(etree.getroot().tag)