import time

from airport import load_airports

# reliable accuracy
print("Clock resolution: {0}sec"
      .format(time.get_clock_info('perf_counter').resolution))

# load_start = time.perf_counter()
# for a in load_airports('../../data/airports.dat'):
#     print(a)
# print("Loading took {0}sec".format(time.perf_counter() - load_start))


def measure(f):
    start = time.perf_counter()
    f()
    return time.perf_counter() - start


spent = measure(lambda: load_airports('../../data/airports.csv'))
print("Loading took {0}sec".format(spent))
assert spent < 0.01, "spent over 0.01sec"
