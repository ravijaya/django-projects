from json import load

content = load(open('test.json'))

for book in content:
    print(book)