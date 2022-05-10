#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You want to iterate in reverse over a sequence.
Solution
    1.Use the built-in reversed() function.
    2.the object has a size that can be determined.
    3.the object implements __reversed__ method.
    4.convert the object into a list first.
    ** turning an iterable into a list cloud consume a lot of memory if it's large.
Discussion
    Many programmers dont't realize that reversed iteration can be customized on user-defined
    classes if they implement the __reverse__ method().
    ** Defined a reversed iterator makes the code much more efficient, as it's no longer
    to pull the data into a list and iterate in reverse on the list.
"""

__author__ = 'Frankie Fu'

# Solution
a = [1, 2, 3, 4]

for x in reversed(a):
    print(x)


'''
Reversed iteration only work if the object in question has a size that can be
determined or if the object implements __reversed__ method. if neither of these
can be satisfied, you'll have to convert the object into a list first.
'''
# reversing file
f = open('./data/reversed_data.txt')
print(f"f['__reversed__']: {hasattr(f, '__reversed__')}")
print(f"list['__reversed__']: {hasattr(list, '__reversed__')}")
for line in reversed(list(f)):
    print(line, end='')


# Discussion
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


print("countdown: ")
countdown = CountDown(5)
for x in countdown:
    print(x)

print("countdown reversed: ")
for x in reversed(countdown):
    print(x)