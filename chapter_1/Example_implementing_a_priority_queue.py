#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Problem
    You want to implement a queue that sorts items by give priority and always returns
    the item with the highest priority on each pop operation.
Solution
    uses the 'heapq' module to implement a simple priority queue.
Discussion
    The core of this recipe concerns the use of the heapq module. The functions heapq.heappush()
    and heapq.heappop() insert and remove items from a list _queue in a way such that
    the first item in the list has the smallest priority. The heappop() method always
    returns the "smallest" item, so that the key to making the queue pop the correct items.
    Moreover, since the push and pop operations have O(logN) complexity where N is the
    number of items in the heap, they are fairly efficient even for fairly large values of N.

    (priority, index, item) tuples.
"""

__author__ = 'Frankie Fu'
import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


# Here is an example of how it might be used:
class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Item({self.name})'


q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)
print(q._queue)

print(q.pop())
# Item(bar)
print(q.pop())
# Item(spam)
print(q.pop())
# Item(foo)
print(q.pop())
# Item(grok)


# Discussion
# In this recipe, the queue consists of tuples of the form(-priority, index, item). The
# priority value is negated to get the queue to sort items from highest priority to
# lowest priority. This is opposite of the normal heap ordering, which sorts from lowest
# to highest value.

# To elaborate on that, instances of Item in the example can't be ordered.
a = Item('foo')
b = Item('bar')
# print(a < b)
# TypeError: '<' not supported between instances of 'Item' and 'Item'

a = (1, Item('foo'))
b = (5, Item('bar'))
print(a < b)
# True
c = (1, Item('grok'))
# print(a < c)
# TypeError: '<' not supported between instances of 'Item' and 'Item'

# By introducing the extra index and making(priority, index, item) tuples, you avoid
# this problem entirely since no two tuples will ever have the same value for index(and
# Python never bothers to compare the remaining tuple values once the result of comparison
# can be determined)
a = (1, 0, Item('foo'))
b = (4, 1, Item('bar'))
c = (1, 2, Item('grok'))
print(a < b)
# True
print(a < c)
# True









