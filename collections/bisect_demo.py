# use the bisection functions to maintain a list in sorted order
import bisect

values = [5, 7, 13, 20, 25, 31, 36, 43, 47, 49, 50, 75]

# exercise the left and right bisection routines
print(bisect.bisect_right(values, 25))
print(bisect.bisect(values, 25))  # same
print(bisect.bisect_left(values, 25))

# use insort to insert new items
bisect.insort_right(values, 28)  # will insert to the right
print(values)
bisect.insort_left(values, 10)  # will insert to the left
print(values)

print()

# bisect can be used as an array lookup using breakpoints
breakpoints = [60, 70, 80, 90]
gradeLetters = 'FDCBA'
scores = [81, 68, 53, 91, 90, 80, 76, 71, 84]


def calc_grade(score):
    # use the bisect function to identify cutoff points for the letter grades
    i = bisect.bisect(breakpoints, score)
    return gradeLetters[i]


results = [calc_grade(score) for score in scores]
print(results)
