# creating an instance without invoking init

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


if __name__ == '__main__':
    # creating an instance without invoking the __init__() method
    d = Date.__new__(Date)
    # the resulting instance is uninitialized
    # print(d.year)  # AttributeError: 'Date' object has no attribute 'year'

    # set appropriate instance variable
    data = {'year': 2021, 'month': 9, 'day': 20}
    for key, value in data.items():
        setattr(d, key, value)
    print(d.year, d.month, d.day)
