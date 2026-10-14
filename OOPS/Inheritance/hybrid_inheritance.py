class Employee:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Employee:", self.name)


class FullTimeEmployee(Employee):
    def full_time_details(self):
        print("Employment type: Full-time")


class ContractEmployee(Employee):
    def contract_details(self):
        print("Employment type: Contract")


class Payroll:
    def calculate_bonus(self):
        return 10000


class Manager(FullTimeEmployee, Payroll):
    def manage_team(self):
        print(self.name, "manages the team")


manager = Manager("Mehar")

manager.show_name()
manager.full_time_details()
manager.manage_team()
print("Bonus:", manager.calculate_bonus())