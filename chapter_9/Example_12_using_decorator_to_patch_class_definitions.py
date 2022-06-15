#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You want to inspect or rewrite protions of a class definition to alter its behavior, but without
    using inheritance or metaclasses.
Solution
    This might be perfect use for a class decorator.
Discussion
    Class decorators can often be used as a straightforward alternative to other more advanced techniques
    involving mixins or metaclass.

    In some sense, the class decorator solution is much more direct in how it operates, and it doesn't
    introduce new dependencies into the inheritance hierarchy. As it turns out, it's also just a bit faster,
    due to not relying on the "super()" function.

    decorator order: before a decorator that simply wraps an existing method with some extra logic.
"""

__author__ = 'Frankie Fu'


# Solution
# For example, here is a class decorator that rewrites the __getattribute__ special method to perform logging.
def log_getattribute(cls):
    # Get the original implementation
    ori_getattribute = cls.__getattribute__

    # Make a new definition
    def new_getattribute(self, name):
        print('getting:', name)
        return ori_getattribute(self, name)

    # Attach to the class and return
    cls.__getattribute__ = new_getattribute
    return cls


# Example use
@log_getattribute
class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass


# Here is what happens if you try to use the class in the solution
a = A(42)
print(a.x)

a.spam()


# Discussion
# For example, an alternative implementation of the solution might involve inheritance.
class LoggedGetattribute:
    def __getattribute__(self, name):
        print('getting:', name)
        return super().__getattribute__(name)


# Example
class B(LoggedGetattribute):
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass


b = B(2)
print(b.x)
b.spam()
