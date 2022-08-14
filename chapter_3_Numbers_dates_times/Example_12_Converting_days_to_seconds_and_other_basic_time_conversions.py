"""
Converting Days to Seconds, and Other Basic Time Conversions
Problem
    You have code that needs to perform simple time conversions, like days to seconds, hours
    to minutes, and so on.
Solution
    datetime module:
        timedelta: days, seconds, total_seconds()
        datetime is aware of leap year.
Discussion
    dateutil module.
"""

__author__ = 'Frankie Fu'

# Solution
# To Perform conversions and arithmetic involving different units of time, use the 'datetime' module.
# For example, to represent an interval of time, create a 'timedelta' instance, like this:
from datetime import timedelta
a = timedelta(days=2, hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days, c.seconds)
# 2 37800

print(c.seconds / 3600)
# 10.5
print(c.total_seconds() / 3600)
# 58.5

# If you need to represent specific dates and times, create 'datetime' instances and use the standard
# mathematical operations to manipulate them. For example:
from datetime import datetime

a = datetime(2012, 9, 23)
print(a + timedelta(days=10))
# 2012-10-03 00:00:00

b = datetime(2012, 12, 21)
d = b - a
print(d.days)
# 89

now = datetime.today()
print(now)
# 2022-08-14 22:03:22.822647
print(now + timedelta(minutes=10))
# 2022-08-14 22:13:22.822647

# When making calculations, it should be noted that 'datetime' is aware of leap years. For example:
a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print(a - b)
# 2 days, 0:00:00

print((a - b).days)
# 2
c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print((c - d).days)
# 1

# Discussion
# For most basic date and time manipulation problems, the datetime module will suffice. If you need to perform
# more complex date manipulations, such as dealing with time zones, fuzzy time ranges, calculating the dates
# of holidays, and so forth, look at the 'dateutil' module.

# To illustrate, many similar time calculations can be performed with the 'dateutil.relativedelta()' function().
# However, one notable feature is that it fills in some gaps pertaining to the handling of months(and their
# differing number of days). For instance:
a = datetime(2012, 9, 23)
# print(a + timedelta(months=1))
# TypeError: 'months' is an invalid keyword argument for __new__()

from dateutil.relativedelta import relativedelta

print(a + relativedelta(months=1))
# 2012-10-23 00:00:00

print(a + relativedelta(months=4))
# 2013-01-23 00:00:00

# Time between two dates
b = datetime(2012, 12, 21)
d = b - a
print(d)
# 89 days, 0:00:00

d = relativedelta(b, a)
print(d, d.months, d.days)
# relativedelta(months=+2, days=+28) 2 28






