from concurrent.futures import ThreadPoolExecutor
import urllib.request


def fetch_url(url):
    a = urllib.request.urlopen(url)
    data = a.read()
    return data


pool = ThreadPoolExecutor(10)
a = pool.submit(fetch_url, "http://www.python.org")
b = pool.submit(fetch_url, "http://www.pypy.org")

print(a.result())
