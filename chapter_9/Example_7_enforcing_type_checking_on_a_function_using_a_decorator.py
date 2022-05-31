#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You want to optionally enforce type checking of function arguments as a kind of assertion or contract.
# Solution
    Illustrates the idea:
        @typeassert(int, int)
        def add(x, y)
            return x + y

        add(2, 3)  # 5
        add(2, 'hello')
        # TypeError: Argument y must be <class 'int'>
# Discussion
    1. global __debug__ variable.(-O or -OO). you may want to disable the functionality added by the decorator.
      To do this, simple have your decorator function return the function unwrapped.
        def decorate(func):
            if not __debug__:
                return func
    2.inspect.signature(). It involves examining and working with the argument signature of the function being wrapped.
      It allows you to extract signature information from a callable.

    3.sig.bind_partial(). Use it to perform a partial binding of the supplied types to argument names.
      bound_types.arguments is dictionary maps the argument names to the supplied values
      in the same order as the function signature.

    4.sig.bind() is like bind_partial() except that it dose not allow for missing arguments.
"""

__author__ = 'Frankie Fu'

# Solution
# implementation of the '@typeassert' decorator
from inspect import signature
from functools import wraps


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError('Argument {} must be {}'.format(name, bound_types[name]))
            return func(*args, **kwargs)

        return wrapper

    return decorate


# use this decorator is rather flexible, types can be specified by position or by keyword
@typeassert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)


print(f'__debug__: {__debug__}')
spam(1, 2, 3)
# 1, 2, 3
spam(1, 'hello', 3)
# 1 hello 3
# spam(1, 'hello', 'world')
# Argument z must be <class 'int'>

# Discussion
# inspect.signature()
sig = signature(spam)
print(sig)  # (x, y, z=42)
print(sig.parameters)  # OrderedDict([('x', <Parameter "x">), ('y', <Parameter "y">), ('z', <Parameter "z=42">)])
print(sig.parameters['z'].name)  # z
print(sig.parameters['z'].default)  # 42
print(sig.parameters['z'].kind)  # POSITIONAL_OR_KEYWORD

# bind_partial()
bound_types = sig.bind_partial(int, z=int)
print(bound_types)  # <BoundArguments (x=<class 'int'>, z=<class 'int'>)>
print(bound_types.arguments)  # 'x': <class 'int'>, 'z': <class 'int'>}

# bind()
bound_values = sig.bind(1, 2, 3)
print(bound_values.arguments)  # {'x': 1, 'y': 2, 'z': 3}

# Using this mapping, it is relatively easy to enforce the required assertions.
for name, value in bound_values.arguments.items():
    if name in bound_types.arguments:
        if not isinstance(value, bound_types.arguments[name]):
            raise TypeError()


# A somewhat subtle aspect of the solution is that the assertions do not get applied to unsupplied arguments with
# default values.
@typeassert(int, list)
def bar(x, items=None):
    if items is None:
        items = []
    items.append(x)
    return items


print(bar(2))  # [2]

# print(bar(2, 3))  # TypeError: Argument items must be <class 'list'>

print(bar(4, [1, 2, 3]))  # [1, 2, 3, 4]

"""
A final point of design discussion might be the use of decorator arguments versus function annotations.
Why not write the decorator to look at annotations like this?
    @typeassert
    def spam(x:int, y, z:int = 42)
        print(x, y, z)
        
One possible reason for not using annotations is that each argument to a function can only have a single 
annotation assigned. Thus, if the annotations are used for type assertions, they can't really be used for anything else.
Likewise, the @typeassert decorator won't work with functions that use annotations for a different purpose. 
By using decorator arguments, as shown in the solution, the decorator becomes a lot more general purpose 
and can be used with any function whatsoever-even funtions that use annotations.

"""


@typeassert(str, str)
def spam2(x: int, y, z: int = 42):
    print(x, y, z)


spam2('1', '3', 3)
# spam2(1, '2', 3)  # TypeError: Argument x must be <class 'str'>
