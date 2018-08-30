# HTTP Package

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224
import sys
from http.client import HTTPResponse
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
import json

URL = "https://www.googlea9pis.com/books/v1/volumes?q=isbn:1101904224"
HEADERS = {
    'Content-Type': 'application/json',
}


def read_demo():
    q = Request(URL, method='GET', headers=HEADERS)
    try:
        conn: HTTPResponse = urlopen(q)
        print(json.loads(conn.read(), encoding='utf-8'))
    except HTTPError as e:
        print({
            'error': e.reason,
            'code': e.code
        }, file=sys.stderr)
    except Exception as e:
        print(e, file=sys.stderr)
    else:
        conn.close()


if __name__ == '__main__':
    read_demo()
