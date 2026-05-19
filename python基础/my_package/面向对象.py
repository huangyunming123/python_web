class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old. I am in grade {self.grade}.")


print(Student.__mro__)


