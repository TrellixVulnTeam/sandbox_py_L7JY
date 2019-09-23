from datetime import date, datetime, time

# date, time, datetime are all immutable

# date
# year=1-9999, month=1-12, day=1-31
print(date.min)
print(date.max)
print(date.resolution)

print(date(2018, 1, 1))
print(date(year=2018, month=1, day=1))
# print(date(2017, 2, 29))  # NG

print(date.fromtimestamp(1_000_000_000))
print(date.fromordinal(1))
print(date.fromordinal(730000))

today = date.today()
print(today)
print(today.weekday())  # 0:Mon - 6:Sun
print(today.isoweekday())  # 1:Mon - 7:Sun
print(today.replace(year=1987))

print()

# time
print(time.min)
print(time.max)
print(time.resolution)

print(time())  # time class has no other factory methods

t = time(hour=1, minute=23, second=45, microsecond=6789)
print(t)
print(t.replace(hour=5))
print(t.isoformat())

print()

# datetime
dt = datetime(2018, 1, 1, 2, 3, 4, 56789)
print(dt)
print(dt.replace(year=2019, hour=23))
print(datetime.utcnow())
print(datetime.fromtimestamp(1_000_000_000))
print(datetime.utcfromtimestamp(1_000_000_000))
print(datetime.fromordinal(1))
print(datetime.fromordinal(730000))
print(datetime.combine(date.today(), time()))
print(datetime.strptime('2018-2-9', '%Y-%m-%d'))

print()

now = datetime.now()

print(now)
print(now.isoformat())  # ISO8601
print(now.ctime())  # C format
print(now.date())
print(now.time())
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

print(datetime.min)
print(datetime.max)
print(datetime.resolution)
