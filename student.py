class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def __str__(self):
        return f"{self.name},{self.age},{self.marks}"
