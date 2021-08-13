import requests


def get_cookie():
    # Use a session object to group requests and settings
    # create the session
    sess = requests.Session()
    # use the session to persist a cookie across requests
    sess.get("https://httpbin.org/cookies/set/sample/123456789")
    resp = sess.get("https://httpbin.org/cookies")
    print(resp.text)

    # close the session
    sess.close()


def manipulate_headers():
    # using context manager
    with requests.Session() as sess:
        # Customize the user-agent to simulate different browsers
        # Set the user-agent to be Firefox
        sess.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0"
        })
        resp = sess.get("https://google.com")
        print(len(resp.content))

        # Set the user-agent to be an iPhone
        sess.headers.update({
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) relesys_web_client/1.3.10.0 (RelesysApp/1.3.43 net.relesysapp.nettoenterprise)"
        })
        resp = sess.get("https://google.com")
        print(len(resp.content))


if __name__ == "__main__":
    get_cookie()
    print('---')
    manipulate_headers()
