class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    def get_infor(self):
        return  f"{self.name} has a GPA of {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        return f"Average GPA: {cls.total_gpa/cls.count:.2f}"


student1 = Student("John", 3.5)
student2 = Student("Danny", 3.7)
student3 = Student("Bob", 3.2)

print(Student.get_count())
print(Student.get_average_gpa())