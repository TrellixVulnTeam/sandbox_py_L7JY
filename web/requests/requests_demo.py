# using the requests library to access internet data

# import the requests library
import requests


def print_response(response: requests.Response):
    print('Status code: {}'.format(response.status_code))
    print('Response Headers: ----------------------')
    print(response.headers)
    print('Response Body: ----------------------')
    # print(response.content)  # bytes
    # print(response.json)  # json
    print(response.text)


def get_xml():
    # Use requests to issue a standard HTTP GET request
    url = "http://httpbin.org/xml"
    result = requests.get(url)
    print_response(result)


def get_json():
    # Use requests to issue a standard HTTP GET request
    url = "http://httpbin.org/json"
    result = requests.get(url)
    print_response(result)


def get_params():
    # Send some parameters to the URL via a GET request
    # Note that requests handles this for you, no manual encoding
    params = {'key1': 'value1', 'key2': 'ほげ'}
    url = "http://httpbin.org/get"
    result = requests.get(url, params=params)
    print_response(result)


def post_params():
    # Send some parameters to the URL via a POST request
    # "Content-Type": "application/x-www-form-urlencoded"
    # Note that requests handles this for you, no manual encoding
    params = {'key1': 'value1', 'key2': 'ほげ'}
    url = "http://httpbin.org/post"
    result = requests.post(url, data=params)
    print_response(result)


def custom_headers():
    # Pass a custom header to the server
    url = "http://httpbin.org/get"
    headers = {'User-Agent': 'Hoge Fuga App / 1.0.0'}
    result = requests.get(url, headers=headers)
    print_response(result)


if __name__ == "__main__":
    print("--- GET xml ---")
    get_xml()
    print("--- GET json ---")
    get_json()
    print("--- GET with Params ---")
    get_params()
    print("\n--- POST with Params ---")
    post_params()
    print("\n--- Custom Headers ---")
    custom_headers()
