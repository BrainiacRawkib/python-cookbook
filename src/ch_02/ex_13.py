# aligning texts strings

text = 'Hello World'
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))
print(text.rjust(20, '='))
print(text.center(20, '*'))
print('format >20 -->', format(text, '>20'))
print('format =>20 -->', format(text, '=>20s'))
print('format <20 -->', format(text, '<20'))
print('format ^20 -->', format(text, '^20'))
print('format *^20 -->', format(text, '*^20s'))

format_string = '{:>10s} {:>10s}'.format('Hello', 'World')
print(format_string)
x = 1.2345
print(format(x, '>10'))
print(format(x, '^10.2f'))

if __name__ == '__main__':
    pass
