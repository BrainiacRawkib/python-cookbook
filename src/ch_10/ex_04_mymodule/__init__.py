# __init__.py

# from .a import A
# from .b import B

# to load components as they are needed.


def A():
    from .a import A
    return A()


def B():
    from .b import B
    return B()
