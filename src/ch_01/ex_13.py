# sorting a list of dictionaries by a common key
from operator import itemgetter

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname', 'lname'))
rows_by_fname2 = sorted(rows, key=lambda r: r['fname'])
rows_by_uid = sorted(rows, key=itemgetter('uid'))
rows_by_lname = sorted(rows, key=itemgetter('lname'))
least_by_uid = min(rows, key=itemgetter('uid'))
max_by_uid = max(rows, key=itemgetter('uid'))

if __name__ == '__main__':
    print(rows_by_fname)
    print('rows_by_fname2-->', rows_by_fname2)
    print(rows_by_uid)
    print(rows_by_lname)
    print(least_by_uid)
    print(max_by_uid)
