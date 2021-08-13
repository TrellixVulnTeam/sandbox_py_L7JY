import requests
from requests.exceptions import HTTPError, Timeout, ConnectionError

from utils import print_response, print_error


def send_request(url, timeout=10, banner=None):
    # Use requests to issue a standard HTTP GET request
    try:
        result = requests.get(url, timeout=timeout)

        # raise_for_status will throw an exception if an HTTP error
        # code was returned as part of the response
        result.raise_for_status()

        print_response(result, banner=banner)

    except ConnectionError as err:
        print_error(err, banner)
    except HTTPError as err:
        print_error(err, banner)
    except Timeout as err:
        print_error(err, banner)


if __name__ == "__main__":
    send_request("https://httpbin.org/html", banner="OK")
    send_request("https://no-such-server.xxx", banner="ConnectionError")
    send_request("https://httpbin.org/status/404", banner="HTTPError")
    send_request("https://httpbin.org/delay/3", timeout=1, banner="Timeout")
