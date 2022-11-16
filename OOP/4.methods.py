class Computer:

    retailer = 'Ryans'

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def brand(self):  # instance method: works with instance variable
        return self.a + " " + self.b

    @classmethod  # works with class variable e.g. retailer
    def info(cls):
        return cls.retailer

    @staticmethod  # works with no variable. Extra works!
    def others():
        print("Nitro 5 is new fire!")

com = Computer('Acer', "Ltd.")
print(com.brand())
print(com.info())
com.others()