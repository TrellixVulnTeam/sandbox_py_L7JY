import requests


def print_response(response: requests.Response, fmt="text", banner=None):
    if banner:
        print(f'--- {banner} ---')
    print(f'Status code: {response.status_code}')
    if response.encoding:
        print(f'Character set encoding: {response.encoding}')
    print('Response Headers: ----------------------')
    print(response.headers)
    print('Response Body: ----------------------')
    if fmt == "raw":
        print(response.content)  # property: bytes
    elif fmt == "json":
        print(response.json())  # method: json
    else:
        print(response.text)  # property: text

    print()


def print_error(error, banner=None):
    if banner:
        print(f'--- {banner} ---')
    print(error)
    print()
