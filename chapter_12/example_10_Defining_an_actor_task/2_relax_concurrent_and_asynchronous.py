"""
If you relax the requirements of concurrent and asynchronous message delivery, actor-like objects
can also be minimally defined by generators.
"""


def print_actor():
    while True:
        try:
            msg = yield
            print('Got: ', msg)
        except GeneratorExit:
            print('Actor terminating')


p = print_actor()
next(p)
p.send('Hello')
p.send('World')
# p.close()
