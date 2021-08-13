import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

from utils import print_response


def basic():
    # Access a URL that requires authentication - the format of this
    # URL is that you provide the username/password to auth against
    url = "https://httpbin.org/basic-auth/HogeFuga/passw0rd"

    # Create a credentials object using HTTPBasicAuth
    credentials = HTTPBasicAuth('HogeFuga', 'passw0rd')
    # credentials = ('HogeFuga', 'passw0rd')  # shorthand

    # Issue the request with the authentication credentials
    result = requests.get(url, auth=credentials)
    print_response(result, banner="Basic")


def digest():
    # Access a URL that requires authentication - the format of this
    # URL is that you provide the username/password to auth against
    url = "https://httpbin.org/digest-auth/auth/HogeFuga/passw0rd"

    # Create a credentials object using HTTPDigestAuth
    credentials = HTTPDigestAuth('HogeFuga', 'passw0rd')

    # Issue the request with the authentication credentials
    result = requests.get(url, auth=credentials)
    print_response(result, banner="Digest")


if __name__ == "__main__":
    basic()
    digest()
