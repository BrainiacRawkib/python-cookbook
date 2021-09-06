# iterating over the index-value pairs of a sequence
my_list = ['a', 'b', 'c', 'd', 'e']

for idx, val in enumerate(my_list):
    print(idx, val)

for idx, val in enumerate(my_list, 1):
    print(idx, val)

# showing line number errors using enumerate builtin


def parse_data(filename):
    with open(filename, 'rt') as f:
        for line_no, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print('Line {}: Parse error: {}'.format(line_no, e))


if __name__ == '__main__':
    pass
