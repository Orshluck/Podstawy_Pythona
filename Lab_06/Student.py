class Student:
    def __init__(self, email, name, surname,all_grade,status):
        if all_grade:
            self.all_grade = all_grade
        else:

            self.all_grade = {
                "project": -1,
                "l_1": -1,
                "l_2": -1,
                "l_3": -1,
                "h_1": -1,
                "h_2": -1,
                "h_3": -1,
                "h_4": -1,
                "h_5": -1,
                "h_6": -1,
                "h_7": -1,
                "h_8": -1,
                "h_9": -1,
                "h_10": -1,
                "grade": -1,
            }
        self.email = email
        self.name = name
        self.surname = surname
        self.status = status

    @staticmethod
    def compareStudents(a, b):
        return a.name >= b.name

    def __str__(self):
        return str(self.name) +" "\
            + str(self.surname) + " " \
            + str(self.email) + "  " \
            + str(self.all_grade) +" "\
            + str(self.status)
