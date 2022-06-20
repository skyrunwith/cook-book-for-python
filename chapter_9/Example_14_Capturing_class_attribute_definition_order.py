#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution
    You want to automatically record the order in which attributes and methods are defined inside a class
    body so that you can use it in various operations(e.g, serializing, mapping to database, etc.).
Solution
    Capturing information about the body of class definition is easily accomplished through the use of a
    metaclass.(eg, use an OrderedDict to capture definition order of descriptors)
"""

__author__ = 'Frankie Fu'

from collections import OrderedDict


# Solution
# A set of descriptors for various types
class Typed:
    _excepted_type = type(None)

    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._excepted_type):
            raise TypeError('Expected ' + str(self._excepted_type))

        instance.__dict__[self._name] = value


class Integer(Typed):
    _excepted_type = int


class Float(Typed):
    _excepted_type = float


class String(Typed):
    _excepted_type = str


# Metaclass that uses an OrderedDict for class body
class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)

        d['_order'] = order
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(metacls, name, bases):
        return OrderedDict()


"""
In this metaclass, the definition order of descriptors is captured by using an Ordered Dict during the execution of 
class body. The resulting order of names is then extracted from the dictionary and stored into a class attribute _order. 
This can then be used by methods of the class in various ways.
For Example, here is a simple class that uses that ordering to implement a method for serializing the instance data as 
a line CSV data.
"""


class Structure(metaclass=OrderedMeta):
    def as_csv(self):
        return ",".join(str(getattr(self, name)) for name in self._order)


# Example use
class Stock(Structure):
    name = String()
    shares = Integer()
    price = Float()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price


# Here is an interactive session illustrating the use of the Stock class in example:
s = Stock('GOOD', 100, 490.1)

print(s.name)
# GOOD
print(s.as_csv())
# GOOD,100,490.1

# t = Stock('AAPL', 'a log', 610.23)
# TypeError: Expected <class 'int'>


