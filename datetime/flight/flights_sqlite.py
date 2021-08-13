import sqlite3
from datetime import datetime

from flight_duration import Flight, airports
from recurring_flights import flights

conn = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cur = conn.cursor()

# TIMESTAMP: not an real SQLite type,
# The timestamp(ISO format) string is automatically converted to a datetime object
cur.execute('CREATE TABLE flight('
            'flight_id TEXT, '
            'origin TEXT, '
            'destination TEXT, '
            'departure TIMESTAMP, '
            'arrival TIMESTAMP)')

for flight in flights:
    sql = 'INSERT INTO flight VALUES(?, ?, ?, ?, ?)'
    dep_naive = datetime.combine(flight.departure.date(), flight.departure.time())
    arr_naive = datetime.combine(flight.arrival.date(), flight.arrival.time())
    cur.execute(sql, (flight.id, flight.origin.iata, flight.destination.iata, dep_naive, arr_naive))

# data = cur.execute('SELECT * FROM flight').fetchall()

for row in cur.execute('SELECT * FROM flight'):
    print(row)
    print(Flight(row[0], airports[row[1]], airports[row[2]], row[3], row[4]))

conn.close()
