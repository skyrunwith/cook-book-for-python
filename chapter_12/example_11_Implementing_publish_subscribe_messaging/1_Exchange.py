"""
Message will be delivered to and exchange and the exchange will deliver them to
the attached subscribers.

"""
from collections import defaultdict


class Exchange:
    def __init__(self):
        self._subscribers = set()

    def attach(self, task):
        self._subscribers.add(task)

    def detach(self, task):
        self._subscribers.remove(task)

    def send(self, msg):
        for subscriber in self._subscribers:
            subscriber.send(msg)


# Dictionary for all created Exchanges
_exchanges = defaultdict(Exchange)


# Return the Exchange instance associated with a given name
def get_exchange(name):
    return _exchanges[name]


# Exchange of a task, Any object with a send() method
class Task:
    def send(self, msg):
        print('Msg: ', msg)


task_a = Task()
task_b = Task()

exchange_a = get_exchange('A')
exchange_b = get_exchange('B')
exchange_a.attach(task_a)
exchange_a.attach(task_b)

# send msg
exchange_a.send('msg 1')
exchange_a.send('msg 2')

exchange_a.detach(task_a)
exchange_a.detach(task_b)


class DisplayMessages:
    def __init__(self):
        self.count = 0

    def send(self, msg):
        self.count += 1
        print('msg[{}]: {!r}'.format(self.count, msg))


exc = get_exchange('display')
d = DisplayMessages()
exc.attach(d)
exc.send('display')
exc.detach(d)
