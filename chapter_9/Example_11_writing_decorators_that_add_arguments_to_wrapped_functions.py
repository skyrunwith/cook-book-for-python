#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Problem
    You want to write a decorator that adds an extra argument to the calling signature of the wrapped function.
    However, the added argument can't interfere with the existing calling conventions of the function.

Solution
   1. Extra arguments can be injected into the calling signature using keyword-only arguments.
Discussion
    1. Adding arguments to the signature of wrapped functions is not the most common example of using decorators.
    However, it might be a useful technique in avoiding certain kinds of code replication patterns.
        def a(x, debug =False):
            if debug:
                print('Calling a')
            ...

        def b(x, y, z, debug=False):
            if debug:
                print('Calling b)
            ...

        def c(x, y, debug=False):
            if debug:
                print('Calling c')

    refactor it into following:
        @optional_debug
        def a(x):
            ...

        @optional_debug
        def b(x, y, z):
            ...

        @optional_debug
        def c(x, y):
            ...

    2. One tricky part here concerns a potential name clash between the added argument and the arguments of the function
    being wrapped. For example, if the optional_debug decorator was applied to a function that already had a debug
    argument, then it would bread. If that's a concern, an extra check could be added.
"""

__author__ = 'Frankie Fu'

# Solution
# 1. Extra  arguments can be injected into the calling signature using keyword-only arguments.
from functools import wraps


def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    return wrapper


@optional_debug
def spam(a, b, c):
    print(a, b, c)


spam(1, 2, 3)

spam(1, 2, 3, debug=True)

# Discussion
# 2.
from functools import wraps
import inspect


def optional_debug2(func):
    if 'debug' in inspect.getfullargspec(func).args:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(args, **kwargs)

    # fixed signature
    sig = inspect.signature(func)
    parms = list(sig.parameters.values())
    parms.append(inspect.Parameter('debug', inspect.Parameter.KEYWORD_ONLY, default=False))
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper


# A final refinement to this recipe concerns the proper management of function signatures. An astute programmer will
# realize that the signature of wrapped functions is wrong.
@optional_debug2
def add(x, y):
    return x + y


# (x, y) vs (x, y, *, debug=False)
print(inspect.signature(add))


# TypeError: debug argument already defined
# @optional_debug2
# def add_error(x, y, debug=False):
#     ...