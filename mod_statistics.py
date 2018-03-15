# Statistics Module
import statistics
import math

agesData = [10, 13, 14, 12, 11, 10, 11, 10, 15]

print(statistics.mean(agesData))  # 平均値
print(statistics.mode(agesData))  # 最頻値
print(statistics.median(agesData))  # 中央値
print(sorted(agesData))

print(statistics.variance(agesData))  # 分散
print(statistics.stdev(agesData))  # standard deviation 標準偏差
print(math.sqrt(statistics.variance(agesData)))  # 同上
