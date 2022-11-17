class Student:

    def __init__(self, marks1, marks2):
        self.marks1 = marks1
        self.marks2 = marks2

    def sum(self, a=None, b=None, c=None):
        print(a + b)


s1 = Student(50, 46)
s1.sum(10, 20)