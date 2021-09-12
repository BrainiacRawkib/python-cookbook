# parsing xml documents with namespaces
from xml.etree.ElementTree import parse


class XMLNamespaces:
    def __init__(self, **kwargs):
        self.namespaces = {}
        for name, uri in kwargs.items():
            self.register(name, uri)

    def register(self, name, uri):
        self.namespaces[name] = '{' + uri + '}'

    def __call__(self, path):
        return path.format_map(self.namespaces)


doc = parse('example.xml')

# Some queries that work
print(doc.findtext('author'))
print(doc.find('content'))

# A query involving a namespace (doesn't work)
print(doc.find('content/html'))

# Works if fully qualified
print(doc.find('content/{http://www.w3.org/1999/xhtml}html'))

# Doesn't work
print(doc.findtext('content/{http://www.w3.org/1999/xhtml}html/head/title'))

# Fully qualified
print(doc.findtext('content/{http://www.w3.org/1999/xhtml}html/'
                   '{http://www.w3.org/1999/xhtml}head/{http://www.w3.org/1999/xhtml}title'))

print(format('Using XMLNamespaces', '*^30'))
# using XMLNamespaces class
ns = XMLNamespaces(html='http://www.w3.org/1999/xhtml')
print(doc.find(ns('content/{html}html')))
print(doc.findtext(ns('content/{html}html/{html}head/{html}title')))

if __name__ == '__main__':
    pass
