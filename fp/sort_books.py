from operator import attrgetter, itemgetter

from books import BOOKS, RAW_BOOKS

print('--- sort ---')

pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))
print(pub_sort)
pub_sort2 = sorted(RAW_BOOKS, key=lambda book: book['publish_date'])
print(pub_sort2)
print(pub_sort == pub_sort2)

print()

books_sort = sorted(BOOKS, key=attrgetter('number_of_pages'))
print(books_sort)
books_sort2 = sorted(BOOKS, key=lambda book: book.number_of_pages)
print(books_sort2)
print(books_sort == books_sort2)

print()
