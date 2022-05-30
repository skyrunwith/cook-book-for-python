#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You want to write a decorator function that wraps a function, but has user adjustable attributes
    that can be used to control the behavior of the decorator at runtime.
Solution
    accessor functions.
        change internal variables through the use of "nonlocal" variable declarations.
        The accessor functions are then attached to the wrapper function as function attributes.
Discussion
    The key to this recipe in the accessor functions(eg. set_message() and set_level()) that get
    attached to the wrapper as attributes. Each of these accessors allows internal parameters to be
    adjusted through the use of nonlocal assignments.

    if all of your decorators utilize @function.wraps. accessor functions will propagate through
    multiple levels of decoration.

    accessor functions to return the value of various setting cloud also be written just as easily
    by add extra code such as this:
        @attach_wrapper(wrapper)
        def get_level():
            return level

        # Alternative
        wrapper.get_level = lambda: level

"""

__author__ = 'Frankie Fu'

from functools import wraps, partial
import logging


# Solution

# Utility decorator to attach of function as an attribute of obj
def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        # Attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper
    return decorate


# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, 'example')
def spam():
    print('Spam!')


if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.DEBUG)
    add(2, 3)  # DEBUG:__main__:add

    # Change the log message
    add.set_message('Add called')
    add(2, 3)  # DEBUG:__main__:Add called

    # Change the log level
    add.set_level(logging.WARNING)
    add(2, 3)  # WARNING:__main__:Add called