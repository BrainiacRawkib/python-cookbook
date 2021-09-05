from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


a = datetime(2021, 9, 23)
print(a)
print(a + timedelta(days=1))
print(a + timedelta(days=10))

b = datetime(2021, 12, 21)
d = b - a
print(d)

now = datetime.now()
print(now)

# leap year
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)

print(format('leap year -->', '*^20s'))
print('a - b --> ', a - b)

print(format('not leap year -->', '*^20s'))
a = datetime(2021, 3, 1)
b = datetime(2021, 2, 28)
print('a - b --> ', a - b)

# using dateutil to extend builtin datetime module

# print(a + timedelta(months=1))  # TypeError: 'months' is an invalid keyword argument for this function
print(format('using python dateutil', '*^30s'))
print(a + relativedelta(months=4))
print(a + relativedelta(months=+4))
print(a + relativedelta(months=+10))

# time between two dates
d = b - a
print(d)
d = relativedelta(a, b)
print(d, d.months, d.days)

if __name__ == '__main__':
    pass
