# searching and replacing text
import re
from calendar import month_abbr

text = 'yeah, but no, but yeah, but no, but yeah'
today_text = 'Today is 27/11/2012. PyCon starts 13/3/2013. Launch date is 23/09/2021'

print(text.replace('yeah', 'yep'))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

regex_text = datepat.sub(r'\3-\2-\1', today_text)  # \3, \1, \2 refers to the capture group
print(regex_text)


def change_date(m):
    month_name = month_abbr[int(m.group(2))]
    return '{} {} {}'.format(m.group(1), month_name, m.group(3))


print(datepat.sub(change_date, today_text))

newtext, n = datepat.subn(r'\3-\2-\1', today_text)
print(newtext)
print(n, 'substitutions')

if __name__ == '__main__':
    print()
