# Least to Greatest
pointsInaGame = [0, -10, 15, -2, 1, 12]
sortedGame = sorted(pointsInaGame)
print(sortedGame)

# Alphabetically (case-sensitive, ascii code)
children = ["Sue", "Jerry", "Linda"]
print(sorted(children))
print(sorted(["Sue", "jerry", "linda"]))

# Key Parameters
print(sorted("My favorite child is Linda".split(), key=str.upper))
print(sorted(pointsInaGame, reverse=True))

# dictionary
leaderBoard = {231: "CKL", 123: "ABC", 432: "JKC"}
print(sorted(leaderBoard, reverse=True))
print(leaderBoard.get(432))

# tuple
students = [('alice', 'B', 12), ('tae', 'C', 15), ('eliza', 'A', 16)]
print(sorted(students, key=lambda student: student[0]))
print(sorted(students, key=lambda student: student[1]))
print(sorted(students, key=lambda student: student[2]))
