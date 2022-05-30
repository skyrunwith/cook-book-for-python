#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    you want to write a decorator function that takes arguments.
Solution
    def outer function(arguments)
        def inner decorator(func):
            @wraps(func)
            def wrapper()
    outermost function accepts the desired arguments.
    inner function accepts a function and puts a wrapper around it as normal.
    key part is that the wrapper is allowed to use the arguments passed to outer function.

"""

__author__ = 'Frankie Fu'
from functools import wraps
import logging


# Solution
def logged(level, name=None, message=None):
    """
    Add logging to a function. level is the logging
    level, name is the logger name, and message is the
    log message. If name and message aren't specified,
    they default to the function's module and name.
    """
    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper
    return decorate


# Example use
@logged(level=logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    print(add(3, 4))
    spam()


# Discussion
# underlying calling sequence involved.
'''
@decorator(x, y, z)
def func(a, b):
    pass
    
The decoration process evaluates as follows:
def func(a, b): 
    pass
func = decorator(x, y, z)(func)
'''

add_w = logged(logging.CRITICAL)(add)
print(add_w(1, 2))