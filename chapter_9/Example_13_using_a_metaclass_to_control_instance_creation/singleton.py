#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""  """

__author__ = 'Frankie Fu'
''' Singleton '''


# Now, suppose you want to implement the singleton pattern(i.e., a class where only one instance is ever created).
# That is also relatively straightforward, as shown here:
class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance


# Example
class Spam(metaclass=Singleton):
    def __init__(self):
        print('Creating Spam')


# In this case, only one instance ever gets created.
a = Spam()

b = Spam()
# True
print(a is b)

c = Spam()
# True
print(a is c)


# Discussion
# If you didn't use a metaclass, you might have to hide the classes behind some kind of extra factory
# function. For example, to get a singleton, you might use a hack such as the following:
class _Spam:
    def __init__(self):
        print('Creating _Spam')


_spam_instance = None
def Spam2():
    global _spam_instance

    if _spam_instance is not None:
        return _spam_instance
    else:
        _spam_instance = _Spam()
        return _spam_instance


a = Spam2()

b = Spam2()

c = Spam2()

print(a is b)

print(a is c)