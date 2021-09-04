import re

text = '11/27/2021'
text2 = 'Nov 27, 2021'
text3 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

# simple matching: \d+ means one or more digits
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')  # using capture groups and also compiling the pattern

if datepat.match(text):
    print('text ---> yes')
else:
    print('text ---> no')

if datepat.match(text2):
    print('text2 ---> yes')
else:
    print('text2 ---> no')

print(datepat.findall(text3))
m = datepat.match('11/27/2021')
print(m)
print('m.group(0) --->', m.group(0))
print('m.group(1) --->', m.group(1))
print('m.group(2) --->', m.group(2))
print('m.group(3) --->', m.group(3))
print('m.groups() --->', m.groups())
print('*m.groups() --->', *m.groups())

month, day, year = m.groups()
print(month, day, year)

# find all matches (notice splitting into tuples)
print(text3)

for m, d, y in datepat.findall(text3):
    print('findall--->', f'{m}/{d}/{y}')

# find all iteratively using finditer() method
for m in datepat.finditer(text3):
    print('finditer--->', m.groups())

n = datepat.match('11/27/2012abcdef')
print(n if n else False)

if __name__ == '__main__':
    print()
