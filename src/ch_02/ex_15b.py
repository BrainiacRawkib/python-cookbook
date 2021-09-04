# using a frame hack to manipulate missing keys
import sys
import string
from ch_02.ex_15 import SafeSub


def sub(text):
    return text.format_map(SafeSub(sys._getframe(1).f_locals))


name = 'Guido'
a = 20

text = "%(name) has %(a) cars." % vars()  # issues

# using template strings
template_strings = string.Template('$name has $a cars.')

if __name__ == '__main__':
    print(format('ex_15b.py', '*^20s'))
    print(sub('Hello {name}'))
    print(sub('You have {n} messages.'))
    print(sub('Your favorite color is {color}'))
    print(text)
    print(template_strings.substitute(vars()))
