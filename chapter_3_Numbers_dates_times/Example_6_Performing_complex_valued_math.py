"""
Performing Complex-Valued Math
Problem
    Your code for interacting with the latest web authentication scheme has encountered a singularity and
    your only solution is to go around it in the complex plane. Or maybe you just need to perform some
    calculations using complex numbers.
Solution
    use complex(real, imag) function or by floating-point number with a j suffix.
Discussion
    numpy: make arrays of complex values and perform operations.
    cmath: could produces complex numbers.
"""

__author__ = 'Frankie Fu'

# Solution
# Complex numbers can be specified using the 'complex(real, imag)' function or by floating-point number
# with a 'j' suffix. For example:
a = complex(2, 4)
b = 3 - 5j

print(a)
# (2+4j)
print(b)
# (3-5j)

# The real, imaginary, and conjugate values are easy to obtain, as shown here:
print(a.real)
# 2.0
print(a.imag)
# 4.0
print(a.conjugate())
# (2-4j)

# In addition, all of the usual mathematical operators work:
print(a + b)
# (5-1j)
print(a * b)
# (26+2j)
print(a/b)
# (-0.4117647058823529+0.6470588235294118j)
print(abs(a))
# 4.47213595499958

# To perform additional complex-valued functions such as sines, cosines, or square roots,
# use the 'cmath' module:
import cmath
print(cmath.sin(a))
# (24.83130584894638-11.356612711218174j)
print(cmath.cos(a))
# (-11.36423470640106-24.814651485634187j)
print(cmath.exp(a))
# (-4.829809383269385-5.5920560936409816j)

# Most of Python's math-related modules are aware of complex values. For example, if you use 'numpy', it is
# straightforward to make arrays of complex values and perform operations on them:
import numpy as np

a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)
# [2.+3.j 4.+5.j 6.-7.j 8.+9.j]
print(a + 2)
# [ 4.+3.j  6.+5.j  8.-7.j 10.+9.j]
print(np.sin(a))
# [   9.15449915  -4.16890696j  -56.16227422 -48.50245524j
#  -153.20827755-526.47684926j 4008.42651446-589.49948373j]

# Python's standard mathematical functions do not produce complex values by default, so it is unlikely that such
# a value would accidentally show up in your code. For example:
import math
# print(math.sqrt(-1))
# ValueError: math domain error

# If you want complex numbers to be produced as result, you have to explicitly use 'cmath' or
# declare the use of a complex type in libraries that know about them. For example:
import cmath
print(cmath.sqrt(-1))
# 1j
