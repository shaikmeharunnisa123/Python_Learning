class Employee:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)


class FullTimeEmployee(Employee):
    def calculate_pay(self):
        return 300000


emp = FullTimeEmployee("Mehar")
emp.show_name()
print(emp.calculate_pay())