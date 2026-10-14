# class Employee:
#     pass

# emp1 = Employee()
# emp2 = Employee()   # Two different objects from one class




class Employee:
    company = "Midh Technologies"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

emp1 = Employee("Mehar",50000)
emp2 = Employee("Siri",50000)

print(emp1.name)
print(emp2.name)  # Instance variable

print(emp1.company)
print(emp2.company)
print(Employee.company) # class variable

