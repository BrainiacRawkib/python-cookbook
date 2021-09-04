# interpolating variables in strings
s = '{name} has {n} messages.'

print(s)

name = 'Guido'
n = 37
print(s.format_map(vars()))


class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n


class SafeSub(dict):
    def __missing__(self, key):
        return '{' + key + '}'


a = Info('Brainy', 37)
print(s.format_map(vars(a)))

print(s.format_map(SafeSub(vars())))

if __name__ == '__main__':
    pass
