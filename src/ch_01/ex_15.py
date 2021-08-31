# grouping records together based on a field
from collections import defaultdict
from operator import itemgetter
from itertools import groupby

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

# Sort by the desired field first
rows.sort(key=itemgetter('date'))

rows_by_date = defaultdict(list)


if __name__ == '__main__':
    print(rows)
    # Iterate in groups
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date, items)
        for i in items:
            print('    ', i)

    print('*' * 10, 'defaultdict', '*' * 10)
    for row in rows:
        rows_by_date[row['date']].append(row)  # check ex_06 for clarifications

    print(rows_by_date)
