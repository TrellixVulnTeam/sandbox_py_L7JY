from datetime import datetime

from employee import Employee
from employees1 import Employees as Employees1
from employees2 import Employees as Employees2
from employees3 import Employees as Employees3
from department import Department, Departments

TESTEMPLOYEES = (
    (1, 'Douglas Adams', datetime(1942, 7, 6)),
    (2, 'Sherlock Holmes', datetime(1887, 3, 15)),
    (3, 'Albert Einstein', datetime(1915, 11, 25)),
    (4, 'Sir John A Macdonald', datetime(1867, 8, 1)),
    (5, 'Theodore Roosevelt', datetime(1901, 9, 14))
)

TESTDEPARTMENTS = (
    (101, 'Sci-Fi Comedy', datetime(2010, 10, 1)),
    (102, 'Mystery', datetime(2012, 2, 13)),
    (103, 'Physics', datetime(2014, 5, 14)),
    (104, 'Politics', datetime(2016, 7, 28)),
    (201, 'POTUS', datetime(1776, 7, 4))
)


def populate_employees(employees_class):
    employees = employees_class()
    for number, name, date in TESTEMPLOYEES:
        employees.add_employee(
            Employee(number, name, date)
        )
    return employees


employees1 = populate_employees(Employees1)
employees2 = populate_employees(Employees2)
employees3 = populate_employees(Employees3)

departments = Departments()
for number, name, date in TESTDEPARTMENTS:
    departments.add_department(
        Department(number, name, date)
    )
