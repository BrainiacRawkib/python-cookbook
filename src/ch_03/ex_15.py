# converting strings into datetimes
from datetime import datetime

text = '2021-09-05'

y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()

diff = z - y

print(format('Using strptime() method', '*^30s'))
print(diff)

print(format('Using strpftime() method', '*^30s'))
z = datetime(2021, 9, 5, 1, 47, 5, 177383)
print(z)
nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)

# writing custom solution for better performance over strptime() method


def parse_ymd(s):
    year_s, mon_s, day_s = s.splt('-')
    return datetime(int(year_s), int(mon_s), int(day_s))


if __name__ == '__main__':
    pass
