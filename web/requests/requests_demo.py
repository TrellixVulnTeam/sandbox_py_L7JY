import requests

from utils import print_response


def get_html():
    # Use requests to issue a standard HTTP GET request
    url = "https://httpbin.org/html"
    result = requests.get(url)
    print_response(result, banner="GET html")


def get_xml():
    # Use requests to issue a standard HTTP GET request
    url = "https://httpbin.org/xml"
    result = requests.get(url)
    print_response(result, banner="GET xml")


def get_json():
    # Use requests to issue a standard HTTP GET request
    url = "https://httpbin.org/json"
    result = requests.get(url)
    print_response(result, "json", banner="GET json")


if __name__ == "__main__":
    get_html()
    get_xml()
    get_json()
