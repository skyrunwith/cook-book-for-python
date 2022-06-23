#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Problem
    You want to sort objects of the same class, but they don't natively support comparison
    operations.
Solution
    sorted() key argument(key lambda)
    operator.attrgetter()
Discussion
    attrgetter() is often a tad bit faster.
    allowing multiple fields to be extracted simultaneously.
"""

__author__ = 'Frankie Fu'


# Solution
# If you have a sequence of User instance in your application, and you want to
# sort them by their user_id attribute, you would supply a callable that takes a User
# instance as input and return the user_id.
class User:
    def __init__(self, user_id, fname, lname):
        self.user_id = user_id
        self.fname = fname
        self.lname = lname

    def __repr__(self):
        return f'User({self.user_id}, {self.fname}, {self.lname})'


users = [User(23, 'Brian', 'Jones'), User(3, 'David', 'Beazley'), User(99, 'John', 'Cleese')]
print(users)

print(sorted(users, key=lambda u: u.user_id))

# Instead of using lambda, an alternative approach is to use 'operator.attrgetter()'
from operator import attrgetter

print(sorted(users, key=attrgetter('user_id')))

# Discussion
# If User instance also had a first_name and last_name attribute, you could perform
# a sort like this:
by_name = sorted(users, key=attrgetter('lname', 'fname'))
print('by_name: ', by_name)

print('lambda by_name: ', sorted(users, key=lambda u: (u.lname, u.fname)))

# It also worth noting that the technique used in this recipe can be applied to functions
# such as min() and max().
print(min(users, key=attrgetter('user_id')))

print(max(users, key=attrgetter('user_id')))