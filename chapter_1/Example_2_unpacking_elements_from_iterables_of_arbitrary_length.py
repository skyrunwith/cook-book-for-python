#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You need to unpack N elements from an iterable, but the iterable may be longer than N elements, causing a
    "too many values to unpack" exception.
Solution
    "start expression"
"""

__author__ = 'Frankie Fu'


# Solution
# suppose you run a course and decide at the end of semester that you're going
# to drop the first and last homework grades, and only average the rest of them.
# If there are only four assignments, maybe you simply unpack all four, but what
# if there are 24? A start expression make it easy:

def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle) / len(middle)


print(drop_first_last([4, 5, 6, 7]))

# As another use case, suppose you have user records that consist of a name and
# email address, followed by an arbitrary number of phone number. You could unpack
# records like this:
record = ('Dave', 'dave@example.com', '772-222-2222', '323-323-3231')
name, email, *phone_numbers = record
print(name, email, phone_numbers)

# The starred variable can also be the first one in the list.
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)

# Discussion
# It is worth noting that the star syntax can be especially useful when iterating
# over a sequence of tuples of varying length.
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# Star unpacking can also be useful when combined with certain kinds of string
# processing operations, such as spliting.
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(":")
print(uname, homedir, sh)

# Sometimes you might want to unpack values and throw them away.
record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name, year)

# if you have a list, you can easyily split it into head and tail components like this:
items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head, tail)


# One could imagine writing functions that perform such spliting in order to
# carry out some kind of clever recursive algorithm.
def sum2(items2):
    head, *tail = items2
    return head + sum(tail) if tail else head


print(sum2(items))
