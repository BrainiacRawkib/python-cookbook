# executing code with local side effects
# a = 13
# exec('b = a + 1')
#
# print(b)


def test():
    print(locals())
    a = 13
    loc = locals()
    exec('b = a + 1')
    b = loc['b']
    print(b)
    print(locals())


test()
print(locals())
print(globals())
if __name__ == '__main__':
    pass
