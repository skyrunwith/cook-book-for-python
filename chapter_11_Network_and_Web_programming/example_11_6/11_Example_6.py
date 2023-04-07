"""
Implementing a simple Remote Procedure call with XML-RPC
Problem
    You want an easy way to execute functions or methods in Python programs running on remote machines.
Solution
    Perhaps the easiest way to implement a simple remote procedure call mechanism is to use XML-RPC.
Discussion
    XML-RPC can be an extremely easy way to set up a simple remote procedure call service.
    All you need to do is create a server instance, register function with it using `register_function` method,
    and then launch it using `serve_forever` method. This recipe packages it up to put all of the code together,
    but there no such requirement.
    from xmlrpc.server import SimpleXMLRPCServer

    def add(x, y):
        return x + y

    serv = SimpleXMLRPCServer(('', 15000))
    serv.register_function(add)
    serv.serv_forever()

    Functions exposed via `XML-RPC` only work with certain kinds of data such as strings, numbers,
    lists, dictionaries. For everything else, some study is required. For instance, if you pass
    an instance through `XML-RPC`, only it's instance dictionaries is handled.
    11_6_3_pass_an_instance.oy

    Similarly, handling of binary data is a bit different than you expect:
    11_6_4_handle_binary_data

    As a general rule, you shouldn't expose an `XML-RPC` service to the rest of world as a public API.
    It often works best on internal networks where you want to write a simple distributed programs
    involving a few different machines.

    A downside to `XML-RPC` is its performance. The `SimpleXMLRPCServer` implementation is only single
    threaded, and wouldn't be appropriate for scaling a large application. although it can be made to
    run multithreading, as shown in 11.2. Also, since `XML-RPC` serializes all data as XML, it's inherently
    slower than other approaches. However, one benefit of this encoding ist that it's understood by a variety
    of other programming languages. By using it, clients written in languages other than Python will be
    able to access your service.

    Despite its limitations, `XML-RPC` is worthy knowing about if ever have the need to make a quick and
    dirty remote procedure call system, Oftentimes, the simple solution is good enough.

"""

__author__ = 'Frankie Fu'
