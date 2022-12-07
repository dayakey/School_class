class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(Human):
    def __init__(self, name, age, subject, experience):
        super().__init__(name, age)
        self.subject = subject
        self.experience = experience


class Student(Human):
    def __init__(self, name, age, grade, address):
        super().__init__(name, age)
        self.grade = grade
        self.address = address


def registration():
    registration = input("Are you teacher or student?(Teacher, Student):").capitalize()
    if registration == "Teacher":
        teacher = Teacher(input("Enter your name: "), int(input("Enter your age: ")), input("Enter your subject: "),
                          input("Enter your years of experience: "))
        print(teacher.name)
        print(teacher.age, "years old")
        print(teacher.subject)
        print(teacher.experience, "years of experience")
    elif registration == "Student":
        student = Student(input("Enter your name: "), int(input("Enter your age: ")), int(input("Enter your grade: ")),
                          input("Enter your address: "))
        print(student.name)
        print(student.age, "years old")
        print(student.grade, "grade")
        print(student.address)


registration()

