import numpy as np

grid = np.zeros(shape=(10000, 1000), dtype=float)

# print(format('np.zeros', '*^20s'))
# print(grid)
# grid += 10
# print(grid)
#
# print(format('np.sin(grid)', '*^20s'))
# print(np.sin(grid))

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)

# select row 1
print('row a[1] --> ', a[1])

# select column 1
print('column a[:,1]', a[:, 1], end='\n\n')

# select a subregion and change it
print('a[1:3, 1:3] --> ', a[1:3, 1:3])

print('a[1:3, 1:3] + 10 --> ', a[1:3, 1:3] + 10)

if __name__ == '__main__':
    pass
