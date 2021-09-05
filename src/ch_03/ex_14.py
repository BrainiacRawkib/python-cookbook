# finding the date range for the current month
import calendar
from datetime import date, datetime, timedelta


def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    print('Calendar month range -->', calendar.monthrange(start_date.year, start_date.month))
    end_date = start_date + timedelta(days=days_in_month)
    print('End-date --> ', end_date)
    return start_date, end_date


a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day


# using a generator to produce date range
def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


print(format('Using generator to produce date range', '*^60s'))
start_date = datetime(2021, 9, 1)
end_date = datetime(2021, 10, 1)
for d in date_range(start_date, end_date, timedelta(hours=6)):
    print(d)

if __name__ == '__main__':
    pass
