"""
Performing Matrix and Linear Algebra Calculations
Problem
    You need to perform matrix and linear algebra operations, such as matrix multiplication, finding
    determinants, solving linear equations, and so on.
Solution
    The NumPy library has 'matrix' object that can be used for this purpose.
    np.matrix()
    m.T, m.I
    np.linalg
Discussion
"""

__author__ = 'Frankie Fu'

# Solution
# Matrices are somewhat similar to the array objects described in Recipe 3.9, but follow linear algebra
# rules for computation. Here is an example that illustrates a few essential features:
import numpy as np

m = np.matrix([[1, -2, 3], [0, 4, 5], [7, 8, -9]])
print(m)
# [[ 1 -2  3]
#  [ 0  4  5]
#  [ 7  8 -9]]

# Return transpose
print(m.T)
# [[ 1  0  7]
#  [-2  4  8]
#  [ 3  5 -9]]

# Return inverse
print(m.I)
# [[ 0.33043478 -0.02608696  0.09565217]
#  [-0.15217391  0.13043478  0.02173913]
#  [ 0.12173913  0.09565217 -0.0173913 ]]

# Create a vector and multiply
v = np.matrix([[2], [3], [4]])
print(v)
# [[2]
#  [3]
#  [4]]
print(m * v)
# [[ 8]
#  [32]
#  [ 2]]

# More operations can be found in the 'numpy.linalg' subpackage. For example:
import numpy.linalg

# Determinant
print(numpy.linalg.det(m))
# -229.99999999999983
# Eigenvalues
print(numpy.linalg.eigvals(m))
# [-13.11474312   2.75956154   6.35518158]
# Solve for x in mx = v
x = numpy.linalg.solve(m, v)
print(x)
# [[0.96521739]
#  [0.17391304]
#  [0.46086957]]

print(m*x)
# [[2.]
#  [3.]
#  [4.]]

print(v)
# [[2]
#  [3]
#  [4]]

# Discussion
# Linear algebra is obviously a huge topic that's far beyond the scope of this cookbook. However, if you need
# to manipulate matrices and vectors, NumPy is a good starting point
# Visit http://www.nimpy,org for more detailed information.
