print(format('At runtime', '*^30s'))
print(format('lambda runtime issues', '*^40'))
funcs = [lambda x: x + n for n in range(5)]
for func in funcs:
    print(func(0))

print(format('At point of definition', '*^30s'))
print(format('lambda runtime issues fixed', '*^40'))
funcs = [lambda x, n=n: x + n for n in range(5)]
for func in funcs:
    print('first ->', func(0))
    print('second ->', func(3))

if __name__ == '__main__':
    pass
