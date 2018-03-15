# Random Module
import random

# Random Numbers
print(random.random())  # [0-1)
print(random.randint(1, 1000))
print(random.randrange(3))  # [0, 1, 2]
print("You rolled a " + str(random.randrange(1, 8, 2)))  # [1, 3, 5, 7]

# Random Choices
lotteryWinners = random.sample(range(100), 5)
print(lotteryWinners)

possiblePets = ["cat", "dog", "fish"]
print(random.choice(possiblePets))

x = list(range(25))
print(x)
random.shuffle(x)
print(x)

cards = ["Jack", "Queen", "King", "Ace"]
random.shuffle(cards)
print(cards)
