# type conversion
import csv

col_types = [str, float, str, str, float, int]

with open('stocks.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # apply conversions to the row items
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        print(row)

print(format('Reading as dicts with type conversion', '*^70s'))
field_types = [
    ('Price', float),
    ('Change', float),
    ('Volume', int)
]

with open('stocks.csv') as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key])) for key, conversion in field_types)
        print(row)

if __name__ == '__main__':
    pass
