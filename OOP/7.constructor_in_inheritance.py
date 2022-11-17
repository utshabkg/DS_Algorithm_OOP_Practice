class A:

    def __init__(self):
        print("init in A")

    def feature_a(self):
        print("A")


class B():

    def __init__(self):
        # super().__init__()   # 1 super class
        print("init in B")

    def feature_b(self):
        print("B")


class C(A, B):

    def __init__(self):
        super().__init__()  # 2 super class. Gets the Left one first.
        print("init in C")

    def feature_c(self):
        print("C")

# b = B()
c = C()
