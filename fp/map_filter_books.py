from copy import copy
from functools import partial, reduce
from operator import attrgetter

from books import BOOKS

print('--- map ---')


def sales_price(book):
    """ Apply a 20% discount to the book's price """
    book = copy(book)
    book.price = round(book.price * 0.8, 2)
    return book


sales_books = list(map(sales_price, BOOKS))
print(sales_books)

print()

print('--- filter ---')


def is_long_book(book):
    """ Does a book have more than 600 pages? """
    return book.number_of_pages >= 600


long_books = list(filter(is_long_book, BOOKS))
long_books2 = [book for book in BOOKS if is_long_book(book)]
print(long_books)
print(long_books2)

print()

print('--- chaining: filter-map ---')


def has_roland(book):
    """ predicate """
    return any(["Roland" in subject for subject in book.subjects])


def titlecase(book):
    book = copy(book)
    book.title = book.title.title()
    return book


print(list(map(titlecase, filter(has_roland, BOOKS))))

print()

print('--- chaining: map-filter-sorted ---')


def is_good_deal(book):
    return book.price <= 5


cheap_books = sorted(
    filter(is_good_deal, map(sales_price, BOOKS)),
    key=attrgetter('price')
)
print(cheap_books[0], cheap_books[0].price)

print()

print('--- reduce ---')


def add_book_prices(book1, book2):
    return book1 + book2


total = reduce(add_book_prices, [b.price for b in BOOKS])
print(total)

print()

print('--- partial ---')


def mark_down(book, discount):
    book = copy(book)
    book.price = round(book.price * (1 - discount), 2)
    return book


standard = partial(mark_down, discount=0.2)
print(standard(BOOKS[0]).price)
half = partial(mark_down, discount=0.5)
print(half(BOOKS[0]).price)
half_price_books = map(half, filter(is_long_book, BOOKS))
