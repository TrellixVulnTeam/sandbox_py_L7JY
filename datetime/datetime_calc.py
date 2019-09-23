# Perform calculations with dates and times using timedelta
import datetime

now = datetime.datetime.now()
today = datetime.date.today()

# create some date objects
dt1 = datetime.datetime(2019, 1, 15, 10)
dt2 = datetime.datetime(2019, 1, 20, 15)

# dates and times can be compared
print(dt1 < dt2)
print(dt1 > dt2)

# Subtracting one date from another creates a timedelta
delta = dt2 - dt1
print(delta)

# timedeltas have components
print(delta.days)
print(delta.seconds)

print()

# timedeltas can be used to perform date math
oneyear = datetime.timedelta(days=365)
oneweek = datetime.timedelta(weeks=1)

print("One year from now will be: ", now + oneyear)
print("One week from now will be: ", now + oneweek)
print("One week ago was: ", now - oneweek)

print()

# timedelta
# for datetime and date not time object
timediff = datetime.timedelta(days=365, hours=5, minutes=1)
print(timediff)
print(repr(timediff))
future = now + timediff  # datetime = datetime + timedelta
print(repr(future))
timediff2 = future - now  # timedelta = datetime - datetime
print(repr(timediff2))
future2 = today + datetime.timedelta(hours=11) * 5  # date = date + timedelta
print(repr(future2))

print()

# How many days until April Fools' Day?
today = datetime.date.today()  # get today's date
afd = datetime.date(today.year, 4, 1)  # get April Fool's for the same year
# use date comparison to see if April Fool's has already gone for this year
# if it has, use the replace() function to get the date for next year
if afd < today:
    print(f"April Fool's day already went by {(today - afd).days} days ago")
    afd = afd.replace(year=today.year + 1)  # if so, get the date for next year

# Now calculate the amount of time until April Fool's Day
time_to_afd = abs(afd - today)
print(time_to_afd.days, "days until next April Fools' Day!")
