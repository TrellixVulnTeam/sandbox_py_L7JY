import sqlite3


def transaction():
    con = sqlite3.connect(":memory:")
    cur = con.execute("CREATE TABLE person (id INTEGER PRIMARY KEY, name TEXT NOT NULL)")

    try:
        cur.execute("INSERT INTO person (name) VALUES (?)", ("Hoge Hoge",))
    except sqlite3.DatabaseError as e:
        con.rollback()
        print('rollbacked:', e)
    else:
        con.commit()
        print('committed')

    cur.execute("SELECT COUNT(*) FROM person")
    print(f'{cur.fetchone()[0]} rows in the table.')

    try:
        cur.execute("INSERT INTO person (name) VALUES (?)", ("Fuga Fuga",))
        cur.execute("INSERT INTO person (name) VALUES (?)", (None,))
    except sqlite3.DatabaseError as e:
        con.rollback()
        print('rollbacked:', e)
    else:
        con.commit()
        print('committed')

    cur.execute("SELECT COUNT(*) FROM person")
    print(f'{cur.fetchone()[0]} rows in the table.')

    con.close()


def transaction_with_context_manager():
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE person (id INTEGER PRIMARY KEY, firstname VARCHAR UNIQUE)")

    # Successful, con.commit() is called automatically afterwards
    with con:
        con.execute("INSERT INTO person(firstname) VALUES (?)", ("Joe",))

    # con.rollback() is called after the with block finishes with an exception, the
    # exception is still raised and must be caught
    try:
        with con:
            con.execute("INSERT INTO person(firstname) VALUES (?)", ("Joe",))
    except sqlite3.IntegrityError:
        print("couldn't add Joe twice")

    # Connection object used as context manager only commits or rollbacks transactions,
    # so the connection object should be closed manually
    con.close()


if __name__ == '__main__':
    transaction()
    print('---')
    transaction_with_context_manager()
