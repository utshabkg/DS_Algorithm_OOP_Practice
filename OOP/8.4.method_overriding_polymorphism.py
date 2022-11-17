class A:

    def show(self):
        print("Show A!")


class B(A):

    def show(self):
        print("Show B! calls show() of class B, not A --> Overriding")


a = B()
a.show()  # calls show() of class B, not A --> Overriding
