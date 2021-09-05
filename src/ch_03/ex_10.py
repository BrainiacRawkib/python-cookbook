# performing matrix and linear algebra calculations
import numpy as np
from numpy import linalg as alg

m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])

print(m)

# return transpose
print('Transpose of m --> ', m.T)

# return inverse
print('Inverse of m --> ', m.I)

# create a vector and multiply
print(format('multiplying vectors'))
v = np.matrix([[2], [3], [4]])
print(v)
print('m * v --> ', m * v)

print(format('Linear algebra', '*^30s'))
# Determinant
determinant = alg.det(m)
print(determinant)

# Eigenvalues
eigen = alg.eigvals(m)
print(eigen)

# solve for x in mx = v
x = alg.solve(m, v)
print(x)
print(m * x)
print('v --> ', v)

if __name__ == '__main__':
    pass
