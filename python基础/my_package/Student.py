class Student:
    name = 'zs'

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.name = name

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}')


if __name__ == '__main__':
    # student = Student('小王', 18)
    #
    # student.study('Python')

    print(Student.name)

    student = Student('小王', 18)

    print(student.name)

    print(Student.name)
