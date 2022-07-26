#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Handling HTML and XML Entities in Text
Problem
    You want to replace HTML or XML entities such as &entitiy; or &#code; with their corresponding text.
    Alternatively, you need to produce text, but escape certain characters(e.g, <, >, or &)
Solution
    If you are producing text, replacing special characters such as < or > is relatively easy if you
    use the html.escape() function.

    html.escape(), html.unescape(), str.encode(), xml.sax.saxutils.unescape()
Discussion
    Proper escaping of special characters is an easily overlooked detail of generating HTML or XML.
    This is especially true if you're generating such output yourself using print() or other basic
    string formatting features. Using a utility function such as 'html.escape()' is an easy solution.

    If you need to process text in the order direction, various utility functions, such as
    'xml.sax.saxutils.unescape()', can help. However, you really need to investigate the use of a proper
    parser. For example, if processing HTML or xml, using a parsing module such as html.parser or
    xml.etree.ElementTree should already take care of details related to replacing entities in the input
    text for you.
"""

__author__ = 'Frankie Fu'

# Solution
# For example:

s = 'Elements are written as "<tag>text</tag>."'

import html

print(s)
# Elements are written as "<tag>text</tag>."
print(html.escape(s))
# Elements are written as &quot;&lt;tag&gt;text&lt;/tag&gt;.&quot;

# Disable escaping of quotes
print(html.escape(s, quote=False))
# Elements are written as "&lt;tag&gt;text&lt;/tag&gt;."

# If you're trying to emit text as ASCII and want to embed character code entities for non-ASCII
# characters, you can use the errors='xmlcharrefreplace' argument to various I/O-related functions
# to do it. For example:
s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))
# b'Spicy Jalape&#241;o'

# To replace entities in text, a different approach is needed. If you're actually processing HTML or XML,
# try using a proper HTML or XML parser first. Normally, these tools will automatically take care of replacing
# the values for you during parsing and you don't need to worry about it.

# If, for some reason, you've received bare text with some entities in it and you want them replaced manually,
# you can usually do it using various utility functions/methods associated with HTML or XML parsers.
# For example:
s = 'Spicy &quot;Jalape&#241;o&quot.'
print(html.unescape(s))
# Spicy "Jalapeño".

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))
# The prompt is >>>







