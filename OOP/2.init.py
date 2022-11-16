class Computer:

    def __init__(self, ram, cpu):
        self.ram = ram
        self.cpu = cpu

    def show(self):
        print(self.ram, self.cpu)


com = Computer(16, 'i5')  # constructor
com.show()  # same as Computer.config(com)
