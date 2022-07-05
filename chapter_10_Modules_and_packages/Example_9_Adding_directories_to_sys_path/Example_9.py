#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Adding Directories to sys.path
Problem
    You have Python code that can't be imported because it's not located in a directory listed
    in sys.path. You would like to add new directories to Python's path, but don't want to hardwire
    into your code.
Solution
    First, PYTHONPATH environment variable.
    Second, create .pth file located in site-packages directories.
Discussion
    sys.path.insert() function.
    from os.path import abspath, join, dirname
"""

__author__ = 'Frankie Fu'

# Solution
# There are two common ways to get new directories added to sys.path. First, you can add them through
# the use of the PYTHONPATH environment variable.
import sys
# PYTHONPATH
print(sys.path)

# In a custom application, this environment variable could be set at program startup or through
# a shell script of some kind.

# The second approach is to create a .pth file that lists the directories like this:
'''
# myapplication.pth
/some/dir
/other/dir
'''

# This .pth file needs to be placed into one of Python's site-packages directories, which are
# typically located at /usr/local/lib/python3.3/site-packages or ~/.local/lib/python3.3/site-packages.
# On interpreter startup, the directories listed in the .pth file will be added to sys.path as long as
# they exist on the filesystem. Installation of a .pth file might require administrator access if it's
# being added to the system-wide Python interpreter.

# Discussion
# Faced with trouble locating files, you might be inclined to write code that manually adjusts the value
# of sys.path. For example:
import sys

sys.path.insert(0, 'some/dir')
sys.path.insert(0, 'other/dir')
print('discussion:', sys.path)
# discussion: ['other/dir', 'some/dir', ...]

# Although this "works", it is extremely fragile in practice and should be avoided if posible. Part of
# the problem with this approach is that it adds hardcoded directory names to you source.
# This can cause maintenance problems if your code ever gets moved around to a new location. It's usually
# much better to configure the path elsewhere in a manner that can be adjusted without making source code edits.

# You can sometimes work around the problem of hardcoded directories if you carefully construct an appropriate
# absolute path using module-level variables, such as __file__.
import sys
from os.path import abspath, join, dirname

sys.path.insert(0, abspath((join(dirname(__file__), 'src'))))

print('absolute path: ', sys.path)
# C:\\Users\\frankie\\PycharmProjects\\cook-book-for-python\\chapter_10_Modules_and_packages\\Example_9_Adding_directories_to_sys_path\\src

# This adds an src directory to the path where that directory is located in the same directory as the code
# that's executing the insertion step.

# The site-packages directories are the locations where third-party modules and packages normally
# get installed. If your code was installed in that manner, that's where it would be placed.
# Although .pth files for configuring the path must appear in site-packages, they can refer to
# any directories on the system that you wish. Thus, you can elect to have your code in a completely
# different set of directories as long as those directories are included in a .pth file.






















