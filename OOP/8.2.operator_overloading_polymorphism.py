class Student:

    def __init__(self, marks1, marks2):
        self.marks1 = marks1
        self.marks2 = marks2

    def __add__(self, other):
        marks1 = self.marks1 + other.marks1
        marks2 = self.marks2 + other.marks2
        total_each = Student(marks1, marks2)

        return total_each

    def __gt__(self, other):
        r1 = self.marks1 + self.marks2
        r2 = other.marks1 + other.marks2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return self.marks1, self.marks2


s1 = Student(50, 46)
s2 = Student(45, 48)

# calculate total marks of each student
s3 = s1 + s2  # Student.__add__(s1, s2)
print(s3.marks1, s3.marks2)

# compare of marks
if s1 > s2:
    print("S1 > S2")
else:
    print("S1 < S2")

# getting values of s1 overriding __str__()
print(s1)
