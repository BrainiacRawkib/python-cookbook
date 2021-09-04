# handling HTML and XML entities in text
import html
from html import unescape
from xml.sax.saxutils import unescape as xml_unescape

s = 'Elements are written as "<tag>text</tag>".'

print(s)
print(html.escape(s))

# disable escaping of quotes
print(html.escape(s, quote=False))

s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))

s = 'Spicy &quot;Jalape&#241;o&quot.'
print(unescape(s))

# xml parsing
t = 'The prompt is &gt;&gt;&gt;'
print(xml_unescape(t))

if __name__ == '__main__':
    pass
