# tokenizing text
import re
from collections import namedtuple

text = 'foo = 23 + 42 * 10'

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'
LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))
scanner = master_pat.finditer('foo = 42')
print(scanner)
print([n for n in scanner])
Token = namedtuple('Token', ['type', 'value'])


def generate_tokens(pat, text):
    scan = pat.finditer(text)
    for m in iter(scan.match, None):
        yield Token(m.lastgroup, m.group())


# using generate_token
# for tok in generate_tokens(master_pat, 'foo = 42'):  # not working
#     print(tok)

# filtering tokens
# tokens = (tok for tok in generate_tokens(master_pat, text) if tok.type != 'WS')  # not working
#
# for tok in tokens:
#     print(tok)

# matching the longest pattern first is a good practice
master_pat = re.compile('|'.join([LE, LT, EQ]))  # correct
# master_pat = re.compile('|'.join([LT, LE, EQ]))  # not correct
print(master_pat)

# matching words that form substrings
PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

master_pat = re.compile('|'.join([PRINT, NAME]))

# for tok in generate_tokens(master_pat, 'printer'):  # not working
#     print(tok)

if __name__ == '__main__':
    pass
