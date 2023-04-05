"""
Create a simple REST-BASED interface
Problem
    You want to be able to interact with your program remotely over the network using
    a simple REST-BASED interface. However, you don't want to do it by install a full-fledged
    web programming framework.
Solution
    One of the easiest ways to build a REST-BASED interfaces is to create a tiny library based on
    the `WSGI`standard, as described in `PEP 3333`(http://www.python.org/dev/peps/pep-3333).
Discussion
    In REST-BASED interfaces, you are typically writing programs that respond to common HTTP request.
    However, unlike a full-fledged website, you are just `pushing data around`. The data might be encoded
    in a variety of standard formats such as JSON, XML or CSV. Although it seems minimal, providing an API
    in this manner is useful thing of a variety of applicaitons.

    For example. long-running programs might use a REST API to implement monitoring and diagnostics.
    Big data applications can use REST to build a query/data extraction system. REST can be used to
    in control hardware devices, such as robots, sensors, mills, and light bulbs. REST are well-supported
    by client-side programming environments, such as JavaScript, Androids, IOS and so forth. Thus having
    such an interface can be a way to encourage the development of more complex applications
    this interfaces with your code.

    For implement a simple REST interface, it is often easy enough to base your code on the
    Python WSGI interface. `WSGI` is supported by the standard library, but also by most
    third-party web frameworks. Thus, if you use it, there is a lot of flexibility in
    how your code used later.

    In `WSGI`, you simply implement applications that in the form of a callable that accepts this calling convention.
    import cgi
    def wsgi_app(environ, start_response)
        ...

    The `environ` argument is a dictionary that contains value inspired by the `CGI` interface
    provided by various web servers such as Apache(http://tools.ietf.org/html/rfc3875).
    To extract different fields, you would write code like this:
    def wsgi_app(environ, start_response):
        method = environ.get('REQUEST_METHOD')
        path = environ.get('PATH_INFO')
        # Parse the query params
        params = cgi.FieldStorage(environ.get('wsgi.input), environ=environ)
        ...

    A few common values are shown here. environ['REQUEST_METHOD] is the type of request(e.g., GET, POST, PUT).
    environ['PATH_INFO'] is the path or the resource being requested. The call to `cgi.FieldStorage` extracts
    supplied query parameters from the request and put them into a dictionary-like object for later use.

    The `start_response` is a function that must be called to initiate a response. The first argument is
    the resulting HTTP status. The second argument is a list of tuples(name, value)
    that make up the HTTP header of the response.
    def wsgi(environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/plain')])

    To return data, An `WSGI` application must return a sequence of byte strings. This can be done
    using a list like this:
    def wsgi_app(environ, start_response):
        start_response('200 OK', ['Content-Type', 'text/plain'])
        resp = []
        resp.append(b'Hello World\n')
        resp.append(b'Goodbye\n')
        return resp

    Alternatively, you can use `yield`.
    def wsgi_app(environ, start_response):
        start_response('200 OK', ['Content-Type', 'text/plain'])
        resp = []
        yield b'Hello World\n'
        yield b'Goodbye\n'

    It's important to emphasize that byte sting must be used in the result. If the response consists of text,
    it will need to be encoded into bytes first. Of course, the requirement that the return value be text
    --you could easily write an application function that creates images.

    Although `WSGI` applications are commonly defined as a function, as shown, an instance may also be
    used as long as it implements a suitable `__call__` method.
    class WSGIApplication:
        def __init__(self):
            ...

        def __call__(self):
            ...

    This technique has been used to create the `PathDispatcher` class in this recipe. The dispatcher
    does nothing more than manage a dictionary mapping(method, path) pairs to handler functions.
    When a request arrives, the method and path are extracted and used to dispatch to a handler.

    In addition, any query variables are parsed and put into a dictionary that is stored as
    environ['params](this latter step is so common, it makes a lot of sense in the dispatcher
    in order to avoid a lot of replicated code).

    To use the dispatcher, you simply crate an instance and resister various `WSGI-style` application
    functions with it, as shown in the recipe. Write these functions are extremely straightforward,
    as you follow the rules concerning the `start_response` method and produce output as byte strings.

    On thing to consider when writing such functions is the careful use of string template. Nobody likes
    to work with code that is a tangled mess of `print` functions, XML and various formatting operations.
    In the solution, triple-quote string template are bing defined and used internally. This particular
    approach makes it easier to change the format of the output later(just change the template
    as apposed to any of the code that uses it)

    Finally, an important part of using `WSGI` is that in the implementation is specific to a particular
    `web server`. That is actually the whole idea, since the standard is server and framework neutral,
    you should be able to plug your application into a wide variety of servers.
    In the recipe, the following code is used for testing
    from wsgiref.simple_server import make_server

    dispatcher = Dispatcher()

    httpd = make_server('', 8080, dispatcher)
    print('Serving on port 8080)
    http.serve_forever()

    This will create a simple server that you can use to see if your implementation works. Later on,
    when you're ready to scale things up to a large level, you will change this code with a particular server.

    `WSGI` is intentionally specification. As such, it doesn't support any support for advanced concepts
    such as Authentication, cookies, redirection and so forth. There are no hard to implement yourself.
    However, if you just want a bit of more support, you might consider third-party library.
    such as WebOb(http://webob.org/), Paste(http://pythonpaste.org/)
"""

__author__ = 'Frankie Fu'
