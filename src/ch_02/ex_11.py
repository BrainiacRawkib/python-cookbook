# stripping unwanted characters from strings
import re

# whitespace stripping
s = '      hello world \n'

print(s.strip())
print(s.lstrip())
print(s.rstrip())
print('s.replace() -->', s.replace(' ', ''))
print('s.sub()  -->', re.sub('\s+', '-', s))  # using regex to strip characters

# character stripping
t = '---------hello======='
print(t.lstrip('-'))
t = t.lstrip('-')
print(t.rstrip('='))

if __name__ == '__main__':
    pass
