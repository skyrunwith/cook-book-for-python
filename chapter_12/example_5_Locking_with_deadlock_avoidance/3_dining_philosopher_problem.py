import threading

from chapter_12.example_5_Locking_with_deadlock_avoidance import acquire


def philosopher(left, right):
    while True:
        with acquire(left, right):
            print(threading.currentThread(), 'Eating')


NSTICKS=5
chopsticks = [threading.Lock() for n in range(NSTICKS)]

for n in range(NSTICKS):
    thread = threading.Thread(target=philosopher, args=(chopsticks[n], chopsticks[(n+1)%NSTICKS]))
    thread.start()



