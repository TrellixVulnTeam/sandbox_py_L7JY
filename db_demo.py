# DB-API 2.0
# JDBC, PDOなどと違って、カーソルオブジェクトに対して文を実行する。

import sqlite3
from collections import namedtuple


def my_func(number):
    if number > 3:
        return 'big'
    else:
        return 'little'


TestRow = namedtuple('TestRow', field_names=['id', 'string', 'number'])


def test_factory(cursor, row):
    return TestRow(*row)


def main():
    print('connect')
    # db = sqlite3.connect('tmp/db_demo.db')
    db = sqlite3.connect(':memory:')
    cur = db.cursor()

    print('create')
    cur.execute("DROP TABLE IF EXISTS test")
    cur.execute("""
        CREATE TABLE test (
            id INTEGER PRIMARY KEY, string TEXT, number INTEGER
        )
        """)

    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('one', 1)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('two', 2)
        """)
    print('insert row')
    cur.execute("""
        INSERT INTO test (string, number) VALUES ('three', 3)
        """)
    print('commit')
    db.commit()

    print('insert rows')
    cur.executemany("""
        INSERT INTO test (string, number) VALUES (?, ?)
        """, [('four', 4), ('five', 5), ('six', 6)])
    print('commit')
    db.commit()

    print('count')
    cur.execute("SELECT COUNT(*) FROM test")
    count = cur.fetchone()[0]
    print(f'there are {count} rows in the table.')

    print('read')
    for row in cur.execute("SELECT * FROM test"):
        print(row)

    print('function')
    db.create_function('my_func', 1, my_func)
    for row in cur.execute("SELECT *, my_func(number) FROM test"):
        print(row)

    print('row factory')
    db.row_factory = test_factory
    cur = db.cursor()  # row factoryの読み直し
    for row in cur.execute("SELECT * FROM test"):
        print(row)  # namedtuple

    print('drop')
    cur.execute("DROP TABLE test")
    print('close')
    db.close()


if __name__ == '__main__':
    main()
