# Raising an Exception in Response to Another Exception
def example():
    try:
        int('N/A')
    except ValueError as e:
        raise RuntimeError('A parsing error occurred') from e


if __name__ == '__main__':
    example()
