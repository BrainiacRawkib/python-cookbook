import csv
from urllib.request import urlopen


def dowprices():
    u = urlopen('http://finance.yahoo.com/d/quotes.csv?s=@^DJI&f=sl1')
    lines = (line.decode('utf-8') for line in u)
    rows = (row for row in csv.reader(lines) if len(row) == 2)
    prices = {name: float(price) for name, price in rows}
    return prices
    

if __name__ == '__main__':
    pass
