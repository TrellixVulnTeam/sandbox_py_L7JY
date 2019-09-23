# 夏時間（Daylight Saving Time: DST）の問題があるので、pytz利用を推奨
import datetime

# timezone
pacific = datetime.timezone(datetime.timedelta(hours=-8))
eastern = datetime.timezone(datetime.timedelta(hours=-5))
tokyo = datetime.timezone(datetime.timedelta(hours=9), 'JST')

# naive: depends on the system locale
naive = datetime.datetime(2018, 4, 25, 9, 0)
print(naive)
print(naive.astimezone(datetime.timezone.utc))
print(naive.astimezone(eastern))

print()

# aware:
aware = datetime.datetime(2018, 4, 25, 9, 0, tzinfo=pacific)
print(aware)
print(aware.astimezone(datetime.timezone.utc))
print(aware.astimezone(eastern))
print(aware.astimezone(tokyo))
