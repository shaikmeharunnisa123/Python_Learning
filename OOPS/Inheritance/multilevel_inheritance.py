class Employee:
    def __init__(self, name):
        self.name = name


class FullTimeEmployee(Employee):
    def show_employee(self):
        print("Employee:", self.name)


class Manager(FullTimeEmployee):
    def manage_team(self):
        print(self.name, "manages the team")


manager = Manager("Mehar")
manager.show_employee()
manager.manage_team()