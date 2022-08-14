"""
Determining Last Friday's Date
Problem
    You want a general solution for finding a date for the last occurrence of a day of the week.
    Last Friday, for example.
Solution
    custom get_previous_byday() function.
    dateuti.relativedelta.
Discussion
"""

__author__ = 'Frankie Fu'

# Solution
# Python's 'datetime' module has utility functions and classes to help perform calculations like this.
# A decent, generic solution to this problem looks like this:
from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    return start_date - timedelta(days=days_ago)


# Using this in an interpreter session would look like this:
print(datetime.today())
# 2022-08-14 22:35:26.701799
print(get_previous_byday('Monday'))
# 2022-08-08 22:35:26.701836
print(get_previous_byday('Tuesday'))
# 2022-08-09 22:35:26.701855
print(get_previous_byday('Friday'))
# 2022-08-12 22:35:26.701862

# The optional start_date can be supplied using another datetime instance. For example:
print(get_previous_byday('Tuesday', datetime(2022, 8, 17)))
# 2022-08-16 00:00:00

# Discussion
# This recipe works by mapping the start date and the target date to their numeric position in the week
# (with Monday as day 0). Modular arithmetic is then used to figure out how many days ago the target date
# last occurred. From there, the desired data is calculated from the start date by subtracting an appropriate
# 'timedelta' instance.

# If you're performing a lot of date calculations like this, you may be better off installing the
# 'python-dateutil package' instead. For example, here is an example of performing the same calculation
# using the 'relativedelta()' function from dateutil:
from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
d = datetime.now()

print(d)
# 2022-08-14 22:54:20.952669
# Next friday
print(d + relativedelta(weekday=FR))
# 2022-08-19 22:54:20.952669
# Last friday
print(d - relativedelta(weekday=FR(-1)))
# 2022-08-12 22:54:49.353688
