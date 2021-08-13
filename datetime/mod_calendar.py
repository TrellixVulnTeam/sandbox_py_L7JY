# Calendar Module
import calendar
import locale
from datetime import datetime, timedelta

now = datetime.now()

test_date = now + timedelta(days=2)
three_weeks_ago = now - timedelta(weeks=3)

print(test_date.date())
print(three_weeks_ago.date())

if test_date > three_weeks_ago:
    print("Comparison works")

print()

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
cal = c.formatmonth(2013, 1, 0, 0)
print(cal)

# calendar (shorthand)
c = calendar.month(2013, 1)
print(c)

# create an HTML formatted calendar
c = calendar.HTMLCalendar(calendar.SUNDAY)
cal = c.formatmonth(2013, 1)
print(cal)

print()

# tips
print(calendar.weekday(2001, 10, 11))

print(calendar.isleap(1999))
print(calendar.isleap(2000))
print(calendar.isleap(2100))

print()

print(list(calendar.month_name))
print(list(calendar.day_name))
print(list(calendar.day_abbr))

print()

# iterator
c = calendar.c  # TextCalendar(calendar.MONDAY)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
print(list(c.itermonthdates(2013, 8)))
print(list(c.itermonthdays(2013, 8)))
print(list(c.itermonthdays2(2013, 8)))
print(list(c.itermonthdays3(2013, 8)))  # 3.7
print(list(c.itermonthdays4(2013, 8)))  # 3.7
print(list(c.iterweekdays()))

print()

locale.setlocale(locale.LC_ALL, '')  # 環境から取得して設定する
print(locale.getlocale(locale.LC_TIME))
print(list(calendar.month_name))
print(list(calendar.day_name))
print(list(calendar.day_abbr))

print()

# example: First Friday of every month.
for m in range(1, 13):
    # returns an array of weeks that represent the month
    cal = calendar.monthcalendar(2013, m)
    # The first Friday has to be within the first two weeks
    weekone = cal[0]
    weektwo = cal[1]

    if weekone[calendar.FRIDAY] != 0:
        meetday = weekone[calendar.FRIDAY]
    else:
        # if the first friday isn't in the first week, it must be in the second
        meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" % (calendar.month_name[m], meetday))
