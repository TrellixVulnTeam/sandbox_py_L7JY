# using the requests library to access internet data

import requests
from requests.exceptions import HTTPError, Timeout, ConnectionError


def error(url, timeout=10):
    # Use requests to issue a standard HTTP GET request
    try:
        result = requests.get(url, timeout=timeout)

        # raise_for_status will throw an exception if an HTTP error
        # code was returned as part of the response
        result.raise_for_status()

        print_response(result)
    except ConnectionError as err:
        print(err)
    except HTTPError as err:
        print(err)
    except Timeout as err:
        print("Request timed out: {0}".format(err))


def print_response(response: requests.Response):
    print('Status code: {}'.format(response.status_code))
    print('Response Headers: ----------------------')
    print(response.headers)
    print('Response Body: ----------------------')
    print(response.text)


if __name__ == "__main__":
    print("--- OK ---")
    error("http://httpbin.org/html")  # should work with no errors
    print("--- ConnectionError ---")
    error("http://no-such-server.xxx")  # will generate a ConnectionError
    print("\n--- HTTPError ---")
    error("http://httpbin.org/status/404")  # will generate a HTTPError
    print("\n--- Timeout ---")
    error("http://httpbin.org/delay/5", 2)  # will generate a Timeout
