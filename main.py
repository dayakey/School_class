class Human():
    def __init__(self, name, age, room):
        self.name = name
        self.age = age
        self.room = room

    def classroom(self):
        print("You have lesson", "In", self.room)


class Teacher(Human):
    def __init__(self, name, age, subject, experience, room):
        super().__init__(name, age, room)
        self.subject = subject
        self.experience = experience

    def teach(self):
        print("My name is", self.name, "and I'm", self.age, ", I will teach you", self.subject,
              ", I teach this subject for", self.experience, "and my lessons will be in", self.room)


class Students(Human):
    def __init__(self, name, age, nummer_class, address, room,):
        super().__init__(name, age, room)
        self.nummer_class = nummer_class
        self.address = address


teacher = Teacher(input("Enter teachers name:"), input("Enter teachers age:"), input("Enter teachers subject:"),
                  input("Enter teachers years experience:"), input("Enter teachers lessons room:"))
students = Students()