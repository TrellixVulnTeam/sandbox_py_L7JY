import requests

from utils import print_response


def get_params():
    # Send some parameters to the URL via a GET request
    # Note that requests handles this for you, no manual encoding
    params = {'key1': 'value1', 'key2': 'ほげ'}
    url = "https://httpbin.org/get"
    result = requests.get(url, params=params)
    print_response(result, banner="GET with Params")


def post_params():
    # Send some parameters to the URL via a POST request
    # "Content-Type": "application/x-www-form-urlencoded"
    # Note that requests handles this for you, no manual encoding
    params = {'key1': 'value1', 'key2': 'ほげ'}
    url = "https://httpbin.org/post"
    result = requests.post(url, data=params)
    print_response(result, banner="POST with Params")


def custom_headers():
    # Pass a custom header to the server
    url = "https://httpbin.org/get"
    headers = {
        'User-Agent': 'Hoge Fuga App / 1.0.0',
        'x-custom-header': 'ほげ ふが'.encode('utf-8'),  # in case of non-'latin-1' chars
    }
    result = requests.get(url, headers=headers)
    print_response(result, banner="Custom Headers")


if __name__ == "__main__":
    get_params()
    post_params()
    custom_headers()
