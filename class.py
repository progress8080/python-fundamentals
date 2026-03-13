class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, {self.name}! age is {self.age}"

person = Person("John", 30)
print(person.greet())

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def greet(self):
        return f"Hello, {self.name}! age is {self.age} and grade is {self.grade}"

student = Student("John", 30, "A")
print(student.greet())