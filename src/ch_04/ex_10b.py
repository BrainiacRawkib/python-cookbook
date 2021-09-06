# mapping words in a file to lines
from collections import defaultdict

word_summary = defaultdict(list)

with open('somefile.txt', 'r') as f:
    lines = f.readlines()


for idx, line in enumerate(lines):
    # create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

print(word_summary)

data = [(1, 2), (3, 4), (5, 6), (7, 8)]

# correct!
for n, (x, y) in enumerate(data):
    print(n, '-->', (x, y))

# or use unpacking
for n, *x in enumerate(data):
    print(n, '-->', x)

if __name__ == '__main__':
    pass
