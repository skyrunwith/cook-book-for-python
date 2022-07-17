""" 
Splitting strings on any of multiple delimiters.
Problem
    You need to split a string into fields, but the delimiters (and spacing around them) aren't
    consistent throughout the strings.
Solution
    split() method:
        it's of string objects is really meant for very simple cases, and does not allow for
        multiple delimiters or account for possible whitespace around the delimiters.
Discussion
    re.split() function is useful because you can specify multiple patterns for the separator.
    regular expression pattern involve a capture group enclosed in parentheses.
    noncapture group.
"""

__author__ = 'Frankie Fu'

# Solution
# In case when you need a bit more flexibility, use the re.split() method:
line = 'asdf fjdk; afed, fjek,asdf, foo'
import re
fields = re.split(r'[;,\s]\s*', line)
print(fields)

# Discussion
# re.split() function is useful because you can specify multiple patterns for the separator.
# For example, as shown in the solution, the separator is either a comma(,), semicolon(;), or
# whitespace followed by any amount of extra whitespace. Whenever that pattern is found, the
# entire match becomes the delimiters between whatever fields on either side of the match.
# The result is a list of fields, just as with 'str.split()'

# When using re.split(). you need to be a bit careful should the regular expression
# pattern involve a capture group enclosed in parentheses. If capture groups are used,
# then the matched text is also included in the result. For example, watch what happens here:
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

# Getting the split characters might be useful in certain contexts. For example maybe you
# need the split characters later on to reform an output string:
values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)

# reform the line using the same delimiters
a = ''.join(v+d for v, d in zip(values, delimiters))
print(a)

# If you don't want the separator characters in the result, but still need to use parentheses
# to group parts of the regular expression pattern, make sure you use a noncapture group,
# specified as (?:...). For example:
fields = re.split(r'(?:,|;|\s)\s*', line)
print(fields)













