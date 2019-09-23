# using the requests library to access internet data

import requests
from requests.auth import HTTPBasicAuth


def main():
    # Access a URL that requires authentication - the format of this 
    # URL is that you provide the username/password to auth against
    url = "http://httpbin.org/basic-auth/HogeFuga/hogefuga"

    # Create a credentials object using HTTPBasicAuth
    credentials = HTTPBasicAuth('HogeFuga', 'hogefuga')

    # Issue the request with the authentication credentials
    result = requests.get(url, auth=credentials)
    print_response(result)


def print_response(response: requests.Response):
    print('Status code: {}'.format(response.status_code))
    print('Response Headers: ----------------------')
    print(response.headers)
    print('Response Body: ----------------------')
    print(response.text)


if __name__ == "__main__":
    main()
