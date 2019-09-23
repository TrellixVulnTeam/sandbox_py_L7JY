# "time" module is based on time API from C
import time

print(time.localtime())

start = time.monotonic()
time.sleep(2)
print('CPU seconds used:', time.process_time())
print('Slept 2 seconds:', time.monotonic() - start)

current_time = time.time()
print('Current time:', time.ctime(current_time))
print('42 seconds later:', time.ctime(current_time + 42))

# BAD : daylight saving time, leap year, leap second
print('42 days later:', time.ctime(current_time + 42 * 24 * 3600))
