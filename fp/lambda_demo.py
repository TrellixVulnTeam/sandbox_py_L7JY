from functools import reduce

from books import BOOKS

print('--- lambda ---')


def long_total(a=None, b=None, books=None):
    if a is None and b is None and books is None:
        return None
    if a is None and b is None:
        a = books.pop(0)
        b = books.pop(0)
        return long_total(a, b, books)  # recursion
    if a is not None and books and books is not None and b is None:
        b = books.pop(0)
        return long_total(a, b, books)  # recursion
    if a is not None and b is not None and books is not None:
        return long_total(a + b, None, books)  # recursion
    if a is not None and b is None and not books or books is None:
        return a


print(long_total(None, None, [b.price for b in BOOKS]))

print()

total = reduce(lambda x, y: x + y, [b.price for b in BOOKS], 0)
print(total)
long_books = filter(lambda book: book.number_of_pages >= 600, BOOKS)
print(len(list(long_books)))
good_deals = filter(lambda book: book.price <= 5.99, BOOKS)
print(len(list(good_deals)))

print()
