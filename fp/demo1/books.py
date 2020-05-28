import json

FILE_NAME = '../../data/books.json'


class Book:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title

    def __repr__(self):
        return str(self)


def get_books(raw=False):
    try:
        data = json.load(open(FILE_NAME))
    except FileNotFoundError:
        return []
    else:
        if raw:
            return data['books']
        return [Book(**book) for book in data['books']]


# BOOKS is a list of the Book instances
BOOKS = get_books()
# RAW_BOOKS is a list of book dictionaries
RAW_BOOKS = get_books(raw=True)

if __name__ == '__main__':
    print(BOOKS)
    print(RAW_BOOKS)
