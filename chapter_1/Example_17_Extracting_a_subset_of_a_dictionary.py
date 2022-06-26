"""
Problem
    You want to make a dictionary that is a subtle of another dictionary.
Solution
    Dictionary comprehension.
    "dict() function"
        create a sequence and tuples and passing them to the dict() function.
Discussion
    dict comprehension is a bit clearer and actually runs quite a bit faster than "dict()" function.
"""

__author__ = 'Frankie Fu'

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# Make a dictionary of all prices over 200
p1 = {key: value for (key, value) in prices.items() if value > 200}
print(p1)

# Make a dictionary of tech stocks
tech_names = {'AAPL', 'IBM', 'HPQ', 'MSFT'}
print(tech_names)
p2 = {key: value for (key, value) in prices.items() if key in tech_names}
print(p2)

# Discussion
# Much of what can be accomplished with dictionary comprehension might also be done
# by creating a sequence and tuples and passing them the "dict() function".
p1 = dict((key, value) for (key, value) in prices.items() if key in tech_names)
print(p1)

# Sometimes there are multiple ways of accomplish the same thing.
# Make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = {key: prices[key] for key in prices.keys() & tech_names}
print(p2)