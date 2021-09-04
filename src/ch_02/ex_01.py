# splitting strings on any of multiple delimiters
import re

line = 'asdf fjdk; afed, fjek,asdf, foo'
regex_line = re.split(r'[;,\s]\s*', line)

# using capture group
fields = re.split(r'(;|,|\s)\s*', line)
values = fields[::2]
delimiters = fields[1::2] + ['']

# using non capture group
fields2 = re.split(r'(?:,|;|\s)\s*', line)

if __name__ == '__main__':
    print('regex_line-->', regex_line)
    print('fields-->', fields)
    print(line.split())
    print(values)
    # reform the line using the same delimiters
    print(''.join(v + d for v, d in zip(values, delimiters)))
    print(delimiters)
    print(list(zip(values, delimiters)))
    print('fields2-->', fields2)
