#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Reloading Modules
Problem
   You want to reload an already loaded module because you've made changes to its source.
Solution
     You want to previously loaded module, use 'importlib.reload()'.
Discussion
    It' for debugging.
"""

__author__ = 'Frankie Fu'

# Solution
import spam
import importlib
print(importlib.reload(spam))

# Discussion
# Reloading a module is something that is often useful during debugging and development,
# but which is generally never safe in production code due to the fact that it doesn't always
# work as you expect.

# Under the covers. the reload() operation wipes out the contents of a module's underlying
# dictionary and refreshes it by re-executing the module's source code. The identity of the
# module object itself remains unchanged. Thus, this operation updates the module everywhere
# that it has been imported in a program.

# However, reload() does not update definitions that have been imported using statements such
# as 'from module import name'.
'''
# spam.py
def bar():
    print('bar')
    
def grok():
    print('grok')
'''
import spam
from spam import grok

spam.bar()

grok()

# With out quitting Python. go edit the source to spam.py so that the function
# grok() look likes this:
'''
def grok():
    print('New grok')
'''

# Now go back to the interactive session, perform a reload, and try this experiment:
'''
import imp
imp.reload(spam)
spam.bar()
# bar
grok()  # Notice old output
# grok  
spam.grok()  # Notice new output
# New grok
'''
import spam
import importlib
importlib.reload(spam)  # debugging时，这儿打一个断点，然后去修改grok方法
spam.bar()
# bar
grok()  # Notice old output
# grok
spam.grok()  # Notice new output
# New grok

# In this example, you'll observe that there are two versions of the grok() function
# loaded. Generally, this is not what you want, and is just the sort of thing that eventually
# leads to massive headaches.

# For this reason, reloading of modules is probably something to be avoided in production code.
# Save it for debugging or for interactive sessions where you're experimenting with the interpreter
# and trying things out.


