# Send data to a server using urllib

import urllib.request
import urllib.parse
import json

# create some data to pass to the GET request
args = {
    'name': 'ほげ ふが',
    'is_author': True
}

# the data needs to be url-encoded before passing as arguments
params = urllib.parse.urlencode(args, encoding='utf-8')


def print_response(response):
    print('Status code: {}'.format(response.status))
    print('Response Headers: ----------------------')
    print(response.getheaders())
    print('Response Body: ----------------------')
    body = response.read().decode('utf-8')
    print(body)
    return body


def get():
    url = "http://httpbin.org/get"

    # issue the request with the data params as part of the URL
    response = urllib.request.urlopen(url + "?" + params)
    print_response(response)


def post():
    url = "http://httpbin.org/post"

    # issue the request with a data parameter to use POST (data is not None).
    # "Content-Type": "application/x-www-form-urlencoded"
    # ref. urllib.request.Request
    response = urllib.request.urlopen(url, data=params.encode())  # data: bytes
    print_response(response)


def get_json():
    # use urllib to retrieve some sample JSON data
    response = urllib.request.urlopen("http://httpbin.org/json")
    data = print_response(response)

    # use the JSON module to parse the returned data
    obj = json.loads(data)

    # when the data is parsed, we can access it like any other object
    print(type(obj))
    print(obj)

    print(obj["slideshow"]["author"])

    for slide in obj["slideshow"]["slides"]:
        print(slide["title"])


if __name__ == "__main__":
    print("--- GET ---")
    get()
    print("\n--- POST ---")
    post()
    print("\n--- JSON ---")
    get_json()
