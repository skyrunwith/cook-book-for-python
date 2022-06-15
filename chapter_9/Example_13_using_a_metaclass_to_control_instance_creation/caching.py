#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""  """

__author__ = 'Frankie Fu'
import weakref


class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()

    def __call__(self, *args, **kwargs):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args, **kwargs)
            self.__cache[args] = obj
            return obj


# Example
class Spam(metaclass=Cached):
    def __init__(self, name):
        print('Creating Spam({!r})'.format(name))


# Here's an example showing the behavior of this class:
a = Spam('Guido')

b = Spam('Diana')

c = Spam('Guido')  # Cached
# False
print(a is b)
# True
print(a is c)  # Cached value returned

