"""
Stream(File-like object) demo
"""
import csv
import os
import urllib.request
import io


def text_wrapper_demo():
    d = os.path.dirname(__file__)
    with urllib.request.urlopen(rf'file:///{d}/../data/portfolio.csv') as bs:  # byte stream
        ts = io.TextIOWrapper(bs, newline='', encoding='utf-8')  # text stream
        reader = csv.reader(ts)
        for row in reader:
            print(row)


def string_io_demo():
    for s in io.StringIO("Hoge\nFuga\nFefe"):
        print(s, end="")


if __name__ == '__main__':
    text_wrapper_demo()
    string_io_demo()
