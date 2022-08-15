#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Finding the date range for the current month
Problem
    You have some code that needs to loop over each date in the current month, and want an
    efficient way to calculate that date range.
    datetime.timedelta()
    calendar.monthrange()
Solution

Discussion
"""

__author__ = 'Frankie Fu'

# Solution
# Looping over the dates doesn't require building a list of all the dates ahead of time. You can just
# calculate the starting and stopping date in the range, then use 'datetime.timedelta' objects to increment
# the date as you go.

# Here's a function that takes any 'datetime' object, and returns a tuple containing the first date of
# the month and the starting date of the next month:
from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return start_date, end_date


# With this in place, it's pretty simple to loop over the date range:
a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day


# Discussion
# This recipe works by first calculating a date corresponding to the first day of the month. A quick way
# to do this is to use the 'replace()' method is that it creates the same kinds of object that you started
# with. Thus, if the input was the 'date' instance, the result is a date. Likewise, if the input was a
# 'datetime' instance, you get a 'datetime' instance.

# After that, the 'calender.monthrange()'function is used to find out how many days are in the month in
# question. Any time you need to get basic information about calendars, the 'calendar' module can be
# useful 'monthrange()' is only one such function that returns a tuple  containing the day of the
# week along with the number of days in the month.

# Once the number of days in the month is known, the ending date is calculate by adding an appropriate
# 'timedelta' to the starting date. It's subtle, but an important aspect of this recipe is that the ending
# date is not be included in the range(it ia actually the first day of the next month). This mirrors the
# behavior of Python's slices and range operations, which also never include the end point.

# To loop over the date range, standard math and comparison operators are used. For example, 'timedelta' instances
# can be used to increment the date. The '<' operator is used to check whether a date comes before the ending date.

# Ideally, it would nice to create a function that works like the built-in 'range()' function, but for dates.
# Fortunately, this is extremely easy to implement using a generator:
def date_range(start, stop, step):
    while start < stop:
        yield start
        start += step


# Here is an example of it in use:
for d in date_range(datetime(2012, 9, 1), datetime(2012, 10, 1), timedelta(hours=6)):
    print(d)

# Again, a major part of the ease of implementation is that dates and times can be manipulated using
# standard math and comparison operators.













