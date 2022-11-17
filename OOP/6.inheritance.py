class A:

    def feature_a(self):
        print("A")


class B(A):  # Single Level Inheritance

    def feature_b(self):
        print("B")


class C(B):  # Multi Level

    def feature_c(self):
        print("C")


class X:

    def feature_x(self):
        print("X")


class D(C, X):  # Multiple

    def feature_d(self):
        print("D")


print("Features of A:")
a = A()
a.feature_a()


print("Features of B:")
b = B()
b.feature_a()
b.feature_b()

print("Features of C:")
c = C()
c.feature_a()
c.feature_b()
c.feature_c()

print("Features of D:")
d = D()
d.feature_a()
d.feature_b()
d.feature_c()
d.feature_x()
d.feature_d()
