class Student:

    school_name = "Springfield Elementary"  # class変数

    def __init__(self, name, student_id=332):
        self.name = name
        self.student_id = student_id

    # toString
    def __str__(self):
        return self.school_name + ": " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name
