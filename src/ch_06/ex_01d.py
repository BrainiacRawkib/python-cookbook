import re
import csv
from collections import namedtuple

# scrub headings containing non-valid characters
with open('regex_stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = [re.sub('[^a-zA-Z_]', '_', h) for h in next(f_csv)]
    Row = namedtuple('Row', headers)
    for r in f_csv:
        row = Row(*r)
        print(row)

if __name__ == '__main__':
    pass
