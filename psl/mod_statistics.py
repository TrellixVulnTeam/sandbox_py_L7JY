# statistics Module
import statistics

sample_data = [10, 13, 14, 12, 11, 10, 11, 10, 15]
print('original:', sample_data)
print('sorted:', sorted(sample_data))

print('Mean:', statistics.mean(sample_data))  # 平均値
print('Mode:', statistics.mode(sample_data))  # 最頻値
print('Median:', statistics.median(sample_data))  # 中央値
print('Median_low:', statistics.median_low(sample_data))
print('Median_high:', statistics.median_high(sample_data))

print('Variance:', statistics.variance(sample_data))  # 分散
print('Standard Deviation:', statistics.stdev(sample_data))  # 標準偏差 = √分散
