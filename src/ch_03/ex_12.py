# converting days to seconds, and other basic time conversions
from datetime import timedelta

a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b

print(c)
print(c.days, c.seconds, c.seconds/3600)
print(c.total_seconds())

if __name__ == '__main__':
    pass
