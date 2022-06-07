#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You want to define a decorator inside a class definition and apply it to other functions or methods.
Solution
    It's straightforward, but you first need to sort out the manner in which the decorator will be applied,
    whether it is applied as an instance or a class method.
Discussion
    built-in @property decorator is actually a class withe getter(), setter() and deleter methods that
    each act as a decorator.



"""

__author__ = 'Frankie Fu'

# Solution
# difference in instance or class method.
from functools import wraps


class A:
    # Decorator as an instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 1')
            return func(*args, **kwargs)

        return wrapper

    # Decorator as a class method
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('Decorator 2')
            return func(*args, **kwargs)

        return wrapper


# Here is an example of how the two decorators would be applied:

# As an instance method
a = A()


@a.decorator1
def spam():
    pass


@A.decorator2
def grok():
    pass


spam()
grok()


# Discussion
class Person:
    # Create a property instance
    first_name = property()

    # Apply decorator methods
    @first_name.getter
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')
        self._first_name = value


# inheritance
class B(A):
    @A.decorator2
    def bar(self):
        pass

