"""
Picking Things at Random
Problem
    You want to pick random items out of a sequence or generate random numbers.
Solution
    random module has various functions for random numbers and picking random items.
        random.choice(): pick a random item out of a sequence.
        random.sample(): To take a sampling of N items where selected items are removed from further consideration.
        random.shuffle(): If you simply want to shuffle items in a sequence in place.
        random.randint(): To produce random integers.
        random.random(): To produce uniform floating-point values in the range 0 to 1.
        random.getrandbits(): To get N random-bits expressed as an integer.
        random.seed(): alter the initial seed.
Discussion
"""

__author__ = 'Frankie Fu'

# Solution
# For example, to pick a random item out of a sequence, use 'random.choice()'.
import random
values = [1, 2, 3, 4, 5, 6]

print(random.choice(values))

# To take a sampling of N items where selected items are removed from further consideration,
# use random.sample() instead:
print(random.sample(values, 2))

print(random.sample(values, 3))

# If you simply want to shuffle items in a sequence in place, use random.shuffle():
random.shuffle(values)
print(values)

# To produce random integers, use random.randint():
print(random.randint(0, 10))

# to produce uniform floating-point values in the range 0 to 1.
print(random.random())
# 0.2625845943010493

# To get N random-bits expressed as an integer, use random.getrandbits():
print(random.getrandbits(200))
# 890854851102602270785028279376105402102467443199662873260741

# Discussion
# The random module computes random numbers using the Mersenne Twister algorithm. This is a
# deterministic algorithm, but you can alter the initial seed by using the random.seed() function.
# For example:
random.seed()  # Seed based on system time or os.urandom()
random.seed(12345)  # Seed based on integer given
random.seed(b'bytedata')  # Seed based on byte data

# In addition to the functionality shown, random() includes functions for uniform, Gaussian, and other
# probability distributions. For example, 'random.uniform()' computes uniformly distributed numbers,
# and 'random.gauss()' computes normally distributed numbers. Consult the documentation for information
# on other supported distributions.

# Functions in random() should not be used in programs related to cryptography. If you need such functionality,
# consider using functions in the 'ssl module' instead. For example, ssl.RAND_bytes() can be used to generate
# a cryptographically secure sequence of random bytes.
