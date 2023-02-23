import threading


class ShareCounter:
    _lock = threading.RLock()

    def __init__(self, initial=0):
        self._value = initial

    def increment(self, delta=1):
        with ShareCounter._lock:
            self._value += delta

    def decrement(self, delta=1):
        with ShareCounter._lock:
            self._value -= delta
