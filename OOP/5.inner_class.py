class Office:  # Outer Class

    def __init__(self, employee, emp_id):
        self.employee = employee
        self.emp_id = emp_id
        self.com = self.Computer()

    def show(self):
        print(self.employee, self.emp_id)
        print("Inside Class:", self.com.ram)

    class Computer:  # Inner Class

        def __init__(self):
            self.ram = 16
            self.cpu = 'Ryzen 3'


off = Office('Utshab', 1603022)
off.show()

com = off.com
print("Outside Class:", com.ram)

