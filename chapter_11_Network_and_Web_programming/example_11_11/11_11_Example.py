"""
Passing a Socket File Descriptor Between Processes
Problem
    You have multiple python interpreter processes running and want to pass an open file descriptor from
    one interpreter to another. For instance, Perhaps there is a server process that is responsible for
    receiving connections, but the actual servicing of clients is to be handled by a different interpreter.
Solution
    To pass a file descriptor between processes, you first need to connect the processes together.
    In Unix machines, you might use a `Unix domain socket`, whereas in Windows, you could use a `nemed pipe`.
    However, rather than deal with such low-level mechanics, it is often easier to use `multiprocessing` module
    to set up such a connection.
    Once a connection is established, you can use the `send_handle()` and `recv_handle()` functions in
    `multiprocessing.reduction` to send file descriptor between processes.
    The following example illustrates basics:
        11_11_1_server_process.py

    In this example, two processes are spawned and connected by multiprocessing `Pipe` object. The server
    process opens a socket and waits for client connections. The `worker` process merely waits to receive
    a file descriptor using `recv_handle()`. When the server receives the connection, it sends the resulting
    socket file descriptor to the worker using `send_handle()`. The worker takes over the socket and echoes
    the data back to the client until the connection is closed.

    If you connect to the running server using `Telnet`, or similar tool, here is an example of what you might see:
         Got connection from: ('127.0.0.1', 58290)
         Child: Got fd 9
         Child recv:  b'Hello'

    The most important part of this example is the fact that the client socket accepted in the server is actually
    serviced by completely different process. The server merely hands it off, closes it, and waits for the next
    connection.

Discussion
    Passing file descriptors between processes is something that many programmers don't even realize it. However,
    it can sometimes be a useful tool in building scalable systems. For example, on a multicore machine, you
    have multiple instances of the Python Interpreter and use file descriptor passing to more evenly balance the
    number of clients being handled by each interpreter.

    The `send_handle()` and `recv_handle()` functions as shown in the solution really only works with
    multiprocessing connections. Instead of using pipe, you can connect interpreters as shown in Recipe 11.7,
    and it will work as long as you use `Unix domain socket` or `Windows pipes`. For example, you should implement
    the server and worker as completely separate programs to be started separately. Here is the implementation of the
    server.
        11_11_2_Listener_process.py

    Here is the corresponding client code:
        11_11_2_Client_process.py
    The resulting operation should be exactly the same as the example that uses `Pipe()`

    Under the covers, passing file descriptors involves creating a Unix domain socket and the `sendmsg()` method
    of sockets. Since this technique is not widely known, here is a different implementation of the server that
    shows how to pass file descriptors using sockets.
        11_11_3_sockets_process.py
    Here is an implementation of the worker using sockets:
        11_11_3_sockets_worker_process.py

    If you are going to use file descriptor passing in your program, it is advisable to read more about it in
    an advanced text, such as `Unix Networking Programming` by Richard Stevens(Prentice Hall, 1990). Passing
    file descriptors on Windows uses a different techniques than Unix(not shown). For that platform, it is
    advisable to study the source code to `multiprocessing.reduction` in close detail to see how it works.
"""

__author__ = 'Frankie Fu'
