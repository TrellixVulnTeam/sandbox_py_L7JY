import requests


def send_request(url):
    # introspect the redirection history
    resp = requests.get(url)
    print(resp.url)
    if resp.history:
        print(resp.history)
        orig = resp.history.pop()
        print(orig.url)
        print(orig.status_code, orig.reason)


if __name__ == "__main__":
    send_request("https://google.com")
    print('---')
    send_request("http://google.com")
    print('---')
    send_request("http://github.com")
