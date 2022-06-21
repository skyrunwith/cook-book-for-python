#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You want to make a list of the largest or smallest N items in a collection.
Solution
    The 'heapq' module has two functions-nlargest() and nsmallest()-that do exactly
    what you want.
Discussion
    If you are looking for the N smallest or largest items and N is small compared to
    the overall size of the collection, these functions provide superior performance.

    nlargest() and nsmallest() is adaptive in how it operates and will carry out of some of thest
    optimizations on your behalf.
        min, max, sored(item)[:N]
"""

__author__ = 'Frankie Fu'
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

# Both functions also accept a key parameter that allows them to be used with more
# complicated data structures.
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])

print(cheap)
print(expensive)


# Discussion
# Underneath the covers, they work by first converting the data into a list where items
# are ordered as a heap.
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heap)


# The most important feature of a heap is that heap[0] is always the smallest item.
# subsequent items can be easily found using heapq.heappop() method. Which pops off
# the first item and replaces it with the next smallest item(an operation that requires)
# O(log N) operations where N is the size of the heap).
print(heapq.heappop(heap))

print(heapq.heappop(heap))

print(heapq.heappop(heap))











