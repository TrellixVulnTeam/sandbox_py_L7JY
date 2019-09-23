# pytz library
import datetime
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

# print(pytz.all_timezones)
# print(pytz.country_timezones('us'))

amsterdam = pytz.timezone("Europe/Amsterdam")
naive = datetime.datetime(2018, 1, 1, 20, 15, 0)
print(naive)
aware = amsterdam.localize(naive)
print(aware)
print(aware.tzinfo)
naive_summer = datetime.datetime(2018, 8, 1, 20, 15, 0)
aware_summer = amsterdam.localize(naive_summer)
print(aware_summer)

# Converting Between Timezones
eastern = pytz.timezone("US/Eastern")
aware_ea = aware.astimezone(eastern)
print(aware_ea)
print(aware)
print(aware_ea == aware)  # True
