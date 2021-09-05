# working with binary, octal and hexadecimal
x = 1234

print('bin --> ', bin(x))
print('oct --> ', oct(x))
print('hex --> ', hex(x))
print('bin --> ', format(x, 'b'))
print('oct --> ', format(x, 'o'))
print('hex --> ', format(x, 'x'))

print(format('Negative bin, oct, hex', '*^30s'))
x = -1234

print('bin --> ', bin(x))
print('oct --> ', oct(x))
print('hex --> ', hex(x))
print('bin --> ', format(x, 'b'))
print('oct --> ', format(x, 'o'))
print('hex --> ', format(x, 'x'))

print(format('producing unsigned bit length', '*^40s'), end='\n\n')
x = -1234
print(format(2 ** 32 + x, 'b'))
print(format(2 ** 32 + x, 'x'))

print(format('convert different bases to int', '*^30s'))
print('base 16', int('4d2', 16))
print('base 2', int('10011010010', 2))
import os
print(os.chmod('ex_04.py', 0o755))

if __name__ == '__main__':
    pass
