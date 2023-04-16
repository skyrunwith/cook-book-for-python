""" 
Network and web programming

This chapter is about various topic related to using Python in networked and distributed applications.
Topics are split between using Python as client to access existing servers, and using Python to implement
networked services as a server. Common techniques for writing code involving cooperating and communicating
with interpreters are also given.
"""

__author__ = 'Frankie Fu'
"""
11.1 Interacting with HTTP Services as a client
    You need to access various services as a client.
    
    How to use `urllib` to access existing services.
    How to use `requests library` access existing services.
    All of this is much easier in `requests`(e.g., cookies, authentication, header, encoding, ect.)
        resp.text(the Unicode decoded text from a request)
        reps.content(the raw binary response content)
        reps.json(the response content interpreted as JSON)  
        
11.2. Creating TCP Server (A reliable connection)
    You want to implement server that communicates with clients using TCP internet protocol.
    
    `socketserver` lib :
        a handler method class:
            BaseRequestHandler, StreamRequestHandler.
        server:
            TCPServer, ThreadingTCPServer, ForkingTCPServer
        a pre-allocated pool of worker threads and process with nonthreaded server.
            Thread(target=server.serve_forever)
    `socket` lib to implement server.
        methods:
            server: 
                __init__, bind, listen
                accept, recv, send
            client:
                __init__, connect, send, recv
                
11.3. Creating UDP Server(A unreliable connection)
    you want to implement server that communicates with clients using UDP internet protocol.
    
    `socketserver` lib:
    a handler method class:
        BaseRequestHandler, StreamRequestHandler.
        server:
            UDPServer, ThreadingUDPServer, ForkingUDPServer
    `socket` lib to implement UDP server.
        server:
            __init__, bind
            recvfrom, sendto
        client:
            __init__, sendto, recvfrom
11.5 Create a simple REST-Based server.
    you want to be able to interact with your programs over the network using a simple
    REST-Based interface. However, you don't want to do it by installing a full-fledged 
    web programming framework.
    
    create a tiny library based on `WSGI` standard.
    
    Define wsgi application:
        function: 
            wsgi(environ, start_response)
        class:
            __init__(self):
                self.pathmap={} #  a dictionary that mappings(method, path) pairs to handler function.
            __call__(self):
                ...
        
    requirements:
        the returned result must be encoded into byte strings.
        
    create a simple server.
        from wsgiref.simple_server import make_server
    make serer create the underlying socket server.
    
11.6 Implementing a simple remote procedure with XML-RPC
    You want an easy way to execute functions and methods in Python program running on remote machines.
    
    1.create a server instance(SimpleXMLRPCServer)
    2.use `register_function`
    3.launch it with serve_forever() method
    4.client access the service: create a ServerProxy instance
    
11.7 Communicating simply between interpreters.
    you are running multiple instance of the python interpreter, possibly on different machines,
    you want to exchange data between them using messages.
    
    multiprocessing.connection (Client and Listener).
        use `send` and `recv` passing messages.
        Object is serialized using `pickle`.
    Create a connection use three forms:
        Networking, Unix domain socket, Windows named pipes.
        
    Best suited for long-running connection(not a large number of short connection)
    
11.8 Implementing Remote Procedure Call
    You want to implement simple remote procedure call on top of the message passing layer,
    such as sockets, multiprocessing connections, ZeroMQ.
    
    Serialize data by Encoding function name, arguments and returned value using (pickle, JSON, XML, etc.)
    
    1. RPC flow.
        client use proxy create a tuple that contains function name, arguments, 
        and pickle tuple, send over the connection.
        
        sever received message, unpickle, look up function, and execute it with arguments, 
        pickle result and sent it back.
    2. Security
        Allow RPC access only be internally, behind a firewall, and not exposed to the rest of the world.
    3. Exception handle.
        If using pickle, exception instance can often be serialized and reraised in the client.
        Some other approach, at the least, return the exception string in the response.
        
11.9 Authenticating clients simply
    You want a simple way to authenticate clients connecting to the server in a distributed system, 
    but you don't want the complexity of something like SSL.
    
    Simple but effective authentication can be performed by implementing `a connection handshake` use `hmac`.
    handshake flow: 
        client connect -> server accept -> server send auth message -> client generate message digest and send to server
        -> server recv and compare -> start communication
    client authentication:
        sock.recv -> generate digest -> send
    server authentication:
        generate message -> send -> digest and recv -> compare
    After Authentication a connection, subsequent communication on a connection sent in the clear.
11.10 Add SSL to Network Services.
    You want to implement a network service involving sockets where servers and clients authenticate themselves
    and encrypt transmitted data Using SSL.
    
    The `ssl` module support for adding SSL to low-level socket connections.
        ssl.wrap_socket().
    
    Add ssl support for existing network services already implemented in the Standard Library. such as XML-RPC server.
        1. Define a mixin class: 
        class SSLMixin():
            ...
            1.1 override a get_request() method.
            1.2 get client socket by supper().get_request() method.
            1.3 use ssl.wrap_socket to wrap client socket
        2. Define a server inherit from mixin class.
            class SSLSimpleXMLRPCServer(SSLMixin, SimpleXMLRPCServer) 
            ...
        3. Define a class inherit `SafeTransport` class:
            3.1 __init__ pass `SSLContext` to supper() SafeTransport
        4. SSL verify both directions.
        
    如果server add SSL, 那么server create private key and certificate file. 并将certificate file放到client machine。
    如果是Public servers，还需要从certificate authorities 获取signed certificate.  

11.11 Passing a Socket File Descriptor between Processes.
    You have multiple python interpreter processes running and want to pass an open file descriptor from one to another.
    For instance, Perhaps there is a server process that is responsible for receiving connections, but the actual
    service of clients is to be handled by different interpreters.
    
    1. First, connect the server together.
        1.1 Use Pipe object(a `Unix domain socket` or `named pipe`).
    2. Once connection is established, Use multiprocessing.reduction: send_handle(), recv_handle()
    
    3. The `send_handle()` and `recv_handle()` functions as shown in the solution really only 
       work with multiprocessing connections.
        3.1 Use Listener and Client in `multiprocessing.connection` module. As long as you use `Unix domain socket`
            or `named pipe`
    4. Passing a socket file descriptor involves creating a Unix domain socket and use the `sendmsg` method of sockets.
"""