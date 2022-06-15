#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You want to change the way in which instances are created in order to implements singleton, caching,
    or other similar features.
Solution
    As python programmers know, if you define a class, you call it like a function to create instances.
    singleton, cached.
Discussion
    Using a metaclass to implements various instance creation patterns can often be a much more elegant
    approach than other solutions not involving metaclass.

    Although the solution involving metaclasses involves a much more advanced concept, the resulting code
    feels cleaner and less hacked together.
"""

__author__ = 'Frankie Fu'


# Solution
# call it like a function to create instance.
class Spam:
    def __init__(self, name):
        self.name = name


a = Spam('Guido')
b = Spam('Diana')
c = type(Spam).__call__(Spam, 'c')
print(a.name, b.name, c.name)

"""
If you want to customize this step, you can do it by defining a metaclass and reimplement its __call__() method
in some way. To illustrate, suppose that you didn't want anyone creating instance at all.
"""
class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")


# Example
class Spam(metaclass=NoInstances):
    @staticmethod
    def grok(x):
        print('Spam.grok')


# In this case, users can call the defined static method, but it's impossible to create an instance in normal way.
Spam.grok(42)
# TypeError: Can't instantiate directly
# s = Spam()
