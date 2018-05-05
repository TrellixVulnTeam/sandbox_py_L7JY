# Calendar Module
from datetime import datetime, timedelta
import calendar

now = datetime.now()

testDate = now + timedelta(days=2)
myFirstLinkedInCourse = now - timedelta(weeks=3)

print(testDate.date())
print(myFirstLinkedInCourse.date())

if testDate > myFirstLinkedInCourse:
    print("Comparison works")

print()

# from string
line = input("Enter your date of birth (DD/MM/YYYY): ")
birthday = datetime.strptime(line, "%d/%m/%Y")
print("You were born on a {0:%A}".format(birthday))  # strftime書式でformatしていることに注目

print()

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2013, 1, 0, 0)
print(str)

# calendar (shorthand)
c = calendar.month(2013, 1)
print(c)

# create an HTML formatted calendar
c = calendar.HTMLCalendar(calendar.SUNDAY)
str = c.formatmonth(2013, 1)
print(str)

print()

# tips
print(calendar.weekday(2001, 10, 11))

print(calendar.isleap(1999))
print(calendar.isleap(2000))
print(calendar.isleap(2100))

print()

for name in calendar.month_name:
    print(name)

print()
for day in calendar.day_name:
    print(day)

print()

# iterator
c = calendar.c  # TextCalendar(calendar.MONDAY)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2013, 8):
    print(i)

print()

for i in c.iterweekdays():  # 基準曜日は、calendar初期化時の指定に寄る。
    print(i)
