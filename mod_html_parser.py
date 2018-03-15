# HTML Parser Module

from html.parser import HTMLParser


class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag: ", tag)
        for attr in attrs:
            print("attr:", attr)

    def handle_endtag(self, tag):
        print("End tag: ", tag)

    def handle_comment(self, data):
        print("Comment: ", data)

    def handle_data(self, data):
        print("Data: ", data)


parser = HTMLParser()

htmlFile = open("sample.html", "r")
s = ""
for line in htmlFile:
    s += line
parser.feed(s)
