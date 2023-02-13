import time
from threading import Thread, Event

"""
"countdown is running " message will always appear after "countdown starting" message.
"""


# Code to execute in an independent thread
def countdown(n, started_evt):
    print('countdown starting')
    # started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(5)


# Create the event object that will be used to signal startup
start_evt = Event()

# Launch the thread and pass the startup event
print('Launching countdown')
t = Thread(target=countdown, args=(3, start_evt))
t.start()

# Wait for the thread to start
start_evt.wait()
print('countdown is running')
