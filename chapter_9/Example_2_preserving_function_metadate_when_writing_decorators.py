#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You've written a decorator, but when you apply it to a function, important metadata such as
    the name, doc string, annotations, and calling signature are lost.
Solution
    Whenever you define a decorator, you should always remember to apply the @wraps decorator from
    the functools library to the underlying wrapper function.
    __name__, __doc__, __annotations__
Discussion
    __wrapped__,
    signature()
"""

__author__ = 'Frankie Fu'

import time
from functools import wraps


# Solution
# Here is an example of using the decorator and examining the resulting function metadata:
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


@timethis
def countdown(n: int):
    """
    Counts down
    """
    while n > 0:
        n -= 1


countdown(1000000)

print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)

# Discussion
# if omitting use @wraps, the metadata in the last example would look like this:
print(countdown.__name__)  # wrapper
print(countdown.__doc__)  # None
print(countdown.__annotations__)  # {}

# @wraps makes the wrapped function available to you in the __wrapped__ attribute.
countdown.__wrapped__(1000000)

# The presence of the __wrapped__ attribute also makes decorated functions properly expose
# the underlying signature of the wrapped function.
from inspect import signature

print(signature(countdown))
# (n: int)
# 如果没有 @wraps, 会打印 (*args, **kwargs)
