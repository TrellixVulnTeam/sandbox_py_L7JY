import datetime

now = datetime.datetime.now()

# strftime
# %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
print(now.strftime("%a %A %d %w"))  # day
print(now.strftime("%b %B %m"))  # month
print(now.strftime("%y %Y"))  # year
print(now.strftime("%j"))  # day of the year
print(now.strftime("%W"))  # week of the year

# %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
print(now.strftime("%I:%M:%S %p"))  # 12-Hour:Minute:Second:AM
print(now.strftime("%H:%M:%S"))  # 24-Hour:Minute:Second

# %c - locale's date and time, %x - locale's date, %X - locale's time
print(now.strftime("%c"))
print(now.strftime("%x"))
print(now.strftime("%X"))
print("{:%A %d %B %Y}".format(now))

# strptime
birthday = datetime.datetime.strptime('12/12/1972', "%d/%m/%Y")  # DD/MM/YYYY
print("You were born on {0:%A} of the {0:%W}th week".format(birthday))  # strftime書式でformatしていることに注目


def example(mmdd):
    try:
        date = datetime.datetime.strptime(mmdd, '%m/%d')
        output = date.strftime('%b_%d')
        print(output)
    except ValueError:
        print("That's not a valid date. Please try again.")


example("4/31")
example("2/29")
example("12/12")
