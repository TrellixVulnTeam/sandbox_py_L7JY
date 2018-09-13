from functools import reduce
import operator  # infix operators

print(reduce(operator.add, [1, 2, 3, 4, 5]))

numbers = [1, 2, 3, 4, 5]
accumulator = operator.add(numbers[0], numbers[1])
for item in numbers[2:]:
    accumulator = operator.add(accumulator, item)


def mul(x, y):
    print('mul: {} * {}'.format(x, y))
    return x * y


reduce(mul, range(1, 10))

# print(reduce(mul, []))
print(reduce(mul, [], 111))  # initial value

print()


def count_words(doc):
    normalised_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    for word in normalised_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


documents = [
    'It was the best of times, it was the worst of times.',
    'I went to the woods because I wished to live deliberately, to front only the essential facts of life...',
    'Friends, Romans, countrymen, lend me your ears; I come to bury Caesar, not to praise him.',
    'I do not like green eggs and ham. I do not like them, Sam-I-Am.'
]

print(count_words(documents[0]))


def combine_counts(d1, d2):
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d


total_counts = reduce(combine_counts, map(count_words, documents))
print(total_counts)
