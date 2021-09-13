# attaching informational metadata to function arguments
def add(x: int, y: int) -> int:
    return x + y


help(add)
print(add.__annotations__)

if __name__ == '__main__':
    pass
