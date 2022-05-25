#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    A decorator has been applied to a function, but you want to 'undo' it, gaining access to the
    original unwrapped function.
Solution
    __wrapped__ attribute
Discussion
    useful for debugging, introspection, and other operations involving function.
    However, it only works using '@wraps' or sets __wrapped__ attribute directly.

    built-in decorators @staticmethod, @classmethod create descriptor objects that don't follow
    this convention(instead, they store the original function in a __func__ attribute.)
"""

__author__ = 'Frankie Fu'
from functools import wraps


def somedecorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@somedecorator
def add(x, y):
    return x + y


if __name__ == '__main__':
    ori_add = add.__wrapped__
    print(ori_add(3, 4))


# Discussion
# multiple decorator
def decorator1(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 1')
        return func(*args, **kwargs)
    return wrapper


def decorator2(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Decorator 2')
        return func(*args, **kwargs)
    return wrapper


@decorator1
@decorator2
def add2(x, y):
    return x + y


# what happens when you call the decorated function and the original function through __wrapped__
if __name__ == '__main__':
    print(add2(2, 3))
    # Decorator 1
    # Decorator 2
    # 5

    add2.__wrapped__(2, 3)