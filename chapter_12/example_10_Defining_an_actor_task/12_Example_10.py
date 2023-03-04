"""
Defining an Actor Task
Problem
    You'd like to define tasks with behavior similar to "actors" in the so-called "actor model".
Solution
    The "Actor model" is one of the oldest and most simple approaches to concurrency and distributed computing.

    Actors ara straightforward to define using a combination of `a thread and a queue`.
Discussion
    There is just one core operation, `send()`.

    `send()` a task a message is something that can be scaled up into systems involving multiple processes
    or even large distribute systems.`send()` cloud be programmed to transmit data on a socket connection
    or deliver it via some kind of messaging infrastructure(e.g. AMQP, ZMQ, etc).
"""

__author__ = 'Frankie Fu'
