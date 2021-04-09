from dataclasses import dataclass


class Person:
    first_name: str
    last_name: str

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'Person: {self.first_name} {self.last_name} hash = {hash(self)}'

    def __hash__(self):
        to_hash = (self.first_name, self.last_name)
        return hash(to_hash)

    def __eq__(self, value):
        return (type(self) == type(value)
                and self.last_name == value.last_name
                and self.first_name == value.first_name)


class Person2:
    """no overridden __eq__()"""
    first_name: str
    last_name: str

    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f'Person: {self.first_name} {self.last_name} hash = {hash(self)}'

    def __hash__(self):
        to_hash = (self.first_name, self.last_name)
        return hash(to_hash)


@dataclass(frozen=True)  # frozen-True => hashable
class PersonD:
    first_name: str
    last_name: str


def demo(person_cls):
    p1 = person_cls("Hoge", "Hoge")
    p2 = person_cls("Fuga", "Fuga")
    p3 = person_cls("Hoge", "Hoge")

    print(hash(p1))
    print(p1 == p3)

    s = {p1, p2}
    print(p3 in s)
    s.add(p3)
    print(s)


if __name__ == '__main__':
    demo(Person)
    print('---')
    demo(Person2)
    print('---')
    demo(PersonD)
