# HTTP Package

# https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224

import urllib.request
import json

with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224") as f:
    # get the status code and print it
    print("Status Code: " + str(f.getcode()))
    print("---")

    b = f.read()  # byte array
    decodedtext = b.decode('utf-8')
    print(decodedtext)

print("---")

obj = json.loads(decodedtext)
print(obj['kind'])

print(obj['items'][0]['searchInfo']['textSnippet'])
