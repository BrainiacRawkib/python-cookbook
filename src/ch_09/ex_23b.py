def test1():
    x = 0
    exec('x += 1; print(x)')
    print(x)


test1()


def test2():
    x = 0
    loc = locals()
    print('before:', loc)
    exec('x += 1')
    print('after:', loc)
    print('x =', x)


test2()


print(format('test3()', '*^20s'))


def test3():
    x = 0
    loc = locals()
    print(loc)
    exec('x += 1')
    print(loc)
    locals()
    print(loc)


test3()


print(format('test4()', '*^20'))


def test4():
    a = 13
    loc = {'a': a}
    glb = {}
    exec('b = a + 1', glb, loc)
    b = loc['b']
    print(b)


test4()
if __name__ == '__main__':
    pass
