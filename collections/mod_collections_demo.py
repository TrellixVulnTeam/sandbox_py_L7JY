import random
from collections import Counter, OrderedDict, defaultdict, deque, namedtuple
from typing import NamedTuple


def get_non_dunder_attrs(o):
    return [a for a in dir(o) if not a.startswith('__')]


class ServerAddress(NamedTuple):
    """Python3.6"""
    ip_address: str
    port: int


def namedtuple_demo():
    """Factory function for creating subclass of tuple"""
    ServerAddress = namedtuple('ServerAddress', ['ip_address', 'port'])

    print(get_non_dunder_attrs(tuple))
    print(get_non_dunder_attrs(ServerAddress))

    local_web_server = ServerAddress(ip_address='127.0.0.1', port=80)
    print(local_web_server)
    print(local_web_server.ip_address)
    print(local_web_server.port)
    print(isinstance(local_web_server, tuple))
    print(local_web_server[0])
    print(local_web_server[-1])


def counter_demo():
    """subclass of dict"""
    print(get_non_dunder_attrs(dict))
    print(get_non_dunder_attrs(Counter))

    fruits = Counter()
    fruits['bananas'] += 1
    fruits['apples'] += 1
    fruits['apples'] += 2
    fruits['cherries'] = 4
    print(fruits)
    print(fruits.most_common())
    print(list(fruits.elements()))
    print(fruits.keys())
    print(fruits['lemons'])

    arrived = ['apples', 'apples', 'bananas', 'apples',
               'cherries', 'lemons', 'oranges', 'oranges', ]
    arrived_counter = Counter(arrived)
    fruits.update(arrived_counter)  # 加算（overrides dict.update）
    print(fruits)

    sold = ['apples', 'apples', 'oranges', 'bananas', ]
    sold_counter = Counter(sold)
    fruits.subtract(sold_counter)  # 減算
    print(fruits)


def defaultdict_demo():
    """useful for aggregating data"""
    print(get_non_dunder_attrs(dict))
    print(get_non_dunder_attrs(defaultdict))

    # define a list of items that we want to count
    fruits = ['apple', 'pear', 'orange', 'banana',
              'apple', 'grape', 'banana', 'banana']

    fruits_counter = defaultdict(int)  # int(0): default factory

    for fruit in fruits:
        fruits_counter[fruit.lower()] += 1

    for (k, v) in fruits_counter.items():
        print(f"{k}: {v}")


def ordered_dict_demo():
    """
    挿入順を保証する: Doubly Linked List
    """
    print(get_non_dunder_attrs(dict))
    print(get_non_dunder_attrs(OrderedDict))

    fruits_dict = OrderedDict()
    fruits = ['apples', 'bananas', 'cherries',
              'lemons', 'limes', 'oranges', 'peaches']
    for f in fruits:
        fruits_dict[f] = random.randint(50, 100)
    print(fruits_dict)

    fruits_dict['bananas'] = 50
    print(fruits_dict)

    fruits_dict.move_to_end('bananas')
    print(fruits_dict)
    fruits_dict.move_to_end('bananas', False)  # beginning
    print(fruits_dict)
    print(fruits_dict.popitem())
    print(fruits_dict.popitem(False))  # beginning
    print(fruits_dict)


def deque_demo():
    d = deque()

    # to use deque like a queue always pop from the opposite side
    # that append was called on
    print('# deque as a queue (left to right) - appendleft/pop')
    d.appendleft(1)
    d.appendleft(2)
    d.appendleft(3)
    print(d)
    d.pop()
    print(d)
    d.pop()
    print(d)
    d.pop()
    print(d)

    print('# deque as a queue (right to left) - append/popleft')
    d.append(1)
    d.append(2)
    d.append(3)
    print(d)
    d.popleft()
    print(d)
    d.popleft()
    print(d)
    d.popleft()
    print(d)

    # to use deque like a Stack (LIFO)
    # use the pop/append methods from one side only
    print('# deque as a stack (right side) - append/pop')
    d.append(1)
    d.append(2)
    d.append(3)
    print(d)
    d.pop()
    print(d)
    d.pop()
    print(d)
    d.pop()
    print(d)

    print('# deque as a stack (left side) - appendleft/popleft')
    d.appendleft(1)
    d.appendleft(2)
    d.appendleft(3)
    print(d)
    d.popleft()
    print(d)
    d.popleft()
    print(d)
    d.popleft()
    print(d)


def deque_demo2():
    # rotate
    primes = [2, 3, 5, 7, 11, 13, 17]
    primes_deck = deque(primes)
    print(primes_deck)
    primes_deck.rotate(4)
    print(primes_deck)
    primes_deck.rotate(-2)
    print(primes_deck)

    # maxlen
    deck = deque(maxlen=5)
    deck.extend(range(5))
    print(deck)
    deck.append(10)
    print(deck)
    deck.appendleft(0)
    print(deck)


if __name__ == '__main__':
    namedtuple_demo()
    print('-' * 80)
    counter_demo()
    print('-' * 80)
    defaultdict_demo()
    print('-' * 80)
    ordered_dict_demo()
    print('-' * 80)
    deque_demo()
    print('-' * 80)
    deque_demo2()
