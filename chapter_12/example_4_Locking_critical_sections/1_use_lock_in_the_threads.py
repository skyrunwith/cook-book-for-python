import threading


class ShareCounter:

    def __init__(self, initial=0):
        self._value = initial
        self._lock = threading.RLock()

    def increment(self, delta=1):
        with self._lock:
            self._value += delta

    def decrement(self, delta=1):
        with self._lock:
            self._value -= delta


share = ShareCounter()


def inc(_share):
    for i in range(1000000):
        _share.increment()


a = threading.Thread(target=inc, args=(share,))
b = threading.Thread(target=inc, args=(share,))
c = threading.Thread(target=inc, args=(share,))
a.start()
b.start()
c.start()
a.join()
b.join()
c.join()
print(share._value)
