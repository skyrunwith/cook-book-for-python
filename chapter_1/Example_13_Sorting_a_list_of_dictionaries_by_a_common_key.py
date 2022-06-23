#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You have a list of dictionaries and you would like to sort the entries according to one
    or more of the dictionary values.
Solution
    using the operator module's itemgetter.
Discussion
    sorted function, which accepts a keyword argument "key", This argument is expected
    to be a callable that accepts a single item from rows as input and returns a value
    that will be used as the basis for sorting.

    operator.itemgetter() arguments:
        a dictionary key name,
        a numeric list element,
        any value that can be fed to an object's __getitem__() method.
        tuple.

    itemgetter() typically runs a bit faster.
"""

__author__ = 'Frankie Fu'
# Solution
# Let's say you've queried a database table to get a listing of the members on your website,
# and you receive the following data structure in return:
rows = [
 {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
 {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
 {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
 {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

# It's fairly easy to output these rows ordered by any of the fields common to all of the
# dictionaries.
from operator import itemgetter
rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

# The itemgetter() function can also accept multiple keys.
rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

# Discussion
# The functionality of itemgetter() is sometimes replaced by lambda expressions.
rows_by_fname = sorted(rows, key=lambda r: r['fname'])
rows_by_uid = sorted(rows,key=lambda r: (r['lname', r'fname']))

# applied to functions such as min() and max()
print('min: ', min(rows, key=itemgetter('uid')))
print('max: ', max(rows, key=lambda r: r['uid']))


