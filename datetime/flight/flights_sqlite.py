import sqlite3
from datetime import datetime

from flight_duration import Flight, airports
from recurring_flights import flights


def insert_flight(cur, flight):
    sql = 'INSERT INTO flight VALUES(?,?,?,?,?)'
    dep_naive = datetime.combine(flight.departure.date(), flight.departure.time())
    arr_naive = datetime.combine(flight.arrival.date(), flight.arrival.time())
    cur.execute(sql, (flight.id, flight.origin.iata, flight.destination.iata, dep_naive, arr_naive))


conn = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES)
cur = conn.cursor()

# TIMESTAMP: not SQLite type, Python convert to datetime object
cur.execute('CREATE TABLE flight('
            'flight_id TEXT, '
            'origin TEXT,'
            'destination TEXT,'
            'departure TIMESTAMP,'
            'arrival TIMESTAMP)')

for f in flights:
    insert_flight(cur, f)

data = cur.execute('SELECT * FROM flight').fetchall()
print(data)

for row in data:
    print(Flight(row[0], airports[row[1]], airports[row[2]], row[3], row[4]))
