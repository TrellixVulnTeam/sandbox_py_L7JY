from collections.abc import Iterator


class Employees(Iterator):
    """ Bad """
    _employees = {}
    _headcount = 0
    _empid = 0

    def add_employee(self, employee):
        self._headcount += 1
        self._employees[self._headcount] = employee

    def __iter__(self):
        self._empid = 0
        return self  # 自インスタンスを返す

    def __next__(self):
        if self._empid < self._headcount:
            self._empid += 1
            return self._employees[self._empid]
        else:
            raise StopIteration
