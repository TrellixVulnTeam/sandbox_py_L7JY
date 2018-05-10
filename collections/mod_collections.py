from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
from collections import deque
import random


class Fraction(object):
    def __init__(self):
        self.n = 1
        self.d = 2

    def __repr__(self):
        return '{0}/{1}'.format(self.n, self.d)


def counter_demo():
    c = Counter()
    c['apples'] += 1
    c['bananas'] += 1
    c['apples'] += 2
    c['cherries'] = 4
    print(c.most_common())
    print(c['lemons'])

    prose = 'Hoge Fuga awawa fefe'
    prose_counter = Counter()
    for word in prose.lower().split(' '):
        prose_counter[word[0]] += 1
    print(prose_counter.most_common())
    print(prose_counter.elements())
    print(prose_counter.keys())

    fruites = ['apples', 'apples', 'bananas',
               'cherries', 'lemons', 'oranges', 'oranges', ]
    shipment = Counter(fruites)  # Counter from list
    c.update(shipment)
    sold = ['apples', 'apples', 'oranges', 'bananas', ]
    sales = Counter(sold)
    c.subtract(sales)
    print(c.most_common())


def defaultdict_demo():
    str_dict = defaultdict(str)
    str_dict['foo']
    print(str_dict)

    int_dict = defaultdict(int)
    int_dict['foo']
    print(int_dict)

    float_dict = defaultdict(float)
    float_dict['foo']
    print(float_dict)

    int_dict['hello'] = 'world'
    print(int_dict)

    fraction_dict = defaultdict(Fraction)
    fraction_dict['foo']
    print(fraction_dict)

    def dne(): return 'DNE'

    dne_dict = defaultdict(dne)
    dne_dict['foo']
    print(dne_dict)


def ordered_dict_demo():
    fruites_dict = OrderedDict()
    fruites = ['apples', 'bananas', 'cherries',
               'lemons', 'limes', 'oranges', 'peaches']
    for f in fruites:
        fruites_dict[f] = random.randint(50, 100)
    print(fruites_dict)

    fruites_dict['bananas'] = 50
    print(fruites_dict)

    fruites_dict.move_to_end('bananas')
    print(fruites_dict)
    fruites_dict.move_to_end('bananas', False)  # beginning
    print(fruites_dict)
    print(fruites_dict.popitem())
    print(fruites_dict.popitem(False))  # beginning
    print(fruites_dict)


def namedtuple_demo():
    ServerAddress = namedtuple('ServerAddress', ['ip_address', 'port'])

    print([m for m in dir(()) if not m.startswith('__')])
    print([m for m in dir(ServerAddress) if not m.startswith('__')])

    local_web_server = ServerAddress(ip_address='127.0.0.1', port=80)
    print(local_web_server)
    print(local_web_server.ip_address)
    print(local_web_server[1])

    print(isinstance(local_web_server, tuple))


def deque_demo():
    print([m for m in dir(list) if not m.startswith('__')])
    print([m for m in dir(deque) if not m.startswith('__')])

    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    primes_deck = deque(primes)
    print(primes_deck)
    primes_deck.rotate(4)
    print(primes_deck)
    primes_deck.rotate(-2)
    print(primes_deck)
    for x in range(5):
        primes_deck.rotate(x * len(primes_deck))
        print(primes_deck)

    deck2 = deque(maxlen=5)
    deck2.extend(range(5))
    print(deck2)
    deck2.append(10)
    print(deck2)
    deck2.appendleft(0)
    print(deck2)


def most_common_demo():
    lst = [1, 2, 1, 3, 6, 3, 3]
    result = Counter(lst).most_common()
    print(result)


if __name__ == '__main__':
    counter_demo()
    print()
    defaultdict_demo()
    print()
    ordered_dict_demo()
    print()
    namedtuple_demo()
    print()
    deque_demo()
    print()
    most_common_demo()
