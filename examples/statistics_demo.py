# using Python statistics functions
import statistics
import csv
import array


# Read data from a CSV file and calculate statistics
def read_data():
    with open("../data/StockQuotes.csv") as dataFile:
        data = array.array('f', [])

        reader = csv.reader(dataFile)
        cur_line = 0
        for row in reader:
            if cur_line == 0:
                pass  # this is the headers row
            else:
                # get the closing value
                item = float(row[4])
                data.append(item)
            cur_line += 1

        print(f"Read {cur_line + 1} rows of data.")
        return data


def calc_stats():
    # read the data from the CSV file
    data = read_data()

    data_mean = round(statistics.mean(data), 2)
    data_med = round(statistics.median(data), 2)
    data_std = round(statistics.stdev(data), 2)  # 標準偏差 = √分散
    data_var = round(statistics.variance(data), 2)  # 分散

    print("Mean:", data_mean)
    print("Median:", data_med)
    print("Standard deviation:", data_std)
    print("Variance:", data_var)


calc_stats()
