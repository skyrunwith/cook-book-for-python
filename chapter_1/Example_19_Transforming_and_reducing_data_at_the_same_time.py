"""
Problem
    You need to execute a reduction function(e.g, sum(), min(), max()), but first need to transform
    or filter data.
Solution
    generator expressions argument.
        (x * x for x in nums)
Discussion
    generator expressions when supplied as the single argument to a function.

    it often efficient and elegant approach than first creating a temporary list.
        temporary list creating a large temporary data structure to only be used once and discarded.

    min() and max() accept a key argument that might be useful.
"""

__author__ = 'Frankie Fu'

# Solution
# A very elegant way to combine a data reduction and a transformation is to use a generator-expression
# argument. For example, if you want to calculate the sum of squares, do the following:
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

# Here are a few other examples:
# Determine if any .py files exist in a directory
import os

files = os.listdir('data')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print('join:', ','.join(str(x) for x in s))

# Data reduction across fields of a data structure
portfolio = [
    {'name': 'GOOD', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio)
print('min_shares: ', min_shares)

# Discussion
# The solution shows a subtle syntactic aspect of generator expressions when supplied as the
# single argument to a function(i.g, you don't need repeated parentheses).
# For Example, these statements are the same:
s = sum((x * x for x in nums))
print('sum: ', s)

# Using a generator argument is often a more efficient and elegant approach than first creating
# a temporary list.
# For example, if you didn't use a generator expression, you might consider this alternative implementation:
nums = [1, 2, 3, 4, 5]
s = sum([x * x for x in nums])
print('sum: ', s)

# This works, but it introduces an extra step and creates and extra list. For such a small list,
# it might not matter, but if nums was huge, you would end up creating a large temporary data
# structure to only be used once and discarded. The generator solution transforms the data iteratively
# and is therefore much more memory-efficient.

# Certain reduction functions such as min() and max() accept a key argument that might be useful
# in situations where you might be inclined to use a generator.
# For example, in the portfolio example, you might consider this alternative:

# Original: return 20
min_shares = min(s['shares'] for s in portfolio)
print('original: ', min_shares)
# Alternative: Returns {'name': 'AOL', 'shares': 20}
min_shares = min(portfolio, key=lambda s: s['shares'])
print('alternative: ', min_shares)

