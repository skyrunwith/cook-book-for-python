#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You want to iterate over all of the possible combinations or permutations of a collection of items.
Solution
    itertools.permutations(), takes a collection of items and produces a sequence of tuples that rearranges all of
    the items into all possible permutations.

    itertools.combinations(), produces a sequence of combinations of items taken from the input.

    itertools.combinations_with_replacement(), allows the same item to be chosen more once.
Discussion
    When faced with seemingly complicated iteration problems, it always pays to look at itertools first.
    If the problem is common, chances are a solution is already available.
"""

__author__ = 'Frankie Fu'

# Solution
# itertools,
items = ['a', 'b', 'c']
from itertools import permutations

for p in permutations(items):
    print(p)
'''
('a', 'c', 'b')
('b', 'a', 'c')
('b', 'c', 'a')
('c', 'a', 'b')
('c', 'b', 'a')
'''

# If you want all permutations of a smaller length, you can give an optional length argument.
for p in permutations(items, 2):
    print(p)
'''
('a', 'b')
('a', 'c')
('b', 'a')
('b', 'c')
('c', 'a')
('c', 'b')
'''

# itertools.combinations
from itertools import combinations

for c in combinations(items, 3):
    print(c)
# ('a', 'b', 'c')

for c in combinations(items, 2):
    print(c)
'''
('a', 'b')
('a', 'c')
('b', 'c')
'''

for c in combinations(items, 1):
    print(c)
'''
('a',)
('b',)
('c',)
'''

# itertools.combinations_with_replacement()
from itertools import combinations_with_replacement

for c in combinations_with_replacement(items, 3):
    print(c)
'''
('a', 'a', 'a')
('a', 'a', 'b')
('a', 'a', 'c')
('a', 'b', 'b')
('a', 'b', 'c')
('a', 'c', 'c')
('b', 'b', 'b')
('b', 'b', 'c')
('b', 'c', 'c')
('c', 'c', 'c')
'''