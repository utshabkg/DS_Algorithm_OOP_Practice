class PyCharm:

    def execute(self):
        print('Compile')
        print('Run')


class CustomEditor:

    def execute(self):
        print('Debug')
        print('Compile')
        print('Run')


class Computer:

    def code(self, ide):
        ide.execute()


# ide = PyCharm()
ide = CustomEditor()  # will work as it contains same things as PyCharm
com = Computer()

com.code(ide)
