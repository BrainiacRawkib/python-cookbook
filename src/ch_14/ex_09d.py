# suppressing chaining exception. NB: not advisable
def example3():
    try:
        int('N/A')
    except ValueError:
        raise RuntimeError('A parsing error occurred') from None


if __name__ == '__main__':
    example3()
