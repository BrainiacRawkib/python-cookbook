import ex_04_mymodule


if __name__ == '__main__':
    from ex_04_mymodule import A
    a = ex_04_mymodule.A()
    a.spam()
    b = ex_04_mymodule.B()
    b.bar()

    # The main downside of lazy loading is that
    # inheritance and type checking might break.
    x = A()
    # if isinstance(x, A):  # Error
    #     print('True!')

    if isinstance(x, ex_04_mymodule.a.A):  # Ok
        print('True!')
