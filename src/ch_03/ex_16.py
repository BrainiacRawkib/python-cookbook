# manipulating dates involving time zones
from datetime import datetime, timedelta
from pytz import timezone, utc, country_timezones

d = datetime(2021, 9, 5, 10, 30, 0)
print(d)

# localize the date for chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print('loc_d ---> ', loc_d)

# convert to bangalore
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print('bang_d --->', bang_d)

# using normalize() method to account for one-hour skip in local time
later = central.normalize(loc_d + timedelta(minutes=30))
print('later -->', later)

# using UTC for localizing dates
utc_d = loc_d.astimezone(utc)
print('UTC-d ---> ', utc_d)

# converting from UTC to locale
later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))

# country timezones
print(country_timezones['IN'])
print(country_timezones['NG'])
print(country_timezones['GH'])

if __name__ == '__main__':
    pass
