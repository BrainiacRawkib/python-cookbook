# interacting with a relational database
import sqlite3

stocks = [
    ('GOOG', 100, 490.1),
    ('AAPL', 50, 545.75),
    ('FB', 150, 7.45),
    ('HPQ', 75, 33.2),
]

# initialize database
db = sqlite3.connect('database.db')

# create a cursor
c = db.cursor()

# create a table
c.execute("create table portfolio (symbol text, shares interger, price real)")
db.commit()

# To insert a sequence of rowa into the data
c.executemany('insert into portfolio values (?,?,?)', stocks)
db.commit()

# To perform a query
for row in db.execute('select * from portfolio'):
    print(row)


# To perform queries that accept user-supplied input params
print(format('Perform user-supplied input query', '*^70s'))
min_price = 100
for row in db.execute('select * from portfolio where price >= ?', (min_price,)):
    print(row)

if __name__ == '__main__':
    pass
