from collections import defaultdict
from contextlib import contextmanager


"""
exc = get_exchange('name')
exc.attach(some_tasks)
try:
    ...
finally:
    exc.detach(some_tasks)
"""


class Exchange:
    def __init__(self):
        self.subscribers = set()

    def attach(self, task):
        self.subscribers.add(task)

    def detach(self, task):
        self.subscribers.remove(task)

    @contextmanager
    def subscribe(self, *tasks):
        for task in tasks:
            self.attach(task)

        try:
            yield
        finally:
            for task in tasks:
                self.detach(task)

    def send(self, msg):
        for subscriber in self.subscribers:
            subscriber.send(msg)


_exchanges = defaultdict(Exchange)


def get_exchange(name):
    return _exchanges[name]


exc = get_exchange('name')

# with exc.subscribe(task1, task2):
#     exc.send('msg1')
#     exc.send('msg2')
