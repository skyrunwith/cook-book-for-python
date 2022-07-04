#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Making a Directory or Zip File Runnable As a Main Script
Problem
    You have a program that has grown beyond a simple script into an application involving
    multiple files. You'd like to have some easy way for users to run the program.
Solution
    __main__.py
        If your application program has grown into multiple files, you can put it into its own
        directory and add a __main__.py file.
Discussion
    __main__.py
        it just means this bundle of code that you want to hand someone to execute.
"""

__author__ = 'Frankie Fu'

# Solution
'''
myapplication/
    spam.py
    bar.py
    grok.py
    __main__.py
'''

# If __main__.py is present, you can simply run the Python interpreter on the top-level
# directory like this:
'''
bash % python3 myapplication
'''

# The interpreter will execute the __main__.py file as the main program.

# This technique also works if you package all of your code up into a zip file.
'''
bash % ls
# spam.py bar.py grok.py __main__.py
bash % zip -r myapp.zip *.py
bash % python3 myapp.zip
'''

# Discussion
# Creating a directory or zip file and adding a __main__.py file is one possible way to
# package a large Python application. It's little bit different than a package in that the
# code isn't meant to be used as a standard library module that's installed into the Python
# library. Instead, it's just this bundle of code that you want to hand someone to execute.

# Since directories and zip files are a little different than normal files, you may also want
# to add a supporting shell script to make execution easier. For example, if the code was in a
# file named myapp.zip, you could make a top-level script like this:
'''
python3 /usr/local/bin/myapp.zip
'''



























