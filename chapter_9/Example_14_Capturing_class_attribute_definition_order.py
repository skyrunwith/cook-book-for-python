#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution
    You want to automatically record the order in which attributes and methods are defined inside a class
    body so that you can use it in various operations(e.g, serializing, mapping to database, etc.).
Solution
    Capturing information about the body of class definition is easily accomplished through the use of a
    metaclass.(eg, use an OrderedDict to capture definition order of descriptors)
Discussion
    1. The entire key to this recipe is the __prepare__() method, which is defined in the OrderedMeta metaclass.
    This method is invoked immediately at the start of a class definition with the class name and base classes.
    It must then return a mapping object use when processing the class body. By returning an OrderedDict instead
    of a normal dictionary, the resulting definition order is easily captured.

    2. A final important part of this recipe concerns the treatment of the modified dictionary in the metaclass
    __new__() method. Even though the class was defined using an alternative dictionary, you still have to
    convert this dictionary to a proper dict instance when making the final class object. This is the purpose
    of the 'd = dict(clsdict)' statement.

    3. Being able to capture definition order is a subtle but important feature for certain kinds of applications.
    For instance, in an object relational mapper, classes might be written in a manner to shown in the example:
        class Stock(Model):
            name = String()
            shares = Integer()
            price = Float()
    Underneath the covers, the code might want to capture the definition order to map objects to tuples or
    rows in database table(eg, as_csv method). The solution shown is very straightforward and often simpler
    than alternative approaches(which typically involve maintaining hidden counters within the descriptor classes).

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


# Discussion
# It is possible to extend this functionality even further if you willing to make your own dictionary-like objects.
# For example, consider this variant of the solution that rejects duplicate definitions:

class NoDupOrderedDict(OrderedDict):
    def __init__(self, clsname):
        self.clsname = clsname
        super().__init__()

    def __setitem__(self, name, value):
        if name in self:
            raise TypeError('{} already defined in {}'.format(name, value))
        super().__setitem__(name, value)


class OrderedMeta2(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        d['_order'] = [name for name in clsdict if name[0] != '_']
        return type.__new__(cls, clsname, bases, d)

    @classmethod
    def __prepare__(metacls, clsname, bases):
        return NoDupOrderedDict(clsname)


# Here's what happens if you use this metaclass and make a class with duplicate entries:
class A(metaclass=OrderedMeta2):
    def spam(self):
        pass

    # TypeError: spam already defined in <function A.spam at 0x0000023804A05430>
    # def spam(self):
    #     pass




