# Basic functions
# Minimum and Maximum

playerOneScore = 10
playerTwoScore = 4
print(min(playerOneScore, playerTwoScore))
print(min(0, 12, -19))

print(min("Kathryn", "Katie"))  # alphabetically
print(min("Angela", "Bob"))

print(max(playerOneScore, playerTwoScore))
playerThreeScore = 14
print(max(playerThreeScore, playerTwoScore, playerOneScore))
print(max("Kathryn", "Katie"))

# round()
myGPA = 3.6
print(round(myGPA))
amountOfSalt = 1.4
print(round(amountOfSalt))

apple = -1.2
print(round(apple))
google = -1.6
print(round(google))

# abs()
distanceAway = -13
print(abs(distanceAway))
lengthOfRootInGround = -2.5
print(abs(lengthOfRootInGround))

# pow()
chanceOfTails = 0.5
inARowTails = 3
print(pow(chanceOfTails, inARowTails))

chanceOfOne = .167
inARowOne = 2
print(pow(chanceOfOne, inARowOne))
