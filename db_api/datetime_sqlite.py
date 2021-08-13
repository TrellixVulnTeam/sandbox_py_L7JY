import sqlite3
import datetime

# enable adapter/converter functions
con = sqlite3.connect(":memory:",
                      detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
cur = con.cursor()
cur.execute("CREATE TABLE test(d date, ts timestamp)")

today = datetime.date.today()
now = datetime.datetime.now()

# sqlite3.PARSE_DECLTYPES
# builtin adapter: "date" => date, "timestamp" => datetime
cur.execute("INSERT INTO test(d, ts) VALUES (?, ?)", (today, now))
cur.execute("SELECT d, ts FROM test")
row = cur.fetchone()
print(today, "=>", row[0], type(row[0]))
print(now, "=>", row[1], type(row[1]))

# sqlite3.PARSE_COLNAMES
# builtin converter: [date]/[datetime]
cur.execute('SELECT current_date AS "d [date]", current_timestamp AS "ts [timestamp]"')
row = cur.fetchone()
print("current_date:", row[0], type(row[0]))
print("current_timestamp:", row[1], type(row[1]))

con.close()
