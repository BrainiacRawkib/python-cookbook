# saving memory when creating a large number of instances
class Date:
    __slots__ = ['year', 'month', 'day']  # __slots__ was intended to be an optimization tool.

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
