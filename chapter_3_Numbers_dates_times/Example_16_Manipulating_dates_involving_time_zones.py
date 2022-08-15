#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Manipulating dates involving time zones
Problem
    You had conference call scheduled for December 21, 2012, at 9:30 a.m. in Chicago. At what local time
    did your friend in Bangalore, India, have to show up to attend?
Solution
    timezone.localize(datetime)
    datetime.astimezone(timezone)
Discussion
    advice using UTC dates.
"""

__author__ = 'Frankie Fu'

# Solution
# For almost any problem involving time zones, you should use the 'pytz' module. This package provides
# the Olson time zone database, which is the de facto standard for time zone information found in many
# languages and operating systems.

# A major use of 'pytz' is in localizing simple dates created with the 'datetime' library. For example,
# here is how you would represent a date in Chicago time:
from datetime import datetime, timedelta

import pytz
from pytz import timezone


d = datetime(2012, 12, 21, 9, 30, 0)
print(d)
# 2012-12-21 09:30:00
# Localize the date for chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)
# 2012-12-21 09:30:00-06:00

# Once the date has been localized, it can be converted to other time zones. To find the same time
# in Bangalore, you would do this:
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)
# 2012-12-21 21:00:00+05:30

# If you are going to perform arithmetic with localized dates, you need to be particularly aware of
# daylight saving transitions and other details. For example, in 2013, U.S. standard daylight saving
# time started on March 13, 2:00 a.am local time(at which point, time skipped ahead one hour).
# If you're performing naive arithmetic, you'll get it wrong. For example:
d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)
# 2013-03-10 01:45:00-06:00

later = loc_d + timedelta(minutes=30)
print(later)
# 2013-03-10 02:15:00-06:00

# The answer is wrong because it doesn't account for the one-hour skip in the local time. To fix this,
# use the 'normalize()' method of the time zone. For example:
later = central.normalize(loc_d + timedelta(minutes=30))
print(later)
# 2013-03-10 03:15:00-05:00

# To keep your head from completely exploding, a common strategy for localized date handling is to convert all
# dates to UTC time and to use that for all internal storage and manipulation. For example:
print(loc_d)
# 2013-03-10 01:45:00-06:00
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)
# 2013-03-10 07:45:00+00:00

# Once in UTC, you don't have to worry about issues related to daylight saving time and other matters. Thus, you
# can simply perform normal date arithmetic as before. Should you want to output the date in localized time, just
# convert it to the appropriate time zone afterward. For example:
later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))
# 2013-03-10 03:15:00-05:00

# One issue in working with time zones is simply figuring out what time zone names to use. For example,
# in this recipe, how was it known that 'Asia/Kolkata' aws the correct time zone name for India? To find
# out, you can consult the 'pytz.country_timezones' dictionary using the ISO 3166 country code as a key.
# For example:
print(pytz.country_timezones['IN'])
# ['Asia/Kolkata']

# By the time you read this, it's possible that the pytz module will be deprecated in favor of improved time zone
# support, as described in PEP 431(http://www.python.org/dev/peps/pep-0431).
# Many of the same issues will apply, however(e.g, advice using UTC dates, etc.)
















