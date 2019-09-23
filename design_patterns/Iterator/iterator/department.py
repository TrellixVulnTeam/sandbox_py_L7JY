from collections.abc import Sequence


class Department(object):
    def __init__(self, number, name, date):
        self.number = number
        self.name = name
        self.date = date


class Departments(Sequence):
    """ sequenceもiteratorとして利用可能 """
    _departments = []

    def add_department(self, department):
        self._departments.append(department)

    def __getitem__(self, item):
        return self._departments[item]

    def __len__(self):
        return len(self._departments)
