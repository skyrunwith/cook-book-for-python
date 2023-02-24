import threading
from contextlib import contextmanager


# Thread-local state to store information on locks already acquired
_local = threading.local()


@contextmanager
def acquire(*locks):
    # sort the locks by object identifier
    locks = sorted(locks, key=lambda x: id(x))

    # Make sure lock order of previously acquired lock is not violated.
    acquired = getattr(_local, 'acquired', [])
    if acquired and max(id(lock) for lock in acquired) >= id(locks[0]):
        raise RuntimeError('Lock order violate')

    # Acquire all locks.
    acquired.extend(locks)
    _local.acquired = acquired
    try:
        for lock in locks:
            lock.acquire()
        yield
    finally:
        # Release locks in reverse of acquisition
        for lock in locks:
            lock.release()
        del acquired[-len(locks):]