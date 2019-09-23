class Department(object):
    def __init__(self, deptid, name, date_established):
        self.deptid = deptid
        self.name = name
        self.date_established = date_established


class Departments(object):
    _departments = []

    def add_department(self, department):
        self._departments.append(department)

    def get_department(self, i):
        return self._departments[i]

    @property
    def departments_range(self):
        return (0, len(self._departments) - 1)
