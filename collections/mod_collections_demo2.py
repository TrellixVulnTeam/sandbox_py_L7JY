from collections import Counter
from collections import defaultdict
from collections import OrderedDict
from collections import namedtuple
from collections import deque
import string


def namedtuple_demo():
    # create a Point namedtuple
    Point = namedtuple("Point", "x y")

    p1 = Point(10, 20)
    p2 = Point(30, 40)

    print(p1, p2)
    print(p1.x, p1.y)

    # use _replace to create a new instance
    p1 = p1._replace(x=100)
    print(p1)


def counter_demo():
    # list of students in class 1
    class1 = ["Bob", "James", "Chad", "Darcy", "Penny", "Hannah",
              "Kevin", "James", "Melanie", "Becky", "Steve", "Frank"]

    # list of students in class 2
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

    # Create a Counter for class1 and class2
    c1 = Counter(class1)  # subclass of dict
    c2 = Counter(class2)

    # How many students in class 1 named James?
    print(c1["James"])

    # How many students are in class 1?
    print(sum(c1.values()), "students in class 1")

    # Combine the two classes
    print(id(c1))
    # c1.update(class2)
    c1 += c2
    print(id(c1))
    print(sum(c1.values()), "students in class 1 and 2")

    # What's the most common name in the two classes?
    print(c1.most_common(3))

    # Separate the classes again
    print(id(c1))
    # c1.subtract(class2)
    c1 -= c2
    print(id(c1))
    print(c1.most_common(1))

    # What's common between the two classes?
    print(c1 & c2)


def defaultdict_demo():
    # param: default factory (Supplier function)

    str_dict = defaultdict(str)
    str_dict['foo']
    print(str_dict)

    int_dict = defaultdict(int)
    int_dict['foo']
    print(int_dict)
    int_dict['hello'] = 'world'  # no error
    print(int_dict)

    float_dict = defaultdict(float)
    float_dict['foo']
    print(float_dict)

    fraction_dict = defaultdict(Fraction)
    fraction_dict['foo']
    print(fraction_dict)

    dne_dict = defaultdict(lambda: 'DNE')
    dne_dict['foo']
    print(dne_dict)


def ordered_dict_demo():
    # list of sport teams with wins and losses
    sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)),
                  ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                  ("Kings", (15, 15)), ("Chargers", (20, 10)),
                  ("Jets", (16, 14)), ("Warriors", (25, 5))]

    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

    # create an ordered dictionary of the teams
    teams = OrderedDict(sortedTeams)
    print(teams)

    # Use popitem to remove the top item
    tm, wl = teams.popitem(False)
    print("Top team: ", tm, wl)

    # What are next the top 4 teams?
    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break

    # test for equality
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "c": 3, "b": 2})
    c = {"a": 1, "c": 3, "b": 2}
    print("Equality test: ", a == b)
    print("Equality test: ", a == c)  # True: OrderedDict is subclass of dict


def deque_demo():
    # initialize a deque with lowercase letters
    d = deque(string.ascii_lowercase)

    # deques support the len() function
    print("Item count: " + str(len(d)))

    # deques can be iterated over
    # for elem in d:
    #     print(elem.upper(), end=",")
    print(",".join(elem.upper() for elem in d))

    # manipulate items from either end
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)

    # rotate the deque
    print(d)
    d.rotate(1)  # to right
    print(d)


if __name__ == '__main__':
    namedtuple_demo()
    print()
    defaultdict_demo()
    print()
    counter_demo()
    print()
    ordered_dict_demo()
    print()
    deque_demo()
    print()
