from datetime import date, datetime, timedelta, time, timezone

# datetime
now = datetime.now()

print(now)
print(now.date())
print(now.time())
print(now.year)
print(now.month)
print(now.hour)
print(now.minute)
print(now.second)

print()

# strftime
# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
print(now.strftime("%a %A %d"))  # day
print(now.strftime("%b %B %m"))  # month
print(now.strftime("%y %Y"))  # year

# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print(now.strftime("%I:%M:%S %p"))  # 12-Hour:Minute:Second:AM
print(now.strftime("%H:%M:%S"))  # 24-Hour:Minute:Second

# %c - locale's date and time, %x - locale's date, %X - locale's time
print(now.strftime("%c"))
print(now.strftime("%x"))
print(now.strftime("%X"))

print()

# strptime
dt = datetime.strptime('2018-2-9', '%Y-%m-%d')
print(dt)

print()

# date
# Get today's date from the simple today() method from the date class
today = date.today()
print("Today's date is", today)

# print out the date's individual components
print("Date Components:", today.day, today.month, today.year)

# retrieve today's weekday (0=Monday, 6=Sunday)
print("Today's Weekday #:", today.weekday())

print()

# timedelta
# construct a basic timedelta and print it
timediff = timedelta(days=365, hours=5, minutes=1)
print(timediff)
future = now + timediff  # operator overload : datetime = datetime + timedelta
print(future)
timediff2 = future - now  # operator overload : timedelta = datetime - datetime
print(timediff2)

print()

# combine
print(datetime.combine(date.today(), time()))

print()

# timestamp
print("datetieme.now().timestamp():", now.timestamp())
print("datetime.fromtimestamp():", datetime.fromtimestamp(now.timestamp()))

print()

# print today's date
print("today is: " + str(datetime.now()))

# print today's date one year from now
print("one year from now it will be: " +
      str(datetime.now() + timedelta(days=365)))

# create a timedelta that uses more than one argument
print("in two weeks and 3 days it will be: " +
      str(datetime.now() + timedelta(weeks=2, days=3)))

# calculate the date 1 week ago, formatted as a string
t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")
print("one week ago it was " + s)

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

print()
