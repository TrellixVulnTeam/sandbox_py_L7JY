import abc

from testdata import EMPLOYEES, ACCESSCONTROLS
from employee import Employee


class AbsEmployees(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_employee_info(self, empids):
        pass


class Employees(AbsEmployees):
    def get_employee_info(self, empids):
        return (EMPLOYEES[empid]
                for empid in empids
                if empid in EMPLOYEES)


class Proxy(AbsEmployees):
    """ Composition """

    def __init__(self, employees, reqid):
        self._employees = employees
        self._reqid = reqid

    def get_employee_info(self, empids):
        reqid = self._reqid
        acc = ACCESSCONTROLS

        for e in self._employees.get_employee_info(empids):
            if e.empid == reqid or \
                    (reqid in acc and acc[reqid].can_see_personal):

                # Show everything
                yield Employee(e.empid, e.name,
                               ('%.2f' % e.salary),
                               e.birthdate)

            else:  # Hide birthdate and salary details
                yield Employee(e.empid, e.name, '*****', '*****')


def get_employees_collection(reqid):
    """ factory """
    return Proxy(Employees(), reqid)
