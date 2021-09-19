# defining more than one consructor in a class
import time


class Date:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate constructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_wday)


class NewDate(Date):
    pass


if __name__ == '__main__':
    a = Date(2021, 9, 12)  # Primary
    b = Date.today()  # Alternate
    c = Date.today()  # Creates an instance of Date (cls=Date)
    d = NewDate.today()  # Creates an instance of Date (cls=NewDate)
