def drop_first_last(grades):
    first, *middle, last = grades
    return middle


user_record = ('rawkib', 'admin@admin.com', '773-554-3354', '44-555-3356')
name, email, *contact = user_record

*trailing, current = [10, 8, 9, 7, 4, 5, 2, 3, 4]

records = [
    ('foo', 1, 2), ('bar', 'hello'), ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')


record = ('ACME', 50, 123.45, (12, 18, 2012))
record_name, *_, (*_, year) = record


items = [1, 10, 7, 4, 5, 9]
head, *tail = items


def sum_(items):
    h, *t = items
    return h + sum_(t) if t else h


if __name__ == '__main__':
    print(name, email, contact)
    print(current, trailing)
    for tag, *args in records:
        if tag == 'foo':
            print(do_foo(*args))
        elif tag == 'bar':
            print(do_bar(*args))
    print(uname, '\n', fields, '\n', homedir, '\n', sh)
    print(record_name, year)
    print(head, tail)
    print(sum_(items))
