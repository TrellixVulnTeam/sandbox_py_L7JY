# random Module
import random
import string

# create a random number
print(random.random())

print(random.randrange(3))  # [0-3): [0, 1, 2]
print(random.randrange(1, 9, 2))  # [1, 3, 5, 7]
print(random.randint(1, 3))  # [1-3]: [1, 2, 3]

# get a random number within a range
print(random.uniform(1, 100))  # float

# generate random integers within a given range
print(random.randint(1, 100))

# generate random integers with a step function
# this example chooses from 0 to 100 stepped by 5
print(random.randrange(0, 101, 5))

# Use the seed function to position the generator
random.seed(999)
print([random.randint(1, 100) for _ in range(10)])
random.seed(999)
print([random.randint(1, 100) for _ in range(10)])

# clear seed
random.seed(None)
print([random.randint(1, 100) for _ in range(10)])

print("----------------")

# Use the choice function to randomly select from a sequence
moves = ["rock", "paper", "scissors"]
print(random.choice(moves))

# Use the choices function to create a list of random elements
roulette_wheel = ["black", "red", "green"]
weights = [18, 18, 2]
print(random.choices(roulette_wheel, weights, k=10))  # 3.6

# The sample function randomly selects elements from a population
# without replacement (the chosen items are not replaced)
chosen = random.sample(string.ascii_uppercase, 6)
print(chosen)

# The shuffle function shuffles a sequence in place
cards = ["Jack", "Queen", "King", "Ace"]
print(cards)
random.shuffle(cards)
print(cards)

# to shuffle an immutable sequence, use the sample function first
result = random.sample(string.ascii_uppercase, k=len(string.ascii_uppercase))
random.shuffle(result)
print(''.join(result))
