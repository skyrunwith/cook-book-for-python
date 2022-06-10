#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You want to wrap functions with a decorator, but the result is going to be a callable instance.
    You need your decorator to work both inside and outside class definitions.
Solution
    To define a decorator as an instance, you need to make sure it implements the __call__() and __get__() methods.
Discussion
    There are some rather subtle details that deserve more explanation, especially if you plan to apply
    the decorator to instance methods.
    1. functools.wraps(): namely to copy important metadata from the wrapped function to callable instance.

    2. It is common to overlook the __get__() method shown in the solution. If you omit the __get__() and
    keep all of the other code the same, you'll find that bizarre things happen when you try to invoke
    decorated instance methods. For example:
        s = Spam()
        s.bar(3)
        TypeError: spam() missing 1 required positional argument: 'x'

    The reason it breaks is that whenever functions implementing methods are look up in a class, their __get__() method
    is invoked are as part of the descriptor protocol.
    In this case, the purpose of __get__() is to create a bound method object(which ultimately supplies the self
    argument to the method).

    3. bound method: if the method is accessed on a class, the instance argument to __get__() is set to None and the
    Profiled instance itself is just returned. This makes it possible for someone to extract its ncalls attribute.

    4. If you want to avoid some of this of this mess, you might consider an alternative formulation of the decorator
    using closures and nonlocal variables, as described in Recipe 9.5.

"""

__author__ = 'Frankie Fu'

# Solution
# this code defines a class that puts a simple profiling layer around another function.
import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


# Use this class, you use it like a normal decorator, either inside or outside of a class:
@Profiled
def add(x, y):
    return x + y


class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


# Here is interactive session that shows how these functions work:
print(add(2, 3))  # 5

print(add(4, 5))  # 9

print(add.ncalls)  # 2

s = Spam()

s.bar(1)

s.bar(2)

s.bar(3)

print(Spam.bar.ncalls)

# Discussion
# 3.__get__() is to create a bound method object.
s = Spam()


def grok(self, x):
    pass


print(grok.__get__(s, Spam))
# <bound method grok of <__main__.Spam object at 0x000001B4B6FCD4F0>>


# 4. using closures and nonlocal variables
# This example almost works in exactly the same way except that access to ncalls is now provided through a function
# attached as a function attribute.
def profiled(func):
    ncalls = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)

    wrapper.ncalls = lambda: ncalls
    return wrapper


print(add(2, 3))

print(add(4, 5))

print(add.ncalls)
