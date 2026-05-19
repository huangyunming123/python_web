from python基础.my_package.Student import Student

student = Student('小王', 18)

student.study('python !')

if __name__ == '__main__':
    print('__name__:', __name__)
    # print(dir(student))
    print(str(student))


