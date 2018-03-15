from student import Student
from hs_student import HighSchoolStudent

print(Student.school_name)

mark = Student("Mark")
print(mark.get_name_capitalize())
jessica = Student("Jessica")
print(jessica.get_name_capitalize())

print(mark)
print(jessica)

print(HighSchoolStudent.school_name)

james = HighSchoolStudent("james")
print(james.get_name_capitalize())
print(james.get_school_name())

print(james)
