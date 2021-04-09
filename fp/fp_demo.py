import functools
import itertools

# map
print(list(map(lambda x: x * 2, [x for x in range(10)])))
print([x * 2 for x in range(10)])  # comprehension

print(dict(map(lambda x, y: (x, y), ["a", "b", "c", "d"], itertools.count())))  # zip

# filter
print(list(filter(lambda x: x > 0, [1, -2, 0, 5, 8, -3])))
print(list(filter(None, [0, 1, False, True, [], [0], {}, (), "", "abc"])))  # filter only True value

print()


# functools.reduce
def product(x, y):
    return x * y


print(functools.reduce(product, [1, 2, 3, 4, 5]))

print()


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(1))

print()

# Recursive Problem
courses = {
    'count': 2,
    'title': 'Django Basics',
    'prereqs': [
        {
            'count': 3,
            'title': 'Object-Oriented Python',
            'prereqs': [
                {
                    'count': 1,
                    'title': 'Python Collections',
                    'prereqs': [
                        {
                            'count': 0,
                            'title': 'Python Basics',
                            'prereqs': []
                        }
                    ]
                },
                {
                    'count': 0,
                    'title': 'Python Basics',
                    'prereqs': []
                },
                {
                    'count': 0,
                    'title': 'Setting Up a Local Python Environment',
                    'prereqs': []
                }
            ]
        },
        {
            'count': 0,
            'title': 'Flask Basics',
            'prereqs': []
        }
    ]
}


def prereqs(data, pres=None):
    if pres is None:
        pres = set()
    else:
        pres.add(data['title'])
    if data['prereqs']:
        [prereqs(d, pres) for d in data['prereqs']]
    return pres


print(prereqs(courses))

print()

meals = [
    {'name': 'cheeseburger', 'calories': 750},
    {'name': 'cobb salad', 'calories': 250},
    {'name': 'large pizza', 'calories': 1500},
    {'name': 'burrito', 'calories': 1050},
    {'name': 'stir fry', 'calories': 625},
]

high_cal = filter(lambda meal: meal['calories'] > 1000, meals)
print(list(high_cal))

print()

print('--- currying ---')


def curried_f(x, y=None, z=None):
    def f(x, y, z):
        return x**3 + y**2 + z

    # returns the partial function with current variables saved

    if y is not None and z is not None:  # if you have ALL x, y, z
        return f(x, y, z)  # return as normal
    if y is not None:  # if you have x and y, but NOT z
        return lambda z: f(x, y, z)  # z will be the next run's x!
    return lambda y, z=None: (  # if you have JUST x
        f(x, y, z)
        if (y is not None and z is not None)  # setup for third run
        else lambda z: f(x, y, z)  # z will be the next run's x
    )


# partial application
print(curried_f(2, 3, 4))
print(curried_f(2, 3)(4))
print(curried_f(2)(3, 4))
print(curried_f(2)(3)(4))
print(curried_f(2)(3))
print(curried_f(2))
