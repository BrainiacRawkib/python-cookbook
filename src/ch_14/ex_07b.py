def parse_int(s):
    try:
        n = int(v)
    except Exception as e:
        print("Couldn't parse")
        print('Reason', e)


if __name__ == '__main__':
    parse_int('n/a')
