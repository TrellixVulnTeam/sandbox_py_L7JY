# DB-API 2.0
# JDBC, PDOなどと違って、カーソルオブジェクトに対して文を実行する。

import sqlite3
from dataclasses import dataclass
from numbers import Number

from collections import namedtuple


def my_func(number):
    return 'big' if number > 3 else 'little'


def test_factory(cursor, row):
    TestRow = namedtuple('TestRow', field_names=['id', 'string', 'number'])
    return TestRow(*row)


@dataclass(frozen=True)
class RowData:
    id: int
    string: str
    number: Number


def test_factory2(cursor, row):
    return RowData(*row)


def main():
    print('--- connect ---')
    # isolation_level=None: Auto commit
    # db = sqlite3.connect('tmp/db_demo.db', isolation_level=None)
    # db = sqlite3.connect('tmp/db_demo.db')
    db = sqlite3.connect(':memory:')
    cur = db.cursor()

    print('--- create ---')
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY,
            string TEXT,
            number INTEGER
        )
        """)

    print('--- insert row ---')
    cur.execute("INSERT INTO test (string, number) VALUES ('one', 1)")

    print('--- insert row ---')
    cur.execute("INSERT INTO test (string, number) VALUES ('two', 2)")

    print('--- insert row ---')
    cur.execute("INSERT INTO test (string, number) VALUES ('three', 3)")

    print('--- commit ---')
    db.commit()

    print('--- insert rows ---')
    cur.executemany("INSERT INTO test (string, number) VALUES (?, ?)",
                    [('four', 4), ('five', 5), ('six', 6)])  # sequence of params(tuple)

    print('--- commit ---')
    db.commit()

    print('--- read ---')
    select_all = "SELECT * FROM test"
    for row in cur.execute(select_all):  # iterable
        print(row)

    print('--- count ---')
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]
    print(f'there are {count} rows in the table.')

    print('--- python function ---')
    db.create_function('my_func', 1, my_func)
    for row in cur.execute("SELECT *, my_func(number) FROM test"):
        print(row)

    print('--- row factory ---')
    # db.row_factory = sqlite3.Row  # built-in

    db.row_factory = test_factory  # custom row factory (namedtuple)
    cur = db.cursor()  # row factoryの読み直し
    for row in cur.execute(select_all):
        print(row)

    db.row_factory = test_factory2  # custom row factory (dataclass)
    cur = db.cursor()
    for row in cur.execute(select_all):
        print(row)

    print('--- drop ---')
    cur.execute("DROP TABLE test")

    print('--- close ---')
    db.close()


if __name__ == '__main__':
    main()
