#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Problem
    You want to perform various calculations.(eg. minimum value, maximum value, sorting, etc.)
    on a dictionary of data.
Solution
    zip():
        create a iterator tuple.
        it only be consumed once.
    min()
    max()
    sorted()
Discussion
    zip() inverting the dictionary into a sequence of (value, key) pairs.
        when comparisons, the value element is compared first, followed by the key.
        it allows reductions and sorting to be easily performed on the dictionary content using a single statement.
"""

__author__ = 'Frankie Fu'

# Solution
# Consider a dictionary that maps stock names to prices:
prices = {
    'ACME': 45.23,
    'AAPL': 612.87,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# In order to perform useful calculations on the dictionary content, it is often useful to
# invert the keys and values of the dictionary using "zip()", For example, here is how to
# find the minimum and maximum price and stock name:
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
# (10.75, 'FB')

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)
# (612.87, 'AAPL')

# Similarly, to rank the data, use zip() with sorted(), as in the following:
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)
# [(10.75, 'FB'), (37.2, 'HPQ'), (45.23, 'ACME'), (205.55, 'IBM'), (612.87, 'AAPL')]

# When doing these calculations, be aware that zip() creates an iterator that can only be
# consumed once. For example, the following code is an error:
prices_and_names = zip(prices.values(), prices.keys())
print(min(prices_and_names))  # OK
# print(max(prices_and_names))  # ValueError: max() arg is an empty sequence

# Discussion
# If you try to perform common data reductions on a dictionary, you'll find that they only
# process the keys, not the values, For example:
print(min(prices))  # AAPL
print(max(prices))  # IBM

# This probably not what you want because you're actually trying to perform a calculation
# involving the dictionary values. You might try to fix this using the values() method of a dictionary.
print(min(prices.values()))  # 10.75
print(max(prices.values()))  # 612.87

# Unfortunately, this is often not exactly what you want either. For example, you may want
# to know information about the corresponding keys(e.g, which stock has the lowest price?)
print(min(prices, key=lambda k: prices[k]))  # FB
print(max(prices, key=lambda k: prices[k]))  # AAPL

# However, to get the minimum value, you'll need to perform an extra lookup step. For Example:
min_value = prices[min(prices, key=lambda k:prices[k])]

# It should be noted that in calculations involving (value, key) pairs, the key will be
# used to determine the result in instances where multiple entries happen to have the same
# value. For instance, in calculations such as min() and max(), the entry with the smallest
# or largest key will be returned if there happen to be duplicate values. For example:
prices = {'ZZZ': 45.23, 'AAA': 45.23}
print(min(zip(prices.values(), prices.keys())))
# (45.23, 'AAA')
print(max(zip(prices.values(), prices.keys())))
# (45.23, 'ZZZ')
