# HTTP Package

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224

from urllib.request import Request, urlopen
from urllib.error import HTTPError
import json

URL = "https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224"
HEADERS = {
    'Content-Type': 'application/json'
}


def read_demo1():
    with urlopen(URL) as f:
        # get the status code and print it
        print("Status Code: " + str(f.getcode()))
        print("---")

        b = f.read()  # byte array
        decodedtext = b.decode('utf-8')
        print(decodedtext)

    print("---")

    obj = json.loads(decodedtext)
    print(obj['kind'])
    # print(obj['items'][0]['searchInfo']['textSnippet'])


def read_demo2():
    q = Request(URL, method='GET', headers=HEADERS)
    try:
        conn = urlopen(q)
        s_data = ''.join([line.decode('utf-8') for line in conn.readlines()])  # 非効率
        print(json.loads(s_data))
    except HTTPError as e:
        print({
            'error': e.reason,
            'code': e.code
        })
    finally:
        conn.close()


if __name__ == '__main__':
    read_demo1()
    read_demo2()
