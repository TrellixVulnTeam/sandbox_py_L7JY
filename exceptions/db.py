# Example of Context Manager
import contextlib


class Connection:
    def __init__(self):
        self.xid = 0

    def _start_transaction(self):
        print(f'starting transaction:{self.xid}')
        rslt = self.xid
        self.xid += 1
        return rslt

    def _commit_transaction(self, xid):
        print(f'committing transaction:{xid}')

    def _rollback_transaction(self, xid):
        print(f'rolling back transaction:{xid}')


class Transaction:
    def __init__(self, conn):
        self.conn = conn
        self.xid = conn._start_transaction()

    def commit(self):
        self.conn._commit_transaction(self.xid)

    def rollback(self):
        self.conn._rollback_transaction(self.xid)


@contextlib.contextmanager
def start_transaction(connection):
    tx = Transaction(connection)

    try:
        yield tx
    except Exception:
        tx.rollback()
        raise

    tx.commit()


if __name__ == '__main__':
    conn = Connection()
    try:
        with start_transaction(conn) as tx:
            x = 1 + 1
            raise ValueError()
            y = x + 2
            print(f"transaction:{tx.xid} => {x}, {y}")
    except ValueError:
        print(f"Oops, transaction:{tx.xid} failed.")

    print()
    try:
        with start_transaction(conn) as tx:
            x = 1 + 1
            y = x + 2
            print(f"transaction:{tx.xid} => {x}, {y}")
    except ValueError:
        print(f"Oops, transaction:{tx.xid} failed.")
