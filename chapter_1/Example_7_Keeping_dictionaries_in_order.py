#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Problem
    You want to create a dictionary, and also want to control the order of items
    when iterating or serializing.
Solution
    To control the order of items in a dictionary, you can use an "OrderedDict" from the collections module.
Discussion
    An Ordered internally maintains a doubly linked list that orders the keys according to insertion order.
        when insert, it place at the end of the list.
        existing key doesn't change the order.
    The size of OrderedDict is more than twice as large as a normal dictionary.
        you would need to study the requirements of your application to determine if the
        benefits of using an OrderedDict outweighed the extra memory overhead.
"""

__author__ = 'Frankie Fu'

from collections import OrderedDict

# Solution
# OrderedDict, It exactly preserves the original insertion order of data when iterating.
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])

# An OrderedDict can be particularly useful when you want to build a mapping that you
# may want to later serialize encode into a different format. For example, If you want
# to precisely control the order of fields appearing in a JSON encoding, first building the
# data in an OrderedDict will do the trick.
import json

print(json.dumps(d))
# {"foo": 1, "bar": 2, "spam": 3, "grok": 4}
