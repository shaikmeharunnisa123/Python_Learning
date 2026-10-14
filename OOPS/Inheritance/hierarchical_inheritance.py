class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def show_details(self):
        print(self.name, self.emp_id)


class FullTimeEmployee(Employee):
    def calculate_pay(self):
        return 300000


class ContractEmployee(Employee):
    def calculate_pay(self):
        return 500 * 80


e1 = FullTimeEmployee("Mehar", 60)
e2 = ContractEmployee("Ravi", 61)

e1.show_details()
print(e1.calculate_pay())

e2.show_details()
print(e2.calculate_pay())