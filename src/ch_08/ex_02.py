# customizing string formatting
from datetime import date

_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


if __name__ == '__main__':
    d = Date(2021, 12, 21)
    print(format(d))
    print(format(d, 'mdy'))
    print(format(d, 'dmy'))
    print('The date is {:mdy}'.format(d))
    print('The date is {:dmy}'.format(d))
    print('The date is {:ymd}'.format(d))

    print(format('datetime', '*^20'))
    d = date(2021, 12, 21)
    print(format(d))
    print(format(d, '%A, %B %d, %Y'))
    print('The end is {:%d %b %Y}. Exiting'.format(d))
