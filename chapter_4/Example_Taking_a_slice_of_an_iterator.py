#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You want to take a slice of data produced by an iterator, but the normal slicing operator doesn't work.
Solution
    itertools.islice() function is perfectly suited for taking slices of iterators and generators.
Discussion
    Iterators and generators can't normally be sliced, because no information is known about
    their length(and they don't implement indexing).

    It dose this by consuming and discarding all of the items up to the starting slice index.
    Further items are then produced by the islice object until the ending index has been reached.

    islice() will consume data on the supplied iterator, Since iterator can't be rewound, if going back,
    you should probably just return the data into a list first.
"""

__author__ = 'Frankie Fu'


def count(n):
    while True:
        yield n
        n += 1


c = count(0)
# TypeError: 'generator' object is not subscriptable
# c[10:20]

# Solution
# Now using islice()
import itertools


for x in itertools.islice(c, 10, 20):
    print(x)
