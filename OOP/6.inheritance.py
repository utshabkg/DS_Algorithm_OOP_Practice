class A:

    def featureA(self):
        print("A")


class B(A):  # Single Level Inheritance

    def featureB(self):
        print("B")


class C(B):  # Multi Level

    def featureC(self):
        print("C")

class X:

    def featureX(self):
        print("X")

class D(C, X):  # Multiple

    def featureD(self):
        print("D")


print("Features of A:")
a = A()
a.featureA()


print("Features of B:")
b = B()
b.featureA()
b.featureB()

print("Features of C:")
c = C()
c.featureA()
c.featureB()
c.featureC()

print("Features of D:")
d = D()
d.featureA()
d.featureB()
d.featureC()
d.featureX()
d.featureD()
