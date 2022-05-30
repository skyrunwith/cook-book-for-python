#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You would like to write a single decorator that can be used without argument, such as "@decorator",
    or with optional arguments, such as "@decorator(x,y,z)". However, there seems to be no straightforward
    way to do it due to differences in calling conventions between simple decorators nad decorators taking arguments.
Solution
    '* function arguments'.
Discussion
    clever trick involving functools.partial.
        On the initial invocation of 'logged()'. the function to be wrapped is not passed.
        Thus in the decorator, it has to be optional. This, in turn, forces the other
        arguments to be specified by keyword.
        Furthermore, when arguments are passed, a decorator is supposed to return a function
        that accepts the function and wraps it(see Recipe 9.5)
"""

__author__ = 'Frankie Fu'

from functools import wraps, partial
import logging


# Solution
# Here is a variant of the logging code in 'Recipe 9.5' that define such as decorator.
def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)
    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper


# Example use
"""
As you can see from the example, the decorator can be used in both a simple form(i.e., @logged)
or with optional arguments supplied(i.e, @logged(level=logging.CRITICAL, name='example'))
"""


@logged
def add(x, y):
    return x + y


@logged(level=logging.CRITICAL, name='example')
def spam():
    print('Spam!')


if __name__=='__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    add(2, 3)
    spam()


# Discussion
# a decorator where all arguments are optional could be applied, like this:
@logged()
def add2(x, y):
    return x + y


if __name__=='__main__':
    print(add2(3, 4))