# parsing and analyzing python source
# you can evaluate and execute source code provided in the form of string
x = 42
print(eval('2 + 3 * 4 + x'))

exec('for i in range(10): print(i)')

if __name__ == '__main__':
    pass
