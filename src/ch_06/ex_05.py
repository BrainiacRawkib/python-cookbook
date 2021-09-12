# truncating a dictionary into xml
from xml.etree.ElementTree import Element, tostring
from xml.sax.saxutils import escape, unescape


def dict_to_xml(tag, d):
    """
    Turn a simple dict pf key/value pairs to xml
    :param tag:
    :param d:
    :return:
    """
    elem = Element(tag)
    for key, value in d.items():
        child = Element(key)
        child.text = str(value)
        elem.append(child)
    return elem


def dict_to_xml_str(tag, d):
    """
    Turn a simple dict of key/value pairs into XML.
    :param tag:
    :param d:
    :return:
    """
    parts = ['<{}>'.format(tag)]
    for key, value in d.items():
        parts.append('<{0}>{1}</{0}>'.format(key, value))
    parts.append('</{}>'.format(tag))
    return ''.join(parts)


s = {'name': 'GOOG', 'shares': 100, 'price': 490.1}
e = dict_to_xml('stock', s)
d = {'name': '<spam>'}
print(e)
print(tostring(e))
e = dict_to_xml('item', d)
print(tostring(e))  # to decode the byte strings use the decode() method
print(dict_to_xml_str('item', d))

print(escape('<spam>'))
print(unescape('<spam>'))

if __name__ == '__main__':
    pass
