#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Problem
    You have code organized as a package and want to import a submodule from one of the other
    package submodules without hardcoding the package name into the import statement.
Solution
    use a package relative import.
        from . import grok
        from .. B import bar
Discussion
    This also won't work if parts of a package are executed directly as a script.
        % python3 mypackage/A/spam.py  # Relative imoprts fail
    if you execute the preceding script using the -m option to Python, the relative imports
    will work properly.
        % python3 -m mypackage.A.spam  # Relative imports work

    PEP328: http://www.python.org/dev/peps/pep-0328
        more background on relative package imports.
"""

__author__ = 'Frankie Fu'

# Solution
# To import modules of a package from other modules in the same package, use a package relative import.
# For example, suppose you have a package 'mypackage' organized as follows on the filesystem.
'''
mypackage/
    __init__.py
    A/
        __init__.py
        spam.py 
        grok.py
    B/
        __init__.py 
        bar.py
'''
# If the module mypackage.A.spam wants to import the module grok located in the same directory,
# it should include an import statement like this:
# mypackage/A/spam.py
# from . import grok
from mypackage import A

# If the same module wants to import the module B.bar located in a different directory,
# it can use an import statement like this:
'''
# mypakage/A/spam.py
# from ..B import bar
'''

# Both of the import statements shown operate relative to the location of the spam.py file and
# do not include the top-level package name.

# Discussion
# Inside packages, imports involving modules in the same package can either use fully
# specified absolute names or a relative imports using the syntax shown. For example:
'''
# mypackage/A/spam.py
# from mypackage.A import grok  # OK
# from . import grok  # OK
# import grok  #  Error (not found)
'''



