# determining last friday's date
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *


weekdays = [
    'Monday', 'Tuesday', 'Wednesday', 'Thursday',
    'Friday', 'Saturday', 'Sunday'
]

print('Today\'s date --> ', datetime.today())
print('Today\'s weekday --> ', datetime.today().weekday())  # weekday() Monday == 0, Sunday == 6
print(weekdays.index('Tuesday', 0, 5))


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


print(format('', '*^20s'))
print(get_previous_byday('Monday'))
print(get_previous_byday('Tuesday'))
print(get_previous_byday('Wednesday'))
print(get_previous_byday('Friday'), end='\n\n')

print(format('', '*^20s'))
d = datetime.now()

# Next Friday
print(d + relativedelta(weekday=FR))

# Last Friday
print(d + relativedelta(weekday=FR(-1)))

if __name__ == '__main__':
    pass
