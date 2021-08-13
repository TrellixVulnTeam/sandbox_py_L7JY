# DB-API 2.0

import sqlite3
from dataclasses import dataclass
from numbers import Number

from collections import namedtuple


def my_func(number):
    return 'big' if number > 3 else 'little'


def namedtuple_factory(cursor, row):
    RowNamedTuple = namedtuple('RowNamedTuple', field_names=['id', 'string', 'number'])
    return RowNamedTuple(*row)


@dataclass(frozen=True)
class RowData:
    id: int
    string: str
    number: Number


def dataclass_factory(cursor, row):
    return RowData(*row)


def main():
    print(f'SQLite version {sqlite3.sqlite_version}')

    print('--- connect ---')
    # db = sqlite3.connect('tmp/db_demo.db')
    # db = sqlite3.connect('tmp/db_demo.db', isolation_level=None)  # auto commit
    db = sqlite3.connect(':memory:')
    cur = db.cursor()

    print('--- create table ---')
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY,
            string TEXT,
            number INTEGER
        )
        """)

    # SQLite meta-data
    print('--- table_info ---')
    cur.execute("PRAGMA table_info(test)")
    row = cur.fetchall()
    # (column id, column name, not null, default value, primary key)
    print(row)

    print('--- insert row ---')
    cur.execute("INSERT INTO test (string, number) VALUES ('one', 1)")
    print(f'lastrowid={cur.lastrowid}')

    print('--- insert row ---')
    cur.execute("INSERT INTO test (string, number) VALUES ('two', 2)")
    print(f'lastrowid={cur.lastrowid}')

    print('--- insert row ---')
    cur.execute("INSERT INTO test (string, number) VALUES ('三', 3)")
    print(f'lastrowid={cur.lastrowid}')

    print('--- commit ---')
    db.commit()

    print('--- insert rows ---')
    row_data = [
        ('four', 4),
        ('五', 5),
        ('six', 6),
        ('seven', 7),
        ('八', 8),
    ]
    cur.executemany("INSERT INTO test (string, number) VALUES (?, ?)", row_data)
    print(f'rowcount={cur.rowcount}')

    print('--- commit ---')
    db.commit()

    print('--- read ---')
    select_all = "SELECT * FROM test"
    for row in cur.execute(select_all):  # iterable
        print(row)  # tuple

    print('--- read with row factory (built-in: sqlite3.Row) ---')
    db.row_factory = sqlite3.Row
    cur = db.cursor()  # reload row factory
    for row in cur.execute(select_all):
        print(f'as tuple: {tuple(row)}, as dict: {dict(row)}')

    print('--- read with row factory (custom: namedtuple) ---')
    db.row_factory = namedtuple_factory  # custom row factory
    cur = db.cursor()
    for row in cur.execute(select_all):
        print(row)

    print('--- read with row factory (custom: dataclass) ---')
    db.row_factory = dataclass_factory  # custom row factory
    cur = db.cursor()
    for row in cur.execute(select_all):
        print(row)

    cur.row_factory = None  # reset row factory

    print('--- read by fetchall ---')
    cur.execute(select_all)
    while rows := cur.fetchall():
        print(rows)

    print('--- read by fetchmany ---')
    cur.execute(select_all)
    while rows := cur.fetchmany(3):
        print(rows)

    print('--- count ---')
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]
    print(f'there are {count} rows in the table.')

    print('--- python function ---')
    db.create_function('my_func', 1, my_func)
    for row in cur.execute("SELECT *, my_func(number) FROM test"):
        print(row)

    print('--- drop ---')
    cur.execute("DROP TABLE test")

    print('--- close ---')
    cur.close()
    db.close()


if __name__ == '__main__':
    main()
