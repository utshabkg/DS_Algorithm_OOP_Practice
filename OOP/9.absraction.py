from abc import ABC, abstractmethod


class Computer(ABC):  # abstract class
    @abstractmethod  # absract method
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("You can Programme!")


class Paper(Computer):
    def write(self):
        print("NO! You can't.")
    

class Programmer:
    def work(self, com):
        com.process()


# com = Computer()
lap = Laptop()
prog = Programmer()
prog.work(lap)

# won't run. Paper has no process()
# pap = Paper()
# prog.work(pap)
