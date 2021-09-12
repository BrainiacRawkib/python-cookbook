from xml.etree.ElementTree import iterparse

for evt, elem in iterparse('example.xml', ('end', 'start-ns', 'end-ns')):
    print(evt, elem)

if __name__ == '__main__':
    pass
