def example2():
    try:
        int('N/A')
    except ValueError as e:
        print("Couldn't parse", err)


if __name__ == '__main__':
    example2()
