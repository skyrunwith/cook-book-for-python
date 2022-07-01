#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You want precise control over the symbols that are exported from a module or package
    when a user uses the from module import * statement.
Solution
    Define a variable __all__ in your module that explicitly lists the exported names.
Discussion
    __all__:
    Although the use of from module import * is strongly discouraged, it still sees frequent
    use in modules that define a large number of names. If you don't do anything, this form
    of import will export all names that don't start with an underscore. On the other hand,
    if __all__ is defined, then only the names explicitly listed will be exported.

    If you define __all__ as an empty list, then nothing will be exported. An attributeError
    is raised on import if __all__ contains undefined names.
"""

__author__ = 'Frankie Fu'

# Solution
# somemodule.py
from somemodule import *

print(dir())

