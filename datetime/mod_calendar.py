# Calendar Module
import calendar
import locale
from datetime import datetime, timedelta

now = datetime.now()

testDate = now + timedelta(days=2)
myFirstLinkedInCourse = now - timedelta(weeks=3)

print(testDate.date())
print(myFirstLinkedInCourse.date())

if testDate > myFirstLinkedInCourse:
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
# print(list(c.itermonthdays3(2013, 8)))  # 3.7
# print(list(c.itermonthdays4(2013, 8)))  # 3.7
print(list(c.iterweekdays()))

print()

locale.setlocale(locale.LC_ALL, '')  # 環境から取得して設定する
print(locale.getlocale(locale.LC_TIME))
print(list(calendar.month_name))
print(list(calendar.day_name))
print(list(calendar.day_abbr))
