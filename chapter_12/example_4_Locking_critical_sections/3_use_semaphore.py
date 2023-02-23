from threading import Semaphore
import urllib.request

_fetch_url_sema = Semaphore(5)


def fetch_url(url):
    with _fetch_url_sema:
        urllib.request.urlopen(url)
