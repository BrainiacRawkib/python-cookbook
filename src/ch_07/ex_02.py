# writing functions that only accept keyword arguments
def recv(maxsize, *, block):
    """Receives a message."""
    pass


def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


# print(recv(1024, True))
print(recv(1024, block=True))

print(minimum(1, 5, 2, -5, 10))
print(minimum(1, 5, 2, -5, 10, clip=0))

help(recv)

if __name__ == '__main__':
    pass
