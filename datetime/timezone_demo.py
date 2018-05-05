import datetime

# timezone
pacific = datetime.timezone(datetime.timedelta(hours=-8))
eastern = datetime.timezone(datetime.timedelta(hours=-5))
tokyo = datetime.timezone(datetime.timedelta(hours=9))

naive = datetime.datetime(2018, 4, 25, 9, 0)
aware = datetime.datetime(2018, 4, 25, 9, 0, tzinfo=pacific)

print(naive.astimezone(eastern))
print(aware.astimezone(eastern))
print(aware.astimezone(tokyo))

import pytz

pacific = pytz.timezone('US/Pacific')
eastern = pytz.timezone('US/Eastern')
tokyo = pytz.timezone('Asia/Tokyo')
utc = pytz.utc
fmt = '%Y-%m-%d %H:%M:%S %Z%z'

start = pacific.localize(datetime.datetime(2018, 4, 25, 9, 0))
start_tokyo = tokyo.localize(datetime.datetime(2018, 4, 25, 9, 0))
print(start.strftime(fmt))
print(start_tokyo.strftime(fmt))

start_utc = datetime.datetime(2018, 4, 25, 9, 0, tzinfo=utc)
print(start_utc.strftime(fmt))

start_pacific = start_utc.astimezone(pacific)
start_eastern = start_utc.astimezone(eastern)
print(start_pacific.strftime(fmt))  # 夏時間を考慮する
print(start_eastern.strftime(fmt))

print(pytz.all_timezones)
print(pytz.country_timezones('us'))
