#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You want to put a wrapper layer around a function that adds extra processing(e.g, logging, timing, etc.)
Solution
    define a decorator function.
Discussion
    1.
    A decorator is a function that accepts a function as input and returns a new function as output.
        @timethis
        def countdown(n):
            ...
    it's the same as if you had performed these separate steps
        def countdown(n):
            ...
        countdown = timethis(countdown)
    As an aside, built-in decorator such as @staticmethod, @classmethod, and @property
    work in the same way.
        class A:
            @classmethod:
            def method(cls):
                ...
        class B:
            def method(self):
                ...
            method = classmethod(method)

    2. a decorator accepts any arguments using *args and **kwargs with wrapper() function.
    you can place a call to the original input function and return its result, place extra code
    you want to add(e.g timing).
    The newly created function wrapper is returned as a result and take the place of the original
    function.
"""

__author__ = 'Frankie Fu'

import time
from functools import wraps


def timethis(func):
    """
    Decorator that reports the execution time.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


# Using the decorator
@timethis
def countdown(n):
    """
    Counts down
    """
    while n > 0:
        n -= 1


countdown(1000000)

# Discussion
countdown_de = timethis(countdown)
countdown_de(1000000)


class A:
    @classmethod
    def method(cls):
        print('Class A method')


class B:
    def method(cls):
        print('Class B method')

    method = classmethod(method)


A.method()
B.method()