class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id
        print("Parent constructor")

    def show_details(self):
        print(f"Name: {self.name}, ID: {self.emp_id}")


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_pay(self):
        return self.monthly_salary


class ContractEmployee(Employee):
    def __init__(self, name, emp_id, rate, hours):
        super().__init__(name, emp_id)
        self.rate = rate
        self.hours = hours

    def calculate_pay(self):
        
        return self.rate * self.hours


full_time_emp = FullTimeEmployee("Mehar", 60, 300000)
full_time_emp.show_details()
print("Monthly salary:", full_time_emp.calculate_pay())





