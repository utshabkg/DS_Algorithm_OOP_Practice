class Computer:

    def show(self):
        print("i5, 16GB, 1 TB")


com = Computer()  # constructor
print(type(com))

com.show()  # same as Computer.config(com)
