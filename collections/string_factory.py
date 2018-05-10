# template

template = "Hi, I'm {name} and I love to eat {food}!"


def string_factory(values):
    list_of_strings = []
    for item in values:
        list_of_strings.append(template.format(**item))  # unpack
    return list_of_strings


data = [
    {"name": "Michelangelo", "food": "Pizza"},
    {"name": "Garfield", "food": "Lasagna"}
]

print(string_factory(data))
