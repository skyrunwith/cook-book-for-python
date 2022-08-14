""" 
Working with Infinity and NaNs
Problem
    You need to create or test for the floating-point values of infinity, negative infinity, or NaN(not a number)
Solution
    use float(): float('inf'), float('-inf'), float('nan')
    math.isinf(), math.isnan()
Discussion
    inf and 和正常数字计算，都会产生inf, inf/inf == 0.0
    nan 与任何数计算都为 nan
    inf + inf == nan
"""

__author__ = 'Frankie Fu'

# Solution
# Python has no special syntax to represent these special floating-point values, but they can be created
# using 'float()'. For example:
a = float('inf')
b = float('-inf')
c = float('nan')
print(a, b, c)
# inf -inf nan

# To test for the presence of these values, use the 'math.isinf()' and 'math.isnan()' functions.
# For example:
import math
print(math.isinf(a), math.isinf(b), math.isnan(c))
# True True True

# Discussion
# For more detailed information about these special floating-point values, you should refer to the IEEE 754
# specification.
# However, there are a few tricky details to be aware of, especially related to comparisons and operators.
a = float('inf')
print(a + 45)
# inf
print(a * 10)
# inf
print(10 / a)
# 0.0

# However, certain operations are undefined and will result in a NaN result.
a = float('inf')
print(a / a)
# nan
b = float('-inf')
print(a + b)
# nan

# NaN values propagate through all operations without raising an exception. For example:
c = float('nan')
print(c + 23)
# nan
print(c / 2, c * 2, math.sqrt(c))
# nan nan nan

# A subtle feature of NaN values is that they never compare as equal. For example:
c = float('nan')
d = float('nan')
print(c == d)
# False
print(c is d)
# False

# Because of this, the only safe way to test for a NaN value is to use 'math.isnan(), as shown in this recipe.

# Sometimes programmers want to change Python's behavior to raise exceptions when operations result in an
# infinite or NaN result. The 'fpectl' module can be used to adjust this behavior, but it is not enabled in
# a standard Python build, it's platform-dependent, and really only intended for expert-level programmers,
# See the online Python documentation for further details.

