import threading

from chapter_12.example_5_Locking_with_deadlock_avoidance import acquire

x_lock = threading.Lock()
y_lock = threading.Lock()


def thread1():
    while True:
        with acquire(x_lock):
            with acquire(y_lock):
                print('thread 1')


def thread2():
    while True:
        with acquire(y_lock):
            with acquire(x_lock):
                print('thread 2')


a = threading.Thread(target=thread1)
a.daemon = True
a.start()

b = threading.Thread(target=thread2)
b.daemon = True
b.start()
