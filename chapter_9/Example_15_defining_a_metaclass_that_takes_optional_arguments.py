#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
Problem
    You want to define a metaclass that allows class definitions to supply optional arguments, possibly to control
    or configure aspects of processing during type creation.
Solution
    When defining classes, Python allows a metaclass to be specified using the metaclass keyword argument
    in the class statement.
Discussion
    1. Adding optional keyword arguments to a metaclass requires that you understand all of the steps involved in
    class creation, because the extra arguments are passed to every method involved.
        The __prepare__() method is called first and used to create the class namespace prior to the body of any
        class definition being processed. Normally, this method simply returns a dictionary or other mapping object.

        The __new__() method is used to instantiate the resulting type object. It is called after the class body has
        being fully executed.

        The __init__ method is called last and used to perform any additional initialization steps.

    When writing metaclasses, it is somewhat common to only define 'a __new__() or __init__() method', but not both.
    However, if extra keyword arguments are going to be accepted, then both methods must be provided and given
    compatible signatures. THe default __prepare__() method accepts any set of keyword arguments, but ignores them.
    You only need to define it yourself if the extra arguments would somehow affect management of the class
    namespace creation.

    2. The use of keyword-only arguments in this recipe reflects the fact that such arguments will only be supplied
    by keyword during class creation.

    3. Advantage:
        don't pollute the class namespace with extra names that only pertain to class creation and not the subsequent
        execution of statements in the class.
        they are available to the __prepare__() method, Class Variables only by accessible in __new__() and __init__()
        methods of a metaclass.
"""

__author__ = 'Frankie Fu'
from abc import ABCMeta, abstractmethod


class IStrem(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxsize=None):
        pass

    @abstractmethod
    def write(self, data):
        pass


# However, in custom metaclass, addtional keyword arguments can be supplied, like this:
class MyMeta(type):
    # Optional
    @classmethod
    def __prepare__(metacls, name, bases, *, debug=False, synchronize=False):
        # Custom Processing
        print(f'__prepare__: debug={debug}, synchronize={synchronize}')
        return super().__prepare__(name, bases)

    # Required
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        print(f'__new__: debug={debug}, synchronize={synchronize}')
        return super().__new__(cls, name, bases, ns)

    # Required
    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        # Custom processing
        print(f'__init__: debug={debug}, synchronize={synchronize}')
        super().__init__(name, bases, ns)


class Spam(metaclass=MyMeta, debug=True, synchronize=True):
    def __init__(self):
        pass


# The specification of keyword arguments to configure a metaclass might be viewed as an alternative to using class
# variables for a similar purpose.
class Spam2(metaclass=MyMeta):
    debug = True
    synchronize = True


print(Spam())
print(Spam2.debug, Spam2.synchronize)
