from datetime import datetime

import dateutil.relativedelta as rd
import dateutil.rrule as dr
from dateutil.parser import parse

now = datetime.now()
print(now)

delta = rd.relativedelta(weeks=+1, hour=10)
print(now + delta)

birthdate = datetime(1991, 11, 20, 0, 0)
print(rd.relativedelta(now, birthdate))

episodes = dr.rrule(
    freq=dr.WEEKLY,
    byweekday=rd.MO,
    byhour=21,
    dtstart=datetime(2017, 9, 1, 0, 0),
    count=9
)
print(list(episodes))

print()

# parsing
print(parse('2017'))  # today of 2017
print(parse('2017 January 3, 18:00'))
print(parse('3 January 2017, 18:00 hello', fuzzy=True))
print(parse('01/02/03'))  # month/day/year
print(parse('01/02/03', yearfirst=True))
print(parse('01/02/03', yearfirst=True, dayfirst=True))
