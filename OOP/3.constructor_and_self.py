class Computer:

    def __init__(self):
        self.ram = 16
        self.cpu = 'i5'

    def print(self):
        print(self.ram, self.cpu)

    def update(self):
        self.ram = 32


com = Computer()  # constructor
com.update()
com.print()
