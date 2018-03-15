# Calculating Length

# len() --> returns length

firstName = "Taylor"
print(len(firstName))
lastName = "Swift"
print(len(lastName))
firstName.__len__()

print()
print(len("ほげ"))  # Unicode

print()
ages = [0, 11, 43] + [12, 10]
print(len(ages))
for i in range(0, len(ages)):
    print(ages[i])

print()
ages.remove(43)  # indexではなく、value指定
print(len(ages))
print(ages)

print()
candyCollection = {"bob": 10, "mary": 7, "sam": 18}
print(len(candyCollection))

print()

# Range -> range instance that holds all nums counting by one between 0 and first input
# List -> lists numbers from the inputted tuple

numberedContestants = range(30)
hoge = list(numberedContestants)
print(hoge[2:3])
print(hoge)

luckyWinners = range(7, 30, 5)
print(list(luckyWinners))

print()
