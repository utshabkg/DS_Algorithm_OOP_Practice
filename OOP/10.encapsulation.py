class Computer:

    def __init__(self):
        self.__max_price = 900  # __ is used to denote private attribute

    def sell(self):
        print("Selling Price: {}".format(self.__max_price))

    def setMaxPrice(self, price):  # without this setter function, price can't be updated
        self.__max_price = price


c = Computer()
c.sell()

# change the price, ehich is not seen on output
c.__max_price = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()
