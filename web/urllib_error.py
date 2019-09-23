# handling errors and status codes

# import the request, error, and status modules
import urllib.request
from urllib.error import HTTPError, URLError
from http import HTTPStatus


def error(url):
    # use exception handling to attempt the URL access
    try:
        result = urllib.request.urlopen(url)
        print("Result code: {0}".format(result.status))
        if result.getcode() == HTTPStatus.OK:
            print(result.read().decode('utf-8'))
    # occurs when the server returns a non-success error code
    except HTTPError as err:
        print(err)
    # occurs when something is wrong with the URL itself
    except URLError as err:
        print(err)


if __name__ == "__main__":
    print("--- OK ---")
    error("http://httpbin.org/html")  # should work with no errors
    print("\n--- URLError ---")
    error("http://no-such-server.xxx")  # will generate a URLError
    print("\n--- HTTPError ---")
    error("http://httpbin.org/status/404")  # will generate a HTTPError
