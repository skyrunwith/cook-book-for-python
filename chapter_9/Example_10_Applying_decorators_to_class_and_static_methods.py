#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You want to apply a decorator to a class or static method.
Solution
    Applying decorators to class and static methods is straightforward, but make sure that your decorators are applied
    before @classmethod or @staticmethod.
Discussion
    1. If you get the order of decorators wrong, you'll get an error.
      ** Making sure that these decorators appear first in the decorator list fixes the problem.
    2. Defining class and static methods in abstract class method
"""

__author__ = 'Frankie Fu'

import time
from functools import wraps


# Solution
# A simple decorator
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return r

    return wrapper


# Class illustrating application of the decorator to different kinds of methods
class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1


# The resulting class and static methods should operate normally, but have the extra timing.
s = Spam()
s.instance_method(1000000)

Spam.class_method(1000000)

Spam.static_method(1000000)


# Discussion
class Spam2:

    @timethis
    @staticmethod
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1


# TypeError: 'staticmethod' object is not callable
# Spam2.static_method(1000000)


# define an abstract class method
from abc import ABCMeta, abstractmethod


class A(metaclass=ABCMeta):
    """
    In this code, the order of @classmethod and @abstractmethod matters.
    If you flip the two decorators around, everything breaks.
    """
    @classmethod
    @abstractmethod
    def method(cls):
        pass
