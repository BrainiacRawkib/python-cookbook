# writing functions that accept any number of arguments
import html


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    print('keyv->', keyvals)
    attr_str = ''.join(keyvals)
    print('attr->', attr_str)
    element = '<{name}{attrs}>{value}</{name}>'.format(name=name, attrs=attr_str, value=html.escape(value))
    return element


def anyargs(*args, **kwargs):
    print(args)
    print(kwargs)


# sample use
a = avg(1, 2)
print(a)

a = avg(1, 2, 3, 4)
print(a)

# create '<item size="large" quantity="6">Albatross</item>'
x = make_element('item', 'Albatross', size='large', quantity=6)
print(x)

# create '<p>&lt;spam&gt;</p>'
x = make_element('p', '<spam>')
print(x)

if __name__ == '__main__':
    pass
