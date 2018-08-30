from datetime import date, datetime, timedelta, time, timezone

# date
# year=1-9999, month=1-12, day=1-31
print(date.min)
print(date.max)
print(date.resolution)

print(date(2018, 1, 1))
print(date(year=2018, month=1, day=1))
# print(date(2017, 2, 29))  # NG

today = date.today()
print(today)
print(today.weekday())  # 0:Mon - 6:Sun
print(today.isoweekday())  # 1:Mon - 7:Sun

print(date.fromtimestamp(1_000_000_000))
print(date.fromordinal(1))
print(date.fromordinal(730000))

print()

# time
print(time.min)
print(time.max)
print(time.resolution)

print(time())  # time class has no other factory methods

t = time(hour=1, minute=23, second=45, microsecond=6789)
print(t)
print(t.isoformat())

print()

# datetime
print(datetime(2018, 1, 1, 2, 3, 4, 56789))
print(datetime.utcnow())
print(datetime.fromtimestamp(1_000_000_000))
print(datetime.utcfromtimestamp(1_000_000_000))
print(datetime.fromordinal(1))
print(datetime.fromordinal(730000))
print(datetime.combine(date.today(), time()))
print(datetime.strptime('2018-2-9', '%Y-%m-%d'))

now = datetime.now()

print(now)
print(now.isoformat())
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

print()

# strftime
# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
print(now.strftime("%a %A %d %d"))  # day
print(now.strftime("%b %B %m"))  # month
print(now.strftime("%y %Y"))  # year

# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print(now.strftime("%I:%M:%S %p"))  # 12-Hour:Minute:Second:AM
print(now.strftime("%H:%M:%S"))  # 24-Hour:Minute:Second

# %c - locale's date and time, %x - locale's date, %X - locale's time
print(now.strftime("%c"))
print(now.strftime("%x"))
print(now.strftime("%X"))

print("{:%A %d %B %Y}".format(now))

print()

# timedelta
# for datetime and date not time object
timediff = timedelta(days=365, hours=5, minutes=1)
print(timediff)
print(repr(timediff))
future = now + timediff  # datetime = datetime + timedelta
print(repr(future))
timediff2 = future - now  # timedelta = datetime - datetime
print(repr(timediff2))
future2 = today + timedelta(hours=11) * 5  # date = date + timedelta
print(repr(future2))

print()

# How many days until April Fools' Day?
today = date.today()  # get today's date
afd = date(today.year, 4, 1)  # get April Fool's for the same year
# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print("April Fool's day already went by %d days ago" % (today - afd).days)
    afd = afd.replace(year=today.year + 1)  # if so, get the date for next year

# Now calculate the amount of time until April Fool's Day
time_to_afd = abs(afd - today)
print(time_to_afd.days, "days until next April Fools' Day!")

print()


def example(mmdd):
    try:
        date = datetime.strptime(mmdd, '%m/%d')
        output = date.strftime('%b_%d')
        print(output)
    except ValueError:
        print("That's not a valid date. Please try again.")


example("4/31")
example("2/29")
example("12/12")
