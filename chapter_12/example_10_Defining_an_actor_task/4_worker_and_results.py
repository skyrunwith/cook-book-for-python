"""
Here is a variation of an actor that allows arbitrary functions to be executed in a worker
and results to be communicated back using a special `Result` object.
"""
from threading import Thread, Event

from chapter_12.example_10_Defining_an_actor_task import Actor


class Result:
    def __init__(self):
        self._result = None
        self._evt = Event()

    def set_result(self, value):
        self._result = value

        self._evt.set()

    def result(self):
        self._evt.wait()
        return self._result


class Worker(Actor):
    def submit(self, func, *args, **kwargs):
        r = Result()
        self.send((func, args, kwargs, r))
        return r

    def run(self):
        while True:
            func, args, kwargs, r = self.recv()
            r.set_result(func(*args, **kwargs))


worker = Worker()
worker.start()
r = worker.submit(pow, 2, 3)
print(r.result())
worker.close()
