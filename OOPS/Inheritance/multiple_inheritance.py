class Payroll:
    def calculate_bonus(self):
        return 10000


class Benefits:
    def show_benefits(self):
        print("Health insurance available")


class Employee(Payroll, Benefits):
    def __init__(self, name):
        self.name = name


emp = Employee("Mehar")

print(emp.calculate_bonus())
emp.show_benefits()