"""
Calculating with large numerical arrays
Problem
    You need to perform calculations on large numerical datasets, such as arrays or grids.
Solution
    For any heavy computation involving arrays, use the NumPy library.
Discussion
"""

__author__ = 'Frankie Fu'

# Solution
# The major feature of NumPy is that it gives Python an array object that is much more efficient and better
# suited for mathematical calculation than a standard Python list. Here is a short example illustrating
# important behavioral differences between lists and NumPy arrays:

# Python lists
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x * 2)
# print(x + 10)
# TypeError: can only concatenate list (not "int") to list
print(x + y)

# Numpy arrays
import numpy as np

ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax * 2)
# [2 4 6 8]

print(ax + 10)
# [11 12 13 14]
print(ax + ay)
# [ 6  8 10 12]
print(ax * ay)


# [ 5 12 21 32]

# As you can see, basic mathematical operations involving arrays behave differently. Specifically,
# scalar operations(e.g, ax * 2 or ax + 10) apply the operation on an element-by-element basis.
# In addition, performing math operations when both operands are arrays applies the operation to all elements
# and produces a new array.

# The fact that math operations apply to all of the elements simultaneously makes it very easy and fast to
# compute functions across an entire array. for example, if you want to compute the value of a polynomial:
def f(x):
    return 3 * x ** 2 - 2 * x + 7


print(f(ax))
# [ 8 15 28 47]

# NumPy provides a collection of "universal functions" that also allow for array operations. These are
# replacements for similar functions normally found in the 'math' module, for example:
print(np.sqrt(ax))
# [1.         1.41421356 1.73205081 2.        ]
print(np.cos(ax))
# [ 0.54030231 -0.41614684 -0.9899925  -0.65364362]

# Using universal functions can be hundreds of times faster than looping over the array elements one at a time
# and performing calculations using functions in the 'math' module. Thus, you should prefer their use
# whenever possible.

# Under the covers, NumPy arrays are allocated in the same manner as in C or Fortran. Namely, they are large,
# contiguous memory regions consisting of a homogenous data type. Because of this, it's possible to make arrays
# much larger than anything you would normally put into a Python list. For example, if you want to make a
# two-dimensional grid of 10000 by 100000 floats, it's not an issue:
grid = np.zeros(shape=(10000, 10000), dtype=float)
print(grid)
# [[0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 0.]
#  ...
#  [0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 0.]
#  [0. 0. 0. ... 0. 0. 0.]]

# All of the usual operations still apply to all of the elements simultaneously:
grid += 10
print(grid)
# [[10. 10. 10. ... 10. 10. 10.]
#  [10. 10. 10. ... 10. 10. 10.]
#  [10. 10. 10. ... 10. 10. 10.]
#  ...
#  [10. 10. 10. ... 10. 10. 10.]
#  [10. 10. 10. ... 10. 10. 10.]
#  [10. 10. 10. ... 10. 10. 10.]]

print(np.sin(grid))

# One extremely notable aspect of NumPy is the manner in which it extends Python's list indexing functionality
# especially with multidimensional arrays. To illustrate, make a simple two-dimensional array and try
# some experiments:
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]]
# Select row 1
print(a[1])
# [5 6 7 8]
# Select column 1
print(a[:, 1])
# [ 2  6 10]
# Select a subregion and change it
print(a[1:3, 1:3])
# [[ 6  7]
#  [10 11]]

a[1:3, 1:3] += 10
print(a)
# [[ 1  2  3  4]
#  [ 5 16 17  8]
#  [ 9 20 21 12]]

# Broadcast a row vector across an operation on all rows
print(a + [100, 101, 102, 103])
# [[101 103 105 107]
#  [105 117 119 111]
#  [109 121 123 115]]

# conditional assigment on an array
print(np.where(a < 10, a, 10))
# [[ 1  2  3  4]
#  [ 5 10 10  8]
#  [ 9 10 10 10]]

# Discussion
# NumPy is the foundation for a huge number of science and engineering libraries in Python. It is also one of
# the largest and most complicated modules in widespread use. That said, it's still possible to accomplish
# useful things with NumPy by starting with simple examples and playing around.

# One note about usage is that it is relatively common to use the statement 'import numpy as np', as shown
# in the solution. This simply shortens the name to something that's more convenient to type over and over
# again in your program.

# For more information, you definitely need to visit http://www.numpy.org.
